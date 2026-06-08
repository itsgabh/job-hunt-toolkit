#!/usr/bin/env python3
"""
fetch_jobs.py — free, API-driven job scraper for globally-remote roles.

Pulls from remote-native job APIs (Himalayas, Jobicy, Remotive, Remote OK),
normalizes to a common schema, keyword-filters to your target roles,
geo-filters to your eligible tiers, and dedupes against seen_jobs.json +
job_search_tracker.csv.

ALL targeting (role keywords, excludes, source categories, geography, past
employers) lives in scraper_config.json — the Python source is industry- and
geography-agnostic. Copy scraper_config.example.json to scraper_config.json and
edit it to retarget the scraper. With no config file present, the scraper falls
back to a generic worldwide-remote, match-all search.

Stdlib only. See README.md for usage and scraper_config.example.json for a fully
worked example config (a People/HR + EU search you replace with your own field).

Usage:
    python job_scraper/fetch_jobs.py [--eligible] [--all-geos] [--max N] [--json]
    python job_scraper/fetch_jobs.py --source himalayas,jobicy
"""

import argparse
import csv
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SEEN_PATH = os.path.join(HERE, "seen_jobs.json")
TRACKER_PATH = os.path.join(ROOT, "job_search_tracker.csv")
CONFIG_PATH = os.path.join(HERE, "scraper_config.json")

UA = "Mozilla/5.0 (compatible; remote-job-scraper/1.0; personal job search)"

# --- Built-in geo data the config can reference ------------------------------
# These are reference datasets only. Which of these tiers are *eligible*, and
# which country is "home", are decided by the config (eligible_regions /
# home_country), not hardcoded here.
EU_COUNTRIES = {
    "spain", "portugal", "france", "germany", "italy", "netherlands", "belgium",
    "ireland", "austria", "poland", "sweden", "denmark", "finland", "norway",
    "czech", "czechia", "romania", "greece", "hungary", "croatia", "bulgaria",
    "slovakia", "slovenia", "estonia", "latvia", "lithuania", "luxembourg",
    "malta", "cyprus", "switzerland", "united kingdom", "uk",
}
WORLDWIDE_TOKENS = {"", "anywhere", "worldwide", "global", "remote", "any"}
US_TOKENS = {"united states", "usa", "u.s.", "us only", "us-only", "americas only"}

# --- Generic defaults (used when scraper_config.json is missing) -------------
# Sensible generic remote-job search: match-all roles, worldwide-eligible, no
# past-employer exclusions. The example config reproduces one worked search (a
# People/HR + EU example) — copy scraper_config.example.json to scraper_config.json
# and edit it to target your own field.
DEFAULT_CONFIG = {
    "role_keywords": [],            # empty = match all titles
    "exclude_keywords": [],
    "override_keywords": [],
    "jobicy_industry": "",          # empty = no industry filter on Jobicy
    "remotive_category": "",        # empty = no category filter on Remotive
    "himalayas_queries": ["remote"],
    "eligible_regions": ["worldwide"],
    "home_country": "",
    "past_company_slugs": [],
}

# Populated by load_config() at startup.
CONFIG = dict(DEFAULT_CONFIG)
ROLE_KEYWORDS = []
EXCLUDE_KEYWORDS = []
OVERRIDE_KEYWORDS = []
ELIGIBLE_GEOS = {"worldwide"}
HOME_COUNTRY = ""
PAST_COMPANY_SLUGS = set()
BOOMERANG = set()


def load_config(path=CONFIG_PATH):
    """Load scraper_config.json over DEFAULT_CONFIG and populate module globals.
    Missing file or unreadable JSON falls back to the generic defaults. Keys
    prefixed with '_' (e.g. '_comment') are ignored."""
    global CONFIG, ROLE_KEYWORDS, EXCLUDE_KEYWORDS, OVERRIDE_KEYWORDS
    global ELIGIBLE_GEOS, HOME_COUNTRY, PAST_COMPANY_SLUGS

    cfg = dict(DEFAULT_CONFIG)
    try:
        with open(path) as f:
            user = json.load(f)
        for k, v in user.items():
            if k.startswith("_"):
                continue
            cfg[k] = v
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"[config] {path} unreadable ({e}); using generic defaults", file=sys.stderr)

    CONFIG = cfg
    ROLE_KEYWORDS = [_norm(k) for k in cfg.get("role_keywords", [])]
    EXCLUDE_KEYWORDS = [_norm(k) for k in cfg.get("exclude_keywords", [])]
    OVERRIDE_KEYWORDS = [_norm(k) for k in cfg.get("override_keywords", [])]
    HOME_COUNTRY = _norm(cfg.get("home_country", ""))

    # Eligible region tiers: normalize aliases to the classify_geo vocabulary.
    # "europe"/"eu"/"emea" -> "eu"; the home country name -> "home".
    elig = set()
    for r in cfg.get("eligible_regions", []):
        rn = _norm(r)
        if rn in ("europe", "eu", "emea"):
            elig.add("eu")
        elif rn in ("us", "usa", "united states", "us_only", "us-only"):
            elig.add("us_only")
        elif HOME_COUNTRY and rn == HOME_COUNTRY:
            elig.add("home")
        else:
            elig.add(rn)
    ELIGIBLE_GEOS = elig or {"worldwide"}

    PAST_COMPANY_SLUGS = {slug(s) for s in cfg.get("past_company_slugs", [])}
    return cfg


def _norm(s):
    return (s or "").strip().lower()


def classify_geo(raw):
    """Return one of: worldwide | home | eu | us_only | other.
    `home` is returned when the location matches CONFIG's home_country.
    `raw` may be a string or a list of location strings. Tier eligibility is
    decided later against ELIGIBLE_GEOS (config-driven)."""
    if isinstance(raw, list):
        parts = [_norm(x) for x in raw]
        if not parts:
            return "worldwide"
        joined = " ".join(parts)
    else:
        joined = _norm(raw)
        parts = [p.strip() for p in re.split(r"[,/|]", joined) if p.strip()]
        if not parts:
            parts = [joined]

    if joined in WORLDWIDE_TOKENS or any(p in WORLDWIDE_TOKENS for p in parts):
        # but if it also names a region, fall through to region logic
        if joined in WORLDWIDE_TOKENS:
            return "worldwide"
    if HOME_COUNTRY and HOME_COUNTRY in joined:
        return "home"
    if any(c in joined for c in EU_COUNTRIES) or "europe" in joined or "emea" in joined or joined in ("eu",):
        return "eu"
    if any(t in joined for t in US_TOKENS):
        return "us_only"
    if "worldwide" in joined or "anywhere" in joined or "global" in joined:
        return "worldwide"
    return "other"


# --- Past employers (excluded by default; boomeranging is opt-in) ------------
# Past employers come from config (past_company_slugs) as lowercase,
# underscore-separated name slugs, so the scraper skips them by default.
# Re-include any of them for a given run with --boomerang (e.g.
# --boomerang acme_corp). BOOMERANG holds the allowed name-slugs.


def is_past_employer(company):
    s = slug(company)
    if s in BOOMERANG:
        return False
    return s in PAST_COMPANY_SLUGS


# --- Helpers -----------------------------------------------------------------
def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def slug(s):
    return re.sub(r"[^a-z0-9]+", "_", _norm(s)).strip("_")


def make_key(company, title):
    return f"{slug(company)}_{slug(title)}"


def title_matches(title):
    t = _norm(title)
    if EXCLUDE_KEYWORDS and any(x in t for x in EXCLUDE_KEYWORDS):
        # allow if it ALSO matches an override keyword (config-driven allowlist
        # that rescues otherwise-excluded titles, e.g. "People Systems Engineer")
        if not any(k in t for k in OVERRIDE_KEYWORDS):
            return False
    # empty role_keywords = match all titles (generic default)
    if not ROLE_KEYWORDS:
        return True
    return any(k in t for k in ROLE_KEYWORDS)


def unix_to_date(ts):
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc).strftime("%Y-%m-%d")
    except Exception:
        return "recent"


def norm_record(title, company, url, location_raw, geo, posted, salary, level, source):
    title = html.unescape(title or "").strip()
    company = html.unescape(company or "").strip()
    return {
        "key": make_key(company, title),
        "title": title,
        "company": company,
        "url": url,
        "location_raw": location_raw if isinstance(location_raw, str) else ", ".join(location_raw or []),
        "global_remote": geo,
        "posted": posted,
        "salary": salary,
        "level_raw": level,
        "source": source,
    }


# --- Source fetchers ---------------------------------------------------------
def fetch_himalayas(max_per=40):
    out = []
    queries = CONFIG.get("himalayas_queries") or ["remote"]
    for q in queries:
        url = f"https://himalayas.app/jobs/api/search?q={urllib.parse.quote(q)}&limit={max_per}"
        try:
            d = json.loads(http_get(url))
        except Exception as e:
            print(f"[himalayas] {q!r} error: {e}", file=sys.stderr)
            continue
        for j in d.get("jobs", []):
            loc = j.get("locationRestrictions") or []
            sal = None
            if j.get("minSalary") and j.get("maxSalary"):
                sal = f"{j.get('currency','')}{j['minSalary']}-{j['maxSalary']}"
            out.append(norm_record(
                j.get("title", ""), j.get("companyName", ""), j.get("applicationLink") or j.get("guid", ""),
                loc, classify_geo(loc), unix_to_date(j.get("pubDate")), sal,
                ", ".join(j.get("seniority") or []), "himalayas",
            ))
    return out


def fetch_jobicy(max_per=50):
    out = []
    industry = _norm(CONFIG.get("jobicy_industry", ""))
    ind_q = f"industry={urllib.parse.quote(industry)}&" if industry else ""
    url = f"https://jobicy.com/api/v2/remote-jobs?{ind_q}count={max_per}"
    try:
        d = json.loads(http_get(url))
    except Exception as e:
        print(f"[jobicy] error: {e}", file=sys.stderr)
        return out
    for j in d.get("jobs", []):
        sal = None
        if j.get("salaryMin") and j.get("salaryMax"):
            sal = f"{j.get('salaryCurrency','')}{j['salaryMin']}-{j['salaryMax']}"
        geo = classify_geo(j.get("jobGeo", ""))
        out.append(norm_record(
            j.get("jobTitle", ""), j.get("companyName", ""), j.get("url", ""),
            j.get("jobGeo", ""), geo, (j.get("pubDate", "") or "")[:10] or "recent",
            sal, j.get("jobLevel", ""), "jobicy",
        ))
    return out


def fetch_remotive():
    out = []
    category = _norm(CONFIG.get("remotive_category", ""))
    cat_q = f"category={urllib.parse.quote(category)}&" if category else ""
    url = f"https://remotive.com/api/remote-jobs?{cat_q}limit=100"
    try:
        d = json.loads(http_get(url))
    except Exception as e:
        print(f"[remotive] error: {e}", file=sys.stderr)
        return out
    for j in d.get("jobs", []):
        loc = j.get("candidate_required_location", "")
        out.append(norm_record(
            j.get("title", ""), j.get("company_name", ""), j.get("url", ""),
            loc, classify_geo(loc), (j.get("publication_date", "") or "")[:10] or "recent",
            j.get("salary") or None, j.get("job_type", ""), "remotive",
        ))
    return out


def fetch_remoteok():
    out = []
    try:
        d = json.loads(http_get("https://remoteok.com/api"))
    except Exception as e:
        print(f"[remoteok] error: {e}", file=sys.stderr)
        return out
    for j in d:
        if not isinstance(j, dict) or "position" not in j:
            continue  # first element is a legal/notice object
        loc = j.get("location", "")
        sal = None
        if j.get("salary_min"):
            sal = f"${j.get('salary_min')}-{j.get('salary_max')}"
        out.append(norm_record(
            j.get("position", ""), j.get("company", ""), j.get("url") or j.get("apply_url", ""),
            loc, classify_geo(loc), (j.get("date", "") or "")[:10] or "recent",
            sal, "", "remoteok",
        ))
    return out


# --- Company ATS career-page fetchers ---------------------------------------
# Each fetcher takes the company dict `c` from companies.json and yields
# (title, location, url, posted) tuples.
COMPANIES_PATH = os.path.join(HERE, "companies.json")


def http_post_json(url, payload, timeout=30):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(),
        headers={"User-Agent": UA, "Accept": "application/json", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _ats_greenhouse(c):
    d = json.loads(http_get(f"https://boards-api.greenhouse.io/v1/boards/{c['slug']}/jobs"))
    for j in d.get("jobs", []):
        loc = (j.get("location") or {}).get("name", "")
        yield j.get("title", ""), loc, j.get("absolute_url", ""), (j.get("updated_at", "") or "")[:10]


def _ats_ashby(c):
    d = json.loads(http_get(f"https://api.ashbyhq.com/posting-api/job-board/{c['slug']}"))
    for j in d.get("jobs", []):
        loc = j.get("location", "") or ("Remote" if j.get("isRemote") else "")
        yield j.get("title", ""), loc, j.get("jobUrl") or j.get("applyUrl", ""), (j.get("publishedAt", "") or "")[:10]


def _ats_lever(c):
    d = json.loads(http_get(f"https://api.lever.co/v0/postings/{c['slug']}?mode=json"))
    for j in d:
        loc = (j.get("categories") or {}).get("location", "")
        yield j.get("text", ""), loc, j.get("hostedUrl", ""), ""


def _ats_smartrecruiters(c):
    d = json.loads(http_get(f"https://api.smartrecruiters.com/v1/companies/{c['slug']}/postings?limit=100"))
    for j in d.get("content", []):
        loc = j.get("location") or {}
        loc_str = ", ".join(x for x in (loc.get("city"), loc.get("region"), loc.get("country")) if x)
        if loc.get("remote"):
            loc_str = (loc_str + " (remote)").strip()
        url = f"https://jobs.smartrecruiters.com/{c['slug']}/{j.get('id','')}"
        yield j.get("name", ""), loc_str, url, (j.get("releasedDate", "") or "")[:10]


def _ats_workday(c):
    # Needs host + site (e.g. host="ing.wd3.myworkdayjobs.com", site="ICSGBLCOR").
    # tenant is the first label of the host. cxs endpoint is a POST.
    host, site = c["host"], c["site"]
    tenant = c.get("tenant") or host.split(".")[0]
    payload = {"appliedFacets": {}, "limit": 20, "offset": 0, "searchText": ""}
    d = json.loads(http_post_json(f"https://{host}/wday/cxs/{tenant}/{site}/jobs", payload))
    for j in d.get("jobPostings", []):
        ext = j.get("externalPath", "")
        url = f"https://{host}/{site}{ext}"
        yield j.get("title", ""), j.get("locationsText", ""), url, "recent"


ATS_FETCHERS = {
    "greenhouse": _ats_greenhouse,
    "ashby": _ats_ashby,
    "lever": _ats_lever,
    "smartrecruiters": _ats_smartrecruiters,
    "workday": _ats_workday,
}


# --- URL -> ATS detection ----------------------------------------------------
def detect_ats(url):
    """Given a careers/job URL, return (ats, slug_or_host_info) or (None, None).
    Operates on the original-case URL (Workday site codes are case-sensitive)."""
    I = re.IGNORECASE
    m = re.search(r"(?:boards\.|job-boards\.)?greenhouse\.io/(?:embed/job_board\?for=)?([A-Za-z0-9_-]+)", url, I)
    if "greenhouse.io" in url.lower() and m:
        return "greenhouse", m.group(1).lower()
    m = re.search(r"([A-Za-z0-9_-]+)\.greenhouse\.io", url, I)
    if m and m.group(1).lower() not in ("boards", "job-boards"):
        return "greenhouse", m.group(1).lower()
    m = re.search(r"jobs\.lever\.co/([A-Za-z0-9_-]+)", url, I)
    if m:
        return "lever", m.group(1).lower()
    m = re.search(r"jobs\.ashbyhq\.com/([A-Za-z0-9_.-]+)", url, I) or re.search(r"([A-Za-z0-9_-]+)\.ashbyhq\.com", url, I)
    if m:
        return "ashby", m.group(1).lower()
    m = re.search(r"jobs\.smartrecruiters\.com/([A-Za-z0-9_-]+)", url, I) or re.search(r"smartrecruiters\.com/v1/companies/([A-Za-z0-9_-]+)", url, I)
    if m:
        return "smartrecruiters", m.group(1)
    # Workday: host like ing.wd3.myworkdayjobs.com, optional locale (en-US), then the case-sensitive site code
    m = re.search(r"(([A-Za-z0-9_-]+)\.(wd\d+)\.myworkdayjobs\.com)/(?:[A-Za-z]{2}-[A-Za-z]{2}/)?([A-Za-z0-9_-]+)", url, I)
    if m:
        return "workday", {"host": m.group(1).lower(), "tenant": m.group(2).lower(), "site": m.group(4)}
    return None, None


def fetch_companies():
    out = []
    try:
        with open(COMPANIES_PATH) as f:
            reg = json.load(f).get("companies", [])
    except Exception as e:
        print(f"[companies] registry error: {e}", file=sys.stderr)
        return out
    for c in reg:
        if c.get("status") != "verified":
            continue
        if is_past_employer(c.get("name", "")):  # skip past employers unless boomeranged
            continue
        fn = ATS_FETCHERS.get(c.get("ats"))
        if not fn:
            continue
        try:
            for title, loc, url, posted in fn(c):
                out.append(norm_record(
                    title, c["name"], url, loc, classify_geo(loc),
                    posted or "recent", None, "", f"ats:{c['name']}",
                ))
        except Exception as e:
            print(f"[companies] {c['name']} ({c.get('ats')}) error: {e}", file=sys.stderr)
        time.sleep(0.25)
    return out


SOURCES = {
    "himalayas": fetch_himalayas,
    "jobicy": fetch_jobicy,
    "remotive": fetch_remotive,
    "remoteok": fetch_remoteok,
    "companies": fetch_companies,
}


# --- Dedup -------------------------------------------------------------------
def load_seen():
    try:
        with open(SEEN_PATH) as f:
            return json.load(f).get("seen", {})
    except Exception:
        return {}


def load_tracker_keys():
    keys = set()
    try:
        with open(TRACKER_PATH, newline="") as f:
            for row in csv.DictReader(f):
                if row.get("company") and row.get("role"):
                    keys.add(make_key(row["company"], row["role"]))
    except Exception:
        pass
    return keys


def save_seen(seen):
    with open(SEEN_PATH, "w") as f:
        json.dump({"seen": seen}, f, indent=2)


# --- Main --------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(
        description="Free API-driven remote-job scraper (targeting via scraper_config.json).")
    ap.add_argument("--eligible", action="store_true", default=True,
                    help="keep only your config's eligible_regions (default on)")
    ap.add_argument("--all-geos", action="store_true", help="disable geo filter")
    ap.add_argument("--source", default="", help="comma list: himalayas,jobicy,remotive,remoteok")
    ap.add_argument("--max", type=int, default=60, help="max results to present")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    ap.add_argument("--no-store", action="store_true", help="do not update seen_jobs.json")
    ap.add_argument("--boomerang", default="",
                    help="comma list of past employers to re-include (boomeranging), e.g. acme_corp,globex")
    ap.add_argument("--resolve", default="",
                    help="given a careers/job URL, print the detected ATS + slug for companies.json")
    args = ap.parse_args()

    if args.resolve:
        ats, info = detect_ats(args.resolve)
        if not ats:
            print("Could not detect a supported ATS from that URL.")
            return 1
        if ats == "workday":
            print(json.dumps({"ats": ats, **info}, indent=2))
        else:
            print(json.dumps({"ats": ats, "slug": info}, indent=2))
        return 0

    load_config()

    global BOOMERANG
    BOOMERANG = {slug(x) for x in args.boomerang.split(",") if x.strip()}

    chosen = [s.strip() for s in args.source.split(",") if s.strip()] or list(SOURCES)

    raw = []
    for name in chosen:
        fn = SOURCES.get(name)
        if not fn:
            print(f"[warn] unknown source: {name}", file=sys.stderr)
            continue
        got = fn()
        print(f"[{name}] fetched {len(got)}", file=sys.stderr)
        raw.extend(got)
        time.sleep(0.4)

    seen = load_seen()
    tracker = load_tracker_keys()

    # dedup within this run, then against seen + tracker
    by_key = {}
    dropped_geo = dropped_kw = dropped_dup = dropped_past = 0
    for r in raw:
        if not title_matches(r["title"]):
            dropped_kw += 1
            continue
        if is_past_employer(r["company"]):
            dropped_past += 1
            continue
        if not args.all_geos and r["global_remote"] not in ELIGIBLE_GEOS:
            dropped_geo += 1
            continue
        if r["key"] in seen or r["key"] in tracker:
            dropped_dup += 1
            continue
        by_key.setdefault(r["key"], r)  # first source wins

    results = list(by_key.values())
    geo_order = {"worldwide": 0, "home": 1, "eu": 2, "other": 3, "us_only": 4}
    results.sort(key=lambda r: (geo_order.get(r["global_remote"], 9), r["posted"]), reverse=False)
    results = results[: args.max]

    # store newly-seen
    if not args.no_store:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        for r in results:
            seen[r["key"]] = {
                "title": r["title"], "company": r["company"], "url": r["url"],
                "first_seen": today, "fit": "unrated", "status": "new",
                "geo": r["global_remote"], "source": r["source"],
            }
        save_seen(seen)

    print(f"[summary] {len(results)} new | dropped: {dropped_kw} non-people, "
          f"{dropped_past} past-employer, {dropped_geo} geo-ineligible, "
          f"{dropped_dup} already-seen", file=sys.stderr)

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        print(f"\n{'FIT':4} {'GEO':10} {'TITLE':40} {'COMPANY':22} POSTED")
        for r in results:
            print(f"{'':4} {r['global_remote']:10} {r['title'][:39]:40} {r['company'][:21]:22} {r['posted']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

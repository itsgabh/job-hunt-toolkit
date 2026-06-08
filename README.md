# Job Search Toolkit

An open, **profile-driven** Claude plugin for running a job search end to end — in **any
field**. You fill in **one** profile template, and eight skills personalize to you — JD
fit analysis, CV bullet tailoring, cover letters, an interview story bank, company
research, recruiter outreach, negotiation prep, and multi-role comparison. A free,
API-driven remote-jobs scraper rounds it out.

**No candidate data is baked in.** Every skill reads your `profile.md`. Out of the box
the profile is a blank template with placeholders; until you fill it in, the skills run
but produce generic output. Fill it in once and everything personalizes.

The toolkit is field-agnostic — engineering, sales, design, finance, operations,
marketing, or anything else. You supply your own profile content, resume variants, and
(optionally) scraper keywords; the skills adapt to whatever field you bring.

---

## What's in the box

### The 8 skills

1. **jd-fit-analyzer** — Scores a job description against your profile on a five-dimension
   hard-match rubric, gives a strategic-fit verdict, an apply/pass recommendation, and a
   resume-variant suggestion. The entry point: most workflows start here.
2. **cv-bullet-tailor** — Rewrites 3–5 high-leverage resume bullets to match a JD, two
   honest angles each, traced to specific JD signals. Never invents experience or inflates
   metrics. Picks up the fit analyzer's tailoring priorities.
3. **cover-letter-drafter** — Drafts a first-pass cover letter in your voice: 350–450
   words, one concrete proof story, four opener archetypes, a forbidden-phrase filter.
4. **interview-story-bank** — Builds, captures, and indexes CTAR-formatted behavioral
   interview stories tagged by competency, so you can pull the right story for the right
   question. Standard + elevator versions, plus watchouts.
5. **company-research-brief** — Produces a pre-interview brief: business snapshot, recent
   moves, a maturity read on the function you'd join, likely pain points, and 5–7
   stage-appropriate smart questions. Needs web search/fetch tools.
6. **recruiter-outreach-drafter** — Drafts channel-aware outreach (LinkedIn DM/InMail,
   email, Slack, Teams) in two genuinely different variants, with a follow-up suggestion.
7. **negotiation-prep** — Builds the comp comparison (equity haircuts, PTO-as-cash, tax
   bands), identifies BATNA, sets walk-away/target/aspirational numbers, drafts principled
   counter scripts, and treats flexibility as real comp. The highest-stakes skill.
8. **compare** — Weighs 2–3 roles side by side using the same rubric, surfaces the real
   trade-offs, and ends with a clear "prioritize X" call.

The skills are designed to chain: **jd-fit-analyzer → cv-bullet-tailor /
cover-letter-drafter → company-research-brief / interview-story-bank → negotiation-prep**,
with **compare** as the decision layer when multiple roles are live.

### The job scraper

`job_scraper/fetch_jobs.py` — a stdlib-only, free, API-driven scraper that pulls
remote-native roles from **Himalayas, Jobicy, Remotive, and Remote OK**, plus company ATS
career pages (Greenhouse, Ashby, Lever, SmartRecruiters, Workday) listed in
`companies.json`. It keyword-filters to your target roles, geo-filters to your eligible
tiers, excludes your former employers by default (opt back in with `--boomerang`), and
dedupes against what you've already seen and tracked. All targeting lives in a config
file — the Python source is field- and geography-agnostic.

```bash
# default run (uses your scraper_config.json, or a generic worldwide-remote search)
python job_scraper/fetch_jobs.py

# only specific sources, as JSON
python job_scraper/fetch_jobs.py --source himalayas,jobicy --json

# all geographies, more results
python job_scraper/fetch_jobs.py --all-geos --max 100

# detect a company's ATS + slug to add it to companies.json
python job_scraper/fetch_jobs.py --resolve https://jobs.lever.co/somecompany
```

Retarget it by copying `job_scraper/scraper_config.example.json` to
`job_scraper/scraper_config.json` and editing the fields: `role_keywords` /
`exclude_keywords` / `override_keywords` (role focus), `eligible_regions` / `home_country`
(geography), `jobicy_industry` / `remotive_category` / `himalayas_queries` (source-side
filters), and `past_company_slugs` (your former employers). The shipped example targets a
People/HR + EU search purely as an illustration — replace it with your own field. With no
`scraper_config.json` present, the scraper falls back to a generic worldwide-remote,
match-all search.

---

## Install

This is a standard Claude plugin. Two common ways to use it:

**As a plugin (skills available globally):**

```bash
git clone <your-fork-url> job-search-toolkit
# Point your Claude plugin config at the cloned directory, or copy the skills/
# directory into your Claude skills location.
```

**As skills in a project:** copy the `skills/` directory into your project's
`.claude/skills/` so Claude Code discovers them.

The scraper runs standalone with any Python 3 (no dependencies):

```bash
python job_scraper/fetch_jobs.py
```

See **SETUP.md** for the full step-by-step, including the all-important profile step.

---

## Personalize it (the one required step)

The skills are only as good as your profile. Before using them:

1. Copy `references/profile.template.md` to `references/profile.md`.
2. Fill in every `[BRACKETED]` placeholder with your real, defensible facts — identity,
   work authorization, current role, career arc, strengths, an honest gap inventory,
   career direction, values, flexibility needs, and voice.
3. Copy your filled-in `profile.md` into each `skills/<skill>/references/profile.md`
   (each skill ships self-contained). A one-line command is in **SETUP.md**.
4. Fill in the resume scaffolds in `skills/cv-bullet-tailor/references/original-resumes/`
   (Master / Specialist-IC / Non-profit / Consulting) with your actual resume content.

Your filled-in `profile.md` and resume content are **git-ignored** by default so you
don't accidentally publish your own data. Only the blank `.template` ships.

---

## Honesty by design

These skills are built to be honest, not flattering:

- No skill invents experience or inflates a metric — every claim traces to your `profile.md`.
- The fit analyzer scores real gaps as gaps; "apply" is earned, not default.
- Negotiation prep uses your real walk-away, not an aspirational fantasy.
- A forbidden-phrase filter strips corporate filler ("leverage" as a verb, "synergy",
  "wear many hats", "thrilled to") from anything written in your voice.

---

## License & attribution

MIT (see `LICENSE`) — free to use, modify, and redistribute with attribution. Built by
Gab Hollero ([@itsgabh](https://github.com/itsgabh)).

Built independently first, then iterated. After the initial build I borrowed specific
patterns (ATS endpoints, the application state machine, ATS resume rules) from Andrew
Shwetzer's `career-ops-plugin` (MIT). Mads Lorentzen's `ai-job-search` is a parallel
project I found later and compared notes with. See `ATTRIBUTION.md` for details.

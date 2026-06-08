# Setup

Step-by-step setup for the Job Search Toolkit. The only step you can't skip is
**filling in your profile** (Step 2) — the skills personalize entirely from it.

---

## 1. Clone

```bash
git clone <your-fork-url> job-search-toolkit
cd job-search-toolkit
```

No build step and no dependencies. The scraper uses only the Python 3 standard library.

---

## 2. Fill in your profile (required)

The skills read a `profile.md` that ships as a blank template. Fill it in with your own
real, defensible facts.

```bash
# 1. Create your working copy from the template
cp references/profile.template.md references/profile.md
```

Open `references/profile.md` and replace every `[BRACKETED]` placeholder. Fill in all
sections — keep the headings (skills reference them by name):

- **Identity** — name, location, contact, work authorization, geographic constraints,
  and any recurring extended-remote needs.
- **Current role** and **Career arc** — newest to oldest, with real scope and metrics.
- **Strengths & themes** — capabilities mapped to evidence.
- **Tool stack** — what you actually use.
- **Honest gap inventory** — be candid; the scoring skills depend on it.
- **Education & certifications.**
- **Career direction** — where you want to go next (drives strategic-fit scoring).
- **Values & working culture** — including hard flexibility requirements.
- **Voice & communication style** — how you actually write and speak.

Then propagate the filled-in profile into each skill (each skill ships self-contained):

```bash
# 2. Copy your filled-in profile into every skill
for d in skills/*/references; do cp references/profile.md "$d/profile.md"; done
```

Re-run that command whenever you update your profile.

---

## 3. Fill in your resume variants (for the CV tailor)

The CV bullet tailor only rewrites bullets that already exist in your resume files. Fill
in the four scaffolds with your actual resume content:

```
skills/cv-bullet-tailor/references/original-resumes/master.md        # neutral default
skills/cv-bullet-tailor/references/original-resumes/specialist-ic.md # senior-IC focus
skills/cv-bullet-tailor/references/original-resumes/non-profit.md    # mission-driven
skills/cv-bullet-tailor/references/original-resumes/consulting.md    # fractional/advisory
```

If you only maintain one resume, fill in `master.md` and the tailor will use it.

---

## 4. Optional: seed your story bank and example letters

These ship empty and fill over time:

- `skills/interview-story-bank/references/seed-stories.md` — captured CTAR stories. Run
  the interview-story-bank skill in capture mode to add them.
- `skills/cover-letter-drafter/references/example-letters.md` — keeper cover letters in
  your voice, for tone calibration. Paste revised drafts here as you produce them.

---

## 5. Install the skills

**As a plugin:** point your Claude plugin configuration at this directory.

**As project skills:** copy `skills/` into your project's `.claude/skills/` directory so
Claude Code discovers them. Then just talk to Claude naturally — paste a JD and ask
"should I apply", say "draft a cover letter for this", "build me a STAR story for
leading without authority", "they came back with €X, help me prep", etc. The skill
descriptions trigger automatically.

---

## 6. Configure the scraper (optional)

All scraper targeting lives in a config file — the Python source is field- and
geography-agnostic. Copy the worked example and edit it to match you:

```bash
cp job_scraper/scraper_config.example.json job_scraper/scraper_config.json
```

Then edit these fields in `job_scraper/scraper_config.json`:

- `role_keywords` / `exclude_keywords` / `override_keywords` — your role focus.
- `eligible_regions` / `home_country` — your eligible geographies and home country.
- `jobicy_industry` / `remotive_category` / `himalayas_queries` — source-side filters.
- `past_company_slugs` — your former employers (excluded by default; opt back in per run
  with `--boomerang <slug>`).

The shipped example targets a People/HR + EU search purely as an illustration — replace
every field with the terms and geography of your own field. With no `scraper_config.json`
present, the scraper falls back to a generic worldwide-remote, match-all search.

Add target companies to `job_scraper/companies.json`. Use `--resolve <careers-url>` to
detect a company's ATS and slug. Then run:

```bash
python job_scraper/fetch_jobs.py
```

Results are deduped against `job_scraper/seen_jobs.json` and an optional
`job_search_tracker.csv` (a CSV with `company` and `role` columns) — both are
git-ignored.

---

## What stays private

`.gitignore` excludes your filled-in `profile.md` copies, the scraper's working data,
your tracker CSV, and generated PDFs. Only the blank `.template` and empty scaffolds are
meant to ship. Double-check before you push a fork that your real profile isn't staged.

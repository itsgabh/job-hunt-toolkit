# Attribution

Built by Gab Hollero ([@itsgabh](https://github.com/itsgabh)).

`job-search-toolkit` started as an independent build: a personal job-search skill set
put together before it was needed. After building it, I came across two open-source
projects working the same problem and borrowed selectively from one of them. This file
records that honestly.

## Built first, then iterated

The eight skills and the profile-driven personalization model were built independently.
Roughly two weeks later I found the two projects below. Andrew Shwetzer's
`career-ops-plugin` contributed concrete patterns I adopted after the fact; Mads
Lorentzen's `ai-job-search` was a parallel project I compared notes with.

## Andrew Shwetzer — `career-ops-plugin` (MIT)

Patterns adopted from it after my own build:

- The ATS career-page endpoint patterns (Greenhouse, Ashby, Lever, SmartRecruiters,
  Workday) used by the job scraper.
- The application state-machine framing for an application's lifecycle.
- The `ats-rules` keyword/format guidance used by the CV bullet tailor (noted inline in
  `skills/cv-bullet-tailor/references/ats-rules.md`).
- The Claude-plugin packaging conventions.

## Mads Lorentzen — `ai-job-search` (MIT)

A parallel, independently-built job-application framework (originally for the Danish
market) that I discovered after building my own. No code from it is included in this
package; it is acknowledged here as convergent prior art that arrived at a similar
"profile-driven, repeatable apply workflow" shape.

## What's original here

- The eight-skill job-search set (JD fit analysis, CV bullet tailoring, cover-letter
  drafting, interview story bank, company research brief, recruiter outreach,
  negotiation prep, multi-role compare) with their scoring rubrics, voice rules, and
  CTAR-based interview framing.
- The free, API-driven remote-jobs scraper (`job_scraper/fetch_jobs.py`) pulling from
  Himalayas, Jobicy, Remotive, and Remote OK plus company ATS boards, with config-driven
  keyword and geo filters.
- The profile-template personalization model: no candidate data is baked into the
  skills; every skill reads a user-filled `profile.md`.

This project ships under the MIT License (see `LICENSE`): anyone is free to use, modify,
and redistribute it, keeping the attribution above. Provided in good faith; not an
endorsement by the named authors.

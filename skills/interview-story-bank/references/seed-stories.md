---
type: skill-reference
used_by_skills: [interview-story-bank]
status: empty-starter
---

# Story Bank (your CTAR stories)

This is your personal bank of CTAR-formatted interview stories. It ships **empty** —
you fill it as you build and refine stories. The interview-story-bank skill reads this
file to retrieve a matching story for a behavioral question (Mode 1) and writes to it
when you capture a new one (Mode 2).

How to populate it:

1. Run the skill in **capture mode** ("capture this story: …") to format a real
   experience as CTAR and tag it.
2. Or run **build mode** ("CTAR story for [competency]") — the skill drafts one from
   your `profile.md` and you paste the keeper here.
3. Refine each story until it sounds like something you would actually say out loud.

Only use real experiences traceable to your `profile.md`. No invented details, no
inflated metrics, no composite stories that did not happen.

---

## Entry template

Copy this block for each story.

```
## [Story title]

**Primary competency:** [one main tag from competency-taxonomy.md]
**Secondary competencies:** [other tags]
**Source role:** [employer / context] ([dates])

### Standard (150–200 words)

**Context.** [1–2 sentences — operating environment, scale, constraint.]
**Task.** [1 sentence — often implicit; state only if non-obvious.]
**Action.** [3–5 sentences, verb-led, concrete, scope-specific.]
**Result.** [1–2 sentences — quantified where real, qualitative where not — plus a
lesson-learned line.]

### Elevator (60 words)

[Compressed version — same shape, tighter.]

### What this story shows

[One line — the angle to keep in your head if drilled.]

### Watchouts

- **Likely follow-up:** [the obvious next question + a one-line short answer]
- **Handle carefully:** [a setback, a misstep, or a constraint to handle with care]
```

---

## Stories

_(empty — add your first story above the template, or run the skill in capture mode)_

---

## Coverage notes

As you add stories, track which competencies have strong coverage (3+ stories) and
which are sparse (0–1). The skill flags gaps in Mode 3 (Index).

---
name: interview-story-bank
description: Maintains and produces a bank of CTAR-formatted interview stories from your experience (in references/profile.md), tagged by competency, so you can pull the right story for the right behavioral question. Operates in three modes — build a story for a question, capture a new story from an experience, or index existing stories. Use this whenever you ask for an interview story, say "STAR / CTAR story for [competency]," say "build me a story about [experience]," ask what stories you have for a theme, paste an experience and ask to format it as CTAR, mention an upcoming behavioral interview, or say any "tell me about a time when…" framing. Trigger even if you don't name the skill — "I need an answer for the team leadership question," "what should I say if they ask about ambiguity," "capture this story" all count.
---

# Interview Story Bank

## What this skill does

Three modes, one skill. Behavioral interviews ask the same shape of question across companies; the answer is a CTAR-formatted story drawn from real experience. This skill stores your stories, tags them by competency, and produces the right one for the right question — plus the elevator version, the watchouts, and the follow-up question to anticipate.

**Mode 1 — Build/retrieve.** You ask for a story to answer a specific question or competency. Pull from the seed bank if a match exists; build from `profile.md` if not.

**Mode 2 — Capture.** You describe an experience; the skill formats it as CTAR and tags it for future use.

**Mode 3 — Index.** You ask what stories you have for a theme. The skill returns the list and flags coverage gaps.

**Mode 4 — Question pull.** Given a role title and JD, surface the 5–8 most likely interview questions (common behavioral + role-specific) so you know what to practice before the interview.

## When to use

Trigger whenever you:

- Ask for an interview story / answer for a behavioral question
- Say "STAR / CTAR story for [competency]"
- Say "build me a story about [experience]"
- Ask what stories you have for [theme]
- Paste an experience and ask to format it as CTAR
- Mention an upcoming behavioral interview and want prep
- Use "tell me about a time when…" framing
- Ask "what questions should I prepare for [role]" or "what will they likely ask me"

The skill is mode-aware. Infer the mode from how you phrase the request; ask for clarification only if genuinely ambiguous.

## Inputs (vary by mode)

### Mode 1 — Build/retrieve

- The interview question or competency ("tell me about a time you led without authority")
- Optionally: which role / JD this is for, to bias the story selection

### Mode 2 — Capture

- Raw experience description (a few sentences, doesn't need to be polished)
- Optionally: which competencies the story should be tagged with

### Mode 3 — Index

- A theme or competency to search by, or "show me all stories"

## Required preparation

Read in order:

1. `references/profile.md` — canonical profile. Source of truth for what's actually true.
2. `references/voice-and-style.md` — shared voice rules.
3. `references/ctar-guide.md` — when CTAR fits and when it doesn't, per-element guidance, worked examples.
4. `references/competency-taxonomy.md` — the list of competencies stories are tagged against. Maps interview questions to competencies.
5. `references/seed-stories.md` — the existing bank. Read for both content (matching) and tone calibration.

## Workflow

### Mode 1 — Build/retrieve story for a question

**Step 1.** Map the question to one or more competencies from `competency-taxonomy.md`. Most behavioral questions touch one or two.

**Step 2.** Search `seed-stories.md` for stories tagged with those competencies. If one or more matches, pick the best fit for the question + role context.

**Step 3.** If no good match exists, build one from `profile.md`. Use a real experience that demonstrates the competency. If profile has nothing strong, say so and ask you for context — don't invent.

**Step 4.** Produce two lengths.

- **Standard (150–200 words)** for the main interview answer
- **Elevator (60 words)** for follow-ups or "give me the short version"

**Step 5.** Add a "what this story shows" line — one sentence on the underlying angle, so you can remember the framing if drilled.

**Step 6.** Add watchouts. Anticipate the obvious follow-up question and the one element of the story to handle carefully (a setback, a constraint, a misstep).

### Mode 2 — Capture a new story

**Step 1.** Listen for the four CTAR elements in your raw description. If any are missing, ask focused follow-up questions **one at a time**:

- "What was the situation? When did this happen and what was the team / context?"
- "What was your specific responsibility — what was yours to do?"
- "What did you actually do? What were the moves?"
- "What was the outcome? Any metric, or a qualitative result?"

Don't bombard with all four at once. One question, wait for the answer, then the next.

**Step 2.** Draft the story in 150–200 words with the four CTAR elements visible.

**Step 3.** Tag with 2–4 competencies from `competency-taxonomy.md`. Confirm the tags with you before saving.

**Step 4.** Output in a format you can paste into your story bank as a new entry, with frontmatter.

### Mode 4 — Question pull for a role

**Step 1.** Parse the JD for: role level, scope signals, key responsibilities, any competency language used explicitly.

**Step 2.** Pull the 3–4 most common behavioral questions for this role type from `competency-taxonomy.md` — questions that appear in almost every interview at this level.

**Step 3.** Pull 2–4 role-specific questions derived from JD keywords. If the JD says "scale onboarding globally," the question is "Tell me about a time you built or scaled an onboarding program."

**Step 4.** For each question, check `seed-stories.md` for an existing story match and note it.

**Step 5.** Flag any question with no good story match — these are the prep gaps to address before the interview.

### Mode 3 — Index existing stories

**Step 1.** Search `seed-stories.md` by competency or theme. Return matching stories with their titles and one-line summaries in a table.

**Step 2.** Flag coverage gaps. If a common competency has fewer than two stories, say so: "You only have one story for [competency]. Worth capturing another?"

## Output format

### Mode 1 — Build/retrieve

````markdown
# Story: [story title]

**Question being answered:** [the question or competency]

**Primary competency:** [one main tag]
**Secondary competencies:** [other tags]

---

## Standard answer (150–200 words)

**Context.** [1–2 sentences — operating environment, scale, constraint]

**Task.** [1 sentence — often implicit; state only if non-obvious]

**Action.** [3–5 sentences, verb-led, concrete, scope-specific]

**Result.** [1–2 sentences — quantified where real, qualitative where not — and a lesson-learned line]

---

## Elevator version (60 words)

[Compressed version — keeps the same shape but tighter]

---

## What this story shows

[One line — the angle to keep in your head if drilled]

## Watchouts

- **Likely follow-up:** [the obvious next question + a one-line short answer]
- **Handle carefully:** [the part of the story that needs care — a setback, a misstep, a constraint]
````

### Mode 2 — Capture

````markdown
# New story captured: [story title]

[CTAR-formatted story as above — 150–200 words]

---

## Suggested competency tags

- [tag 1]
- [tag 2]
- [tag 3]

---

## Suggested YAML frontmatter for your story bank

```yaml
title: [story title]
date: [YYYY-MM-DD]
competencies: [tag1, tag2, tag3]
role: [employer or context]
length: [standard / elevator]
```
````

### Mode 4 — Question pull

````markdown
# Interview question prep: [Role Title] at [Company]

## Common behavioral questions (appear in most interviews at this level)

| Question | Competency | Story match |
|---|---|---|
| [question] | [competency tag] | [story title, or "No match — prep needed"] |
| ... |

## Role-specific questions (derived from this JD)

| Question | JD signal that prompted it | Story match |
|---|---|---|
| [question] | [JD phrase] | [story title, or "No match — prep needed"] |
| ... |

## Prep gaps

Questions with no story match — address these before the interview:

- [question] — suggested competency to build a story around: [competency]
````

### Mode 3 — Index

````markdown
# Story index for: [competency / theme]

| Story title | Primary competency | Source role | Length variants |
|---|---|---|---|
| ... | ... | ... | ... |

## Coverage notes

- **Strongest coverage:** [competencies with 3+ stories]
- **Sparse coverage (consider capturing more):** [competencies with 0–1 stories]
````

## Critical rules

- **Truth only.** Every story traces to a real experience in `profile.md` or a story you have captured. No invented details, no inflated metrics, no composite stories that didn't happen.
- **CTAR balance.** Action and Result get most of the space. Context is one or two sentences. Task is often implicit — name it only when non-obvious.
- **Lesson-learned line is mandatory.** Result includes one line of reflection or growth signal. Interviewers want self-awareness, not just outcomes.
- **One primary competency per story.** Each story has a clear primary tag. Secondary tags are fine; "this story is the go-to for five different competencies" usually means the story isn't sharp enough.
- **Don't force CTAR.** If a story doesn't fit cleanly, say so. Some experiences are better as anecdotes than as structured stories.
- **Watchouts in Mode 1 are mandatory.** Anticipating the follow-up is half the value.
- **One question at a time in capture mode.** Don't bombard.
- **No emoji.** Stories are spoken in interviews. Clean text only.
- **Voice preservation.** Same forbidden-phrase list as the resume and cover letter — no "leverage" as verb, no "synergy," no overclaiming. See `voice-and-style.md`.

## What "good" looks like

- you can deliver the standard version in 90 seconds without notes
- The elevator version is the same story, not a different one
- The watchouts section anticipates the follow-up you are most likely to get
- Every claim in the story traces to a real moment
- The lesson-learned line sounds reflective, not performative

## What "bad" looks like

- Stories that span multiple unrelated events stitched together
- CTAR-by-template — context bloat, vague action, soft result
- Lesson-learned lines that sound like a LinkedIn post
- Forbidden phrases sneaking in
- Watchouts section missing or generic ("they might ask a follow-up")

## Companion skills

- **`cv-bullet-tailor`** — sibling. When a bullet on the resume corresponds to a story in this bank, the framing should be consistent. The story is the long form; the bullet is the headline.
- **`cover-letter-drafter`** — sibling. When the cover letter's proof paragraph leans on a story you will also tell in interviews, pull the same CTAR shape from here for consistency across surfaces.
- **`jd-fit-analyzer`** — upstream. The tailoring priorities can hint at which competencies the interview will probe.

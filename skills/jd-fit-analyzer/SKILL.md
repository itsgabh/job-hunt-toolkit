---
name: jd-fit-analyzer
description: Analyze a job description against the user's profile (from references/profile.md) and produce a side-by-side hard match score and strategic fit verdict, plus an apply/pass recommendation and resume variant suggestion. Use whenever the user shares a JD (pasted text, link, or uploaded file), asks "should I apply", "is this a fit", "what do you think of this role", "rate this job", or any variant of evaluating a specific role. Trigger even if the user does not explicitly say "analyze fit" — if there is a JD in the conversation and they are considering it, run the skill.
---

# JD Fit Analyzer

This skill analyzes a single job description and produces a structured side-by-side verdict: hard match score (requirements vs. evidence) and strategic fit verdict (does this role advance your stated direction).

## When to use

Trigger whenever you:
- Paste or upload a JD
- Share a link to a job posting
- Ask if a role is worth applying to
- Ask for a fit assessment, gap analysis, or apply/pass recommendation
- Mention a specific role you're considering and want a take
- Compares two roles (run the skill on each, then synthesize)

Do not trigger for general career advice with no specific role attached.

## Inputs

Required:
- A JD (full text or link). If a link, fetch it first.

Optional context you might add:
- Why this role is on your radar
- A specific concern you want you to weigh in on
- Whether you're actively job-hunting or passively curious

## Required preparation

Before producing the analysis, read these three reference files in order:

1. `references/profile.md` — your canonical profile (current role, career arc, strengths, honest gap inventory, career direction, voice, preferences). This is the canonical record of who you are professionally.
2. `references/rubric.md` — How to score hard match (five weighted dimensions, 0–10 each) and how to derive the strategic fit verdict (five direction-alignment checks, qualitative label).
3. `references/resume-variants.md` — When to recommend each of your four resume variants (Master / Specialist-IC / Non-profit / Consulting).

Always read all three. They are sized to fit together in context and each informs different parts of the output.

## Workflow

### Step 1: Parse the JD

Extract from the JD:
- Company name, role title
- Location and work model (remote / hybrid / onsite, and if hybrid, where)
- Reporting line if visible (who you'd report to, who reports to you)
- Compensation signals (salary range, equity, benefits, contract type)
- Required experience (years, role level)
- Required tools / systems (named platforms)
- Domain / industry
- Scope indicators (headcount supported, geographic reach, programs owned)
- Leadership component (IC, manager, hybrid IC + lead, manager-of-managers)
- Mission signals (is the company purpose-driven, mission-led, non-profit?)
- Red flags: vague responsibilities, scope creep, mismatched seniority, unclear comp, "wear many hats" without compensation, single-person function/team with executive expectations
- Green flags: clear scope, mission resonance, AI-forward signals, async-first, geo that fits your profile

If anything critical is missing from the JD (no location, no scope, no comp signal), note it in the snapshot.

### Step 2: Hard match scoring

Use the rubric in `references/rubric.md`:
- Score each of 5 dimensions out of 10
- Compute weighted overall (formula in rubric.md)
- Build the requirements vs. evidence table
- Classify gaps as hard or soft

Be honest. Inflated scores are useless to you and erode the skill's value. If a JD calls for something you don't have, score it accordingly.

### Step 3: Strategic fit verdict

Run the seven direction-alignment checks in `references/rubric.md`:
1. Broader scope than current?
2. Leadership component?
3. Values & working culture alignment?
4. Flexibility & geographic freedom? (Critical: does it meet the extended-remote needs in your profile, if any?)
5. Consulting compatibility?
6. Mission / impact alignment?
7. Direction match overall (Forward / Lateral / Sideways / Backward)?

Pick one verdict label: Strong fit (forward) / Stretch fit aligned / Lateral / Step sideways / Step back.

Check the hard-pass override on flexibility — if check #4 is a clear "No," cap the recommendation at Watchlist regardless of hard-match strength.

### Step 4: Recommendation

Apply the recommendation matrix in `references/rubric.md` to derive: Apply / Apply with reservations / Watchlist / Pass.

Check override conditions (geographic hard pass, hard gap deal-breakers, "Step back" ceiling).

### Step 5: Resume variant recommendation

Use the decision tree in `references/resume-variants.md`. Pick one variant, justify in one line.

### Step 6: Top 3 tailoring priorities

Concrete tailoring moves for this specific JD. Not generic ("customize your resume") — specific ("lead with the specific tools/systems the JD emphasizes that you actually have").

### Step 7: Smart interview questions

If the recommendation is Apply or Apply with reservations, suggest 3–5 questions you should ask if you progress. These should probe key uncertainties from the JD (vague scope, unclear team structure, ambiguity about leadership opportunity, compensation philosophy of the org, etc.). They should be smart enough that asking them visibly signals you read the JD carefully.

Skip this section for Watchlist / Pass.

## Output format

Use this exact structure. Verdict block FIRST so you can decide in 30 seconds, then detail. Do not deviate.

```
# JD Fit Analysis: [Company] — [Role Title]

## Verdict

| | Hard Match | Strategic Fit |
|---|---|---|
| **Score** | [X.X/10 — Label] | [Verdict label] |
| **Recommendation** | [Apply / Apply with reservations / Watchlist / Pass] | |
| **Resume variant** | [Master / Specialist-IC / Non-profit / Consulting] | |

**One-line bottom line**: [single sentence — what this role is and what to do about it]

## Role snapshot

- **Company**: [name + one-line context]
- **Role**: [title + IC | Manager | Hybrid]
- **Location / work model**: [details, with extended-remote flexibility note if relevant]
- **Reporting line**: [if visible, else "Not specified"]
- **Comp signals**: [salary / equity / benefits visible, or "Not disclosed"]
- **Headline flags**:
  - Strong: [bullet list of green flags]
  - Mixed: [bullet list of yellows]
  - Risk: [bullet list of reds]

## Hard match detail

### Score breakdown
- Required experience: X/10
- Required tools/systems: X/10
- Domain/industry: X/10
- Seniority/scope: X/10
- Geographic/legal: X/10
- **Overall**: X.X/10 — [Label]

### Requirements vs. evidence

Color-code each row: **G** = solid match with a ready interview example, **Y** = partial or positionable, **R** = real gap.

| Requirement | G/Y/R | Have it? | Evidence | Example ready / gap note |
|---|---|---|---|---|
| [requirement 1] | G/Y/R | Yes/Partial/No | [from profile.md] | [story title or gap framing] |
| ... |

The G/Y/R column is the interview-prep handoff: R rows need a story built; Y rows need a framing note; G rows are ready.

### Gaps
- **Hard gaps** (must-address): [list, or "None identified"]
- **Soft gaps** (positionable): [list, or "None identified"]

## Strategic fit detail

| Check | Verdict | Why |
|---|---|---|
| Broader scope than current | Yes / Partial / No | [one line] |
| Leadership component | Yes / Partial / No | [one line] |
| Values & working culture | Yes / Partial / No | [one line] |
| Flexibility & geographic freedom (extended-remote / location needs) | Yes / Partial / No | [one line — flag if "No"] |
| Consulting compatibility | Yes / Partial / No | [one line] |
| Mission / impact alignment | Yes / Partial / No | [one line] |
| Direction match overall | Forward / Lateral / Sideways / Backward | [one line] |

## Tailoring priorities

Top 3 priorities for tailoring the resume to this JD:
1. [specific tailoring move]
2. [specific tailoring move]
3. [specific tailoring move]

*For actual bullet rewrites, hand off to the CV bullet tailor skill.*

## Smart interview questions

(Skip this section if Watchlist or Pass.)

1. [question]
2. [question]
3. [question]
[4–5 optional]
```

## Critical rules

- **Be honest**. If something is a real gap, say so. you are allergic to inflated scoring.
- **No emoji** in the output. Use words: `Yes` / `Partial` / `No`, `Strong` / `Mixed` / `Risk`.
- **Cite evidence** from `profile.md` — don't invent experience or stretch claims.
- **Strategic fit is not a score**, it's a qualitative verdict. Don't try to make it numeric.
- **Length discipline**: a full analysis is 700–1000 words. Don't pad. Each bullet earns its place.
- **Direction first**: when in doubt about strategic fit, weight scope, leadership, values, and flexibility over title or comp.
- **Geographic hard pass**: any role requiring relocation outside the geography your profile allows is an automatic Pass. Flag clearly in snapshot.
- **Extended-remote flexibility cap**: any role that mandates in-office hybrid cadence with no remote-from-abroad option caps the recommendation at Watchlist, because it blocks the extended-remote-from-abroad needs in your profile.
- **Don't recommend Apply for a role with hard gaps that screen-out**. If you would be filtered at application stage by a requirement you don't meet, recommend Pass or Watchlist.
- **Named-tool penalty**: if a specific platform is listed as the key project (not just under qualifications), score it on actual hours not analogue. See rubric.md for the rule.
- **Tailoring is a handoff**, not this skill's job. Surface the top 3 tailoring priorities. The CV bullet tailor skill does the actual rewrites.

## What "good" looks like

A good output:
- Lets you decide in under two minutes whether to apply
- Surfaces the one or two things you didn't notice in the JD
- Names the trade-off honestly (e.g., "close hard match but lateral; if you're looking to keep optionality while consulting on the side, this works")
- Recommends one variant with a one-line reason, not "consider Master or Specialist-IC depending on..."

A bad output:
- Hedges on the verdict
- Lists every requirement without prioritizing the discriminators
- Repeats JD content back at you
- Uses corporate filler ("This role offers an exciting opportunity to...")

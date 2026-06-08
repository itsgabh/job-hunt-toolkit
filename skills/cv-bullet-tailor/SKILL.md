---
name: cv-bullet-tailor
description: Rewrites specific resume bullets to align with a job description — without inventing experience, inflating metrics, or losing your voice. Use this whenever you paste a JD and asks to tailor / rewrite / customize / "make this fit" your resume; whenever you reference an earlier JD fit analysis and asks for the actual rewrites; or whenever you want 2-3 high-leverage bullets reshaped for a specific role. Trigger even when you don't name the skill — "rewrite these bullets," "tailor my resume for X," "front-load AI work on this one," "make my resume fit this JD" all count. Don't trigger for generic resume-writing advice with no specific JD in hand — this skill needs a target role to do its job.
---

# CV Bullet Tailor

## What this skill does

Takes a JD (or a `jd-fit-analyzer` output) plus a chosen resume variant, then produces targeted rewrites for 3–5 high-leverage bullets. Each rewrite ships with two genuinely-different angles and a one-line rationale tracing it to a specific JD signal.

This is the natural follow-up to `jd-fit-analyzer`. The jd-fit-analyzer surfaces three tailoring priorities; this skill does the actual rewrites.

## When to use

Trigger whenever you:

- Paste a JD and asks to tailor, rewrite, or customize your resume
- Reference an earlier JD fit analysis and asks to "make the tailoring changes" or "do the rewrites"
- Name specific bullets to focus on, or asks for "a full pass"
- Ask to lean into a specific theme on your resume for a role ("lead with AI/automation," "front-load your scale-up work")

Do not trigger for:

- Generic resume advice with no target JD ("how do I make my resume stronger")
- Full resume rewrites from scratch — the four variants are already the source of truth
- LinkedIn profile rewrites — different surface, different voice calibration

## Inputs

Required:

- A JD (pasted text, file, or link you provide) **or** an existing `jd-fit-analyzer` output
- A resume variant to start from: **Master**, **Specialist-IC**, **Non-profit**, or **Consulting**
  - If a JD fit analysis was provided, use its variant recommendation as the default
  - If not, ask you which variant — or propose one and confirm

Optional:

- Specific bullets to focus on (otherwise the skill picks 3–5 with the highest leverage)
- A focus theme ("lead with AI work," "front-load your scale-up work," "neutralize a named-tool gap")

## Required preparation

Before drafting anything, read these in order:

1. `references/profile.md` — the canonical profile. The authoritative record of what's actually true. No claim in any rewrite can go beyond what's here or in the original resume.
2. `references/voice-and-style.md` — voice attributes, forbidden phrases, verb preferences. Run the "would you actually say this" check on every rewrite line before shipping it.
3. `references/ctar-guide.md` — when to apply CTAR (Context → Task → Action → Result) and when to skip it.
4. `references/original-resumes/<variant>.md` — load only the variant being tailored. The bullets you rewrite must trace back to bullets that already exist there.
5. `references/ats-rules.md` — ATS keyword and formatting rules. Apply the keyword-mirroring rules to every rewrite so the bullets survive an automated parse.

If a JD fit analysis was provided, read its "Tailoring priorities" section first. Those three priorities are the spine of the rewrite plan.

## Workflow

### Step 1 — Identify tailoring scope

If a JD fit analysis was provided, lift its three tailoring priorities directly. They were derived from the same profile, so they hold.

If only a JD was provided, do a short derivation: read the JD's "what you'll do" and "what we're looking for" sections, then match the most-emphasized signals against the profile. Pick the three highest-leverage themes to target.

Then identify which 3–5 bullets in the chosen variant carry those themes most clearly. The targets are the bullets where a rewrite genuinely changes how a recruiter reads them — not bullets that are already serving the JD as-is, and not bullets too far from the JD's emphasis to be worth lifting.

Why 3–5: most of the resume is fine for any given JD. Rewriting more than that usually means the variant is wrong, not the bullets. See Step 6.

### Step 2 — Produce two rewrites per targeted bullet

For each bullet, draft two genuinely-different angles:

- **Rewrite A** leans on one thread (e.g., the AI / automation angle)
- **Rewrite B** leans on a different thread (e.g., the scale / scope angle)

Both must be honest. Both must trace to claims already in the profile or the original resume. The two should give you a real choice — not two near-duplicates of the same idea.

If the JD only has one dominant signal and a second angle feels forced, that's a signal the bullet doesn't earn a rewrite at all. Drop it from the targeted set and move on. One strong rewrite plus an apology is worse than no rewrite.

Each rewrite gets a one-sentence **Why** that names the specific JD signal it serves. If you can't write that sentence cleanly, the rewrite isn't earning its place.

### Step 3 — Apply CTAR where it fits

CTAR (Context → Task → Action → Result) is your preferred frame when a bullet describes a real initiative. See `references/ctar-guide.md` for the full rules.

Use CTAR when:

- The bullet describes a specific project or initiative
- A measurable result exists
- The action verb chain matters for clarity

Skip CTAR when:

- The bullet is a general ownership statement ("Owned the end-to-end process")
- It's a tool list or a skills summary
- It's a multi-initiative summary bullet covering several projects at once

Don't force CTAR onto a bullet just because the format looks tidy. CTAR bloat — long context, vague action, soft result — is worse than a punchy non-CTAR bullet.

### Step 4 — Reshape the summary paragraph (if useful)

If the JD's framing is meaningfully different from the variant's default summary, draft a revised summary paragraph. Show original vs. revised side by side, with a one-line **Why**.

If the variant's summary already serves the JD, leave it alone and say so in the "What was NOT changed" section.

### Step 5 — Reorder the skills line (if useful)

If JD-relevant tools are currently buried mid-line in the skills section, draft a revised order with those tools moved up front. Show original vs. revised.

If the order already serves the JD, leave it alone. The skills line should never invent tools you don't have.

### Step 6 — Check whether the variant is fighting the JD

After drafting, step back and ask: are these rewrites all fighting the same friction?

Recommend switching variants when either holds:

- More than roughly a third of the variant's bullets would need rewriting to serve the JD, or
- The rewrites are all working around the variant's framing rather than the bullet wording (e.g., the Master summary frames you as a generalist but the JD wants a senior IC — that's a positioning problem, not a bullet problem)

When recommending a switch, name the variant to try instead and the one-line reason. Don't switch silently; surface the call so you decides.

## Output format

Use this template exactly. Verdict-style summary at the top so you can decide in 30 seconds whether to read the rest.

````markdown
# CV Tailoring: [Company] — [Role Title]

**Variant tailored:** [Master / Specialist-IC / Non-profit / Consulting]
**Bullets rewritten:** [N]
**Variant switch recommended?** [Yes — try X / No]

---

## Tailoring priorities

If a JD fit analysis was provided, lift its three tailoring priorities verbatim — they're already action-oriented and stable. If only a JD was provided, derive three priorities inline. Each priority is one numbered line, action-oriented (a tailoring move, not a theme).

1. [tailoring move — e.g., "Reorder skills line to lead with the specific tools/systems the JD emphasizes that you actually have"]
2. [tailoring move]
3. [tailoring move]

---

## Summary paragraph

[Include this block only if reshaping the summary. Otherwise skip.]

**Original:**
> [original paragraph]

**Revised:**
> [revised paragraph]

**Why:** [one sentence — what JD signal this serves]

---

## Bullet rewrites

### Bullet 1 — [section / role / line reference]

**Original:**
> [bullet text from the chosen variant]

**Rewrite A:**
> [rewrite — one angle]

**Rewrite B:**
> [rewrite — a different angle]

**Why:** [one sentence — what JD signal these rewrites serve, and what differs between A and B]

### Bullet 2 — [section / role / line reference]
[same structure]

### Bullet 3 — [section / role / line reference]
[same structure]

[Continue for 3–5 bullets total. If fewer than 3 bullets earn rewrites, ship what earned the spot and note in the "What was NOT changed" section why the others didn't.]

---

## Skills line revision

[Include this block only if reordering the skills line. Otherwise skip.]

**Original:**
> [skills line]

**Revised:**
> [revised — JD-relevant tools moved earlier]

---

## Summary of changes applied

- [one-line summary]
- [one-line summary]
- [one-line summary]

## What was NOT changed (and why)

- [Section]: [one-line reason — e.g., "Education and certifications — not JD-relevant"]
- [Section]: [one-line reason]
- [Section]: [one-line reason]
````

## Critical rules

These are the gates. Run every rewrite through them before shipping.

- **No invention.** Every rewrite must trace to a claim in `profile.md` or the original resume. If the JD asks for something you don't have, the rewrite cannot create it. Surface the gap honestly instead.
- **No metric inflation.** Whatever the original number is, it stays. Don't round it up. Don't add a percentage that wasn't in the original. Don't add a "%" where the original said "improved."
- **Voice preservation.** Pass the "would you actually say this in a Slack message" test on every line. See `voice-and-style.md` for the forbidden-phrase list (no "leverage" as verb, no "synergy," no "wear many hats," no "thrilled to," etc.).
- **Two angles, or skip the bullet.** If a second angle has to be forced, the bullet isn't a high-leverage target. Drop it. The two-angle rule earns you a real choice; one angle plus apology doesn't.
- **CTAR balance.** When CTAR fits: one line of context, an action-led verb chain, a quantified result. Avoid CTAR bloat. A rewritten CTAR bullet should be roughly the length of the original, not double.
- **Don't rewrite the whole resume.** 3–5 high-leverage bullets is the target. If you find yourself eyeing the tenth, the variant is wrong — recommend switching at Step 6.
- **Trace every change.** The "Why" line on each rewrite is mandatory. No "Why" line means the rewrite hasn't earned its place.
- **Honest about what wasn't changed.** The "What was NOT changed" section is mandatory. It builds trust that the skill made deliberate choices, not lazy ones.
- **Emoji default: none.** Default to no emoji; if your profile defines a deliberate exception, respect it.

## What "good" looks like

- you can pick A or B for each bullet in under a minute
- Rewrites read like you wrote them in a Slack message, not like ChatGPT wrote them
- The tailoring is concrete and traces cleanly to specific JD signals
- The skill names a variant switch when the variant is genuinely fighting the JD

## What "bad" looks like

- Generic improvements that could apply to any JD ("strengthen the action verbs")
- Inflated metrics, stretched scope, invented experience
- "Leveraged cross-functional synergies to drive transformational outcomes" energy
- Rewriting ten bullets when the variant was wrong to begin with
- A and B are two slightly-different versions of the same angle

## Companion skills

- **`jd-fit-analyzer`** — runs upstream. Produces the verdict, the variant recommendation, and the three tailoring priorities that this skill turns into actual rewrites.
- **`cover-letter-drafter`** — runs downstream. Draws on the same profile and voice rules.

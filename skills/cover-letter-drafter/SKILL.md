---
name: cover-letter-drafter
description: Drafts a first-pass cover letter in your voice given a JD (or a JD fit analysis), warm-but-direct, 350–450 words, with one specific proof story and a direct close. Use this whenever you ask to draft / write / generate a cover letter, say "cover letter for [company/role]," paste a JD and ask to "draft something for this," or reference an earlier JD fit analysis and ask for the letter. Trigger even when you don't explicitly name the skill — "write me something for this role," "give me a first pass at the letter," "draft the application" all count. Don't trigger for generic "how to write cover letters" advice with no specific JD in hand.
---

# Cover Letter Drafter

## What this skill does

Produces a first-draft cover letter for a specific role, in your voice: warm-but-direct, systems-oriented, understated impact, no corporate filler. Target length 350–450 words. One concrete proof story, one specific reason for this company at this time, one direct close. Also returns one alternative opener in a different style so you have an A/B choice on the hook.

## When to use

Trigger whenever you:

- Ask to draft, write, or generate a cover letter
- Say "cover letter for [company/role]"
- Paste a JD and ask to "draft something for this"
- Reference an earlier JD fit analysis and ask for the letter

Do not trigger for generic cover-letter advice with no target JD.

## Inputs

Required:

- A JD (text, link, or file) **or** an existing `jd-fit-analyzer` output

Optional:

- A specific angle to lead with ("lead with the AI tooling work")
- An opener style preference (problem / story / direct fit / why-this-company)
- A connection or referral context ("a contact from their team flagged this to me")

## Required preparation

Read in order:

1. `references/profile.md` — canonical profile. No claim in the letter can go beyond what's here.
2. `references/voice-and-style.md` — voice rules and forbidden phrases. Run the "would you say this in a Slack message" check on every line.
3. `references/cover-letter-patterns.md` — four opener archetypes, three-paragraph structure, common pitfalls per archetype.
4. `references/example-letters.md` — starter set of three reference letters in your voice covering different opener styles. Read for tone calibration, not as templates to copy.

## Workflow

### Step 1 — Read the JD for hooks

Identify the one or two strongest signals where your profile genuinely lights up the JD. Hooks look like:

- Their key project is X; you have direct experience with X
- Their stated values match how you actually work, and your profile shows it
- Their tooling overlaps strongly with your stack
- A specific transition they're navigating (regional expansion, scaling, post-Series-X formalization) maps to your own scale-up experience

A hook is something specific you can name in one sentence. If you can't, keep reading — most JDs have one or two hidden in the "what you'll do" section.

### Step 2 — Pick an opener style

One of four. Default to **direct fit** unless context clearly suggests otherwise.

| Style | When to use | Risk |
|---|---|---|
| **Problem-opener** | The JD describes a clear, named problem | Reads as presumptuous if you misread |
| **Story-opener** | A specific experience of yours maps tightly to the role | Runs long if not disciplined |
| **Direct-fit-opener** | The role-fit alignment is unusually clean | Reads as boring without specifics |
| **Why-this-company-opener** | You have genuine resonance with the company's mission or values | Reads as flattery if not substantiated |

See `cover-letter-patterns.md` for example openings in each style and what each pitfall looks like.

### Step 3 — Draft three paragraphs

**Paragraph 1 — Opener (60–90 words).** Lead with the strongest signal from Step 1. Name the specific role and company. Establish the mutual-fit framing. No "I am writing to apply for…" anywhere.

**Paragraph 2 — Proof (130–180 words).** One concrete example from your experience that maps to the JD's most-emphasized theme. CTAR-shaped: brief context, action chain, result. Quantified where the metric is real and load-bearing. Bridge to a second supporting capability only if space allows — don't list three half-stories.

**Paragraph 3 — Fit and close (90–130 words).** Why this specific role, this specific company, this specific timing. Name one element of values / culture / direction that resonates. Direct close — a short, confident next-step line. No "looking forward to hearing from you" or "available at your earliest convenience."

### Step 4 — Run the voice filter

Pass every sentence through the forbidden-phrase list. Strip on sight:

- "I am thrilled / excited / passionate / honored"
- "Hope this finds you well"
- "Wanted to reach out"
- "I am writing to apply for"
- "Leverage" as a verb
- "Synergy / synergistic"
- "Wear many hats" / "rockstar / ninja"
- "Circle back" / "touch base"
- "At [Company], I [verb-ed]" as opener (too templated)
- "I am [adjective] about [thing]"

Replace each with concrete specifics. If a sentence needs a forbidden phrase to work, the sentence is the problem.

### Step 5 — Produce one alternative opener

After the main draft, draft one alternative opening paragraph using a different style from Step 2. Gives you a real A/B on the hook without rewriting the whole letter.

If only one opener style genuinely fits the role and a second style would feel forced, say so explicitly — same rule as the cv-bullet-tailor skill. Forced variety is worse than honest single-angle.

## Output format

Use this template exactly.

````markdown
# Cover Letter: [Company] — [Role Title]

**Style chosen:** [Problem / Story / Direct fit / Why-this-company]
**Hook chosen:** [one sentence — which JD signal you led with and why]
**Word count target:** 350–450

---

## Draft

[Paragraph 1 — Opener]

[Paragraph 2 — Proof]

[Paragraph 3 — Fit and close]

---

**Word count:** [actual count]

---

## Alternative opener (style: [different style])

[Alternative opening paragraph — 60–90 words]

---

## Notes

- **What I leaned into:** [one line — the strongest signal and why]
- **What I deliberately did NOT include:** [one line — e.g., "Did not address a named-tool gap; that is a screen-stage conversation, not a cover-letter topic"]
- **Suggested next step before sending:** [one line — e.g., "Read it aloud; if any sentence sounds like ChatGPT wrote it, flag it"]
````

## Critical rules

- **350–450 words. Never 600+.** Cover letters that long don't get read.
- **One concrete proof story, not three.** Specific beats comprehensive. Pick the best and commit.
- **Don't address gaps in the cover letter.** Gaps are interview conversations. Only address one if you explicitly ask.
- **Don't restate the resume.** The letter adds context the resume can't carry — fit, motivation, the specific connection.
- **Direct close, no filler sign-off.** "I'd welcome a conversation about [specific thing]" beats "I look forward to the opportunity to discuss further."
- **Reference the company's actual words carefully.** If you quote or paraphrase from the JD, make sure it's accurate. Don't invent values they don't claim.
- **Company name and role name appear at least twice.** Signals the letter wasn't recycled.
- **Voice filter is mandatory.** Step 4 is a gate, not a suggestion.
- **Alternative opener uses a different style** — not the same hook with synonyms swapped.

## What "good" looks like

- You read it once and say "yeah, that's me"
- Opener earns attention in the first sentence
- Proof paragraph has one specific, quantified moment
- Close has a concrete next-step line
- Word count lands at 380–420

## What "bad" looks like

- 600+ words with three "proof" paragraphs
- Variants of "I am writing to apply for the [role] position at [company]"
- "I am thrilled to…" anywhere
- Generic capability lists that could apply to any candidate
- "Looking forward to hearing from you" close

## Companion skills

- **`jd-fit-analyzer`** — runs upstream. Its three tailoring priorities tell this skill which signals to lead with.
- **`cv-bullet-tailor`** — sibling. The resume handles the credential proof; this letter handles the fit, motivation, and specific connection.
- **`interview-story-bank`** — when the proof paragraph leans on a story you will also tell in interviews, pull the same CTAR shape from the story bank for consistency.

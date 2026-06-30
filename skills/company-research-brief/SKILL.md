---
name: company-research-brief
description: Researches a company and produces a structured pre-interview brief — business model, recent moves, maturity of the function you'd join, likely pain points relevant to the role, and 5-7 stage-appropriate smart questions you can ask. Use this whenever you ask to research / brief / pre-read on a company, says "what do I need to know about [company]," mentions an upcoming interview and want prep, asks for smart questions to ask, or pastes a JD and wants company context in addition to fit analysis. Trigger even when you don't name the skill — "interview is Tuesday, help me prep," "tell me about [company]" with interview context, "what should I ask them" all count. This skill needs web search and fetch tools to work properly.
---

# Company Research Brief

## What this skill does

Given a company (and optionally a role and interview stage), produces a structured pre-interview brief: business snapshot, recent moves, a maturity assessment of the function you'd join, likely pain points the role would address, positioning opportunities for you, things to clarify, and 5–7 smart questions tailored to the interview stage.

This is the search-heaviest skill in the set. It needs working `WebSearch` and `WebFetch` tools to produce a real brief — without them, it can structure what you already knows but can't add new information.

## When to use

Trigger whenever you:

- Ask to research, brief, or pre-read on a company
- Say "what do I need to know about [company]"
- Mention an upcoming interview and want prep on the company
- Ask for smart questions to ask at [company]
- Paste a JD and asks for company context (alongside or instead of fit analysis)

## Inputs

Required:

- Company name

Optional but useful:

- The role being interviewed for (changes the lens — which pain points matter)
- The interview stage (recruiter screen / hiring manager / panel / final)
- The JD text (helps focus the brief)

If interview stage isn't provided, ask for it — the smart questions change meaningfully by stage.

## Required preparation

Read in order:

1. `references/profile.md` — canonical profile (so positioning and questions can reference your experience specifically)
2. `references/research-checklist.md` — what to look for and where
3. `references/function-maturity-rubric.md` — how to read maturity signals
4. `references/smart-question-archetypes.md` — question patterns by stage and by pain point

## Tools required

- **WebSearch** — primary tool for finding company info
- **WebFetch** — for reading specific articles, press releases, careers pages, founder posts

Load both via ToolSearch at the start of the run if they aren't already available.

## Workflow

### Step 1 — Build the search plan

Identify what to search for, in this order of priority:

1. **Company snapshot** — business model, product, customers, stage, geography, employee count
2. **Recent moves (last 12 months)** — funding, layoffs, exec changes, product launches, acquisitions, regional expansion
3. **Function signals** — who leads the function you'd join, recent hires into it, Glassdoor / RepVue / Levels.fyi reviews, public content from the function (blog, podcasts), other open roles in it
4. **Cultural and values signals** — values pages, founder interviews, leadership posts
5. **Industry and competitive context** — competitors, what's happening in their space

### Step 2 — Run searches

Use focused queries — one to six words each. Start broad ("Acme Corp company"), narrow as needed ("Acme Corp Series C funding 2025"). Aim for 8–12 search calls total. More than 20 means you're spinning.

For every claim you find, capture three things: **the claim, the source, the date**. No claim ships without a source.

### Step 3 — Synthesize the snapshot

Build the snapshot section. Be concrete. "Series B, $40M raised in March 2025, 80 employees per LinkedIn" beats "growing rapidly."

### Step 4 — Assess function maturity

Use `function-maturity-rubric.md` to assign a maturity level for the function you'd join: Founder-led / Early / Mid / Mature. State the signals you used.

The maturity level changes the role's shape and the questions to ask. A "first hire" role for a founder-led function is a different job from a specialist role in a mature function — even if the JDs use similar language.

### Step 4b — Comp benchmark

If the JD does not disclose salary, search for market rates:

- Levels.fyi for the role title + company (or similar stage/size companies)
- Glassdoor salary tool for the role title + location
- LinkedIn Salary if visible
- Any comp data in the JD itself (benefits, equity signals, contract type)

Produce a range with source and date. Flag when the data is thin or outdated. If the JD does disclose comp, sanity-check it against market: is it above, at, or below band?

### Step 5 — Identify likely pain points

Cross-reference what you found against the role. Examples:

- Post-Series-B with no dedicated leader for the function → formalizing the function is the pain
- Recent layoffs → retention and culture rebuild
- Rapid international expansion → multi-country coordination and compliance
- Founder-led function transitioning to its first dedicated hire → greenfield, role definition unclear

Flag two kinds explicitly:

- **Positioning opportunities** — pain points that map to your strengths
- **Risks to acknowledge** — pain points that map to your gaps

### Step 6 — Draft smart questions

Use `smart-question-archetypes.md`. Draft 5–7 questions tailored to:

- The interview stage (recruiter screen ≠ hiring manager ≠ panel ≠ final)
- The pain points you identified
- your specific experience as the lens (so the questions land as informed, not generic)

Good smart questions both signal you did the homework and test whether the role is actually right for you. Bad questions are generic ("what's the culture like?") or test-the-interviewer ("describe your management style").

## Output format

Use this template. Skip any section that has nothing to say — half a brief that's accurate beats a full brief that's padded.

````markdown
# Company Research Brief: [Company Name]

**Interview stage:** [stage, or "Not specified"]
**Role:** [role, or "Not specified"]

---

## Snapshot

- **Business model:** [one paragraph — what they do, who pays them]
- **Stage / funding:** [Series, total raised, latest round + date]
- **Headcount:** [number, source]
- **Geography:** [HQ + key offices + workforce distribution]
- **Mission / positioning:** [their stated mission or category claim]
- **Notable customers / users:** [3–5 names if available]

---

## Recent moves (last 12 months)

| Date | Move | Source |
|---|---|---|
| ... | ... | [URL or citation] |

---

## Function maturity

**Level:** Founder-led / Early / Mid / Mature

**Signals:**

- [observation with source]
- [observation with source]

**Who leads the function:** [name, title, background — or "not publicly identified"]

---

## Comp benchmark

- **Market range:** [low – high, role title + location/remote, source + date]
- **JD disclosed:** [salary or "Not disclosed"]
- **Assessment:** Above / At / Below band — [one line]

---

## Likely pain points relevant to this role

1. **[pain point]** — [why this matters to the role + source or inference]
2. **[pain point]** — [same]
3. **[pain point]** — [same]

---

## Positioning opportunities

Signals from this brief that map to your strengths:

- [observation → your matching capability]
- [observation → your matching capability]

## Risks / things to clarify

- [thing to ask about]
- [thing to ask about]

---

## Smart questions to ask

(Tailored to the interview stage.)

1. [question]
2. [question]
3. [question]
4. [question]
5. [question]
6. [optional]
7. [optional]

---

## Sources

- [URL or source]
- [URL or source]

## What I couldn't find

- [thing] — no public signal; worth asking in the interview
- [thing] — best guess: [inference]
````

## Critical rules

- **Cite everything.** Every claim must have a source URL or date. Hallucinated company facts are worse than no brief.
- **If you can't find something, say so.** "Not publicly available" is more useful than a confident guess.
- **Bias toward primary sources.** Company blog, press releases, founder posts, official LinkedIn > aggregators, Wikipedia, Glassdoor (which can be noisy).
- **Recency matters.** A 2023 signal is much less useful than one from the last six months. Date everything.
- **Maturity assessment is a judgment, not a search result.** State your reasoning so you can sanity-check.
- **Smart questions are stage-tailored.** A recruiter-screen question is different from a hiring-manager question is different from a panel question. Don't repeat the same five across stages.
- **No fluff filler.** Skip sections that have nothing to say.
- **Time-box the search.** 8–12 search calls is the target. Past 20, stop.
- **No emoji.** Same as the rest of the skill set.

## What "good" looks like

- you walk into the interview knowing the three things you didn't know before
- The smart questions land as informed because they reference specific things from the brief
- The maturity assessment matches your read of the JD after you see the brief
- Every source is clickable and recent

## What "bad" looks like

- "Founded in 2018, [Company] is a leading provider of…" (company-website regurgitation)
- Smart questions like "What's the culture like?"
- Claims with no source attached
- A confident assertion about something the brief actually couldn't verify

## Companion skills

- **`jd-fit-analyzer`** — runs upstream. Its strategic-fit verdict and tailoring priorities help focus this brief's pain-point section on what matters for the role.
- **`interview-story-bank`** — runs alongside. Once the brief identifies the likely pain points, the story bank can suggest which stories to prep for the behavioral round.

(The function maturity rubric uses generic stages; an HR example is given as one bracketed illustration among others — adapt to whatever function the role sits in.)
- **`negotiation-prep`** — runs downstream. The company snapshot here feeds the comp-comparison and BATNA analysis when an offer arrives.

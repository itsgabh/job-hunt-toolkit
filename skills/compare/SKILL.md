---
name: compare
description: Compare 2-3 job opportunities side by side for the user and recommend which to prioritize. Centralizes each role's hard-match score and strategic-fit verdict (reusing jd-fit-analyzer's rubric), builds a comparison table across hard match, comp/flexibility, geo/eligibility, level fit, async culture, and consulting compatibility, surfaces the key trade-offs, and ends with a clear "prioritize X" call. Use whenever the user shares two or more roles at once, asks "which should I pick / prioritize", "compare X and Y", "which of these is the better move", or references multiple prior fit analyses and want them weighed against each other. Trigger even if the user does not name the skill — if there are multiple roles on the table and they want a decision, run it.
---

# Compare

This skill takes 2-3 roles and produces a side-by-side comparison plus a clear "prioritize X" recommendation. It is the decision layer that sits on top of jd-fit-analyzer: where the analyzer evaluates one role in isolation, this skill weighs several against each other and tells you where to put your energy first.

It does not re-derive scores from scratch when a fit analysis already exists. It centralizes what's known, fills gaps, and decides.

## When to use

Trigger whenever you:
- Share two or three roles at once (JDs, links, or prior jd-fit-analyzer outputs)
- Ask "which should I pick / prioritize / go after first"
- Asks "compare X and Y" or "which of these is the better move"
- Reference multiple prior fit analyses and want them weighed against each other
- Have one offer in hand and another role in pipeline and wants to know where to lean

Do not trigger for a single role (use jd-fit-analyzer) or for general career advice with no specific roles attached.

This is a companion skill:
- **`jd-fit-analyzer`** runs upstream. It produces the per-role hard-match score, strategic-fit verdict, and resume variant. This skill reuses those outputs rather than redoing them.
- **`negotiation-prep`** runs downstream, once you have picked a role and has an offer. Its comp-comparison method (equity haircuts, PTO-as-cash, flexibility-as-comp) is reused here for the comp row.

## Inputs

Required:
- 2 or 3 roles, each as one of: a JD (text or link), or a prior jd-fit-analyzer output. Mixed inputs are fine (one analyzed, one raw JD).

Optional context:
- Which roles already have offers vs. are still in pipeline (changes the recommendation from "where to apply effort" to "which to accept")
- Comp figures if known (otherwise compare on what the JDs disclose)
- Any concern you want weighted (e.g. "I care most about the leadership step this time")

If more than 3 roles are supplied, compare the strongest 3 and say which were set aside and why. Three is the ceiling — beyond that the table stops being decision-useful.

## Required preparation

Read these before producing the comparison. They keep scores consistent with jd-fit-analyzer and the comp method consistent with negotiation-prep.

1. `../jd-fit-analyzer/references/profile.md` — canonical profile. The "Career direction", "Values & working culture preferences", and "Flexibility & remote work requirements" sections drive the tie-breakers. This is the canonical record of who you are.
2. `../jd-fit-analyzer/references/rubric.md` — the hard-match dimensions (5 weighted, 0-10) and the seven strategic-fit direction checks. Reuse these exactly so a score in this skill means the same thing as a score from jd-fit-analyzer.
3. `../jd-fit-analyzer/references/resume-variants.md` — only if a role lacks a prior analysis and you need to note its variant.
4. `../negotiation-prep/references/comp-comparison-rubric.md` — equity haircuts by stage, PTO-as-cash, flexibility-as-comp, local tax bands, and the work-from-anywhere non-negotiable. Use this for the comp row.

If a role already has a jd-fit-analyzer output, reuse its score and verdict — do not recompute. Only run the rubric fresh for roles that lack one.

## Workflow

### Step 1 — Centralize each role

For each role, assemble: hard-match score (0-10 + label), strategic-fit verdict, resume variant, comp signal, geo/eligibility, level, and culture flags.

- If a jd-fit-analyzer output exists, lift its numbers and verdict verbatim. Note "(reused)".
- If not, run the rubric in `rubric.md` to produce the hard-match score and strategic-fit verdict. Note "(scored now)".

Do not let two roles be scored by different methods without saying so — consistency is the whole point.

### Step 2 — Comp and flexibility per the comp rubric

For each role, summarize comp using `comp-comparison-rubric.md`:
- Base if disclosed; flag "not disclosed" honestly rather than guessing
- Equity haircut by stage (early-stage 70-80%, mid 50-60%, late 30-40%) — never compare an RSU grant to an option grant at face value
- PTO normalized; convert to cash equivalent only if it's a real differentiator
- Flexibility-as-comp: does it support any extended-remote stays in your profile, async, hours flexibility, consulting compatibility

The work-from-anywhere / extended-remote item is a hard gate. A role that blocks it is genuinely worse than a higher-base role that supports it, and that must show in the recommendation, not just the table.

### Step 3 — Build the comparison table

One column per role. Rows are the discriminators (exact format below). Keep cell text to a few words — the prose carries the nuance.

### Step 4 — Surface the trade-offs in prose

Two to four short paragraphs naming the real tensions the table can't hold. This is where the value is. Examples of the shape: "A is the bigger comp number but the rigid hybrid blocks an extended-remote stay; B is €8K lighter but truly async." Or "B is the only one with a leadership component, but it's also the biggest hard-match stretch." Name what's actually being traded.

### Step 5 — Recommend

Lead with the call. State which to prioritize and why in two or three sentences. Then:
- If any role is a clear pass, say so and why (don't leave dead weight on the table)
- If two are close, name the tie-breaker you used (per profile.md: scope, leadership, values, flexibility over title or comp)
- If the situation is "offer in hand vs. pipeline", account for timing and BATNA, and hand off to negotiation-prep for the offer itself

## Output format

Use this exact structure. Verdict and recommendation FIRST so you can decide fast, then the detail.

```
# Compare: [Role A] vs [Role B] (vs [Role C])

## Recommendation

**Prioritize [X].** [Two or three sentences: why X first, what it advances, the main trade-off you accepted.]

- **Clear pass**: [Role + one-line reason, or "None — all three are live"]
- **Tie-breaker used** (if close): [scope / leadership / values / flexibility — per profile.md]

## At a glance

| | [Role A] | [Role B] | [Role C] |
|---|---|---|---|
| Hard match | [X.X/10 — Label] | ... | ... |
| Strategic fit | [verdict label] | ... | ... |
| Comp (incl. equity/flex) | [Stronger / Mixed / Weaker + one note] | ... | ... |
| Geo / eligibility | [Yes / Partial / No — worldwide / EU / your-geo, work auth, extended-remote] | ... | ... |
| Level fit (the level your profile states) | [Yes / Partial / Risk — vs the role's level] | ... | ... |
| Async / remote culture | [Strong / Mixed / Risk] | ... | ... |
| Consulting-compatible | [Yes / Partial / No] | ... | ... |
| Source | [(reused) / (scored now)] | ... | ... |

## Trade-offs

[2-4 short paragraphs naming the real tensions: comp vs flexibility, leadership stretch vs safe fit, mission vs money, timing. Honest, no hedging.]

## Per-role notes

**[Role A]** — [2-3 lines: the one thing that makes or breaks it, resume variant if relevant.]

**[Role B]** — [same]

**[Role C]** — [same]

## Next step

[One line: e.g. "Apply to X now with the Specialist-IC variant; keep Y warm; pass on Z." If an offer is in hand, hand off: "For the X offer, run negotiation-prep."]
```

## Critical rules

- **Verdict first.** The recommendation block leads. you decides in under a minute, then reads the why.
- **No emoji.** Use words: `Yes` / `Partial` / `No`, `Strong` / `Mixed` / `Risk`, `Stronger` / `Weaker`.
- **Honest, no inflation.** you are allergic to flattery and inflated scoring. If two roles are mediocre, say both are mediocre and which is less so. A real "pass on all of these" is a valid output.
- **Consistency with jd-fit-analyzer.** Same hard-match dimensions, same strategic-fit checks, same score meaning. Reuse existing analyses rather than recomputing; flag when a role was scored fresh.
- **Level fit is a discriminator.** Use the level your profile states. A role pitched two brackets above that level (e.g. a Director-level role at a 1,000-person co with no manager track when your profile is an IC) is a hard-match risk, not a strategic plus. Score it honestly.
- **Flexibility is a hard gate.** Extended-remote-from-abroad needs (per your profile) and async culture are real comp. A role that blocks work-from-abroad caps low regardless of base — surface that in the recommendation, not just the table.
- **Geographic hard pass.** Any role requiring relocation outside the geography your profile allows is an automatic pass; it cannot win the comparison. Flag it and move on.
- **Don't average into mush.** The point is to discriminate. If the table looks like three near-identical rows, you haven't found the real differences — look harder at scope, leadership, flexibility, and direction.
- **Tie-breakers come from profile.md.** When roles are close, weight scope, leadership, values, and flexibility over title or comp — per "Career direction" and "Values & working culture preferences".
- **Length discipline.** A full compare is 600-900 words. The table plus a tight recommendation plus the trade-offs. Don't pad; don't recap the JDs back at you.
- **Stay in lane.** This skill decides which role to prioritize. It does not draft cover letters, tailor bullets, or run the offer negotiation — hand those to their skills.

## What "good" looks like

- you knows which role to chase first within a minute, and why
- The table discriminates — the rows show real differences, not three lookalike columns
- The trade-off prose names the one tension you were actually stuck on
- Flexibility and level fit are weighted as real factors, not footnotes
- Clear passes are called as passes; close calls name their tie-breaker

## What "bad" looks like

- Hedging ("they're all good in different ways, it depends")
- Re-running scores that already existed, with different numbers than the prior analysis
- A comp row that compares an RSU grant to an option grant at face value
- Treating a role two brackets above your stated level as a clear win on level when it's actually a stretch
- Padding to length by restating each JD

## Companion skills

- **`jd-fit-analyzer`** — upstream. Produces the per-role hard-match score, strategic-fit verdict, and resume variant this skill centralizes. Run it on any role that doesn't have an analysis yet.
- **`negotiation-prep`** — downstream. Once a role is prioritized and an offer lands, hand off for the comp comparison and counter prep. This skill reuses its comp method (equity haircuts, PTO-as-cash, flexibility-as-comp) for the comp row.
- **`company-research-brief`** — sibling. If a comparison hinges on funding stage or function maturity that the JD doesn't reveal, that brief fills the gap.

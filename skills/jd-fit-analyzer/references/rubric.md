# Scoring Rubric

How to derive the two parallel verdicts the JD fit analyzer outputs.

---

## Part A: Hard match score (0–10 overall)

Score five dimensions out of 10 each, then take a weighted average for the overall score. The match table that follows the score breakdown is where the actual evidence lives — the scores summarize that table.

### Dimension 1: Required experience (weight: 25%)

Years of experience and role-level match.

- **10** — Years of experience and role level exactly match the listed requirement. JD says "5–7 years in the role's domain"; you have 6.
- **7–9** — Within range or slightly stretching above/below.
- **4–6** — One bracket off (e.g., JD asks for 8–10 years; you have 6).
- **0–3** — Two brackets off, role level mismatch (e.g., asks for VP/Director with people management; you are an IC).

### Dimension 2: Required tools/systems (weight: 25%)

Match against the JD's required tool stack.

- **10** — Has every required tool, with depth of use evident from experience.
- **7–9** — Has most required tools; one missing but learnable; or has a strong analogue (a different platform in the same product category — strong analogue, fast ramp).
- **4–6** — Has half the stack; one named-tool gap on a tool that's hard to learn quickly.
- **0–3** — Missing most or all named tools, no clear analogue.

**Critical scoring rule — named-tool penalty:** If a specific platform appears as a **named key project / primary responsibility** (not just listed under "nice to have" or "qualifications"), score the tool dimension based on whether you actually have hours on THAT named platform, not whether you have analogous experience. Softening qualifiers like "or similar" reduce screen-out risk but do not change the day-one ramp reality.

- JD names a platform as the central project + you have no hours on it → score 4/10 max regardless of an analogue in the same category. The "or similar" gets you past the recruiter screen; the named-key-project text is what you would actually be doing.
- JD lists a category of tools ("X, Y, Z, or similar") with no single named system as the central project + you have a comparable tool in that category → score 7–8/10. Genuinely platform-agnostic JD.

When a JD names a specific platform in your field that you do not have, distinguish by how hard it is to ramp:
- **Enterprise-grade platforms** (heavyweight, long implementation cycles, specialist-config) → hard-to-ramp; deep penalty. Even with "or similar" framing, score 3–5/10 if it's a named key project.
- **Mid-market platforms** (lighter, transferable from a comparable mid-market tool) → light penalty. Score 6–8/10.
- **Niche tool you do not know but that switches fast** (e.g. many category-standard SaaS apps) → moderate penalty; ramp is quick.

*Example of this enterprise-vs-mid-market split, drawn from HR systems (swap in the named platforms of your own field): enterprise HRIS like Workday, SAP SuccessFactors, or Oracle HCM behave like the hard-to-ramp tier; mid-market HRIS like Personio, BambooHR, or Rippling behave like the transferable mid-market tier; a niche ATS you don't know behaves like the fast-switch tier.*

### Dimension 3: Domain / industry (weight: 15%)

Sector match.

- **10** — Tech / SaaS / remote-first / international (adjust to your home turf in profile.md).
- **7–9** — Adjacent (fintech, AI-forward, scale-up SaaS).
- **4–6** — Different domain but transferable (hospitality, services).
- **0–3** — Heavily regulated industry or domain requiring specialist knowledge you lack (e.g., pharma compliance, defense, financial services with regulator-facing requirements).

### Dimension 4: Seniority / scope (weight: 20%)

Match between the role's listed scope and your demonstrated scope (from profile.md).

- **10** — Population, geography, and program scope all within your range or modest stretch.
- **7–9** — Stretches you by 1.5–2x on one dimension (population, geography, or programs owned).
- **4–6** — Major stretch on multiple dimensions; or under-scoped vs. your experience.
- **0–3** — Way above (Director-level at a 1,000+ co with no people-manager track) or way below (entry-level coordinator).

### Dimension 5: Geographic / legal (weight: 15%)

- **10** — In your home location, your country, or fully-remote in your eligible region. No work-authorization issues. (Set your home geo and work auth in profile.md.)
- **7–9** — Fully-remote globally, compatible with your geography and work authorization.
- **4–6** — Hybrid in your city but expects frequent office presence.
- **0–3** — Requires relocation outside the geography your profile allows. **If your profile rules out relocation, this is a hard pass regardless of other scores.** Flag clearly.

### Overall hard match

Weighted average:
`Overall = 0.25*Experience + 0.25*Tools + 0.15*Domain + 0.20*Scope + 0.15*GeoLegal`

Round to one decimal place. Map to qualitative label:

| Score | Label |
|---|---|
| 9.0–10 | Excellent match |
| 7.5–8.9 | Strong match |
| 6.0–7.4 | Solid match with gaps |
| 4.5–5.9 | Stretch with significant gaps |
| 0–4.4 | Poor match |

### Requirements vs. evidence table

Required for every analysis. Format:

| Requirement | Have it? | Evidence | Gap/Stretch |
|---|---|---|---|

- **Have it?**: `Yes` / `Partial` / `No` (no emoji)
- **Evidence**: cite the specific role, scope, or metric from `profile.md`
- **Gap/Stretch**: if Yes, what makes it strong; if Partial, what's missing; if No, how big the gap is

Sort the table: hard requirements first, nice-to-haves last.

### Gap classification

- **Hard gaps**: requirements explicitly listed as required where you have no evidence and no close analogue. Could be a screening filter.
- **Soft gaps**: nice-to-haves, or hard requirements where you have a strong analogue but not the exact named thing. Positionable in a cover letter.

---

## Part B: Strategic fit verdict

This is a qualitative judgment, not a numeric score. Pick one verdict label from the list below based on the direction-alignment checks.

### Direction alignment checks

Run all seven. Each gets a `Yes` / `No` / `Partial` with a one-line reason.

1. **Broader scope than current role?**
   - More domains/programs covered? More people/scope supported? More geographies? More programs owned? Or strategic remit (OKRs, planning) on top of execution?
   - "Yes" if it clearly expands beyond your current remit (per profile.md).

2. **Leadership component?**
   - Direct reports listed? Team lead responsibility? Manager-of-managers? Cross-functional leadership without formal reports?
   - "Yes" if there's any structured leadership opportunity (even informal "lead this initiative across the team").

3. **Values & working culture alignment?**
   - Check `profile.md` "Values you’re drawn to" and "Values you’re NOT drawn to".
   - Look for: async signals, people-first framing, transparency/ownership language, calm-productivity cues, AI-forward without buzz.
   - Flag as risk: "wear many hats" / "rockstar / ninja" language, return-to-office mandates, crunch signals, hyper-growth-at-all-costs framing, vague mission while listing aggressive growth metrics.
   - "Yes" if multiple positive signals are explicit; "Partial" if one positive but ambiguous overall; "No" if the JD's tone clashes with your values.

4. **Flexibility & geographic freedom?**
   - Does the role meet any extended-remote-from-abroad needs in your profile (e.g. recurring weeks working from another country)? Check for: "work from anywhere," "work from abroad," generous PTO, async-first culture.
   - Are working hours flexible (async or core-hours) vs. strict 9–5?
   - Is the role truly remote, or hybrid with mandatory in-office cadence that would block your extended-remote needs?
   - "Yes" if work-from-anywhere is explicit OR culture is async-first with generous flexibility. "Partial" if remote-friendly but ambiguous on extended remote-from-abroad. "No" if rigid hybrid with mandatory in-office days that would block the extended-remote periods your profile depends on.

5. **Consulting compatibility?**
   - Is the role full-time only, or does it allow fractional/advisory work alongside? Are there contract/advisory pathways visible?
   - Usually "No" for traditional full-time roles. "Yes" only if part-time / fractional / contract is explicitly an option, or if the working pattern (e.g., 4-day week, flexible) leaves room for consulting on the side.

6. **Mission / impact alignment?**
   - Is the company mission-driven? Non-profit, B-corp, climate, education, healthcare access, social impact, civic tech?
   - "Yes" for clear mission orientation. "Partial" for purpose-driven for-profits with weak signal. "No" for standard commercial SaaS / enterprise software without explicit mission.

7. **Direction match (overall)**
   - Forward: clearly advances your trajectory (broader scope OR leadership OR impact dimension)
   - Lateral: same scope and same dimensions
   - Sideways: title up but scope narrower or domain misaligned
   - Backward: under-scoped, regression in responsibility

### Verdict labels

Pick one:

- **Strong fit (forward)** — Four or more "Yes" answers across checks 1–6, plus Forward on #7. Role clearly advances your direction.
- **Stretch fit aligned** — Two or three "Yes" answers, Forward on #7. Stretches you but in your direction.
- **Lateral** — Solid hard match, but checks 1–6 are mostly No/Partial and #7 is Lateral. Pays the bills, doesn't advance.
- **Step sideways** — Mixed: some strategic positives but offset by misalignment (e.g., title up, scope narrower; or non-profit but pure-IC contributor with no leadership).
- **Step back** — Under-scoped, regression, or pulls away from direction.

### Hard-pass override on flexibility

If check #4 (Flexibility & geographic freedom) is a clear "No" — i.e., the role mandates in-office hybrid cadence with no remote-from-abroad option — this is at least a Watchlist regardless of other strengths, because you lose the extended-remote periods your profile depends on. Flag this prominently.

### Strategic verdict writing

The strategic fit verdict in the output should be one sentence: `[Verdict label] — [why in 10–15 words]`.

Examples:
- "Strong fit (forward) — broader scope, hybrid people + strategy ops, AI-forward, matches stated direction."
- "Lateral — close hard match but same IC scope as current role, no leadership component, traditional SaaS."
- "Stretch fit aligned — broader scope and first-manager opportunity, even if the domain stretches you."

---

## Part C: Apply / Pass recommendation

Use the matrix below. Hard match and strategic fit jointly determine the recommendation.

|   | Strong fit (forward) | Stretch fit aligned | Lateral | Step sideways | Step back |
|---|---|---|---|---|---|
| **Excellent / Strong match (7.5+)** | Apply | Apply | Apply with reservations | Watchlist | Pass |
| **Solid with gaps (6.0–7.4)** | Apply | Apply with reservations | Watchlist | Pass | Pass |
| **Stretch with significant gaps (4.5–5.9)** | Apply with reservations | Watchlist | Pass | Pass | Pass |
| **Poor match (0–4.4)** | Watchlist | Pass | Pass | Pass | Pass |

**Watchlist** = don't apply now, but keep an eye on the company / wait for a better-suited future role.

Override conditions:
- Geographic/legal score below 4 (relocation required) → automatic Pass regardless of other dimensions.
- Hard gaps include a non-negotiable like a security clearance you do not have → Pass.
- Strategic alignment is "Step back" → never higher than Watchlist.
- Strategic check #4 (Flexibility & geographic freedom) is a clear "No" — i.e., mandatory in-office cadence that blocks your extended-remote needs → never higher than Watchlist regardless of hard-match score.

---
name: negotiation-prep
description: Prepares the user for compensation negotiation given a role offer (or expected offer) — builds the comp comparison, identifies BATNA, sets walk-away and target numbers, drafts principled counter scripts, treats flexibility levers (work-from-anywhere for any recurring stays abroad, async, PTO) as real comp components. Use this whenever the user receives an offer and wants to evaluate or negotiate it, asks for help preparing a counter, asks about BATNA / ZOPA / anchoring, want to compare an offer to your current role or another offer, asks "should I take this," or want counter scripts for specific levers. Trigger even when they don't name the skill — "they came back with €X," "help me prep for the comp conversation," "how should I respond to this offer" all count. This is the highest-stakes skill in the set; accuracy and honesty matter most here.
---

# Negotiation Prep

## What this skill does

Walks you through negotiation prep end-to-end: captures the offer, builds an apples-to-apples comp comparison (current vs. offered vs. market), identifies BATNA, sets walk-away and target numbers, prioritizes which levers to pull first, drafts principled counter scripts in your voice, and lists watchouts for what not to say.

Flexibility (work-from-anywhere for any recurring stays abroad, async culture, PTO, consulting compatibility) is treated as a real comp component — not a soft preference. If your profile flags recurring stays abroad, that accommodation may be worth real money, and the skill quantifies that thinking explicitly.

## When to use

Trigger whenever you:

- Receive an offer and want to evaluate or negotiate it
- Ask for help preparing a counter
- Ask about BATNA, ZOPA, anchoring, or walk-away
- Want to compare an offer to your current role or another offer
- Ask "should I take this offer / push back / accept"
- Want negotiation scripts for specific levers (base, equity, signing, PTO, work-from-anywhere)

## Inputs

Required:

- Role + company
- The offer (or expected offer): base, bonus, equity, benefits, PTO, location, work model, start date

Strongly preferred:

- your current total comp (or implied ballpark)
- Real walk-away number — what would make you say no
- Ideal number — what would make you say yes immediately
- Market data for the role and geo (you can supply, or skill can search via web tools if available)
- Other offers in play (drives BATNA strength)

Optional:

- Specific concerns ("equity grant is small but RSU not options" / "they pushed back on work-from-abroad")

If the offer has missing components, push back and ask — accuracy matters here more than anywhere else.

## Required preparation

Read in order:

1. `references/profile.md` — canonical profile. The flexibility section ("Extended-remote needs," "Values you are drawn to," "Flexibility & remote work requirements") is load-bearing for the flexibility-as-comp framing.
2. `references/negotiation-framework.md` — BATNA, ZOPA, anchoring, reservation price, aspiration price, multi-issue trading principles.
3. `references/comp-comparison-rubric.md` — apples-to-apples comparison method, equity valuation rules, local tax treatment, PTO-as-cash framework.
4. `references/flexibility-levers.md` — non-cash levers in priority order, with estimated value and framing patterns.
5. `references/counter-script-archetypes.md` — script patterns by lever, in your voice.

## Workflow

### Step 1 — Capture the offer state

Document the offer in full. The table in the output format covers what's needed. If the user is giving partial info, push back — missing data is the most common failure mode in offer prep. Required fields:

- Base (currency, gross/net if relevant)
- Bonus (target percentage, structure, conditions)
- Equity (type — RSU/option/RSA, amount, vesting, strike if options, 409A or last preferred for valuation)
- Benefits (health, retirement, parental leave, etc.)
- PTO and flexibility policy (including work-from-abroad specifics)
- Work model (remote / hybrid / in-office)
- Location and tax jurisdiction
- Start date
- Sign-on / relocation if any
- Title and reporting line

### Step 2 — Build the comp comparison

Three-column table: **Current (your current role)** | **Offered** | **Market** (you-supplied or skill-searched).

Compute:

- Total comp Year 1 = base + (bonus × probability of hitting) + (equity / vesting years, conservatively valued)
- Total comp annualized over equity vest
- Hourly equivalent if PTO differs significantly between options
- Total comp after local income tax (estimate — flag that you should verify with a tax advisor)
- Flexibility-adjusted comparison (qualitative — name the extended-remote, async, work-from-anywhere alignment)

### Step 3 — Identify BATNA

What's your best alternative if this offer falls through?

Candidates:

- Stay in your current role (highest-quality info — you know it)
- Another active offer (if in flight)
- Continue consulting alongside passive job search (self-employment status, where you have it, is the legal scaffolding)
- Combine consulting with passive job search (status quo)

Estimate BATNA value in total comp + flexibility terms. Note confidence — staying in your current role has high BATNA confidence; another offer not yet finalized has lower confidence.

### Step 4 — Set walk-away and target

- **Walk-away** — minimum acceptable. Below this, you take BATNA. Be specific: "Below €X base + Y flexibility, walk." Walk-away must be defendable — if you say you would walk at €X, you have to mean it.
- **Target** — confident, well-anchored ask. The number that makes you say yes.
- **Aspirational** — the same-day yes number, if they ask "what would close this."

Each is anchored to market data, scope, and experience — not personal needs.

### Step 5 — Prioritize negotiation order

Generally:

1. **Base first** — usually the highest expected-value lever
2. **Equity second** — if equity matters in this offer
3. **Flexibility / work-from-anywhere** — easy for them to grant, valuable to you
4. **Signing bonus last** — smallest commitment, often used to bridge a gap

But order changes based on what's most asymmetric — what's easy for them to give but valuable for you. Sometimes work-from-anywhere is more valuable than base, and the negotiation should reflect that.

### Step 6 — Draft counter scripts

Two to three scripts per major lever. Each script:

- Anchors the ask with reasoning (not "I want more" — "Based on [market data / scope / experience], I'm looking at [number]")
- Is principled, not adversarial
- Leaves space for them to come back with options
- Matches your voice — warm but direct, no power plays, no aggressive anchoring

### Step 7 — Identify watchouts

What NOT to say. The classic mistakes:

- "What's the most you can offer?" — gives away leverage
- "I can't afford to take less than X" — turns it into a sob story
- "I have a mortgage" — anchoring on personal needs
- Apologizing for negotiating
- Accepting on the spot

## Output format

````markdown
# Negotiation Prep: [Company] — [Role Title]

## Offer captured

| Component | Value | Notes |
|---|---|---|
| Base | €X | gross/net, currency |
| Bonus | Y% target | structure, conditions |
| Equity | [type, amount, vesting] | strike / valuation if options |
| Health / benefits | [summary] | |
| PTO | [days] | flex policy, work-from-abroad terms |
| Work model | [remote / hybrid / in-office] | |
| Location | [base location, tax jurisdiction] | |
| Start date | [date] | |
| Sign-on / relocation | [if any] | |
| Title / reporting line | [role, reports to] | |

**Missing from current offer (need to clarify):**

- [thing]
- [thing]

---

## Comp comparison

| Component | Current (your current role) | Offered | Market (median) |
|---|---|---|---|
| Base | ... | ... | ... |
| Total comp (Year 1) | ... | ... | ... |
| Total comp (annualized over equity vest) | ... | ... | ... |
| PTO days | ... | ... | ... |

**Flexibility comparison (qualitative):**

- Extended-remote-from-abroad support (per your profile, if applicable): [analysis]
- Async culture: [analysis]
- Hours flexibility: [analysis]
- Consulting compatibility: [analysis]

---

## BATNA

**Best alternative:** [stay in current role / other offer / continue consulting]
**Estimated value:** [total comp + flexibility]
**Confidence:** [high / medium / low]

---

## Targets

| | Value | Reasoning |
|---|---|---|
| **Walk-away** | €X | Below this, take BATNA |
| **Target** | €Y | Anchored by [market data / scope / experience] |
| **Aspirational** | €Z | The number that gets a same-day yes |

---

## Negotiation order

1. **[Lever 1]** — [reasoning]
2. **[Lever 2]** — [reasoning]
3. **[Lever 3]** — [reasoning]

---

## Counter scripts

### Lever 1: [e.g., Base]

**Script A (anchored, principled):**
> [script text]

**Script B (more direct):**
> [script text]

### Lever 2: [e.g., Work-from-anywhere]

**Script A:**
> [script text]

**Script B:**
> [script text]

### Lever 3: [e.g., Signing bonus]

[same structure]

---

## What if they say

| Their response | Your move |
|---|---|
| "That's outside our range" | [response approach + sample line] |
| "We can do part of that" | [response approach + sample line] |
| "Let me check with my manager" | [response approach + sample line] |
| "We need an answer by [date]" | [response approach + sample line] |
| "Final offer" | [response approach + sample line] |

---

## Watchouts (do NOT say)

- [phrase to avoid + why]
- [phrase to avoid + why]

---

## Closing checklist before saying yes

- [ ] All comp components in writing
- [ ] Equity terms confirmed (type, amount, vesting, exercise window if options)
- [ ] PTO and work-from-abroad terms confirmed in writing
- [ ] Start date locked
- [ ] Local tax implications checked with a tax advisor
- [ ] BATNA loss is acceptable
- [ ] Slept on it at least one night
````

## Critical rules

- **Numbers in writing, not verbal.** Push you to get everything in writing before saying yes.
- **Local tax matters.** Total comp comparison accounts for income tax and self-employment implications in your jurisdiction where relevant. Flag explicitly that the user should verify with a tax advisor — the skill doesn't do tax advice, it surfaces the question.
- **Flexibility is a comp component.** Extended-remote-from-abroad allowances, where your profile flags them, are worth real money. Treat as a real negotiation item, not a soft preference.
- **Tactics match the voice.** Warm-but-direct. No aggressive anchoring, no power plays. Principled framing with confident asks.
- **BATNA must be honest.** If staying in your current role is the BATNA but you are ready to leave for direction reasons, the BATNA is weaker than it looks on paper.
- **Walk-away should be defendable.** If you say you will walk below €X, you have to mean it.
- **Don't accept the first offer.** Even if it's good. The counter-and-improve dance is expected. Counter at least once.
- **Match anchor to data.** "I'm looking at €X based on [market data / scope / experience]" — never "I'm looking at €X because I need it."
- **Equity needs careful math.** Options vs RSUs, vesting cliff, valuation assumptions, dilution — all real. Don't compare a $50K RSU grant to a $50K option grant as equal.
- **Sleep on it.** Never say yes on the call. Always sleep on it.
- **No emoji.** Same as the rest of the set.

## What "good" looks like

- Comp comparison is accurate and apples-to-apples
- Walk-away is a number you would actually enforce
- Counter scripts sound like you talking, not a textbook
- Flexibility is treated as a real negotiation item with a number-or-clear-tradeoff attached
- Watchouts are specific to this offer, not generic

## What "bad" looks like

- Comp comparison that conflates RSU and option grants
- Walk-away set so high or low it's not actionable
- Scripts that sound aggressive or sycophantic
- Treating flexibility as an afterthought
- Generic watchouts ("don't seem desperate")

## Companion skills

- **`jd-fit-analyzer`** — runs upstream. Its variant pick and strategic-fit verdict provide the context for whether negotiation should be aggressive (Strong fit) or measured (Lateral).
- **`company-research-brief`** — provides the funding stage, recent moves, and function maturity that calibrate the comp expectations.
- **`recruiter-outreach-drafter`** — sibling. The counter-script voice and the outreach voice should be consistent — same forbidden-phrase list, same warm-but-direct register.

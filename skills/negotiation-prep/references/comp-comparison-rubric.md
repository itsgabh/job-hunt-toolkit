---
type: skill-reference
used_by_skills: [negotiation-prep, compare]
---

# Comp Comparison Rubric

How to compare offers apples-to-apples. The temptation in offer comparison is to look at base salary first; the discipline is to compare total comp including equity, PTO, and flexibility.

---

## The total-comp formula

For each offer:

```
Total Comp (Year 1) =
  Base
  + (Bonus × Probability of hitting)
  + (Equity / Vesting years × Conservative valuation)
  + (Benefits monetary value)
```

For each offer:

```
Total Comp (annualized over vest) =
  Base
  + (Bonus × Probability of hitting)
  + Equity value at expected liquidity / Years to liquidity
```

The annualized-over-vest view is more honest for early-stage equity, where the bulk of the value is theoretical until liquidity.

---

## Equity valuation

Equity is where comp comparison goes wrong most often. Three rules:

### 1. Distinguish RSU, ISO/NSO, and option-equivalent

- **RSU (Restricted Stock Unit)** — taxed as ordinary income at vesting. Value is the share price × number of units. Many jurisdictions treat RSUs as employment income, taxed at vesting; check yours.
- **ISO (Incentive Stock Option)** — US-specific; not applicable outside the US.
- **NSO (Non-Qualified Stock Option)** — taxed at exercise on the spread. In many jurisdictions, treated as employment income; exercise can create a tax event whether or not you have sold. Check your local treatment.
- **Option-equivalent (local)** — many EU startups use phantom stock or similar instruments. Tax treatment varies; check the specific instrument.

**Never compare an RSU grant to an option grant at face value.** An RSU grant of $50K is roughly $50K (less tax). An option grant with a $50K paper value at the current 409A is closer to $5–10K of expected value depending on the strike, the dilution, and the liquidity probability.

### 2. Apply a conservative haircut for illiquidity

For private-company equity, apply a haircut to the face value:

- **Late-stage company (Series D+ with strong revenue)** — 30–40% haircut
- **Mid-stage company (Series B–C, revenue but not yet near IPO)** — 50–60% haircut
- **Early-stage company (Series A or earlier)** — 70–80% haircut
- **Pre-product or pre-revenue** — assume zero for comp comparison; treat as upside, not as comp

These haircuts are conservative on purpose. Equity that turns into real money is great; equity that doesn't, isn't.

### 3. Factor in the vesting schedule

Standard is four-year vesting with a one-year cliff. Variations:

- **Front-loaded vesting (e.g., 30/25/25/20)** — more value to you early, useful if you might leave before four years
- **Cliff longer than one year** — riskier; you get nothing if you leave before the cliff
- **No cliff** — better for you
- **Acceleration on change-of-control** — useful if the company is likely to be acquired

For comp comparison, divide the conservatively-valued equity by the vesting years to get the annualized contribution.

---

## Tax adjustment for your jurisdiction

Use your country of tax residence for everything you earn while resident. The comparison should include after-tax estimates. The bands below are illustrative — replace them with your jurisdiction's, or have your tax advisor confirm.

**Illustrative marginal rates (a generic progressive EU example — replace with your own jurisdiction's):**

| Income band (€) | Approximate marginal rate |
|---|---|
| 0 – 12,450 | 19% |
| 12,450 – 20,200 | 24% |
| 20,200 – 35,200 | 30% |
| 35,200 – 60,000 | 37% |
| 60,000 – 300,000 | 45% |
| 300,000+ | 47–50% |

(These are illustrative. A tax advisor has the exact numbers for your jurisdiction. The skill flags the band you're in but doesn't compute your exact tax.)

For comp comparison purposes, apply your top marginal rate to the top slice of any new offer. (Example: if the top band is 45%, a €5K base increase nets to roughly €2,750.)

**Special cases:**

- **Self-employed / contractor income** — often carries additional social-security and tax obligations on top of income tax, so the net rate on consulting income can be higher than employment income at the same gross. Check your local rules.
- **Benefits in kind** — some are tax-advantaged (e.g. health cover, meal vouchers up to a limit, depending on jurisdiction). Convert to gross-equivalent for comparison.
- **Equity vesting events** — create tax bills even without selling. Plan for them.

---

## PTO as cash equivalent

When PTO differs significantly between offers, convert to cash for comparison:

```
PTO value = (PTO days - reference PTO days) × Daily rate
```

Where daily rate = Base / 220 working days/year.

Example: an offer with 30 days PTO vs. one with 20 days PTO, at €65K base, is a €65K / 220 × 10 = ~€2,950 PTO advantage.

This is a rough proxy. PTO that's used differs from PTO that's accrued — unlimited PTO that nobody takes is worth less than 25 days that everyone uses.

---

## Flexibility as a comp component

Flexibility doesn't have a clean number, but it can have real value depending on your profile. The skill uses a qualitative add-on rather than forcing a number.

**Typical high-priority flexibility items (edit to match your profile):**

1. **Work-from-anywhere for any recurring stays abroad** your profile flags (e.g. several weeks a year from another country). If your profile marks this non-negotiable, an offer that doesn't accommodate it caps at Watchlist regardless of base.
2. **Async culture as operating principle, not stated value.** Worth real money in quality of life and effectiveness.
3. **Hours flexibility** (no rigid 9–5 EU expectation).
4. **Consulting compatibility** (continued self-employed / contractor work alongside, if relevant).
5. **Generous PTO** (25+ days target).

**For the comp comparison output, frame flexibility as:**

- A qualitative table row that names each of the five items and whether the offer accommodates it (Yes / Partial / No / Not specified)
- A summary line: "On flexibility, this offer is [stronger / weaker / equivalent] to your current-role baseline"
- A flag if any non-negotiable item (work-from-anywhere) is unmet

---

## Apples-to-apples checklist

Before declaring two offers comparable:

- [ ] Same time horizon (Year 1 vs. annualized over vest — pick one and apply consistently)
- [ ] Equity valued with the same haircut method
- [ ] Tax-adjusted to the same jurisdiction (your country of tax residence)
- [ ] PTO normalized either as days or as cash equivalent — not mixed
- [ ] Flexibility scored qualitatively on the same items for both offers
- [ ] Benefits-in-kind included on both sides
- [ ] Sign-on bonuses amortized appropriately (a sign-on that vests over two years is a different beast from one paid upfront)

If the checklist isn't satisfied, the comparison is unreliable.

---

## Common comparison traps

### Comparing equity grants without checking liquidity probability

A $100K equity grant at a Series A startup is not equivalent to a $100K equity grant at a Series D company. The Series A grant is closer to a lottery ticket; the Series D grant is closer to deferred cash.

### Ignoring the cliff

A four-year vest with a one-year cliff means you get nothing if you leave at month 11. If you're not confident you'll stay 12+ months, the equity discount should be heavier.

### Confusing base salary with total comp

A €70K base with no bonus, no equity, and 20 days PTO is a worse offer than a €60K base with a meaningful bonus, real equity, and 30 days PTO — even though the base looks higher.

### Forgetting tax on equity

Equity vesting events can trigger tax even if you don't sell, in many jurisdictions. A €50K RSU vest can create a €20–25K tax bill in cash, not stock. Plan for it.

### Not pricing flexibility

If your profile flags recurring stays abroad, an offer that blocks them is genuinely worse than a lower-base offer that supports them — the difference can be in the tens of thousands over a few years, but it doesn't show on a comp table.

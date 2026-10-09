---
type: shared-reference
used_by_skills: [cv-bullet-tailor, cover-letter-drafter, interview-story-bank, recruiter-outreach-drafter]
---

# Voice and Style Guide

Shared reference for skills that produce written content in your voice: CV bullets,
cover letters, interview stories, outreach messages.

This file has two layers:

1. **Your voice** — the part that is specific to you. It is NOT hard-coded here. It
   lives in the **"Voice & communication style"** section of your `profile.md`. Read
   that section first; it tells the skill how you actually write and speak. The
   placeholders below show the kind of attributes to capture there.
2. **The generic rules** — forbidden phrases, verb preferences, formatting, and the
   "would you actually say this" test. These apply to almost anyone writing clean,
   non-corporate prose and are kept here as-is. Edit them if your taste differs.

When building a new skill that references this file, copy it into the skill's
`references/` folder so the package stays self-contained.

---

## Voice attributes (fill from your profile)

Summarize your voice in a handful of attributes in `profile.md`. Common ones worth
deciding on:

### 1. Warmth vs. directness
How warm vs. blunt is your register? Real warmth usually shows in specificity
(remembering details, the right follow-up) rather than adjectives. Decide how much
hedging you tolerate.

### 2. Systems vs. narrative framing
Do you think in patterns, processes, and systems — or in stories and
relationships? Whichever it is, the writing should sound like it. "I rebuilt the
onboarding flow" reads differently from "I helped with onboarding."

### 3. Impact framing — understated vs. bold
Do you let metrics speak ("Helped scale from X to Y") or claim the transformation
("Pioneered…")? Pick one and hold it. Most credible professional writing is understated.

### 4. Reflective vs. transactional
Do your stories end with a lesson learned? Do cover letters explain *why this role now*,
not just *I'm qualified*? Capture whether reflection is part of your voice.

### 5. Frameworks visible or not
Some people use structure as thinking (CTAR, RACI, numbered steps, tables); others
find it stiff. State your preference so the skills match it.

> The skills read these from `profile.md`. If that section is blank, the output will
> be generic. Fill it in.

---

## Forbidden phrases

Hard-cut these from any output. They're cliché signals that mark text as auto-generated
or corporate. (Adjust to taste, but these defaults serve most professional writing well.)

### Generic corporate filler
- "Leverage" as a verb (use: use, draw on, apply, bring to bear)
- "Synergy / synergistic / synergize"
- "Wear many hats"
- "Rockstar / ninja / wizard / guru"
- "Move the needle"
- "At the end of the day"
- "Circle back" / "touch base"
- "Boil the ocean"
- "Bandwidth" (use: capacity, availability)
- "Drink the Kool-Aid"
- "Bleeding edge"
- "Mission critical"
- "Best-in-class" / "world-class"
- "Game-changer / game-changing"

### Performative enthusiasm
- "I am thrilled / excited / passionate / honored"
- "I am writing to express my interest"
- "I'm so pumped"
- "Couldn't be more excited"
- "Dream role / dream company"

### Cover letter / email filler
- "Hope this finds you well"
- "Wanted to reach out"
- "I came across your profile / posting"
- "I am writing to apply for"
- "Please find attached"
- "Looking forward to hearing from you"
- "At your earliest convenience"
- "Don't hesitate to reach out"
- "Thank you for your time and consideration"

### Hedging
- "Just wanted to" / "just a quick"
- "Sorry to bother you"
- "I think maybe / I think probably"
- "I'm not sure if this is right but..."

### Resume bullet anti-patterns
- "Responsible for [vague scope]" (use: owned, ran, delivered, built)
- "Helped with [task]" (use: contributed to, partnered on — only if true)
- "Worked closely with [team]" (use: partnered with, collaborated with — and be specific)
- "Various / multiple / several" (be specific: 3, 5, 10+)

---

## Verb preferences

### Strong action verbs that age well
- Built, designed, owned, ran, delivered, migrated, scaled, automated, mentored,
  partnered with, refined, established, coordinated, optimized, audited, implemented

### Verbs to avoid (or use sparingly)
- Spearheaded (overused)
- Orchestrated (corporate)
- Drove (overused)
- Pioneered (overclaim risk)
- Transformed (overclaim risk)
- Revolutionized (overclaim, always)
- Architected (use: designed)
- Operationalized (use: rolled out, ran)

---

## Tone calibration

### When to be more reflective
- Cover letters (especially the "why this company" paragraph)
- Interview story endings (lesson-learned)
- LinkedIn long-form posts
- Self-evaluation / performance review writing

### When to be more direct
- Resume bullets (no time for reflection — punch and move)
- Recruiter outreach (channel-constrained)
- Negotiation scripts (clarity beats nuance)
- Cold messages (specificity over warmth)

### Tonal landmines
- Don't write like you're trying to be liked. Try to be useful.
- Don't write like a senior exec trying to look casual. Match the seniority you
  actually have; the voice should sound like that level.
- Don't try too hard to be funny if that isn't you.
- Don't be sentimental. Even mission-driven stories read better framed operationally
  than emotionally.

---

## Emoji rule

**Default: no emoji.** Outputs (resume content, cover letters, stories, outreach) ship
with zero emoji unless your `profile.md` voice section explicitly says otherwise. If your
voice genuinely includes deliberate emoji use, note that in your profile as the explicit
exception — and treat whatever you set there as the upper bound, not a starting point.

---

## Formatting preferences

- Tables for comparison
- Numbered lists when order matters
- Bullet lists when order doesn't
- Sub-bullets indented under parent claims
- Bold for emphasis sparingly — overuse defeats the purpose
- Code blocks for technical content
- No headers below H3 in body output (use bold inline label instead)

---

## The "would you actually say this" test

Before shipping any output, run this check against your own voice:

1. Would you use this word/phrase in a Slack message? If no, suspect.
2. Would you add this sentence if writing the same thing for yourself? If no, cut.
3. Does this make a specific claim or a generic one? If generic, sharpen or remove.
4. Does this earn its place, or is it filler? If filler, cut.
5. Is the metric / scope / outcome real (traceable to `profile.md`)? If invented,
   rewrite to true.

If output fails any of these, revise before delivering.

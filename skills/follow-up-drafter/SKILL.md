---
name: follow-up-drafter
description: Drafts post-interview follow-up materials in the user's voice. Mode 1 (any stage) — thank-you email + LinkedIn connection note personalized to the specific interview. Mode 2 (final round only) — 30-60-90 day onboarding plan as a PDF-ready attachment, built from what was learned across all interview rounds. Use whenever the user finishes an interview and wants to follow up, says "draft a thank you for [interviewer]", "follow-up after my [company] interview", "draft a 30-60-90", or asks what to send after an interview. Trigger even when they don't name the skill — "interview just ended, what do I send?" counts.
---

# Follow-Up Drafter

Two modes. **Mode 1** (any stage) — a thank-you email and a LinkedIn connection note, personalized to the specific interview. Should take 5 minutes total. **Mode 2** (final round only) — a 30-60-90 day onboarding plan as a PDF-ready attachment, built from everything learned across the interview process. Speed matters for Mode 1: send within 24 hours, ideally same day. Mode 2 can take a day to draft properly.

## When to use

Trigger whenever the user:

- Finishes an interview and asks what to send
- Says "draft a thank you for [interviewer / company]"
- Asks for a follow-up email or LinkedIn note after an interview
- Says "interview just ended" with any hint of wanting to follow up
- Says "draft a 30-60-90" or "onboarding plan" after a final round

**Mode selection:** if the interview stage is final round and the user has enough context from prior rounds, offer Mode 2 in addition to Mode 1. If stage is anything else (recruiter screen, hiring manager, panel), run Mode 1 only — a 30-60-90 sent too early reads as presumptuous.

## Inputs

### Mode 1 — thank-you email + LinkedIn note

Required:

- Interviewer name and role/title
- Company name
- One specific thing discussed in the interview (a topic, a problem they mentioned, a shared interest, a moment that landed)

Optional:

- Interview stage (recruiter screen / hiring manager / panel / final)
- Anything the interviewer said about next steps
- Whether there's a specific point to reinforce or something that came out poorly

If the specific-thing is missing, ask for it before drafting — it's what separates a genuine note from a template.

### Mode 2 — 30-60-90 day plan (final round only)

Required:

- Role title and key responsibilities from the JD
- Pain points surfaced across all interview rounds (what problems kept coming up?)
- Names of key stakeholders or teams mentioned during interviews

Optional but makes it sharper:

- Anything the hiring manager said about what success looks like in year one
- Tools, systems, or processes to inherit
- Open headcount or team structure signals

If there isn't enough context from prior rounds to write something specific, say so — a generic 30-60-90 is worse than none.

## Required preparation

Read:

1. `references/profile.md` — for voice, positioning, and any experience references
2. `references/voice-and-style.md` — shared voice rules; forbidden phrases apply here too

## Workflow

### Mode 1

**Step 1.** Identify the one specific moment or topic to anchor the note. This is the personalization hook — without it, both pieces read as templates.

**Step 2.** Draft the thank-you email. Target: 3–4 sentences, plain text, no subject-line fluff. Structure: thanks for the time → specific callback → brief reaffirmation of fit or genuine interest → next-steps line.

**Step 3.** Draft the LinkedIn connection note. Target: 1–2 sentences, 200-character limit. Reference the conversation; don't just say "great to meet you."

**Step 4.** If the user mentioned they stumbled on something or want to add a point they forgot, add an optional P.S. line to the email only — one sentence, natural, not over-explained.

### Mode 2 — 30-60-90 day plan

Use these five questions to reverse-engineer the plan:

1. Why are they hiring for this role?
2. What are they looking for?
3. What would impact in this role look like?
4. How can I show I'm the best fit?
5. What would I be doing in this role that I can demonstrate right now?

**Step 1.** Map the pain points gathered across all interview rounds to the three time horizons. The 30-day section is about learning and relationship-building (not delivering); 60 days is about understanding priorities and aligning; 90 days is about early wins and concrete project plans.

**Step 2.** Draft each section with 3–5 specific, named actions — not generic goals. "Meet the product support, sales, and workforce management leads" beats "develop key relationships." Pull names and team structures from what was shared in interviews.

**Step 3.** Add a brief header that frames the document — one paragraph max — acknowledging what was heard about the role's priorities and anchoring the plan to those.

**Step 4.** Note where the plan is built on assumptions vs. confirmed context, so the hiring team can see the reasoning. This signals judgment, not overconfidence.

**Step 5.** Attach to the Mode 1 thank-you email with one sentence of context: "I put together a rough 30-60-90 based on what we discussed — happy to refine it if I'm missing context." Don't oversell the document in the email.

## Output format

### Mode 1

````markdown
# Post-interview follow-up: [Company] — [Interviewer Name]

## Thank-you email

**To:** [interviewer email if known, else "[interviewer name] <email>"]
**Subject:** Thank you — [role title] conversation

[body — 3–4 sentences]

[optional P.S. if there is something to add or fix]

---

## LinkedIn connection note

(200 characters max)

[note]

---

## Send timing

- Email: today, within [X] hours if possible
- LinkedIn: after email is sent (don't lead with LinkedIn for first contact)
````

### Mode 2 (attach to Mode 1 email)

````markdown
# 30-60-90 Day Plan — [Role Title] at [Company]

## What I heard this role needs to solve

[1 short paragraph — the pain points as understood from the interview process. Anchors the whole document.]

---

## First 30 days — learn and listen

Goal: understand the people, the priorities, and the landscape before acting.

- [specific action — named people/teams where possible]
- [specific action]
- [specific action]

## Days 31–60 — align and prioritize

Goal: understand the business objectives and identify where to focus first.

- [specific action]
- [specific action]
- [specific action]

## Days 61–90 — early wins and project plans

Goal: deliver on one or two concrete priorities and align on what comes next.

- [specific action]
- [specific action]
- [specific action]

---

*Built from what I learned across our conversations. Happy to refine any section where I'm working from assumptions.*
````

## Critical rules

- **One specific callback is mandatory.** A generic "great to speak with you" is worse than nothing. If no specific moment is given, ask before drafting.
- **Email is 3–4 sentences, not more.** Interviewers read dozens of these. Brevity signals confidence.
- **LinkedIn note is 1–2 sentences.** It's a connection request, not a second email.
- **No emoji.** No exclamation points (one max, on the sign-off only). No "I really enjoyed our conversation" opener.
- **No forbidden phrases** from `voice-and-style.md`.
- **Don't re-pitch.** The email is a thank-you, not a second cover letter. One brief reaffirmation line is the ceiling.
- **P.S. is optional and surgical.** Use only for a genuine addition or correction.
- **30-60-90 is final round only.** Do not suggest it for earlier stages. Sending it after a recruiter screen reads as tone-deaf.
- **30-60-90 must be specific.** If the inputs don't support specific named actions, say so and ask for more context rather than producing a generic plan. A vague plan signals the opposite of what it's meant to show.
- **Don't oversell the 30-60-90 in the email.** One sentence of context is enough. The document speaks for itself.

## What "good" looks like

- Interviewer reads the email and remembers specifically what they talked about
- The 30-60-90 names real people and problems from the interviews, not generic milestones
- Can be sent within a day of the final round, with minimal editing

## What "bad" looks like

- "I really enjoyed learning about [Company] and the exciting work you're doing"
- Three paragraphs restating the resume
- LinkedIn note that's just "Great to meet you, looking forward to connecting!"
- A 30-60-90 sent after round one
- A 30-60-90 with goals like "build relationships" and "understand priorities" and nothing more specific

## Companion skills

- **`company-research-brief`** — upstream. The brief's pain points section is the primary input for the 30-60-90; its smart questions generate the callback moment for the email.
- **`interview-story-bank`** — sibling. If the user wants to reference a story in the P.S., pull the elevator version from there.
- **`negotiation-prep`** — downstream. Once an offer arrives, that skill takes over.

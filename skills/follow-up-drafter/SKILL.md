---
name: follow-up-drafter
description: Drafts a post-interview thank-you email and a LinkedIn connection note in the user's voice, personalized to the specific interview just had. Use whenever the user finishes an interview and wants to follow up, says "draft a thank you for [interviewer]", "follow-up after my [company] interview", or asks what to send after an interview. Trigger even when they don't name the skill — "interview just ended, what do I send?" counts.
---

# Follow-Up Drafter

Drafts two pieces of post-interview outreach — a thank-you email and a LinkedIn connection note — personalized to the specific interview. Should take 5 minutes total. Speed matters: send within 24 hours, ideally same day.

## When to use

Trigger whenever the user:

- Finishes an interview and asks what to send
- Says "draft a thank you for [interviewer / company]"
- Asks for a follow-up email or LinkedIn note after an interview
- Says "interview just ended" with any hint of wanting to follow up

## Inputs

Required:

- Interviewer name and role/title
- Company name
- One specific thing discussed in the interview (a topic, a problem they mentioned, a shared interest, a moment that landed)

Optional but makes the output sharper:

- Interview stage (recruiter screen / hiring manager / panel / final)
- Anything the interviewer said about next steps
- Whether there's a specific point to reinforce or something that came out poorly

If the specific-thing is missing, ask for it before drafting — it's what separates a genuine note from a template.

## Required preparation

Read:

1. `references/profile.md` — for voice, positioning, and any experience references
2. `references/voice-and-style.md` — shared voice rules; forbidden phrases apply here too

## Workflow

**Step 1.** Identify the one specific moment or topic to anchor the note. This is the personalization hook — without it, both pieces read as templates.

**Step 2.** Draft the thank-you email. Target: 3–4 sentences, plain text, no subject-line fluff. Structure: thanks for the time → specific callback → brief reaffirmation of fit or genuine interest → next-steps line.

**Step 3.** Draft the LinkedIn connection note. Target: 1–2 sentences, 200-character limit. Reference the conversation; don't just say "great to meet you."

**Step 4.** If the user mentioned they stumbled on something or want to add a point they forgot, add an optional P.S. line to the email only — one sentence, natural, not over-explained.

## Output format

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

## Critical rules

- **One specific callback is mandatory.** A generic "great to speak with you" is worse than nothing. If no specific moment is given, ask before drafting.
- **Email is 3–4 sentences, not more.** Interviewers read dozens of these. Brevity signals confidence.
- **LinkedIn note is 1–2 sentences.** It's a connection request, not a second email.
- **No emoji.** No exclamation points (one max, on the sign-off only). No "I really enjoyed our conversation" opener.
- **No forbidden phrases** from `voice-and-style.md`.
- **Don't re-pitch.** The email is a thank-you, not a second cover letter. One brief reaffirmation line is the ceiling.
- **P.S. is optional and surgical.** Use only for a genuine addition or correction.

## What "good" looks like

- Interviewer reads it and remembers specifically what they talked about
- Can be sent within minutes of the interview ending, with minimal editing
- Sounds like the user, not like a template

## What "bad" looks like

- "I really enjoyed learning about [Company] and the exciting work you're doing"
- Three paragraphs restating the resume
- LinkedIn note that's just "Great to meet you, looking forward to connecting!"
- Sent three days later

## Companion skills

- **`company-research-brief`** — upstream. The brief's smart questions often generate the specific callback moment.
- **`interview-story-bank`** — sibling. If the user wants to reference a story in the P.S., pull the elevator version from there.
- **`negotiation-prep`** — downstream. Once an offer arrives, that skill takes over.

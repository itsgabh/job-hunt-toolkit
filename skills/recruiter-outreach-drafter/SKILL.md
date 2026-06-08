---
name: recruiter-outreach-drafter
description: Drafts cold or warm outreach messages to recruiters, hiring managers, or contacts at target companies — in your voice, channel-aware (LinkedIn DM, email, async tool like Slack/Teams/etc.), with two genuinely different variants and a follow-up suggestion. Use this whenever you ask to draft a LinkedIn / email / DM / outreach message, say "message to [recruiter / hiring manager / contact]," want to reach out to someone at a specific company, ask for a referral request or warm intro, or say "follow up on" an earlier touchpoint. Trigger even when you don't name the skill — "draft something to send to [a named contact]," "I want to reach out to the head of [team] at [a company]," "write the follow-up email" all count.
---

# Recruiter Outreach Drafter

## What this skill does

Drafts outreach messages in your voice, calibrated to the channel and to the relationship type. Returns two genuinely different variants (different hooks or different asks, not synonyms swapped) plus a follow-up suggestion for the second touch. Channels: LinkedIn DM, LinkedIn InMail, email, async tool (Slack/Teams/etc.). Types: cold, warm, referral follow-up, role-specific interest, general networking, follow-up after a touchpoint.

## When to use

Trigger whenever you:

- Ask to draft a LinkedIn / email / DM / outreach message
- Say "message to [recruiter / hiring manager / contact]"
- Want to reach out to someone at a specific company
- Ask for a referral request or warm intro
- Say "follow up on" an earlier conversation or application

## Inputs

Required:

- **Target person** — role + company (name optional but helpful)
- **Outreach type** — cold / warm / referral follow-up / role-specific interest / general networking / follow-up
- **Channel** — LinkedIn DM / LinkedIn InMail / email / async tool (Slack/Teams/etc.)

If type or channel isn't specified, ask. Both change the message materially.

Optional but useful:

- Specific role or company context you want to mention
- Existing connection or referral source ("[a contact] suggested I reach out")
- Specific ask (15-min chat / role inquiry / advice / intro to someone else)
- Tone calibration (formal / casual / peer)

## Required preparation

Read in order:

1. `references/profile.md` — canonical profile
2. `references/voice-and-style.md` — voice rules. Forbidden-phrase list is enforced harder here than anywhere else — outreach is where filler dies fastest.
3. `references/outreach-patterns.md` — message structures by type, with worked examples
4. `references/channel-conventions.md` — length, tone, and signature norms per channel

## Workflow

### Step 1 — Identify type and channel

Match the inputs to a pattern in `outreach-patterns.md`. Confirm the channel against `channel-conventions.md` for length and tone.

### Step 2 — Calibrate length to channel

| Channel | Target length | Notes |
|---|---|---|
| LinkedIn DM | 60–120 words | Conversational, no signature, no formal salutation |
| LinkedIn InMail | 100–150 words | Subject required, more formal |
| Email (cold) | 100–180 words | Subject line mandatory |
| Email (warm) | 80–150 words | Subject can be informal |
| Async tool (Slack/Teams/etc.) | 40–100 words | Async-native, concise; can run slightly longer than a quick chat message |

If the input length doesn't fit the channel, default to the channel's norm.

### Step 3 — Draft the message

The structure varies by type but generally:

**Hook (1–2 sentences).** Specific. Reference a recent post, a project, a mutual connection's name, a JD detail. Avoid: "I came across your profile" / "I saw you work at [Company]" / "I'm a big fan of your work."

**Context (1–2 sentences).** Who you are, why now. One specific line that maps your profile to why this person should care. Avoid full credentials dumps.

**Ask (1 sentence).** Clear and low-friction. "Would you be open to a 15-min chat about [specific thing] next week?" / "Could you point me to who's leading [project] on your team?" / "Worth applying via the careers page, or is there a faster path?"

**Close (optional, 1 line).** Only if it adds something. Don't add "Looking forward to hearing from you" or "Available at your earliest convenience." A direct close like "Happy to share more if useful" works.

### Step 4 — Produce two variants

Two messages with **different hooks or different asks** — not the same message with synonyms swapped. Each variant has its own subject line if it's an email. After each variant, name the hook used in one line.

If only one angle genuinely works (same rule as the cover-letter and CV-tailor skills), say so. One strong variant plus a flagged "no second angle that earns its place" is better than a forced B.

### Step 5 — Add follow-up suggestion

Most replies happen on the second touch. Provide:

- **Suggested timing** for the follow-up (e.g., "one week from initial send")
- **Suggested approach** for the follow-up (what angle to use)
- Optional: a 40–60 word drafted follow-up message

## Output format

````markdown
# Outreach: [Target person] at [Company]

**Type:** [Cold / Warm / Referral follow-up / Role-specific / Networking / Follow-up]
**Channel:** [LinkedIn DM / LinkedIn InMail / Email / Async tool (Slack/Teams/etc.)]
**Target length:** [from channel conventions]

---

## Variant A

[Subject line if email — e.g., **Subject:** Application — [Role], [your email]]

[Message body]

**Hook used:** [one line — what specific signal you led with]

---

## Variant B

[Subject line if email]

[Message body]

**Hook used:** [one line — a different angle]

---

## Follow-up if no reply

**Suggested timing:** [e.g., "one week from initial send"]

**Suggested approach:** [one line — what angle to use for the follow-up]

[Optional: drafted follow-up message, 40–60 words]

---

## Notes

- **What I leaned into:** [one line]
- **What I deliberately did NOT include:** [one line — e.g., "Didn't mention salary expectations; too early for a cold message"]
- **Voice check passed on:** [confirm the forbidden phrases didn't sneak in]
````

## Critical rules

- **Specific over generic, every time.** "I saw your post on [specific topic] at [company] last week" beats "I admire what you are doing at [company]." If you can't find something specific, ask the user to provide one.
- **No "hope this finds you well," "wanted to reach out," "I came across your profile," "I am writing to express my interest."** These signal mass-mailing.
- **Asks are small.** A 15-min chat, a question, advice, an intro — not "hire me" or "tell me everything about your company."
- **Channel conventions matter.** A 200-word LinkedIn DM is too long. A 40-word cold email looks like a typo. Match the channel.
- **Subject lines are part of the message.** For emails, the subject is doing real work — specific subjects beat generic ones.
- **Two variants meaningfully different.** Different hooks or different asks. Not paraphrased duplicates.
- **Follow-up suggestion is mandatory.** Most replies happen on the second touch.
- **No emoji unless the channel pattern with this contact includes them.** Cold outreach: no. Peer LinkedIn DM where you have a casual rapport: maybe.

## What "good" looks like

- You can send variant A or B without further editing
- Each variant has a clearly different angle, not a paraphrase
- The hook references something specific (a post, a project, a connection, a JD detail)
- The ask is one sentence and easy to say yes to
- Word count fits the channel

## What "bad" looks like

- Generic openers that could be sent to anyone
- 200-word LinkedIn DMs
- Multiple asks in one message ("a chat, advice, and an intro to your manager")
- Forbidden phrases sneaking in
- Subject lines like "Quick question" / "Hello" / "Following up"

## Companion skills

- **`jd-fit-analyzer`** — when the outreach is about a specific role, the fit analysis tells you which hooks are real.
- **`company-research-brief`** — provides the specific signal to lead with for cold messages (a recent move, a named priority, a founder post).
- **`cover-letter-drafter`** — sibling. The voice and forbidden-phrase list are identical. Sometimes the outreach message and the cover letter borrow from the same hook.

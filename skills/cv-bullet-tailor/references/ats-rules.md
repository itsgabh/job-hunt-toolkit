# ATS Rules

Rules to keep tailored bullets and resumes parseable by Applicant Tracking
Systems. (Adapted from andrew-shwetzer/career-ops-plugin, MIT.)

The cv-bullet-tailor only rewrites bullets, so the **keyword strategy** below is
the load-bearing part here. The layout/format rules apply when generating a full
resume document (e.g. an ATS-safe variant).

## Keyword strategy (apply to every rewrite)

- **Mirror the JD's exact phrasing.** If the JD spells a term a particular way,
  the bullet uses [the term the JD uses], not your own shorthand or a synonym.
  Match the term the parser will search for. (Your own preferred term can follow
  in parentheses if useful.)
- **Front-load the most important keywords.** The summary line and the first role
  carry the keywords the JD emphasizes most. A keyword buried in the oldest role
  is worth less to the parser.
- **One relevant keyword per bullet** where it lands naturally. Don't keyword-stuff;
  don't leave a high-relevance bullet keyword-free either.
- **Spell out acronym + full form once:** write "[Full Term] ([ACRONYM])" the first
  time it appears (e.g. "Applicant Tracking System (ATS)"). The parser may match
  either form.
- **Never invent a keyword** you cannot back up. Mirroring the JD's *wording* for
  experience you genuinely have is fine; claiming a skill you lack is not (same
  honesty rule as the rest of the skill).

## Layout / format (for full ATS-safe resume output)

- Single column. No sidebars, text boxes, or floating elements.
- Standard section headers, exactly: Experience, Education, Skills,
  Certifications, Summary. Not "Career Journey" or "Toolkit."
- No images, logos, or icons. No header/footer (put name + contact in the body).
  *(Note: if your CV uses contact icons, e.g. a moderncv LaTeX template, strip them
  for an ATS-safe variant and use plain text.)*
- Standard fonts, 10-12pt body. Consistent date format throughout.
- Real selectable text only — no text-in-images. Plain bullets or hyphens.
- LinkedIn URL as plain text, not an icon-only link.
- Max 2 pages.

## When this matters most

Apply the keyword rules always. Apply the full layout rules when the target
company clearly screens with an ATS (most mid-to-large companies; Greenhouse,
Workday, Lever, Ashby all parse) and the application is a resume upload rather
than a structured form.

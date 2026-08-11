## Context
The Vietnamese curriculum currently has a chapter on decimals, ratios, and measurement, but several lessons in that area are really "everyday math" lessons: measuring real objects, reading clocks and calendars, and working with money. Those lessons are practical and useful, but they read more like life-application lessons than like the conceptual bridge chapter around decimals and ratios.

At the same time, the repository already contains a separate OpenSpec proposal for a later applications chapter made of "Toán Học Trong ..." enrichment lessons. This change must not collapse those two tracks into one.

## Goals
- Create a distinct learner-facing chapter for everyday math in life.
- Move only the five identified lessons: `05-12`, `05-13`, `05-14`, `05-15`, `05-16`.
- Keep the broader applied/exploration chapter separate.
- Preserve redirects, interactive mappings, and chapter sequencing.

## Non-Goals
- Rewriting the mathematical content of the moved lessons.
- Moving the optional "Toán Học Trong ..." lessons in this change.
- Creating full English lesson parity for the moved Vietnamese lessons.

## Decisions

### Add a dedicated new chapter instead of reusing the broader applications chapter
These five lessons are foundational real-life math lessons, not enrichment essays or capstone applications. They deserve a dedicated chapter that sits naturally in the learner path, separate from the later "math in sports/music/finance/..." expansion track.

### Treat the moved lessons as one coherent sequence
The new chapter should present the lessons as a continuous progression around:
- measurement
- practical unit conversion
- time and calendar reasoning
- money and everyday calculation

Visible numbering and chapter metadata should be refreshed so the published learner experience reads as one chapter rather than a set of borrowed lessons.

### Preserve old routes
Because the moved lessons already have published-style paths and may be linked from existing pages or external references, the old URLs should redirect to the new canonical chapter URLs.

### Keep the implementation path-based
Interactive includes and redirects are keyed by `page.path` and URL structure, so moving the lessons requires synchronized updates to:
- `_data/vi_interactive_lessons.json`
- `_data/vi_lesson_redirects.json`
- curriculum manifest / validation scripts

## Open Questions
- Which numeric chapter id should be used for the new learner-facing chapter so it fits cleanly with the existing sequence and does not collide with the separate applied-math chapter proposal?
- Whether the moved lessons should retain the visible `05-xx` numbering in titles for continuity or be renumbered to the new chapter prefix immediately.

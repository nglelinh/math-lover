## Context
The Vietnamese curriculum currently has a chapter on decimals, ratios, and measurement, but several lessons in that area are really "everyday math" lessons: measuring real objects, reading clocks and calendars, and working with money. Those lessons are practical and useful, but they read more like life-application lessons than like the conceptual bridge chapter around decimals and ratios.

At the same time, the repository already contains a separate OpenSpec proposal for a later applications chapter made of "Toán Học Trong ..." enrichment lessons. This change must not collapse those two tracks into one.

**Published constraints (main, 2026-09):** Chapter 09 is combinatorics; Chapter 10 is Grade 6 exam prep. Those ids are taken. The five everyday-life lessons still live under `contents/vi/chapter06/_posts/`.

## Goals
- Create a distinct learner-facing **Chapter 11** for everyday math in life.
- Move only the five identified lessons: `05-12`, `05-13`, `05-14`, `05-15`, `05-16`.
- Keep the broader applied/exploration chapter as **Chapter 12**.
- Preserve redirects, interactive mappings, and chapter sequencing.

## Non-Goals
- Rewriting the mathematical content of the moved lessons.
- Moving the optional "Toán Học Trong ..." lessons in this change.
- Creating full English lesson parity for the moved Vietnamese lessons.
- Implementing the file move in the same PR that only corrects the OpenSpec plan (implementation is a later, approved pass).

## Decisions

### Chapter id: `chapter11` / sequence 11
This is the first free slot after published Chapters 09 and 10. It does not collide with combinatorics or exam prep. Display sequence 11 matches the folder so sidebar ordering (`sort: "sequence"`) and URLs stay obvious.

Do not reuse Chapter 09 even if an older draft of `add-vi-applied-math-chapter` once claimed that folder.

### Add a dedicated new chapter instead of reusing the broader applications chapter
These five lessons are foundational real-life math lessons, not enrichment essays or capstone applications. They deserve a dedicated chapter that sits naturally in the learner path, separate from the later "math in sports/music/finance/..." expansion track.

### Treat the moved lessons as one coherent sequence
The new chapter should present the lessons as a continuous progression around:
- measurement
- practical unit conversion
- time and calendar reasoning
- money and everyday calculation

Visible numbering and chapter metadata should be refreshed to `11-01` … `11-05` so the published learner experience reads as one chapter rather than a set of borrowed `05-xx` titles.

Suggested order after the move:

1. `26-01-01-01_10_Do_luong.md` — measurement intuition
2. `26-01-01-04_07_Do_luong_don_vi_do_dai_khoi_luong.md` — units of length and mass
3. `26-01-01-01_08_Thoi_gian.md` — time
4. `26-01-01-04_08_Thoi_gian_xem_dong_ho_va_lich.md` — clocks and calendars
5. `26-01-01-01_09_Tien.md` — money

### Preserve old routes
Because the moved lessons already have published-style paths and may be linked from existing pages or external references, the old `contents/vi/chapter06/...` URLs should redirect to the new `contents/vi/chapter11/...` canonical URLs.

### Keep the implementation path-based
Interactive includes and redirects are keyed by `page.path` and URL structure, so moving the lessons requires synchronized updates to:
- `_data/vi_interactive_lessons.json`
- `_data/vi_lesson_redirects.json`
- `scripts/vi_curriculum_manifest.json` (`required_lessons` currently maps all five basenames to `"06"`)
- `scripts/audit_curriculum.rb` (`VISIBLE_CHAPTERS` is currently `%w[01 02 03 04 05 06 07 08]`; Chapter 11 must be added when the move ships)

### Display placement
Append Chapter 11 after Chapter 10 in the published sequence. Inserting it earlier (for example after decimals) would require remapping sequences 9–10 and is out of scope. The pedagogical home is still "everyday quantity work"; the numeric id is chosen for collision-safety, not to claim it is more advanced than exam prep.

## Open Questions
- Resolved: numeric chapter id is **11**.
- Resolved: visible titles should be renumbered to the `11-xx` prefix immediately on move.
- Still open: whether Chapter 11 should later be re-sequenced to sit next to Chapter 06 (decimals) once a broader navigation redesign is approved.

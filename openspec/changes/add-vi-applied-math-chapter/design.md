## Context
The current learner-facing Chapter 07 (`contents/vi/chapter03/`) is meant to cover logic, puzzles, rules, and equation-solving. In practice, it also contains a large optional extension block of real-world application lessons such as sports, music, architecture, finance, science, and programming. Those optional lessons are useful, but they currently make the logic chapter much longer than the surrounding chapters and blur the distinction between "reasoning skills" and "applications of math".

Several of the application lessons also use the Vietnamese interactive include, so a clean split has to update path-based mappings and preserve old URLs.

**Conflict with published Chapter 09:** on main, `contents/vi/chapter09/` is already **Tổ Hợp và Phương Pháp Đếm**. This change originally proposed reusing that folder. That plan is withdrawn. The applications chapter must use a free slot.

## Goals
- Keep learner-facing Chapter 07 focused on logic and problem solving.
- Create a dedicated learner-facing **Chapter 12** for optional “Toán Học Trong …” applied-math exploration.
- Move the optional application lessons without breaking interactive blocks or old links.
- Keep the change tight: do not reshuffle unrelated required lessons again.
- Stay distinct from Chapter 11 everyday real-life math (time, money, measurement).

## Non-Goals
- Rewriting the mathematical content of the moved lessons.
- Creating full English lesson parity for the new applications chapter in the same change.
- Reusing or renaming Chapter 09 (combinatorics) or Chapter 10 (exam prep).
- Moving the five everyday-life lessons still in `contents/vi/chapter06/` (that is `add-vi-real-life-math-chapter`).

## Canonical Split

### Learner Chapter 07 (`contents/vi/chapter03/`): Logic and Problem Solving
Keep here:
- Required lessons `07-01` through `07-13`
- `Kỹ Năng Giải Toán`
- `Bài Học Cuối Cùng - Tạm Biệt`
- Hidden chapter review / internal support pages that still belong to the logic track

### Learner Chapter 12 (`contents/vi/chapter12/`): Ứng Dụng Toán Học
Move here:
- `Toán Học Trong Thể Thao`
- `Toán Học Trong Âm Nhạc`
- `Toán Học Trong Kiến Trúc`
- `Cuộc Sống Không Toán Học`
- `Toán Học Trong Y Tế`
- `Toán Học Trong Không Gian`
- `Toán Học Trong Lập Trình`
- `Toán Học Trong Nấu Ăn`
- `Toán Học Trong Mua Sắm`
- `Toán Học Trong Giao Thông`
- `Toán Học Trong Nông Nghiệp`
- `Toán Học Trong Thời Tiết`
- `Toán Học Trong Du Lịch`
- `Toán Học Trong Trò Chơi`
- `Toán Học Trong Tài Chính`
- `Toán Học Trong Phim Ảnh`
- `Toán Học Trong Thời Gian`
- `Toán Học Trong Khoa Học`
- `Toán Học Trong Nghệ Thuật`
- `Toán Học Trong Khoa Học Máy Tính`
- `Toán Học Trong Thiên Văn`
- `Toán Học Trong Kho`
- Hidden application duplicates that mirror the same topics and should stay aligned with their visible counterparts

## Decisions

### Use internal `chapter12`, not `chapter09`
Chapter 09 is published combinatorics. Chapter 10 is exam prep. Chapter 11 is reserved for everyday real-life math. `chapter12` is the next free folder/sequence pair and preserves the chapter-to-path relationship used elsewhere.

### Append after the current Chapter 10 exam-prep stage
Applied-math exploration works as a late, optional capstone after learners have seen arithmetic, fractions, measurement, geometry, logic, data, counting methods, and (for Vietnamese Grade 6 track) exam practice. Do not insert it between existing Chapters 01–10.

### Move only the application-themed optional lessons
This keeps the change tightly scoped. Core required Logic lessons remain where they are, and only the optional application cluster is split out.

### Renumber the moved lessons as a dedicated chapter sequence
The moved lessons should no longer display as `07-33`, `07-34`, etc. They should read as a coherent learner-facing Chapter 12 sequence. The affected Logic chapter should also avoid visibly jumping from `07-13` into high-numbered extension titles where possible.

### Preserve interactive mappings and redirects
Many application lessons include `vi-interactive-lesson.html`, so `_data/vi_interactive_lessons.json` must be updated together with redirects from the old chapter03 URLs to the new chapter12 URLs.

## Risks / Trade-Offs
- Optional lessons may still have inconsistent numbering if only the moved lessons are renumbered.
  - Mitigation: refresh visible numbering for both the new applications chapter and any remaining visible Logic extensions.

- The new chapter adds another visible learner-facing stop in the curriculum.
  - Mitigation: append it as sequence 12 so the existing 01–10 path is not disturbed.

- English chapter parity remains incomplete if only the Vietnamese lessons move.
  - Mitigation: add an English chapter landing page so the visible chapter map stays aligned, while keeping lesson parity as a separate concern.

## Open Questions
- Whether Chapter 12 should be marked optional/enrichment in navigation so exam-prep remains the last “core” stop for Grade 6 families.

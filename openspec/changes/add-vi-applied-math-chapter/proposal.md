## Why
The learner-facing Vietnamese Logic and Problem Solving chapter has become too crowded because it now mixes core reasoning lessons with a long tail of optional "math in real life" lessons. That makes the logic track harder to scan and weakens the difference between abstract reasoning and applied exploration.

## Curriculum conflict (do not use chapter09)

**Current published reality (main, 2026-09):**

- Learner-facing **Chapter 09** (`contents/vi/chapter09/`, `contents/en/chapter09/`, `sequence: 9`) is **Tổ Hợp và Phương Pháp Đếm / Combinatorics and Counting Methods**. It already has published combinatorics lessons.
- Learner-facing **Chapter 10** is **Ôn Thi Vào Lớp 6 / Grade 6 Entrance Exam Prep**.
- Folder number is not the same as display order for Chapters 01–08 (`scripts/vi_curriculum_manifest.json` remaps folders). Chapters 09 and 10 currently *do* use matching folder + `sequence` ids.

An earlier draft of this change proposed moving “Toán Học Trong …” lessons into `contents/vi/chapter09/`. That **conflicts** with combinatorics and must not be implemented.

**Recommended path:** keep combinatorics in Chapter 09. Create a later optional applications chapter as **Chapter 12** (`contents/*/chapter12/`, `sequence: 12`) titled **Ứng Dụng Toán Học / Math Around Us**. Keep it separate from:

- Chapter 09 combinatorics
- Chapter 10 exam prep
- the everyday time/money/measurement chapter proposed as **Chapter 11** in `add-vi-real-life-math-chapter`

Do not archive this change: the split is still needed. Only the chapter id is corrected.

## What Changes
- Create a dedicated learner-facing Vietnamese applications chapter **after** combinatorics and exam prep (internal folder `chapter12`, display `sequence: 12`).
- Move the optional real-world application lessons that currently live under `contents/vi/chapter03/_posts/` into `contents/vi/chapter12/_posts/`.
- Keep the core logic track focused on reasoning, equations, puzzles, and pattern-finding by leaving the required Logic lessons in learner-facing Chapter 07 (`contents/vi/chapter03/`).
- Reorder moved lesson metadata and visible title prefixes so the new applications chapter reads as one continuous learner-facing sequence.
- Update Vietnamese chapter landing pages, chapter display sequencing, interactive lesson mappings, redirects, and curriculum validation so the new chapter is first-class and old links keep working.
- **Do not** overwrite `contents/*/chapter09/` or `contents/*/chapter10/`.

## Impact
- Affected specs: `vi-curriculum-sequencing`
- Related open change: `add-vi-real-life-math-chapter` (Chapter 11 — everyday measurement/time/money; distinct content)
- Affected code (when implemented):
  - `contents/vi/chapter03/_posts/*.md`
  - `contents/vi/chapter12/index.html`
  - `contents/en/chapter12/index.html`
  - `contents/vi/chapter12/_posts/*.md`
  - `_data/vi_interactive_lessons.json`
  - `_data/vi_lesson_redirects.json`
  - `scripts/vi_curriculum_manifest.json`
  - `scripts/audit_curriculum.rb`

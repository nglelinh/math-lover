## 1. Chapter definition
- [x] 1.1 Define a dedicated Vietnamese learner-facing chapter for everyday real-life math applications as **Chapter 11** (`contents/*/chapter11/`, `sequence: 11`, title **Toán Học Trong Đời Sống / Everyday Math in Life**).
- [x] 1.2 Document that this new chapter is distinct from the broader "Toán Học Trong ..." applications chapter (**Chapter 12**, `add-vi-applied-math-chapter`) and does not collide with Chapter 09 (combinatorics) or Chapter 10 (exam prep).

## 2. Curriculum move (implementation pass — not in the hygiene-only PR)
- [ ] 2.1 Create Vietnamese and English landing pages at `contents/vi/chapter11/index.html` and `contents/en/chapter11/index.html` with `chapter: "11"` and `sequence: 11`.
- [ ] 2.2 Move lessons `05-12`, `05-13`, `05-14`, `05-15`, and `05-16` from `contents/vi/chapter06/_posts/` into `contents/vi/chapter11/_posts/`.
- [ ] 2.3 Update each moved lesson's `chapter`, `order`, `categories`, and visible title prefix to `11-01` … `11-05` so they form one coherent chapter.
- [ ] 2.4 Refresh the old Chapter 06 landing page copy and lesson scope so it no longer presents those everyday-life lessons as part of the chapter.

## 3. Compatibility
- [ ] 3.1 Update `_data/vi_interactive_lessons.json` for the moved lesson paths.
- [ ] 3.2 Preserve old chapter06 URLs with redirects to the new chapter11 paths.
- [ ] 3.3 Update `scripts/vi_curriculum_manifest.json` so the five basenames map to `"11"`, add `"11": 11` under `chapter_sequences`, and extend `scripts/audit_curriculum.rb` `VISIBLE_CHAPTERS` beyond 01–08.

## 4. Verification
- [ ] 4.1 Run `python3 scripts/check_vi_interactive_coverage.py`, `ruby scripts/audit_curriculum.rb`, and `bundle exec jekyll build`.
- [ ] 4.2 Manually verify the new Chapter 11 landing page, one moved lesson, and one old URL redirect.
- [ ] 4.3 Run `openspec validate add-vi-real-life-math-chapter --strict`.

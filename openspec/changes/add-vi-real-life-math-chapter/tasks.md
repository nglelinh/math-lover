## 1. Chapter definition
- [ ] 1.1 Define a dedicated Vietnamese learner-facing chapter for everyday real-life math applications.
- [ ] 1.2 Document that this new chapter is distinct from the broader "Toán Học Trong ..." applications chapter proposed elsewhere.

## 2. Curriculum move
- [ ] 2.1 Create Vietnamese and English landing pages for the new chapter and assign it a learner-facing display sequence.
- [ ] 2.2 Move lessons `05-12`, `05-13`, `05-14`, `05-15`, and `05-16` into the new chapter folder.
- [ ] 2.3 Update each moved lesson's `chapter`, `order`, `categories`, and visible title prefix so they form one coherent chapter.
- [ ] 2.4 Refresh the old Chapter 06 landing page copy and lesson scope so it no longer presents those everyday-life lessons as part of the chapter.

## 3. Compatibility
- [ ] 3.1 Update `_data/vi_interactive_lessons.json` for the moved lesson paths.
- [ ] 3.2 Preserve old URLs with redirects to the new chapter paths.
- [ ] 3.3 Update curriculum manifest / sequencing files so the new chapter is validated like the other learner-facing chapters.

## 4. Verification
- [ ] 4.1 Run the relevant curriculum validation scripts and `bundle exec jekyll build`.
- [ ] 4.2 Manually verify the new chapter landing page, one moved lesson, and one old URL redirect.
- [ ] 4.3 Run `openspec validate add-vi-real-life-math-chapter --strict`.

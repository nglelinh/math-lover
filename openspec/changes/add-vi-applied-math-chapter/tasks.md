## 1. Chapter scope
- [ ] 1.1 Define the dedicated Vietnamese applications chapter as the home for optional real-world "math in ..." lessons that currently overload the Logic chapter.
- [ ] 1.2 Document which optional lessons move into the new chapter and which logic lessons remain in place.

## 2. Curriculum reorganization
- [ ] 2.1 Create learner-facing Chapter 09 landing pages for Vietnamese and English and wire the new display sequence into the published chapter order.
- [ ] 2.2 Move the selected Vietnamese optional application lesson files into `contents/vi/chapter09/_posts/` and update each file's `chapter`, `order`, `categories`, and visible title prefix.
- [ ] 2.3 Refresh the affected Logic chapter metadata and visible numbering so it no longer presents application lessons as part of the core reasoning track.

## 3. Compatibility and validation
- [ ] 3.1 Update `_data/vi_interactive_lessons.json` for every moved application lesson that uses the Vietnamese interactive include.
- [ ] 3.2 Preserve old chapter03 lesson URLs with redirects to their new chapter09 locations.
- [ ] 3.3 Extend the chapter-sequence manifest and curriculum audit so the new learner-facing applications chapter is validated alongside Chapters 01-08.

## 4. Verification
- [ ] 4.1 Run `python3 scripts/check_vi_interactive_coverage.py`, `ruby scripts/audit_curriculum.rb`, and `bundle exec jekyll build`.
- [ ] 4.2 Manually verify the new Chapter 09 page, a representative moved lesson, and at least one old chapter03 URL redirect.
- [ ] 4.3 Run `openspec validate add-vi-applied-math-chapter --strict`.

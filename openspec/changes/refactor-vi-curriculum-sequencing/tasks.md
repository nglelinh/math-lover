## 1. Canonical chapter map
- [x] 1.1 Define the target scope and learner-facing order for each visible Vietnamese chapter so Chapter 01 is limited to number sense, patterns, and early arithmetic, and the logic/problem-solving unit appears after Chapter 05.
- [x] 1.2 Document the required lesson migration map, including which lesson files move, which chapter/order values change, and which lessons remain in place.
- [x] 1.3 Decide and document whether the new learner-facing order is implemented by chapter renumbering, explicit display-order metadata, or another consistent mechanism.

## 2. Vietnamese lesson reorganization
- [x] 2.1 Move misplaced required Vietnamese lesson files into their destination chapter folders and update each lesson front matter (`chapter`, `order`, `categories`) to match the canonical internal chapter map.
- [x] 2.2 Reconcile duplicate or overlapping sequences across the visible Vietnamese chapters so the required path reads as a progressive curriculum rather than repeated topic clusters.
- [x] 2.3 Update Vietnamese chapter landing pages, learner-facing chapter navigation, and visible chapter numbering so the published order follows the new sequence metadata.
- [x] 2.4 Create a dedicated geometry chapter, move visible geometry lessons into it, and retune the affected decimal/measurement, logic, and data chapter numbering after the new chapter is inserted.

## 3. Compatibility and validation
- [x] 3.1 Update `_data/vi_interactive_lessons.json` so moved lesson paths still resolve to the correct Vietnamese interactive templates.
- [x] 3.2 Preserve old Vietnamese lesson URLs with redirects or equivalent migration support after file moves.
- [x] 3.3 Extend `scripts/audit_curriculum.rb` or equivalent validation so future curriculum drift is reported when chapter sequencing no longer matches the canonical map.
- [x] 3.4 Extend the canonical manifest and chapter-sequence validation so the new geometry chapter is treated as a first-class visible chapter.

## 4. Verification
- [x] 4.1 Run `bundle exec jekyll build` and `python3 scripts/check_vi_interactive_coverage.py`.
- [x] 4.2 Run `ruby scripts/audit_curriculum.rb` and confirm the reordered Vietnamese curriculum has no structural gaps introduced by the move.
- [x] 4.3 Manually verify representative moved lessons from each affected destination chapter for navigation, redirect behavior, and sidebar ordering, including the new placement of the logic/problem-solving chapter after Chapter 05.
- [x] 4.4 Manually verify the new geometry chapter page and confirm former geometry lesson URLs redirect from their previous chapter paths to the new chapter.

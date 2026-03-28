## Why
The current Vietnamese curriculum no longer follows a coherent chapter sequence. Chapter 01 mixes number sense with fractions, geometry, probability, charts, ratios, and integers; later chapters also duplicate or conflict with each other. This makes the course harder to navigate for children and parents and weakens the intended progression from simple number ideas to logic, fractions, measurement, and applications.

## What Changes
- Define a canonical Vietnamese chapter map so each visible chapter has one clear learning purpose.
- Place the current logic/problem-solving unit after learner-facing Chapter 05 by introducing explicit chapter display sequencing instead of renumbering every underlying chapter folder.
- Reassign misplaced required Vietnamese lessons to chapters whose themes match their actual content, starting with the overloaded Chapter 01 and the duplicated overlaps across Chapters 02, 04, 05, 06, and 07.
- Consolidate all visible fraction lessons into learner-facing Chapter 03 so fraction ideas stay in one continuous track, and narrow learner-facing Chapter 04 to integers and number relationships.
- Create a dedicated learner-facing geometry chapter after the current decimals/measurement stage and move all visible geometry lessons into that chapter.
- Reorder moved lessons within their destination chapters, update front matter fields such as `chapter`, `order`, and `categories`, and refresh visible lesson numbering/title prefixes so the published learner path reads in the new order.
- Update Vietnamese chapter landing pages, learner-facing chapter ordering, the Vietnamese interactive lesson mapping, and curriculum audit tooling so the new structure stays consistent.
- Preserve old Vietnamese lesson URLs with redirects so existing links do not break after file moves.

## Impact
- Affected specs: `vi-curriculum-sequencing` (new)
- Affected code:
  - `contents/vi/chapter*/_posts/*.md`
  - `contents/vi/chapter*/index.html`
  - `contents/en/chapter08/index.html`
  - `contents/vi/chapter08/index.html`
  - learner-facing chapter navigation in layouts/includes if visible ordering changes
  - `_data/vi_interactive_lessons.json`
  - `scripts/audit_curriculum.rb`
  - redirect-related behavior in `_plugins/redirect_generator.rb` or equivalent migration support

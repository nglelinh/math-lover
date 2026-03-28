## Why
The learner-facing Vietnamese Logic and Problem Solving chapter has become too crowded because it now mixes core reasoning lessons with a long tail of optional "math in real life" lessons. That makes the logic track harder to scan and weakens the difference between abstract reasoning and applied exploration.

## What Changes
- Create a dedicated learner-facing Vietnamese applications chapter after the current Data, Probability, and Applications stage.
- Move the optional real-world application lessons that currently live under `contents/vi/chapter03/_posts/` into a new `contents/vi/chapter09/_posts/` chapter folder.
- Keep the core logic track focused on reasoning, equations, puzzles, and pattern-finding by leaving the required Logic lessons in learner-facing Chapter 07.
- Reorder moved lesson metadata and visible title prefixes so the new applications chapter reads as one continuous learner-facing sequence.
- Update Vietnamese chapter landing pages, chapter display sequencing, interactive lesson mappings, redirects, and curriculum validation so the new chapter is first-class and old links keep working.

## Impact
- Affected specs: `vi-curriculum-sequencing`
- Affected code:
  - `contents/vi/chapter03/_posts/*.md`
  - `contents/vi/chapter09/index.html`
  - `contents/en/chapter09/index.html`
  - `contents/vi/chapter09/_posts/*.md`
  - `_data/vi_interactive_lessons.json`
  - `_data/vi_lesson_redirects.json`
  - `scripts/vi_curriculum_manifest.json`
  - `scripts/audit_curriculum.rb`

## Why
Vietnamese lessons currently have inconsistent interactive support: only a small subset of chapters load interactive scripts, and most Vietnamese lesson posts do not include interactive containers. This creates an uneven learning experience and does not satisfy the goal of interactive illustration coverage across all Vietnamese lessons.

## What Changes
- Add a dedicated Vietnamese interactive illustration capability that guarantees at least one interactive illustration block in every published Vietnamese lesson post.
- Restrict this rollout to Vietnamese lessons only (`page.lang == 'vi'`), leaving English lessons unchanged.
- Backfill existing Vietnamese lessons and define an authoring/validation path so all future Vietnamese lessons include interactive illustrations by default.
- Introduce a repeatable validation check to prevent new Vietnamese lessons from missing required interactive blocks.

## Impact
- Affected specs: `vi-lesson-interactivity` (new)
- Affected code:
  - `_layouts/post.html` (language-gated script loading)
  - `public/js/` (Vietnamese interactive modules)
  - `contents/vi/chapter*/_posts/*.md` (existing lesson backfill)
  - `ILLUSTRATIONS_GUIDE.md` (Vietnamese authoring guidance)
  - optional validation tooling under `scripts/` for coverage checks

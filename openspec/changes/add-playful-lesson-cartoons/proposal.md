## Why
Note: independent of the 2026-09 chapter-id hygiene (Ch.09 = combinatorics; everyday-life and applied-math tracks are planned as Ch.11 and Ch.12).

Vietnamese lessons already use static illustrations and some interactive elements, but they rarely include playful character-driven moments that make the pages feel lively for children. We need a small, repeatable way to add funny cartoons to Vietnamese lessons without turning the pages into distraction-heavy decoration.

## What Changes
- Add an optional cartoon callout pattern for Vietnamese lesson pages so authors can place short, funny, concept-linked cartoons inside lessons using the existing image workflow.
- Pilot the pattern in one Vietnamese lesson so the team can establish the right tone, layout, and placement before broader rollout.
- Extend illustration guidance with rules for cartoon tone, placement, file naming, and when humor helps the lesson in Vietnamese content.
- Keep the rollout intentionally limited: cartoons are occasional enhancements, not a new requirement for every Vietnamese lesson.

## Impact
- Affected specs: `lesson-cartoon-illustrations` (new)
- Affected code:
  - `ILLUSTRATIONS_GUIDE.md`
  - `contents/vi/chapter*/_posts/*.md` for the Vietnamese pilot lesson
  - `img/chapter_img/chapter*/` for cartoon assets
  - optional `scripts/illustrations/` updates if the pilot uses a repeatable generator

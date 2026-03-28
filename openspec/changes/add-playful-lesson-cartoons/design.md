## Context
The repository already supports static PNG illustrations in lessons and interactive lesson widgets, but those visuals are mostly explanatory rather than characterful. The requested change is to make Vietnamese lessons feel more alive by allowing occasional funny cartoons while keeping the content math-first and easy to maintain in a GitHub Pages workflow.

## Goals
- Introduce a lightweight cartoon callout pattern that fits the existing markdown and image pipeline.
- Keep humor tied to the current math idea so cartoons support attention and recall.
- Establish a reusable pattern through one Vietnamese pilot lesson.

## Non-Goals
- Requiring cartoons in every lesson.
- Introducing a new animation or JavaScript system just for cartoons.
- Redesigning lesson layouts or replacing existing explanatory illustrations.
- Changing English lesson content in this rollout.

## Decisions

### Use static cartoon callouts first
Cartoons will be introduced as static images embedded with the existing `{{ site.baseurl }}/img/...` pattern. This keeps the rollout compatible with Jekyll, GitHub Pages, and the current authoring model.

### Make the first rollout a paired pilot
The first implementation should land in one Vietnamese lesson. A single-language pilot is enough to validate humor, tone, and placement without committing the whole repository to a broader backfill or requiring English updates in the same change.

### Keep cartoons concept-linked and brief
Each cartoon should reinforce the lesson concept, such as pairing socks for even numbers or a confused pizza slice for fractions. Humor should be warm and child-friendly, and the cartoon should sit beside short Vietnamese explanatory text rather than replace it.

### Reuse the current asset structure
Cartoon assets should live in the existing chapter image directories so contributors do not need a separate storage model. If a generator is helpful, it should live under `scripts/illustrations/`; otherwise a hand-authored PNG is acceptable for the pilot.

## Trade-Offs
- Static cartoons are easier to ship, but they are less expressive than animated or interactive cartoons. This is acceptable for a first rollout because the user request is about liveliness, not animation.
- Optional usage avoids editorial burden, but it also means adoption may be uneven. The pilot and updated guidance are intended to create a pattern authors can copy when it clearly adds value in Vietnamese lessons.

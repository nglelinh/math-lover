## Context
The repository currently supports interactive JavaScript for only a few chapter-specific experiences, and those scripts are not consistently localized for Vietnamese. At the same time, there are 100+ Vietnamese lesson posts, so manual one-off interactive implementations per lesson would be hard to maintain.

The requested scope is:
- apply to all current Vietnamese lessons
- enforce the same requirement for future Vietnamese lessons
- do not change English lesson behavior

## Goals / Non-Goals
- Goals:
  - Ensure every published Vietnamese lesson has at least one interactive illustration section.
  - Keep English lessons unchanged.
  - Establish a validation mechanism so future Vietnamese lessons cannot be added without interactive coverage.
- Non-Goals:
  - Full redesign of all existing interactive UI components.
  - Feature parity updates for English interactive components.
  - New framework adoption beyond current Jekyll + vanilla JavaScript approach.

## Decisions
- Decision: Use Vietnamese-only activation at layout level.
  - Rationale: Keeps English output stable and limits risk to requested scope.
  - Approach: Gate interactive script includes with `page.lang == 'vi'`.

- Decision: Standardize on reusable interactive templates instead of unique bespoke widgets for every lesson.
  - Rationale: 110 Vietnamese posts need scalable maintenance; reusable templates reduce duplication.
  - Approach: Maintain a small set of container IDs and module behaviors that can be reused across lessons.

- Decision: Add a repository validation check for Vietnamese coverage.
  - Rationale: "All lessons + future lessons" needs an enforceable guardrail, not only documentation.
  - Approach: Validate published Vietnamese lesson markdown for required interactive container markers and report missing files.

## Risks / Trade-offs
- Risk: Some abstract lessons may not align cleanly with existing interactive templates.
  - Mitigation: Allow a generic fallback interactive template and track follow-up improvements per chapter.

- Risk: Backfilling 110 lessons can introduce inconsistent placement or wording.
  - Mitigation: Use a standard insertion section (for example, guided discovery) and a short reusable Vietnamese instruction pattern.

- Trade-off: Reusable templates are faster to deliver but less custom than per-lesson bespoke interactions.
  - Mitigation: Prioritize broad baseline coverage now; iterate with chapter-specific enrichment later.

## Migration Plan
1. Add Vietnamese-only interactive loading in layout and implement reusable Vietnamese templates.
2. Backfill all existing Vietnamese lessons with required interactive blocks.
3. Add and run coverage validation in local/CI workflow.
4. Fix gaps reported by validation until coverage is complete.

## Open Questions
- Should hidden Vietnamese posts (`hidden: true`) be exempt from coverage validation by default? (current proposal assumes yes)

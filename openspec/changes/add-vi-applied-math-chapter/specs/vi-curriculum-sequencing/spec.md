## ADDED Requirements
### Requirement: Optional Vietnamese Application Lessons Must Have a Dedicated Chapter
Optional Vietnamese lessons focused on real-world math applications SHALL be grouped under a dedicated learner-facing applications chapter rather than remaining inside the Logic and Problem Solving chapter.

#### Scenario: Application lessons move out of the Logic chapter
- **GIVEN** the visible Vietnamese learner-facing curriculum after this change
- **WHEN** the optional "math in sports, music, architecture, science, finance, programming, and daily life" lessons are reviewed
- **THEN** they appear under the dedicated applications chapter instead of the Logic and Problem Solving chapter

#### Scenario: Logic chapter keeps its core identity
- **GIVEN** the learner-facing Logic and Problem Solving chapter after this change
- **WHEN** a learner or parent reviews the chapter contents
- **THEN** the chapter focuses on reasoning, equations, puzzles, rules, and closely related support lessons rather than a large mixed list of applied-math topics

### Requirement: New Applications Chapter Must Behave Like a First-Class Learner Chapter
The dedicated Vietnamese applications chapter SHALL participate in chapter sequencing, navigation, and validation like the other learner-facing chapters.

#### Scenario: Chapter sequence includes the new applications chapter
- **GIVEN** the Vietnamese and English chapter landing pages and curriculum manifest
- **WHEN** chapter ordering is rendered or validated
- **THEN** the new applications chapter appears as an explicit learner-facing chapter in the published sequence

### Requirement: Moved Application Lessons Must Preserve Routing and Interactive Behavior
When Vietnamese application lessons move into the dedicated applications chapter, their new paths SHALL continue to resolve the correct interactive blocks and their old URLs SHALL redirect to the new canonical locations.

#### Scenario: Moved application lesson still resolves its interactive include
- **GIVEN** a moved Vietnamese application lesson that uses `vi-interactive-lesson.html`
- **WHEN** the site is built after the chapter split
- **THEN** the lesson still resolves the correct interactive lesson configuration for its new `page.path`

#### Scenario: Old logic-chapter URL redirects to the applications chapter
- **GIVEN** a Vietnamese application lesson that previously lived under `contents/vi/chapter03/`
- **WHEN** a learner opens the old lesson URL
- **THEN** the site redirects to the lesson's new canonical URL under the applications chapter

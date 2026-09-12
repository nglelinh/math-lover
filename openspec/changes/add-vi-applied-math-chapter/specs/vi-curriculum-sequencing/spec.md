## ADDED Requirements
### Requirement: Optional Vietnamese Application Lessons Must Have a Dedicated Chapter
Optional Vietnamese lessons focused on real-world math applications SHALL be grouped under a dedicated learner-facing applications chapter (internal folder `chapter12`, display sequence 12) rather than remaining inside the Logic and Problem Solving chapter or overwriting published Chapters 09 or 10.

#### Scenario: Application lessons move out of the Logic chapter
- **GIVEN** the visible Vietnamese learner-facing curriculum after this change
- **WHEN** the optional "math in sports, music, architecture, science, finance, programming, and daily life" lessons are reviewed
- **THEN** they appear under learner-facing Chapter 12 (Ứng Dụng Toán Học) instead of the Logic and Problem Solving chapter

#### Scenario: Logic chapter keeps its core identity
- **GIVEN** the learner-facing Logic and Problem Solving chapter after this change
- **WHEN** a learner or parent reviews the chapter contents
- **THEN** the chapter focuses on reasoning, equations, puzzles, rules, and closely related support lessons rather than a large mixed list of applied-math topics

#### Scenario: Combinatorics and exam-prep chapters stay intact
- **GIVEN** published Chapter 09 (Tổ Hợp và Phương Pháp Đếm) and Chapter 10 (Ôn Thi Vào Lớp 6)
- **WHEN** the applications chapter is added
- **THEN** those two chapters keep their existing folders, sequences, landing pages, and lesson files

### Requirement: New Applications Chapter Must Behave Like a First-Class Learner Chapter
The dedicated Vietnamese applications chapter SHALL participate in chapter sequencing, navigation, and validation like the other learner-facing chapters, using folder `chapter12` and display sequence 12.

#### Scenario: Chapter sequence includes the new applications chapter
- **GIVEN** the Vietnamese and English chapter landing pages and curriculum manifest
- **WHEN** chapter ordering is rendered or validated
- **THEN** Chapter 12 appears as an explicit learner-facing applications chapter after Chapter 11 (everyday real-life math) and does not reuse sequence 9 or 10

### Requirement: Moved Application Lessons Must Preserve Routing and Interactive Behavior
When Vietnamese application lessons move into the dedicated applications chapter, their new paths SHALL continue to resolve the correct interactive blocks and their old URLs SHALL redirect to the new canonical locations.

#### Scenario: Moved application lesson still resolves its interactive include
- **GIVEN** a moved Vietnamese application lesson that uses `vi-interactive-lesson.html`
- **WHEN** the site is built after the chapter split
- **THEN** the lesson still resolves the correct interactive lesson configuration for its new `page.path` under `contents/vi/chapter12/`

#### Scenario: Old logic-chapter URL redirects to the applications chapter
- **GIVEN** a Vietnamese application lesson that previously lived under `contents/vi/chapter03/`
- **WHEN** a learner opens the old lesson URL
- **THEN** the site redirects to the lesson's new canonical URL under `contents/vi/chapter12/`

## ADDED Requirements
### Requirement: Vietnamese Required Lessons Must Follow Canonical Chapter Scopes
Visible required Vietnamese lessons under `contents/vi/chapter*/_posts/*.md` SHALL be organized into chapters whose themes match the canonical curriculum sequence for number sense, multiplicative thinking, fractions, number relationships, measurement/geometry, logic/problem solving, and data/probability.

#### Scenario: Chapter 01 is limited to foundational number sense
- **GIVEN** the visible required Vietnamese lessons in Chapter 01
- **WHEN** the curriculum structure is reviewed after this change
- **THEN** Chapter 01 contains only foundational number-sense, pattern, and early arithmetic lessons rather than fractions, probability, charts, measurement, ratios, or geometry units

#### Scenario: Logic and problem solving appear after learner-facing Chapter 05
- **GIVEN** the visible learner-facing Vietnamese chapter sequence
- **WHEN** the curriculum is reviewed after this change
- **THEN** the logic/problem-solving unit appears after learner-facing Chapter 05 via the published chapter sequence, even if the internal chapter folder IDs remain stable

#### Scenario: Later chapters receive the lessons that match their themes
- **GIVEN** a Vietnamese required lesson about fractions, logic, measurement, decimals, or data
- **WHEN** the curriculum is reorganized
- **THEN** that lesson appears under the chapter whose published scope matches the lesson’s actual topic

#### Scenario: Fraction lessons are consolidated under learner-facing Chapter 03
- **GIVEN** the visible learner-facing Vietnamese chapter sequence after this change
- **WHEN** fraction lessons are reviewed across learner-facing Chapters 03 and 04
- **THEN** the fraction sequence appears under learner-facing Chapter 03 and learner-facing Chapter 04 is reserved for integers and number relationships

#### Scenario: Geometry lessons are consolidated under a dedicated learner-facing chapter
- **GIVEN** the visible learner-facing Vietnamese chapter sequence after this change
- **WHEN** geometry lessons are reviewed across the decimal/measurement stage and the new geometry stage
- **THEN** visible geometry lessons appear under the dedicated learner-facing geometry chapter rather than being split across unrelated chapters

### Requirement: Reorganized Vietnamese Lessons Must Stay Internally Consistent
When a Vietnamese lesson is moved to a new chapter, its file location, front matter chapter metadata, order, and chapter category SHALL be updated together so the repository reflects one consistent curriculum structure.

#### Scenario: Moved lesson metadata matches its destination chapter
- **GIVEN** a Vietnamese required lesson that is reassigned to a different chapter
- **WHEN** the lesson file is updated
- **THEN** its directory path, `chapter`, `order`, and `categories` all match the destination chapter and chapter sequence

### Requirement: Interactive Mapping Must Follow Lesson Moves
Vietnamese lesson moves SHALL preserve the interactive lesson experience by updating path-based mapping entries under `_data/vi_interactive_lessons.json`.

#### Scenario: Moved lesson still loads its interactive block
- **GIVEN** a Vietnamese lesson that has an interactive block and is moved to a new chapter path
- **WHEN** the site is built
- **THEN** the lesson still resolves the correct interactive template and learner guidance for its new `page.path`

### Requirement: Legacy Vietnamese Lesson URLs Must Continue to Resolve
Reorganizing Vietnamese lesson files SHALL preserve access from old lesson URLs so existing bookmarks and links do not break.

#### Scenario: Old lesson URL redirects to the new chapter path
- **GIVEN** a Vietnamese lesson that previously lived under one chapter URL and is moved to another
- **WHEN** a learner opens the old URL
- **THEN** the site redirects the learner to the lesson’s new canonical URL

### Requirement: Curriculum Drift Must Be Detectable
Repository validation SHALL report structural drift when visible required Vietnamese lessons no longer match the canonical chapter map after the reorganization.

#### Scenario: Validation detects a lesson in the wrong chapter family
- **GIVEN** a visible required Vietnamese lesson is added or left under a chapter that does not match the canonical curriculum scope
- **WHEN** curriculum validation is run
- **THEN** the audit reports the mismatch instead of silently accepting the drift

## ADDED Requirements
### Requirement: Interactive Coverage for Vietnamese Lessons
The system SHALL provide at least one interactive illustration block in every published Vietnamese lesson post under `contents/vi/chapter*/_posts/*.md`.

#### Scenario: Existing Vietnamese lesson renders an interactive block
- **GIVEN** a published Vietnamese lesson post already present in the repository
- **WHEN** the site is built and the lesson page is rendered
- **THEN** the page includes at least one interactive illustration container that is initialized by a Vietnamese interactive module

#### Scenario: New Vietnamese lesson is required to include interactivity
- **GIVEN** a newly added published Vietnamese lesson post
- **WHEN** repository validation is executed
- **THEN** validation fails if the lesson does not include an interactive illustration container

### Requirement: Vietnamese-Only Interactive Activation
Interactive illustration assets introduced by this change SHALL be activated only for Vietnamese lesson pages and SHALL NOT change English lesson behavior.

#### Scenario: Vietnamese lesson loads interactive assets
- **GIVEN** a lesson page where `page.lang` is `vi`
- **WHEN** the page is rendered
- **THEN** the Vietnamese interactive script bundle is included and initializes available interactive containers

#### Scenario: English lesson remains unchanged
- **GIVEN** a lesson page where `page.lang` is not `vi`
- **WHEN** the page is rendered
- **THEN** Vietnamese-only interactive assets from this change are not loaded

### Requirement: Vietnamese Guidance for Interactive Blocks
Each interactive illustration block in Vietnamese lessons SHALL include short Vietnamese learner guidance text describing how to use the interaction.

#### Scenario: Learner sees Vietnamese usage instructions
- **GIVEN** a Vietnamese lesson page with an interactive illustration block
- **WHEN** the learner reaches that section
- **THEN** the page shows concise Vietnamese instructions adjacent to the interactive container

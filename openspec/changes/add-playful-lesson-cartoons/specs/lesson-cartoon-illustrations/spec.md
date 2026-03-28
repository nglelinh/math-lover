## ADDED Requirements
### Requirement: Optional Cartoon Callouts in Vietnamese Lessons
The lesson authoring system SHALL support occasional static cartoon callouts in Vietnamese lesson markdown using the existing image asset workflow.

#### Scenario: Author embeds a cartoon callout
- **GIVEN** an author is editing a Vietnamese lesson post
- **WHEN** the author references a cartoon image stored under `img/chapter_img/chapter*/` with the standard `{{ site.baseurl }}/img/...` path pattern
- **THEN** the lesson renders the cartoon without requiring a new runtime dependency or a custom page layout

### Requirement: Cartoons Must Support the Math Idea
Cartoon callouts SHALL be age-appropriate, visually simple, and directly related to the current math concept so they add personality without distracting from the lesson goal.

#### Scenario: Cartoon humor stays concept-linked
- **GIVEN** a Vietnamese lesson section explaining a specific math idea
- **WHEN** a cartoon callout is added to that section
- **THEN** the cartoon humor reinforces the same concept or example and the surrounding text keeps the math explanation primary

### Requirement: Vietnamese Pilot and Authoring Guidance
The repository SHALL document how to add cartoon callouts and establish the pattern with at least one Vietnamese lesson example.

#### Scenario: Contributor follows the documented pattern
- **GIVEN** a contributor wants to add a cartoon to a future lesson
- **WHEN** they consult `ILLUSTRATIONS_GUIDE.md`
- **THEN** they find guidance for tone, placement, asset naming, and Vietnamese lesson usage expectations

#### Scenario: Pilot lesson establishes the pattern
- **GIVEN** the selected pilot lesson is a Vietnamese lesson
- **WHEN** the cartoon callout pattern is introduced
- **THEN** the lesson includes a cartoon moment tied to the same math concept as the surrounding section

### Requirement: Vietnamese Cartoon Rollout Remains Optional
The initial Vietnamese cartoon rollout SHALL remain optional and SHALL NOT require every published Vietnamese lesson to include a cartoon callout.

#### Scenario: Lesson without cartoon remains valid
- **GIVEN** a published Vietnamese lesson that does not include a cartoon callout
- **WHEN** the site is built or repository validation is run
- **THEN** the lesson remains valid and does not fail solely because no cartoon is present

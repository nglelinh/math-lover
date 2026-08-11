## ADDED Requirements
### Requirement: Everyday Real-Life Math Lessons Must Form a Dedicated Chapter
The Vietnamese learner-facing curriculum SHALL group the lessons about measurement, practical units, time, calendar, and money into a dedicated chapter for everyday real-life math.

#### Scenario: Real-life math lessons are no longer mixed into the decimals bridge chapter
- **GIVEN** the published Vietnamese learner-facing curriculum after this change
- **WHEN** lessons `05-12`, `05-13`, `05-14`, `05-15`, and `05-16` are reviewed
- **THEN** they appear under a dedicated real-life math chapter rather than inside the decimals / ratios bridge chapter

#### Scenario: The new chapter reads as a coherent life-application sequence
- **GIVEN** the new dedicated chapter
- **WHEN** a learner or parent opens the chapter landing page and lesson list
- **THEN** the chapter presents a coherent progression around measurement, time, calendar, and money in daily life

### Requirement: The Real-Life Math Chapter Must Stay Separate From the Broader Applications Chapter
The dedicated everyday real-life math chapter SHALL remain distinct from the broader applications chapter used for "Toán Học Trong ..." enrichment lessons.

#### Scenario: Everyday-life lessons are not merged into the broader applications chapter
- **GIVEN** both chapter concepts exist in the curriculum plan
- **WHEN** the curriculum is reviewed after this change
- **THEN** lessons `05-12` through `05-16` belong to the dedicated real-life math chapter and not to the broader "Toán Học Trong ..." applications chapter

### Requirement: Moved Lessons Must Preserve Navigation and Interactive Behavior
When the five real-life math lessons move into their own chapter, their interactive mappings, sequencing, and old URLs SHALL continue to resolve correctly.

#### Scenario: Interactive lesson config follows the moved files
- **GIVEN** a moved real-life math lesson that uses the Vietnamese interactive include
- **WHEN** the site is built after the chapter split
- **THEN** the lesson resolves its interactive configuration using its new `page.path`

#### Scenario: Old URLs redirect to the new chapter
- **GIVEN** a real-life math lesson that previously lived under `contents/vi/chapter06/`
- **WHEN** a learner opens the old lesson URL
- **THEN** the site redirects to the lesson's new canonical URL under the dedicated real-life math chapter

#### Scenario: Chapter sequence includes the new real-life math chapter
- **GIVEN** the learner-facing chapter order, sidebar, and curriculum manifest
- **WHEN** chapter sequencing is rendered or validated
- **THEN** the new real-life math chapter appears as an explicit chapter in the published sequence

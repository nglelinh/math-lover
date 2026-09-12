## ADDED Requirements
### Requirement: Everyday Real-Life Math Lessons Must Form a Dedicated Chapter
The Vietnamese learner-facing curriculum SHALL group the lessons about measurement, practical units, time, calendar, and money into a dedicated chapter for everyday real-life math using internal folder `chapter11` and display sequence 11.

#### Scenario: Real-life math lessons are no longer mixed into the decimals bridge chapter
- **GIVEN** the published Vietnamese learner-facing curriculum after this change
- **WHEN** lessons `05-12`, `05-13`, `05-14`, `05-15`, and `05-16` are reviewed
- **THEN** they appear under learner-facing Chapter 11 (Toán Học Trong Đời Sống) rather than inside the decimals / ratios bridge chapter

#### Scenario: The new chapter reads as a coherent life-application sequence
- **GIVEN** the new dedicated Chapter 11
- **WHEN** a learner or parent opens the chapter landing page and lesson list
- **THEN** the chapter presents a coherent progression around measurement, time, calendar, and money in daily life with visible `11-xx` numbering

### Requirement: The Real-Life Math Chapter Must Stay Separate From the Broader Applications Chapter
The dedicated everyday real-life math chapter SHALL remain distinct from the broader applications chapter used for "Toán Học Trong ..." enrichment lessons and SHALL NOT reuse published Chapter 09 (combinatorics) or Chapter 10 (exam prep).

#### Scenario: Everyday-life lessons are not merged into the broader applications chapter
- **GIVEN** both chapter concepts exist in the curriculum plan
- **WHEN** the curriculum is reviewed after this change
- **THEN** lessons `05-12` through `05-16` belong to Chapter 11 and not to Chapter 12 ("Toán Học Trong ..." applications)

#### Scenario: Chapter 11 does not overwrite combinatorics or exam prep
- **GIVEN** published Chapter 09 and Chapter 10
- **WHEN** Chapter 11 is added
- **THEN** Chapters 09 and 10 keep their existing folders, sequences, and lesson files

### Requirement: Moved Lessons Must Preserve Navigation and Interactive Behavior
When the five real-life math lessons move into their own chapter, their interactive mappings, sequencing, and old URLs SHALL continue to resolve correctly.

#### Scenario: Interactive lesson config follows the moved files
- **GIVEN** a moved real-life math lesson that uses the Vietnamese interactive include
- **WHEN** the site is built after the chapter split
- **THEN** the lesson resolves its interactive configuration using its new `page.path` under `contents/vi/chapter11/`

#### Scenario: Old URLs redirect to the new chapter
- **GIVEN** a real-life math lesson that previously lived under `contents/vi/chapter06/`
- **WHEN** a learner opens the old lesson URL
- **THEN** the site redirects to the lesson's new canonical URL under `contents/vi/chapter11/`

#### Scenario: Chapter sequence includes the new real-life math chapter
- **GIVEN** the learner-facing chapter order, sidebar, and curriculum manifest
- **WHEN** chapter sequencing is rendered or validated
- **THEN** Chapter 11 appears as an explicit chapter with display sequence 11

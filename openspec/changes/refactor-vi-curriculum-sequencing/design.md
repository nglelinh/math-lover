## Context
The Vietnamese curriculum is the only fully populated version of the 8-12 course. Over time, required lessons were added to the wrong chapter buckets, so the visible course path now mixes beginner topics and advanced topics in the same chapter and duplicates similar ideas across later chapters. The most obvious example is Chapter 01, which currently includes fractions, measurement, probability, data, ratios, 3D solids, and integers even though the chapter landing page defines it as number sense and patterns.

This drift is not limited to Chapter 01:
- Chapter 02 includes prime numbers, GCF/LCM, decimals, percentages, and geometry, which conflict with both its chapter description and later chapters.
- Chapter 04 includes hidden algebra lessons plus measurement, data, and percentage lessons that do not fit the current "Fractions and Fair Sharing" scope.
- Chapter 07 includes probability and data as expected, but also equations, percentages, and sequence lessons that fit earlier concept chapters better.

The requested sequencing adjustment adds one more constraint:
- the logic/problem-solving unit currently associated with internal Chapter 03 should move later in the learning path, after learner-facing Chapter 05.

Because lesson URLs depend on chapter folders and because Vietnamese interactive blocks are keyed by `page.path`, a safe reorganization must cover routing, metadata, and mapping together.

## Goals
- Restore a coherent Vietnamese chapter progression for visible required lessons.
- Remove the Chapter 01 overload and reduce topic duplication across later chapters.
- Place the logic/problem-solving stage after the fractions, number-relationship, decimal/measurement, and dedicated geometry stages.
- Keep the migration safe by preserving old lesson URLs and updating interactive mappings.
- Add validation so chapter drift is easier to catch in future edits.

## Non-Goals
- Rewriting the mathematical content of every moved lesson from scratch.
- Completing English parity for all Vietnamese lessons in this same change.
- Redesigning the interactive system itself beyond path updates needed for moved lessons.

## Canonical Learner-Facing Chapter Order

The implementation keeps the existing chapter folders and `chapter` metadata stable for routing, categories, and bilingual matching, then adds explicit `sequence` metadata on chapter landing pages so the published learner order can differ from the internal chapter ID.

### Learner Chapter 01 (`contents/*/chapter01/`): Number Sense and Patterns
Focus on ideas children can build from counting, parity, simple patterns, and early arithmetic reasoning.

Keep here:
- `01-01 Khám phá số chẵn - Quy luật của cặp đôi`
- `01-02 Khám phá các mẫu hình kỳ diệu`
- `01-11 Khám phá phép trừ - Suy nghĩ sâu hơn`
- `01-12 Khám phá phép cộng - Những điều thú vị`
- `01-15 Khám phá toán với quy luật - Tìm quy luật để giải toán`

### Learner Chapter 02 (`contents/*/chapter02/`): Multiplicative Thinking
Focus on repeated groups, multiplication, division, and operation properties that prepare learners for factors and fractions.

Move or keep here:
- `01-03 Khám phá phép nhân kỳ diệu`
- `01-06 Khám phá phép chia - Chia công bằng`
- `02-03 Phép nhân nâng cao - Mẹo tính nhanh`
- `02-04 Phép chia nâng cao - Chia có dư`
- `02-05 Tính chất phép toán - Quy luật thú vị`

### Learner Chapter 03 (`contents/*/chapter04/`): Fractions and Fair Sharing
Focus on core fraction concepts, visual equal-sharing lessons, and the fraction-fluency sequence that follows naturally from them.

Move or keep here:
- `01-07 Khám phá phân số - Chia làm phần bằng nhau`
- `Một Nửa và Một Phần Tư - Chia Sẻ Công Bằng`
- `05-06 Phân số bằng nhau - Khi nào hai phân số bằng nhau?`
- `05-07 So sánh phân số - Ai lớn hơn, ai nhỏ hơn?`
- `05-08 Cộng trừ phân số - Kết hợp các phần`
- `05-09 Hỗn số - Khi phân số lớn hơn 1`
- English-aligned Chapter 04 fraction lessons already present

### Learner Chapter 04 (`contents/*/chapter05/`): Integers and Number Relationships
Focus on integers, special numbers, factors, multiples, and divisibility after the fraction sequence has already been completed in learner-facing Chapter 03.

Move or keep here:
- `01-13 Khám phá số nguyên - Số âm và Số dương`
- existing Chapter 05 lessons on square numbers, factors, multiples, primes, UCLN, and BCNN

### Learner Chapter 05 (`contents/*/chapter06/`): Decimals, Ratios, Geometry, and Measurement
Focus on decimal notation, ratio thinking, time, money, measurement, and applied quantity relationships.

Move or keep here:
- `01-08 Khám phá thời gian - Đồng hồ và Lịch`
- `01-09 Khám phá tiền - Tiền Việt Nam`
- `01-10 Khám phá đo lường - Chiều dài, Cân nặng, Dung tích`
- `01-19 Khám phá tỷ lệ - So sánh bằng phép chia`
- `02-07 Số thập phân - Thế giới của phẩy`
- `02-08 Tỷ số và Tỷ lệ phần trăm`
- `04-04 Tỷ lệ thuận nghịch - Hai đại lượng`
- `04-05 Phần trăm ứng dụng - Trong cuộc sống`
- `04-07 Đo lường - Đơn vị đo độ dài và khối lượng`
- `04-08 Thời gian - Xem đồng hồ và lịch`
- `07-05 Tỉ lệ phần trăm nâng cao - Ứng dụng trong cuộc sống`

### Learner Chapter 06 (`contents/*/chapter08/`): Geometry and Spatial Reasoning
Focus on shapes, angles, perimeter, area, solids, volume, and spatial reasoning in one continuous geometry track.

Move or keep here:
- `01-05 Khám phá hình học - Thế giới của các hình`
- `02-09 Hình học nâng cao - Góc và Đường thẳng`
- `04-06 Hình học - Hình tam giác và hình vuông`
- `06-06 Hình học - Hình chữ nhật và hình bình hành`
- `06-07 Hình học - Hình thoi và hình thang`
- `01-18 Khám phá chu vi và diện tích - Đo lường hình phẳng`
- `03-02 Hình học nâng cao - Diện tích và Chu vi`
- `06-08 Diện tích hình tam giác và hình tròn`
- `01-16 Khám phá hình khối - Thế giới 3D`
- `06-09 Thể tích hình hộp chữ nhật và hình lập phương`
- `07-06 Hình học không gian - Hình cầu và hình nón`
- `07-07 Hình trụ - Đo lường và ứng dụng`

### Learner Chapter 07 (`contents/*/chapter03/`): Logic and Problem Solving
Focus on reasoning, puzzle structure, variables, equations, rule-finding, and challenge-style lessons that should come after learners have seen more arithmetic and measurement structure.

Move or keep here:
- `01-04 Thử thách trí tuệ - Suy luận thông minh`
- `01-20 Khám phá toán học vui - Games và Puzzle`
- `03-01 Toán tư duy - Thử thách trí não`
- `03-04 Các bài toán đố - Giải bằng tư duy`
- `03-06 Lưới số và Ô số Sudoku`
- `03-07 Toán suy luận - Tìm quy luật`
- `03-08 Toán vui - Trò chơi và Câu đố`
- `04-01 Đại số sơ bộ - Giới thiệu về biến số` (currently hidden but structurally belongs here)
- `04-02 Phương trình - Tìm số bí mật`
- `07-04 Phương trình nâng cao - Giải toán có ẩn số`
- `07-08 Dãy số - Tìm quy luật và số tiếp theo`

### Learner Chapter 08 (`contents/*/chapter07/`): Data, Probability, and Applications
Focus on probability, statistics, charts, and modern application lessons that belong at the end of the core path.

Move or keep here:
- `01-14 Khám phá xác suất - May rủi trong toán học`
- `01-17 Khám phá biểu đồ - Nói chuyện bằng hình ảnh`
- `04-09 Dữ liệu - Thu thập và biểu diễn thông tin`
- existing Chapter 07 data, chart, probability, and computing lessons

## Key Findings Driving the Migration
- Chapter 01 currently contains at least 15 required lessons whose themes better match Chapters 02, 03, 04, 05, 06, or 07.
- Chapter 02 duplicates Chapter 05 for prime/factor content and duplicates Chapter 06 for decimal/percentage/geometry content.
- Geometry currently sits inside the decimal/measurement stage even though it forms a large enough concept family to justify its own learner-facing chapter.
- Chapter 04 has already been redefined as fractions, but the learner-facing Chapter 04 track still contains fraction-fluency lessons that should be consolidated into the learner-facing fraction chapter.
- The current logic/problem-solving chapter sits too early for the sequence you requested and needs to move after the fraction and fluency stages.
- Vietnamese interactive coverage is path-based, so lesson moves must be coordinated with `_data/vi_interactive_lessons.json`.
- Moving posts changes generated URLs, so redirects are required to avoid breaking existing links and bookmarks.

## Migration Decisions

### Move files instead of only editing metadata
The lesson file path should match the declared internal chapter because chapter folders drive URLs, contributor expectations, and mapping lookups. Keeping old folders with new `chapter` metadata would preserve internal inconsistency.

### Use explicit display-order metadata instead of renumbering folders
The curriculum should be organized around the order learners actually follow, but chapter folder names and `chapter` front matter remain the stable internal identifiers. Chapter landing pages therefore carry a `sequence` value that drives sidebar order, chapter headings, and learner-facing numbering.

### Add a dedicated geometry chapter instead of leaving geometry embedded in measurement
Geometry now spans enough visible required lessons to warrant its own learner-facing stage. Splitting it out keeps the decimal/measurement chapter tighter and gives shapes, area, and 3D reasoning a clearer conceptual home.

### Preserve compatibility with redirects
Old Vietnamese lesson URLs should continue to resolve. The redirect strategy can extend the existing redirect plugin or generate equivalent redirect pages during the migration.

### Update audit rules to check curriculum intent
The current curriculum audit checks for order gaps and parity gaps, but it does not verify that lessons live under chapters matching their actual topic family. The migration should add a canonical scope check for visible Vietnamese required lessons.

## Risks / Trade-Offs
- A broad move can introduce broken links, missing interactive mappings, or sidebar order gaps if handled piecemeal.
  - Mitigation: apply the migration in one chapter-map pass, then run build and coverage audits immediately.

- Some lessons sit on chapter boundaries, such as integers or basic geometry.
  - Mitigation: choose the destination chapter by overall curriculum progression rather than by a single keyword, and document those choices in the canonical map.

- Decoupling learner-facing chapter numbering from internal chapter IDs introduces a risk of inconsistent labels across chapter pages and lesson titles.
  - Mitigation: make `sequence` authoritative for published chapter headings/sidebar labels and refresh visible lesson title prefixes to match the learner-facing order.

- English parity will still be incomplete after the Vietnamese reorganization.
  - Mitigation: keep this change focused on the Vietnamese source-of-truth curriculum and leave English lesson expansion for a separate change.

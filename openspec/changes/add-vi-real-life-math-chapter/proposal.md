## Why
Các bài `05-12` đến `05-16` hiện đang nằm rải trong Chapter 06 dù nội dung của chúng thiên về các tình huống đời sống hằng ngày như đo lường, xem giờ, lịch, và tiền. Nhóm bài này không hoàn toàn khớp với trọng tâm hiện tại của Chapter 06 là số thập phân, tỉ số, phần trăm và cầu nối lên giai đoạn 10-12 tuổi.

Ngoài ra, repo đã có một proposal riêng để tạo chapter "ứng dụng toán học" cho nhóm bài "Toán học trong ..." ở mức mở rộng. Nhóm bài `05-12` đến `05-16` nên được tách thành một chapter riêng về toán học trong cuộc sống hằng ngày, thay vì gộp vào chapter ứng dụng mở rộng đó.

## Concrete chapter id

**Use learner-facing Chapter 11.**

| Role | Folder | `sequence` | Title |
|------|--------|------------|--------|
| Combinatorics (already published) | `chapter09` | 9 | Tổ Hợp và Phương Pháp Đếm |
| Exam prep (already published) | `chapter10` | 10 | Ôn Thi Vào Lớp 6 |
| **Everyday real-life math (this change)** | **`chapter11`** | **11** | **Toán Học Trong Đời Sống / Everyday Math in Life** |
| Optional “Toán Học Trong …” enrichment | `chapter12` | 12 | Ứng Dụng Toán Học (`add-vi-applied-math-chapter`) |

Folder number is not always display order for Chapters 01–08 (`scripts/vi_curriculum_manifest.json`). Chapters 09–10 currently match folder + sequence. Chapter 11 should follow that same pair so navigation (`sequence`) and paths stay aligned.

The five lessons **are still** in `contents/vi/chapter06/_posts/` on main. This hygiene update documents the corrected plan. Lesson files are **not** moved until the proposal is approved and validation (interactive coverage, curriculum audit, Jekyll build) is run in an implementation pass.

## What Changes
- Tạo learner-facing **Chapter 11** (`contents/vi/chapter11/`, `contents/en/chapter11/`, `sequence: 11`) cho "Toán Học Trong Đời Sống".
- Chuyển các bài `05-12`, `05-13`, `05-14`, `05-15`, `05-16` sang `contents/vi/chapter11/_posts/`.
- Cập nhật front matter, title prefix hiển thị, `chapter: '11'`, `order`, `categories: [chapter11]`, chapter landing page, sequencing, điều hướng, interactive mappings, và redirects liên quan.
- Cập nhật `scripts/vi_curriculum_manifest.json` để các basename sau đổi canonical chapter từ `"06"` sang `"11"`:
  - `26-01-01-01_08_Thoi_gian.md`
  - `26-01-01-01_09_Tien.md`
  - `26-01-01-01_10_Do_luong.md`
  - `26-01-01-04_07_Do_luong_don_vi_do_dai_khoi_luong.md`
  - `26-01-01-04_08_Thoi_gian_xem_dong_ho_va_lich.md`
- Giữ chapter ứng dụng mở rộng kiểu "Toán Học Trong ..." ở **Chapter 12**; không gộp hai nhóm nội dung này làm một.
- Visible numbering: renumber immediately to `11-01` … `11-05` (do not keep stale `05-xx` prefixes).

## Impact
- Affected specs: `vi-curriculum-sequencing`
- Related open change: `add-vi-applied-math-chapter` (Chapter 12 — optional “Toán Học Trong …” essays)
- Affected code (when implemented):
  - `contents/vi/chapter06/_posts/26-01-01-01_08_Thoi_gian.md`
  - `contents/vi/chapter06/_posts/26-01-01-01_09_Tien.md`
  - `contents/vi/chapter06/_posts/26-01-01-01_10_Do_luong.md`
  - `contents/vi/chapter06/_posts/26-01-01-04_07_Do_luong_don_vi_do_dai_khoi_luong.md`
  - `contents/vi/chapter06/_posts/26-01-01-04_08_Thoi_gian_xem_dong_ho_va_lich.md`
  - `contents/vi/chapter06/index.html`
  - `contents/vi/chapter11/index.html`
  - `contents/en/chapter11/index.html`
  - `_data/vi_interactive_lessons.json`
  - `_data/vi_lesson_redirects.json`
  - `scripts/vi_curriculum_manifest.json`
  - `scripts/audit_curriculum.rb` (`VISIBLE_CHAPTERS` currently only lists 01–08)
  - navigation/rendering files that depend on chapter sequencing

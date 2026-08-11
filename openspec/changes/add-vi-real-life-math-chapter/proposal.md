## Why
Các bài `05-12` đến `05-16` hiện đang nằm rải trong Chapter 06 dù nội dung của chúng thiên về các tình huống đời sống hằng ngày như đo lường, xem giờ, lịch, và tiền. Nhóm bài này không hoàn toàn khớp với trọng tâm hiện tại của Chapter 06 là số thập phân, tỉ số, phần trăm và cầu nối lên giai đoạn 10-12 tuổi.

Ngoài ra, repo đã có một proposal riêng để tạo chapter "ứng dụng toán học" cho nhóm bài "Toán học trong ..." ở mức mở rộng. Nhóm bài `05-12` đến `05-16` nên được tách thành một chapter riêng về toán học trong cuộc sống hằng ngày, thay vì gộp vào chapter ứng dụng mở rộng đó.

## What Changes
- Tạo một learner-facing chapter mới riêng cho "ứng dụng toán học trong cuộc sống" trong tuyến tiếng Việt.
- Chuyển các bài `05-12`, `05-13`, `05-14`, `05-15`, `05-16` sang chapter mới này.
- Cập nhật front matter, title prefix hiển thị, `chapter`, `order`, `categories`, chapter landing page, sequencing, điều hướng, interactive mappings, và redirects liên quan.
- Giữ chapter ứng dụng mở rộng kiểu "Toán Học Trong ..." là một proposal tách biệt; không gộp hai nhóm nội dung này làm một.

## Impact
- Affected specs: `vi-curriculum-sequencing`
- Affected code:
  - `contents/vi/chapter06/_posts/26-01-01-01_08_Thoi_gian.md`
  - `contents/vi/chapter06/_posts/26-01-01-01_09_Tien.md`
  - `contents/vi/chapter06/_posts/26-01-01-01_10_Do_luong.md`
  - `contents/vi/chapter06/_posts/26-01-01-04_07_Do_luong_don_vi_do_dai_khoi_luong.md`
  - `contents/vi/chapter06/_posts/26-01-01-04_08_Thoi_gian_xem_dong_ho_va_lich.md`
  - `contents/vi/chapter06/index.html`
  - `contents/vi/<new-chapter>/index.html`
  - `contents/en/<new-chapter>/index.html`
  - `_data/vi_interactive_lessons.json`
  - `_data/vi_lesson_redirects.json`
  - `scripts/vi_curriculum_manifest.json`
  - navigation/rendering files that depend on chapter sequencing

# Ôn thi vào lớp 6 — Trường chuyên & chất lượng cao

Thư mục này là **kho nguồn** (đề, ảnh, catalog). Nội dung đã được biên soạn thành **Chương 10** của course Math-Lover:

## Course Chapter 10 (primary)

Toàn bộ đề dùng để học đã được **nhúng vào Chương 10** (`contents/vi/chapter10/`, `contents/en/chapter10/`).  
Học trên site: sidebar **10. Ôn Thi Vào Lớp 6** — không cần mở thư mục này.

Thư mục `on-thi-lop-6/` chỉ còn là **kho lưu trữ / nguồn thô** (backup).


- VI: `contents/vi/chapter10/`
- EN: `contents/en/chapter10/`
- Ảnh bài học: `img/chapter10/`

Thư mục này tập trung **tài liệu thô & đầy đủ** (đề text, scan cả trang, kế hoạch) để thi vào các trường THCS chuyên / CLC — **ưu tiên Hà Nội và TP.HCM**.

## Mục tiêu

1. **Thu thập & catalog** đề thi vào lớp 6 các trường hot (kèm link nguồn + ghi chú đáp án).
2. **Kế hoạch ôn luyện** theo giai đoạn, bám sát dạng đề thật.
3. **Liên kết** từng chuyên đề với các **bài lesson** đang có trong course Math-Lover.
4. **Luyện dạng** với ngân hàng bài toán (đã chuẩn hóa công thức LaTeX ở phần biên tập).

> **Phạm vi môn:** Course hiện tại là **Toán**. Kế hoạch ưu tiên Toán + tư duy logic; Tiếng Việt / Tiếng Anh được ghi chú cấu trúc đề để phụ huynh biết, nhưng **không** thay thế tài liệu riêng hai môn đó.

## Cấu trúc thư mục

| File / thư mục | Nội dung |
| --- | --- |
| [01-danh-sach-truong.md](./01-danh-sach-truong.md) | Danh sách trường trọng điểm (HN, HCM, cả nước), cấu trúc đề, lưu ý tuyển sinh |
| [02-catalog-de-thi.md](./02-catalog-de-thi.md) | Catalog nguồn đề + đáp án (link công khai) |
| [03-ke-hoach-on-luyen.md](./03-ke-hoach-on-luyen.md) | Lộ trình ôn 6–12 tháng (3 cấp độ) |
| [04-map-lesson-course.md](./04-map-lesson-course.md) | Map chuyên đề thi ↔ lesson trong course |
| [05-chuyen-de-trong-tam.md](./05-chuyen-de-trong-tam.md) | 20+ chuyên đề Toán trọng tâm trong đề CLC |
| [luyen-tap/](./luyen-tap/) | **Luyện dạng:** 30 bài biên tập + ngân hàng raw |
| [de-thi/](./de-thi/) | Phân loại theo vùng + **nội dung full text** |
| [de-thi/INDEX-NOI-DUNG.md](./de-thi/INDEX-NOI-DUNG.md) | **Mục lục đề đã lấy nội dung** |
| [de-thi/HINH-MINH-HOA.md](./de-thi/HINH-MINH-HOA.md) | **Mục lục hình** (`hinh/` theo từng trường) |
| [sources.json](./sources.json) | Catalog máy đọc được (JSON) |

### Luyện tập nhanh

| File | Khi nào dùng |
| --- | --- |
| [luyen-tap/30-bai-luyen-dang-clc.md](./luyen-tap/30-bai-luyen-dang-clc.md) | 30 bài **đã biên tập + LaTeX** — luyện dạng hằng tuần |
| [luyen-tap/bai-toan-tuong-tu-tu-raw.md](./luyen-tap/bai-toan-tuong-tu-tu-raw.md) | ~942 bài unique (extract thô) — tham khảo thêm, chất lượng OCR không đều |

## Cách dùng nhanh

1. Đọc **[01-danh-sach-truong](./01-danh-sach-truong.md)** → chọn 2–3 trường mục tiêu.
2. Xem **[05-chuyen-de-trong-tam](./05-chuyen-de-trong-tam.md)** → biết cần vững dạng nào.
3. Theo **[03-ke-hoach-on-luyen](./03-ke-hoach-on-luyen.md)** → học theo tuần.
4. Mỗi chuyên đề mở **[04-map-lesson-course](./04-map-lesson-course.md)** → học lesson tương ứng trong `contents/vi/`.
5. Luyện dạng: **[30 bài CLC](./luyen-tap/30-bai-luyen-dang-clc.md)** rồi đề thật từ **[02-catalog-de-thi](./02-catalog-de-thi.md)**.

## Quy ước công thức toán (LaTeX)

Áp dụng thống nhất với course Math-Lover (MathJax):

| Quy ước | Ví dụ |
| --- | --- |
| Dùng `$$...$$` (không dùng `$...$`) | `$$\dfrac{2}{3}$$` |
| Phân số | `$$\dfrac{a}{b}$$` |
| Lũy thừa / đơn vị | `$$48\,\mathrm{cm}^2$$` |
| Biểu thức | `$$2{,}75 \times 0{,}99 + 2{,}75 : 100$$` |
| Số có gạch trên | `$$\overline{ab}$$`, `$$\overline{a1024b}$$` |
| Dãy số | `$$1;\ 3;\ 5;\ \ldots$$` |

**Đã chuẩn hóa (2026-08-10):**

- Toàn bộ **file đề**: chỉ còn tiêu đề + metadata (năm, thời gian, điểm…) + nội dung câu; bỏ quảng cáo / HDG dài / ghi chú ôn.
- Công thức: `\(...\)` → `$$...$$`; phân số/đơn vị OCR đã sửa khi nhận diện được.
- File **30 bài luyện dạng** viết lại sạch + LaTeX.
- Đã xóa `_raw*` và `ocr/` theo từng trường.

**Chưa / hạn chế:**

| Vùng | Ghi chú |
| --- | --- |
| `_downloads/` | PDF/ảnh/OCR local — đối chiếu hình; không bắt buộc khi ôn |
| `luyen-tap/bai-toan-tuong-tu-tu-raw.md` | Ngân hàng thô; chất lượng không đều |
| Một số đề | Thiếu hình vẽ (chỉ mô tả) — xem PDF trong `_downloads/` nếu cần |

## Review nhanh cấu trúc (tóm tắt)

| Thành phần | Trạng thái |
| --- | --- |
| Kế hoạch + map lesson + chuyên đề | Ổn, dùng được ngay |
| Đề HN (NTT, AMS, MC, Cầu Giấy, LTV…) | Nhiều năm; một phần full text, một phần tóm tắt |
| Đề HCM (TDN 2022–2026, Thủ Đức, TQT1, Hoa Lư, NAK) | Ưu tiên cao; TDN 2025–2026 biên tập rõ |
| Trường xét tuyển (Colette, LQD, NHC…) | Chỉ README / tình trạng — **không** có đề toán riêng |
| Luyện dạng 30 bài | **Khuyến nghị** luyện hằng tuần |
| Ngân hàng 942 bài | Phụ; cần chọn lọc khi dùng |

## Lưu ý pháp lý & nguồn

- Thư mục **không host PDF đề thi bản quyền** của bên thứ ba làm “bản phát hành”. PDF trong `_downloads/` chỉ phục vụ OCR/đối chiếu local.
- Chỉ **catalog link** đến nguồn công khai (Sở GDĐT, báo, trang tổng hợp giáo dục) trong các file catalog.
- Luôn ưu tiên **đề/đáp án chính thức** từ Sở GDĐT hoặc website trường khi có.
- Cấu trúc tuyển sinh **thay đổi theo năm** — kiểm tra thông báo mới nhất trước khi ôn “sát đề”.

## Cập nhật

- **Tạo lần đầu:** 2026-08-10  
- **Review + LaTeX:** 2026-08-10 — chuẩn hóa `$$...$$` trên đề curated; viết lại 30 bài CLC; gắn luyện tập vào kế hoạch ôn  
- **Phạm vi thu thập:** chủ yếu đề Toán / tư duy logic 2019–2026, HN + HCM + một số tỉnh  
- **Gợi ý tiếp:** mock test timed; biên tập thêm 20–30 bài từ ngân hàng raw theo từng chuyên đề A1–D6  

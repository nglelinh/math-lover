---
layout: post
title: 09-01 Đếm có hệ thống — Không bỏ sót, không đếm trùng
chapter: '09'
order: 1
owner: Math Lover Team
lang: vi
categories:
- chapter09
lesson_type: required
---
Mở tủ quần áo, em thấy **3 chiếc áo** và **2 chiếc quần**. Em muốn biết có bao nhiêu bộ đồ khác nhau — nhưng nếu đếm lung tung thì dễ nhầm hoặc đếm lại một bộ hai lần!

Hôm nay ta học cách **đếm có hệ thống**: ghi ra từng khả năng một cách gọn gàng.

![Xúc xắc — mỗi mặt là một kết quả](https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Dice.svg/960px-Dice.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

---

## Mục tiêu

Sau bài học này, em có thể:

- đếm số khả năng mà không bỏ sót
- tránh đếm trùng một kết quả hai lần
- dùng bảng hoặc danh sách để kiểm tra lại

---

## Kiến thức đã biết

Em đã biết đếm số, liệt kê đồ vật và chơi các trò có nhiều kết quả (tung xúc xắc, rút thăm).

Điều mới hôm nay: **cách sắp xếp việc đếm** để chắc chắn đã đủ.

---

## Khám phá toán học

### 1. Hai lỗi thường gặp khi đếm

- **Bỏ sót:** quên một khả năng (ví dụ quên bộ áo xanh + quần đen).
- **Đếm trùng:** tính cùng một khả năng hai lần (ví dụ đếm “áo đỏ quần xanh” rồi lại đếm “quần xanh áo đỏ” như hai bộ khác).

### 2. Đếm bằng danh sách có quy tắc

**Quy tắc vàng:** chọn thứ tự cố định — ví dụ **chọn áo trước, quần sau**.

Với 2 áo (Đỏ, Xanh) và 2 quần (Đen, Trắng):

| Áo | Quần | Bộ đồ |
|----|------|-------|
| Đỏ | Đen | Đỏ–Đen |
| Đỏ | Trắng | Đỏ–Trắng |
| Xanh | Đen | Xanh–Đen |
| Xanh | Trắng | Xanh–Trắng |

Tổng cộng: **4 bộ**.

### 3. Kiểm tra bằng đánh số

Đánh số 1, 2, 3, 4 cho từng bộ. Nếu nhảy từ 3 sang 5 mà không có số 4 — có thể đã bỏ sót!

---

## Hoạt động khám phá

<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->

### Hoạt động 1: Đếm cửa

Nhà có 2 cửa trước (A, B) và 2 cửa sau (1, 2). Liệt kê mọi cặp **cửa trước + cửa sau**.

**Gợi ý:** A1, A2, B1, B2 → **4 cách**.

### Hoạt động 2: Thẻ chữ cái

Có thẻ **M** và **P**. Ghép 2 thẻ thành từ 2 chữ (có thứ tự).

Liệt kê: MP, PM → **2 từ** (không tính MM hay PP vì mỗi thẻ chỉ dùng một lần).

---

## Ví dụ

**Ví dụ 1:** Menu có 3 món khai vị. Em muốn thử từng món một lần. Có bao nhiêu lần chọn?

**Giải:** 3 món → **3 lần chọn** (mỗi món một khả năng).

**Ví dụ 2:** Tủ có 4 ngăn kéo. Mỗi ngăn có 1 đồ chơi khác nhau. Có bao nhiêu cách lấy đúng 1 đồ?

**Giải:** 4 ngăn → **4 cách**.

---

## Câu hỏi suy nghĩ

1. Vì sao nên chọn “áo trước, quần sau” thay vì đếm ngẫu nhiên?
2. Khi nào em biết mình đã đếm trùng?
3. Danh sách và bảng giúp gì khi kiểm tra?

---

## Bài tập luyện tập

### Bài 1
Có 3 màu bút: đỏ, xanh, vàng. Em chọn đúng 1 màu. Có bao nhiêu cách?

### Bài 2
Ghép 1 trong 2 loại bánh (mì, ngọt) với 1 trong 3 loại nước (cam, táo, dưa). Lập bảng và đếm số bộ.

### Bài 3
Liệt kê tất cả kết quả khi tung 1 đồng xu 2 lần (S = Sấp, N = Ngửa). Có bao nhiêu kết quả?

### Bài 4
Em đếm được 5 bộ đồ nhưng bạn đếm được 6. Hai em nên làm gì để kiểm tra ai đúng?

---

## Video tham khảo

Xem thêm trên YouTube để củng cố bài học:

1. [Xác suất cơ bản — Khan Academy](https://www.youtube.com/watch?v=uzkc-qNVoOk) — Khan Academy
2. [Mẫu hình số — Math Antics](https://www.youtube.com/watch?v=vV7C7bXm4VI) — Math Antics
3. [Phép nhân cơ bản — Khan Academy](https://www.youtube.com/watch?v=mvOkMYCygps) — Khan Academy

*Video: YouTube — kênh giáo dục; nội dung phù hợp lứa tuổi 8–10*

## Góc cha mẹ

### Điều em đang khám phá

Con đang học **kỷ luật khi đếm** — nền tảng của tổ hợp và xác suất. Không cần thuộc công thức; chỉ cần thói quen liệt kê có quy tắc.

### Gợi ý thảo luận

- Cùng con lập bảng “áo + quần” với quần áo thật trong nhà
- Chơi trò “liệt kê hết” khi chọn phim hoặc món ăn
- Hỏi: “Em làm sao biết đã đủ?”
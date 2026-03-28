---
layout: post
title: 04-06 Bội chung nhỏ nhất - Tìm số nhỏ nhất chia hết cho cả hai
chapter: '05'
order: 6
owner: Math Lover Team
lang: vi
categories:
- chapter05
lesson_type: required
---

Trong bài học này, chúng ta sẽ học cách tìm số nhỏ nhất có thể chia hết cho cả hai số cùng lúc!

![BCNN]({{ site.baseurl }}/img/chapter_img/chapter05/05_lcm.svg)

---

## Mục tiêu

Trong bài học này, em sẽ:

- Hiểu khái niệm bội chung nhỏ nhất (BCNN)
- Tìm BCNN của hai số
- Ứng dụng BCNN trong thực tế

---

## Kiến thức đã biết

Em đã biết tìm bội số và UCLN. Hôm nay, chúng ta sẽ học về BCNN nhé!

---

## Khám phá toán học

### Bội chung nhỏ nhất là gì?

**Bội chung nhỏ nhất (BCNN)** của hai số là số nhỏ nhất chia hết cho cả hai số đó.

**Ví dụ:** Tìm BCNN của 4 và 6

**Bước 1:** Tìm bội số của mỗi số
- Bội của 4: 4, 8, 12, 16, 20, 24, ...
- Bội của 6: 6, 12, 18, 24, 30, ...

**Bước 2:** Tìm các bội chung
- Bội chung: 12, 24, ...

**Bước 3:** Chọn số nhỏ nhất
- **BCNN(4, 6) = 12**

### Cách tìm BCNN nhanh

**Bước 1:** Phân tích mỗi số thành thừa số nguyên tố
- 4 = 2²
- 6 = 2 × 3

**Bước 2:** Lấy tất cả thừa số với số mũ lớn nhất
- 2² và 3
- BCNN = 2² × 3 = **12**

---

## Hoạt động khám phá


<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->

### Hoạt động 1: Tìm BCNN

Tìm BCNN của:
- 3 và 5 → BCNN = 15
- 4 và 7 → BCNN = 28
- 6 và 8 → BCNN = 24

### Hoạt động 2: Ứng dụng

Hai bạn đến thư viện cùng ngày. Bạn thứ nhất đến mỗi 4 ngày, bạn thứ hai đến mỗi 6 ngày. Hỏi sau bao nhiêu ngày thì họ gặp nhau ở thư viện?

**Giải:** Tìm BCNN(4, 6) = 12
→ Họ gặp nhau sau **12 ngày**

### Hoạt động 3: Tìm BCNN nhanh

Tìm BCNN của 15 và 20:
- 15 = 3 × 5
- 20 = 2² × 5
- BCNN = 2² × 3 × 5 = 60

---

## Toán học qua các thời đại

### 🕰️ BCNN trong lịch sử

**Lịch sử lịch:** Người xưa dùng BCNN để tính **chu kỳ mặt trăng và mặt trời** để làm lịch!

**Câu chuyện:** Một năm có 365 ngày, một tháng có khoảng 29,5 ngày. BCNN(365, 29.5) giúp tạo ra lịch chính xác!

### 📜 Ứng dụng hiện đại

**Âm nhạc:** Nhịp trống và tiếng đàn có thể trùng nhau sau một khoảng thời gian được tính bằng BCNN!

**Máy tính:** BCNN được dùng trong việc đồng bộ thời gian xử lý!

---

## Bài tập luyện tập

### Bài 1: Tìm BCNN

a) BCNN(5, 7)
b) BCNN(8, 12)
c) BCNN(10, 15)

### Bài 2: Giải toán

Hai xe buýt khởi hành cùng lúc. Xe thứ nhất quay lại sau 8 phút, xe thứ hai sau 12 phút. Hỏi sau bao lâu hai xe gặp nhau?

### Bài 3: Trắc nghiệm

BCNN của 3 và 4 là:
   A. 7   B. 12   C. 24

---

## Góc cha mẹ

### Điều em đang khám phá

Con đang học cách tìm **số nhỏ nhất** chia hết cho nhiều số - rất hữu ích trong cuộc sống!

### Gợi ý thảo luận

- Cùng con tìm ví dụ BCNN trong thực tế
- Giải thích ứng dụng trong lịch trình
- Chơi trò tính chu kỳ lặp lại

### Kỹ năng phát triển

- Tư duy logic
- Lập kế hoạch
- Giải quyết vấn đề

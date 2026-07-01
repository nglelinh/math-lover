---
layout: post
title: '08-07 Toán học trong tin học - Mã nhị phân'
chapter: '07'
order: 7
owner: Math Lover Team
lang: vi
categories:
- chapter07
lesson_type: required
---
Trong bài học này, chúng ta sẽ khám phá cách máy tính "nghĩ" và làm việc với các con số!
![Ma nhi phan]({{ site.baseurl }}/img/chapter_img/chapter07/09_binary.svg)


![Phân rã nhị phân — toán trong máy tính](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Binary_decomposition.png/960px-Binary_decomposition.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

---

## Mục tiêu

Trong bài học này, em sẽ:

- Hiểu khái niệm mã nhị phân
- Đổi số thập phân sang nhị phân
- Hiểu cách máy tính lưu trữ thông tin

---

## Kiến thức đã biết

Em đã biết về số thập phân và hệ thập phân. Hôm nay, chúng ta sẽ học về hệ nhị phân nhé!

![Mã lập trình — toán trong tin học](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/960px-Programming_code.jpg)

*Ảnh: Wikimedia Commons*


---

## Khám phá toán học

### Hệ nhị phân là gì?

**Hệ nhị phân** chỉ dùng 2 chữ số: 0 và 1

**So sánh:**
| Thập phân | Nhị phân |
|-----------|----------|
| 0 | 0 |
| 1 | 1 |
| 2 | 10 |
| 3 | 11 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |

### Cách đổi thập phân sang nhị phân

**Ví dụ:** Đổi 13 sang nhị phân

**Bước 1:** Chia 13 cho 2, ghi số dư
- 13 ÷ 2 = 6 dư 1

**Bước 2:** Chia tiếp 6 cho 2
- 6 ÷ 2 = 3 dư 0

**Bước 3:** Chia tiếp 3 cho 2
- 3 ÷ 2 = 1 dư 1

**Bước 4:** Chia tiếp 1 cho 2
- 1 ÷ 2 = 0 dư 1

**Kết quả:** Đọc ngược: 1101

### Tại sao máy tính dùng nhị phân?

Máy tính chỉ hiểu 2 trạng thái:
- Có điện (1)
- Không điện (0)

---

## Hoạt động khám phá


<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->
### Hoạt động 1: Đổi số
Đổi các số sau sang nhị phân:
a) 7 → 111
b) 10 → 1010


![Trục số — thứ tự các số](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c0/Number_line.svg/960px-Number_line.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

### Hoạt động 2: Đổi ngược

Đổi các số nhị phân sau sang thập phân:
a) 100 → 4
b) 1111 → 15

### Hoạt động 3: Khám phá bit

Máy tính dùng **bit** (viết tắt của binary digit)
- 8 bit = 1 byte
- 1 byte có thể lưu trữ 256 giá trị (0-255)

---

## Toán học qua các thời đại

### 🕰️ Mã nhị phân trong lịch sử

**Gottfried Leibniz** (1646-1716) - nhà toán học Đức - phát minh ra hệ nhị phân!

**George Boole** (1815-1864) - phát triển Đại số Boolean - nền tảng của máy tính!

### 📜 Ứng dụng hiện đại

**Máy tính:** Tất cả dữ liệu đều được lưu dạng nhị phân
**Mã hóa:** Bảo mật thông tin
**Nghệ thuật:** Ảnh nhị phân (pixel đen trắng)

---

## Bài tập luyện tập

### Bài 1: Đổi sang nhị phân

a) 5 = ?
b) 12 = ?
c) 20 = ?

### Bài 2: Đổi sang thập phân

a) 101 = ?
b) 1100 = ?
c) 10000 = ?


---

## Video tham khảo

Xem thêm trên YouTube để củng cố bài học:

1. [Nhân chia lũy thừa 10 — Math Antics](https://www.youtube.com/watch?v=qJB19dAZPpY) — Math Antics
2. [Mẫu hình số — Math Antics](https://www.youtube.com/watch?v=vV7C7bXm4VI) — Math Antics
3. [Giá trị chữ số thập phân — Math Antics](https://www.youtube.com/watch?v=KG6ILNOiMgM) — Math Antics

*Video: YouTube — kênh giáo dục; nội dung phù hợp lứa tuổi 8–10*


## Góc cha mẹ

### Điều em đang khám phá

Con đang học về **mã nhị phân** - cách máy tính "nghĩ" và làm việc!

### Gợi ý thảo luận

- Giải thích cách máy tính lưu trữ ảnh
- Chơi trò đổi số nhị phân
- Tìm hiểu về bit và byte

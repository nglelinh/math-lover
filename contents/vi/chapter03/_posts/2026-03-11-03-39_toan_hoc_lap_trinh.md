---
layout: post
title: 07-39 Toán Học Trong Lập Trình
chapter: '03'
order: 39
owner: Math-Lover Team
lang: vi
categories:
- chapter03
lesson_type: optional
---
## Mục tiêu

Trong bài học này, các em sẽ khám phá mối liên hệ giữa toán học và lập trình, hiểu được tầm quan trọng của toán học trong việc viết chương trình máy tính, và bắt đầu tư duy lập trình.

---

## Giới thiệu

Các em có biết **máy tính** hoạt động như thế nào không?
Máy tính dùng toán học để:
- Tính toán
- Xử lý dữ liệu
- Tạo ra mọi thứ từ game đến internet!
Hãy cùng khám phá!


![Phân rã nhị phân — toán trong máy tính](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Binary_decomposition.png/960px-Binary_decomposition.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*


---

## 1. Ngôn Ngữ Lập Trình
### Máy tính hiểu gì?



![Mã lập trình — toán trong tin học](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/960px-Programming_code.jpg)

*Ảnh: Wikimedia Commons*

Máy tính chỉ hiểu **0 và 1**!

Đây gọi là **hệ nhị phân**!

### Ví dụ

```
5 trong hệ nhị phân = 101
10 trong hệ nhị phân = 1010
```

### Toán học

$$101_2 = 1 \times 2^2 + 0 \times 2^1 + 1 \times 2^0 = 4 + 0 + 1 = 5$$

---

## 2. Biến Trong Lập Trình

### Biến là gì?

**Biến** là nơi lưu trữ giá trị!

Giống như đại số, dùng chữ để đại diện số!

### Ví dụ

```
x = 5        # x là biến, giá trị = 5
y = x + 3   # y = 8
```

---

## 3. Phép Toán

### Các phép toán cơ bản

| Phép toán | Ký hiệu | Ví dụ |
|-----------|---------|--------|
| Cộng | + | 5 + 3 = 8 |
| Trừ | - | 5 - 3 = 2 |
| Nhân | * | 5 * 3 = 15 |
| Chia | / | 6 / 3 = 2 |
| Chia lấy dư | % | 7 % 3 = 1 |
| Lũy thừa | ** | 2 ** 3 = 8 |

---

## 4. Cấu Trúc Điều Kiện

### If - Else

Nếu... thì... nếu không...

### Ví dụ

```
if x > 10:
    print("Lớn hơn 10")
else:
    print("Nhỏ hơn hoặc bằng 10")
```

### Toán học

Dùng **bất đẳng thức** để kiểm tra điều kiện!

---

## 5. Vòng Lặp

### For loop

Lặp lại một số lần nhất định!

### Ví dụ

```
for i in range(5):
    print(i)
```

Kết quả: 0, 1, 2, 3, 4

### Toán học

Dùng **phép cộng** để đếm!

---

## 6. Hàm

### Hàm là gì?

**Hàm** là một khối code thực hiện một công việc!

### Ví dụ

```
def tinh_binh_phuong(x):
    return x * x

ket_qua = tinh_binh_phuong(5)  # ket_qua = 25
```

### Toán học

Giống như f(x) = x² trong đại số!

---

## 7. Mảng

### Mảng là gì?

**Mảng** là danh sách các giá trị!

### Ví dụ

```
so = [1, 2, 3, 4, 5]
print(so[0])  # In ra 1
print(so[2])  # In ra 3
```

### Toán học

Giống như **tập hợp** trong toán học!

---

## 8. Thuật Toán

### Thuật toán là gì?

**Thuật toán** là tập hợp các bước để giải quyết vấn đề!

### Ví dụ: Tìm số lớn nhất

```
def tim_max(mang):
    max_val = mang[0]
    for so in mang:
        if so > max_val:
            max_val = so
    return max_val
```

---

## 9. Game

### Game được tạo như thế nào?

Game dùng:
- **Vật lý**: Tính chuyển động
- **Toán học**: Tính va chạm
- **Đồ họa**: Vẽ hình ảnh

### Ví dụ

Di chuyển nhân vật:
```
x = x + van_toc_x
y = y + van_toc_y
```

---

## 10. Trí Tuệ Nhân Tạo (AI)

### AI là gì?

Máy tính có thể "học" và "suy nghĩ"!

### Toán học

- **Xác suất**: Dự đoán kết quả
- **Thống kê**: Học từ dữ liệu
- **Đại số**: Xử lý ma trận

### Ví dụ

Nhận dạng hình ảnh:
- Phân tích pixels
- So sánh với mẫu
- Đưa ra kết quả

---

## Bảng Tóm Tắt

| Lập trình | Toán học |
|-----------|----------|
| Biến | Ẩn số |
| Phép toán | +, -, ×, ÷ |
| Điều kiện | Bất đẳng thức |
| Vòng lặp | Đếm |
| Hàm | f(x) |
| Mảng | Tập hợp |
| Thuật toán | Quy trình |

---

## Em Có Biết?

- **Facebook** dùng thuật toán để hiển thị bài viết!
- **Google** dùng toán học để tìm kiếm!
- **Game Minecraft** được viết bằng code!

---

## Câu Hỏi Suy Nghĩ

1. Em muốn tạo ra gì với lập trình?

2. Toán học giúp lập trình như thế nào?

3. Em có muốn trở thành lập trình viên không?

---

## Hoạt Động


<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->

**Thử thách:**

Viết code tính tổng các số từ 1 đến 10!

```
tong = 0
for i in range(1, 11):
    tong = tong + i
print(tong)  # Kết quả: 55
```

---

**Nhớ rằng:** Lập trình là cách hiện thực hóa toán học! 💻🔢🎮🎉

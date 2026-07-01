---
layout: post
title: 07-06 Tam giác Pascal - Mẫu hình kỳ diệu
chapter: '03'
order: 6
owner: Math Lover Team
lang: vi
categories:
- chapter03
lesson_type: required
---
## Mở đầu gợi tò mò
Viết các hàng số sau:

```text
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
```

Thoạt nhìn chúng giống một tam giác số rất đẹp. Nhưng điều kỳ diệu hơn là ở bên trong tam giác này có rất nhiều quy luật:

- tổng mỗi hàng
- số đối xứng hai bên
- liên hệ với tổ hợp và mẫu hình

Hôm nay, chúng ta sẽ làm quen với một trong những bức tranh số nổi tiếng nhất của toán học.

![Tam giac Pascal]({{ site.baseurl }}/img/chapter_img/chapter03/03_05_tam_giac_pascal.svg)


![Tam giác Pascal — mẫu hình số](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Pascal_triangle.svg/960px-Pascal_triangle.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

---

## Mục tiêu

Sau bài học này, em có thể:

- tự dựng các hàng đầu của tam giác Pascal
- giải thích quy luật tạo số trong tam giác
- nhận ra một vài mẫu hình đẹp như tổng mỗi hàng và tính đối xứng
- dùng tam giác Pascal để dự đoán số tiếp theo trong một hàng

---

## Kiến thức đã biết

Em đã biết cộng số và đã học về quy luật.
Tam giác Pascal là nơi hai kỹ năng đó gặp nhau:
- cộng để tạo hàng mới
- quan sát để phát hiện mẫu hình


![Số tam giác — xếp chấm thành tam giác](https://upload.wikimedia.org/wikipedia/commons/thumb/8/85/Triangular_number_10_with_triangle.svg/960px-Triangular_number_10_with_triangle.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*


---

## Khám phá toán học

### 1. Dựng tam giác Pascal

Ta bắt đầu từ số:

$$1$$

Hàng tiếp theo là:

$$1 \quad 1$$

Từ đó trở đi:

- số đầu hàng luôn là 1
- số cuối hàng luôn là 1
- mỗi số ở giữa bằng tổng của hai số ngay phía trên nó

Ví dụ:

```text
      1
    1   1
  1   2   1
1   3   3   1
```

Vì:

$$1 + 1 = 2$$

và:

$$1 + 2 = 3$$

$$2 + 1 = 3$$

### 2. Tính đối xứng

Quan sát hàng:

$$1 \quad 4 \quad 6 \quad 4 \quad 1$$

Ta thấy số bên trái và bên phải giống nhau.

Đó là vì tam giác Pascal luôn **đối xứng** qua trục giữa.

### 3. Tổng mỗi hàng

Tính tổng các hàng đầu:

- hàng 1:

$$1$$

- hàng 2:

$$1 + 1 = 2$$

- hàng 3:

$$1 + 2 + 1 = 4$$

- hàng 4:

$$1 + 3 + 3 + 1 = 8$$

- hàng 5:

$$1 + 4 + 6 + 4 + 1 = 16$$

Ta thấy tổng mỗi hàng đang gấp đôi hàng trước:

$$1, 2, 4, 8, 16, \ldots$$

Đó là một quy luật rất đẹp.

### 4. Các đường chéo thú vị

Nhìn theo đường chéo ta được:

- đường chéo thứ nhất: toàn số 1
- đường chéo thứ hai: 1, 2, 3, 4, 5, ...
- đường chéo thứ ba: 1, 3, 6, 10, ...

Đường chéo thứ ba chính là các **số tam giác**, vì chúng có thể xếp thành hình tam giác bằng chấm tròn.

### 5. Vì sao tam giác này quan trọng?

Tam giác Pascal cho thấy toán học rất thú vị:

- chỉ từ phép cộng đơn giản
- ta tạo ra rất nhiều quy luật sâu sắc

Nó giống như một khu vườn số học, nơi mỗi hàng lại mở ra một điều mới.

---

## Hoạt động khám phá


<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->
### Hoạt động A: Xây tam giác bằng hạt đậu
Chuẩn bị:


![Cấp số cộng — tăng đều từng bước](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Academ_Arithmetic_progressions_along_a_knotted_loop.svg/960px-Academ_Arithmetic_progressions_along_a_knotted_loop.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

- hạt đậu hoặc viên sỏi nhỏ
- giấy

Em hãy xếp:

- 1 hạt
- rồi 2 hàng
- rồi 3 hàng

Sau đó viết số tương ứng thành tam giác Pascal để thấy các hàng đang "lớn dần" như thế nào.

### Hoạt động B: Tô màu quy luật

In hoặc chép 6 hàng đầu của tam giác Pascal.

Tô màu:

- các số 1
- các số chẵn
- một đường chéo bất kỳ

Sau đó quan sát xem hình gì xuất hiện.

### Hoạt động C: Tự dựng hàng tiếp theo

Cho hàng:

$$1 \quad 5 \quad 10 \quad 10 \quad 5 \quad 1$$

Hãy tự dựng hàng tiếp theo bằng cách cộng hai số kề nhau.

---

## Ví dụ có hướng dẫn

### Ví dụ 1: Dựng hàng mới

Từ hàng:

$$1 \quad 4 \quad 6 \quad 4 \quad 1$$

ta dựng hàng tiếp theo:

- đầu hàng: 1
- 1 + 4 = 5
- 4 + 6 = 10
- 6 + 4 = 10
- 4 + 1 = 5
- cuối hàng: 1

Vậy hàng mới là:

$$1 \quad 5 \quad 10 \quad 10 \quad 5 \quad 1$$

### Ví dụ 2: Tổng một hàng

Tính tổng hàng:

$$1 \quad 3 \quad 3 \quad 1$$

Ta có:

$$1 + 3 + 3 + 1 = 8$$

### Ví dụ 3: Tìm số còn thiếu

```text
1   ?   6   ?   1
```

Vì hàng này đối xứng và là hàng thứ 5 quen thuộc nên các số còn thiếu là:

$$4$$

và:

$$4$$

---

## Thang thử thách

Mức 1:

- Viết 5 hàng đầu của tam giác Pascal.

Mức 2:

- Hàng:

$$1 \quad 6 \quad 15 \quad 20 \quad 15 \quad 6 \quad 1$$

có bao nhiêu số?

Mức 3:

- Tổng của hàng:

$$1 \quad 5 \quad 10 \quad 10 \quad 5 \quad 1$$

là bao nhiêu?

Mức 4:

- Em hãy tìm hai quy luật khác ngoài ba quy luật đã học hôm nay.

---

## Câu hỏi suy nghĩ

1. Vì sao tam giác Pascal vừa là bài học về phép cộng, vừa là bài học về quy luật?
2. Em thấy quy luật nào đẹp nhất: đối xứng, tổng mỗi hàng hay các đường chéo?
3. Nếu tiếp tục viết thêm 10 hàng nữa, em đoán sẽ còn phát hiện ra điều gì?


---

## Video tham khảo

Xem thêm trên YouTube để củng cố bài học:

1. [Tam giác Pascal — Numberphile](https://www.youtube.com/watch?v=0iMtlus-afo) — Numberphile
2. [Bí ẩn dãy Fibonacci — Numberphile](https://www.youtube.com/watch?v=Nu-lW-Ifyec) — Numberphile
3. [Mẫu hình số — Math Antics](https://www.youtube.com/watch?v=vV7C7bXm4VI) — Math Antics

*Video: YouTube — kênh giáo dục; nội dung phù hợp lứa tuổi 8–10*


## Góc cha mẹ

Tam giác Pascal là một ví dụ rất đẹp về việc trẻ có thể tiếp cận ý tưởng sâu chỉ bằng phép cộng đơn giản.

Phụ huynh có thể hỗ trợ bằng cách:

- cùng con dựng từng hàng một
- hỏi "Con thấy gì lặp lại?"
- khuyến khích con tự tô màu để phát hiện mẫu hình

Mục tiêu không phải là học hết mọi ứng dụng, mà là để con cảm nhận rằng trong toán học, một quy luật nhỏ có thể mở ra rất nhiều điều bất ngờ.

---

## Toán học qua thời gian

Ở phương Tây, tam giác này thường mang tên Blaise Pascal. Nhưng nhiều thế kỷ trước Pascal, các nhà toán học ở Trung Quốc và Ba Tư đã biết đến tam giác số này và nghiên cứu nó rất kỹ.

Điều đó cho thấy vẻ đẹp của toán học không thuộc riêng một nơi nào. Khi con người quan sát quy luật thật kỹ, họ có thể gặp nhau ở cùng một ý tưởng, dù sống ở những thời đại rất khác nhau.

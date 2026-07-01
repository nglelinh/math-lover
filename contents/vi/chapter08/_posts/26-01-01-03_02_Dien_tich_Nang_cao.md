---
layout: post
title: 06-07 Hình học nâng cao - Diện tích và Chu vi
chapter: '08'
order: 7
owner: Math Lover Team
lang: vi
categories:
- chapter08
lesson_type: required
---
## Mở đầu gợi tò mò
Một bạn nhỏ muốn làm hàng rào quanh bồn hoa và cũng muốn phủ cỏ kín phần đất bên trong.

Bạn ấy phải trả lời hai câu hỏi khác nhau:

- cần bao nhiêu mét hàng rào?
- cần phủ bao nhiêu phần mặt đất?

Hai câu hỏi này nghe giống nhau, nhưng thật ra là hai ý khác nhau:

- **chu vi** là đo xung quanh
- **diện tích** là đo phần ở bên trong

Hôm nay, chúng ta sẽ khám phá điều đó với tam giác và hình thang.

![Dien tich Nang cao]({{ site.baseurl }}/img/chapter_img/chapter03/03_02_dien_tich_nang_cao.svg)


![Hình tam giác](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Triangle.svg/960px-Triangle.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

---

## Mục tiêu

Sau bài học này, em có thể:

- phân biệt rõ chu vi và diện tích
- hiểu vì sao công thức diện tích tam giác có chia 2
- tính diện tích hình tam giác và hình thang
- giải thích kết quả bằng hình vẽ hoặc bằng lời

---

## Kiến thức đã biết

Em đã biết tính:
- chu vi hình vuông, hình chữ nhật
- diện tích hình chữ nhật
Kiến thức đó rất quan trọng, vì hôm nay ta sẽ dùng hình chữ nhật để hiểu các hình mới.



![Hình vuông — bốn cạnh bằng nhau](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Square_%28geometry%29.svg/960px-Square_%28geometry%29.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

Ý tưởng lớn của bài này là:

**nhiều công thức hình học thật ra được tạo ra từ việc cắt, ghép và so sánh với hình quen thuộc.**

---

## Khám phá toán học

### 1. Chu vi và diện tích không giống nhau

Hãy tưởng tượng một mảnh bìa hình chữ nhật dài 8 cm, rộng 4 cm.

Chu vi là:

$$8 + 4 + 8 + 4 = 24\text{ cm}$$

Diện tích là:

$$8 \times 4 = 32\text{ cm}^2$$

Chu vi dùng đơn vị **cm**, còn diện tích dùng **cm²** vì ta đang đếm số ô vuông đơn vị phủ kín mặt hình.

### 2. Vì sao diện tích tam giác phải chia 2?

Lấy một hình chữ nhật có đáy 8 cm và chiều cao 5 cm.

Nếu kẻ một đường chéo, hình chữ nhật sẽ chia thành **hai tam giác bằng nhau**.

Diện tích hình chữ nhật là:

$$8 \times 5 = 40\text{ cm}^2$$

Mỗi tam giác chiếm một nửa, nên diện tích tam giác là:

$$40 \div 2 = 20\text{ cm}^2$$

Vì thế:

$$S_{\text{tam giác}} = \frac{đáy \times chiều\ cao}{2}$$

Điều quan trọng là chiều cao phải là đoạn thẳng vuông góc với đáy.

### 3. Hình thang có liên quan gì đến tam giác?

Hình thang có hai đáy song song: đáy lớn và đáy nhỏ.

Một cách hiểu đẹp là ghép **hai hình thang giống nhau** để tạo thành một hình bình hành.

Ví dụ, hình thang có:

- đáy lớn 10 cm
- đáy nhỏ 6 cm
- chiều cao 4 cm

Nếu ghép hai hình thang như vậy, ta được hình bình hành có đáy:

$$10 + 6 = 16\text{ cm}$$

và chiều cao:

$$4\text{ cm}$$

Diện tích hình bình hành mới là:

$$16 \times 4 = 64\text{ cm}^2$$

Mỗi hình thang chỉ chiếm một nửa, nên:

$$64 \div 2 = 32\text{ cm}^2$$

Từ đó:

$$S_{\text{hình thang}} = \frac{(đáy\ lớn + đáy\ nhỏ) \times chiều\ cao}{2}$$

### 4. Kiểm tra xem kết quả có hợp lý không

Nếu tam giác có đáy 6 cm, chiều cao 4 cm:

$$S = \frac{6 \times 4}{2} = 12\text{ cm}^2$$

Em có thể tự hỏi:

- nếu coi nó là nửa của hình chữ nhật 6 x 4 thì diện tích có đúng là 12 không?

Câu trả lời là có.

Biết tự kiểm tra như vậy giúp em ít nhầm công thức hơn.

---

## Hoạt động khám phá


<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->
### Hoạt động A: Cắt đôi hình chữ nhật
Chuẩn bị:



![Hình tròn — tất cả điểm cách tâm bằng nhau](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9e/Circle.svg/960px-Circle.svg.png)

*Ảnh: Wikimedia Commons — sơ đồ toán học*

- giấy kẻ ô vuông
- kéo
- bút chì

Cách làm:

1. Vẽ một hình chữ nhật 6 ô x 4 ô.
2. Kẻ đường chéo để chia thành 2 tam giác.
3. Đếm số ô vuông của cả hình chữ nhật.
4. Suy ra số ô vuông của mỗi tam giác.

Mục tiêu:

- tự phát hiện vì sao diện tích tam giác bằng một nửa hình chữ nhật

### Hoạt động B: Ghép hai hình thang

1. Vẽ hai hình thang giống nhau trên giấy.
2. Cắt ra và thử ghép thành một hình lớn hơn.
3. Quan sát xem hình mới có giống hình bình hành không.

Câu hỏi:

- đáy mới được tạo bởi những đoạn nào?
- tại sao cuối cùng phải chia 2?

### Hoạt động C: Săn chu vi và diện tích

Chọn một vật gần em:

- mặt bàn
- quyển vở
- tấm thảm

Hỏi:

- nếu viền quanh vật đó thì em đang quan tâm đến chu vi hay diện tích?
- nếu muốn phủ kín bề mặt thì em đang quan tâm đến chu vi hay diện tích?

---

## Ví dụ có hướng dẫn

### Ví dụ 1: Tam giác

Tam giác có đáy 10 cm, chiều cao 6 cm.

Diện tích là:

$$S = \frac{10 \times 6}{2} = 30\text{ cm}^2$$

### Ví dụ 2: Hình thang

Hình thang có đáy lớn 12 cm, đáy nhỏ 8 cm, chiều cao 5 cm.

Diện tích là:

$$S = \frac{(12 + 8) \times 5}{2} = \frac{20 \times 5}{2} = 50\text{ cm}^2$$

### Ví dụ 3: So sánh hai hình

Một hình chữ nhật có kích thước 8 cm và 5 cm.

Một tam giác có cùng đáy 8 cm và cùng chiều cao 5 cm.

Diện tích hình chữ nhật:

$$8 \times 5 = 40\text{ cm}^2$$

Diện tích tam giác:

$$\frac{8 \times 5}{2} = 20\text{ cm}^2$$

Vậy tam giác chỉ bằng **một nửa** hình chữ nhật tương ứng.

---

## Thang thử thách

Mức 1:

- Tính diện tích tam giác có đáy 6 cm, chiều cao 4 cm.

Mức 2:

- Tính diện tích hình thang có đáy lớn 9 cm, đáy nhỏ 5 cm, chiều cao 4 cm.

Mức 3:

- Một tam giác có diện tích 24 cm² và đáy 8 cm. Hãy tìm chiều cao.

Mức 4:

- Em hãy vẽ hai hình khác nhau nhưng có cùng diện tích 24 cm².

---

## Câu hỏi suy nghĩ

1. Vì sao diện tích tam giác lại phải chia 2, còn hình bình hành thì không?
2. Nếu chiều cao tăng gấp đôi còn đáy giữ nguyên, diện tích thay đổi thế nào?
3. Em thấy hình học dễ hiểu hơn khi học bằng công thức hay bằng cắt ghép? Vì sao?

---

## Góc cha mẹ

Bài học này giúp con chuyển từ "nhớ công thức" sang "hiểu công thức từ đâu ra".

Phụ huynh có thể hỗ trợ bằng cách:

- cho con cắt ghép giấy thật
- hỏi "Tại sao phải chia 2?"
- để con giải thích bằng hình vẽ thay vì chỉ nói đáp án

Khi con hiểu được mối liên hệ giữa hình chữ nhật, tam giác và hình thang, việc ghi nhớ công thức sẽ nhẹ nhàng hơn rất nhiều.

---

## Toán học qua thời gian

Cách đây hàng nghìn năm, người Ai Cập cổ đại đã phải đo lại ruộng đất sau mỗi mùa lũ. Việc đó khiến con người nghĩ rất nhiều về hình dạng, độ dài và diện tích.

Từ nhu cầu đo đất, xây nhà và chia đất, hình học dần trở thành một ngành toán học quan trọng.

Tên gọi "geometry" trong tiếng Hy Lạp có thể hiểu là **đo đất**. Điều đó nhắc chúng ta rằng hình học không sinh ra từ bảng vở trước tiên, mà sinh ra từ những câu hỏi rất thật trong cuộc sống.

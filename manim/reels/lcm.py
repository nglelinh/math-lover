from common import *
from math import lcm, pi

TX = {
    "title": {"vi": "Hai bạn gặp lại nhau", "en": "When do they meet again?"},
    "a": {"vi": "Bạn A: cứ 4 ngày một lần", "en": "Friend A: every 4 days"},
    "b": {"vi": "Bạn B: cứ 6 ngày một lần", "en": "Friend B: every 6 days"},
    "meet": {"vi": "Cùng đến thư viện vào ngày 12!", "en": "Both at the library on day 12!"},
    "lcm": {"vi": "BCNN(4, 6) = 12", "en": "LCM(4, 6) = 12"},
    "ma": {"vi": "Bội của 4:", "en": "Multiples of 4:"},
    "mb": {"vi": "Bội của 6:", "en": "Multiples of 6:"},
    "cap_same": {"vi": "Bội chung nhỏ nhất", "en": "Least common multiple"},
    "more": {"vi": "Rồi lại gặp ở 24, 36, …", "en": "Then again on 24, 36, …"},
    "day": {"vi": "ngày", "en": "day"},
}
assert lcm(4, 6) == 12
common = [n for n in range(1, 50) if n % 4 == 0 and n % 6 == 0]
assert common[:3] == [12, 24, 36]


class Lcm(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        U = 0.62
        x0 = -6 * U
        ay = 2.4
        P = lambda d: np.array([x0 + d * U, ay, 0])
        axis = Line(P(0) + LEFT * 0.2, P(12) + RIGHT * 0.3, color=DIM, stroke_width=3)
        ticks = VGroup(*[Line(P(d) + DOWN * 0.1, P(d) + UP * 0.1, color=DIM, stroke_width=2) for d in range(13)])
        nums = VGroup(*[VGroup(Circle(radius=0.2, fill_color="#10121a", fill_opacity=1, stroke_width=0), T(str(d), 24, DIM)).move_to(P(d)) for d in range(1, 13)]).set_z_index(5)
        self.play(Create(axis), Create(ticks), FadeIn(nums), run_time=1.0)

        la = T(tr(TX["a"]), 30, SKY).move_to([0, 5.3, 0])
        lb = T(tr(TX["b"]), 30, PINK).move_to([0, -0.2, 0])
        # A hop phía trên
        self.play(FadeIn(la), run_time=0.4)
        hero_a = Dot(P(0), radius=0.16, color=SKY)
        self.add(hero_a)
        for k in range(1, 4):
            arc = Arc(radius=2 * U, start_angle=pi, angle=-pi, arc_center=P(4 * k - 2) + UP * 0.0, color=SKY, stroke_width=5)
            # cung nằm phía trên trục: Arc từ pi quay ngược chiều kim đồng hồ sang 0 đi qua đỉnh
            self.play(Create(arc), hero_a.animate.move_to(P(4 * k)), run_time=0.8 if k == 1 else 0.6)
            self.play(Indicate(nums[4 * k - 1][1], color=SKY, scale_factor=1.5), run_time=0.3)
        # B hop phía dưới
        self.play(FadeIn(lb), run_time=0.4)
        hero_b = Dot(P(0), radius=0.16, color=PINK)
        self.add(hero_b)
        for k in range(1, 3):
            arc = Arc(radius=3 * U, start_angle=pi, angle=pi, arc_center=P(6 * k - 3), color=PINK, stroke_width=5)
            self.play(Create(arc), hero_b.animate.move_to(P(6 * k)), run_time=1.0 if k == 1 else 0.8)
            self.play(Indicate(nums[6 * k - 1][1], color=PINK, scale_factor=1.5), run_time=0.3)
        glow = Circle(radius=0.38, color=SUN, stroke_width=6).move_to(P(12))
        c = swap_cap(self, c, cap(TX["cap_same"], 38, SUN))
        self.play(Create(glow), nums[11][1].animate.set_color(SUN), run_time=0.8)
        meet = fit(T(tr(TX["meet"]), 32, SUN)).move_to([0, -2.4, 0])
        self.play(FadeIn(meet), run_time=0.6)
        # danh sách bội
        rows = []
        for key, mult, col, y in (("ma", [4, 8, 12, 16], SKY, -3.6), ("mb", [6, 12, 18], PINK, -4.5)):
            t = T(tr(TX[key]), 28, col)
            items = VGroup(*[T(str(m) + ("," if i < len(mult) - 1 else ", …"), 30, SUN if m == 12 else WHITE) for i, m in enumerate(mult)]).arrange(RIGHT, buff=0.2)
            row = VGroup(t, items).arrange(RIGHT, buff=0.3).move_to([0, y, 0])
            rows.append(row)
        self.play(FadeIn(rows[0]), run_time=0.6)
        self.play(FadeIn(rows[1]), run_time=0.6)
        res = T(tr(TX["lcm"]), 50, SUN).move_to([0, -5.7, 0])
        self.play(Write(res), run_time=1.0)
        self.wait(5.0)

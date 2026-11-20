from common import *

TX = {
    "title": {"vi": "Số chẵn: xếp thành cặp", "en": "Even numbers: make pairs"},
    "pair": {"vi": "Ghép mỗi 2 chấm thành 1 cặp", "en": "Group the dots in pairs"},
    "even": {"vi": "Chẵn", "en": "Even"},
    "odd": {"vi": "Lẻ", "en": "Odd"},
    "rule1": {"vi": "Chẵn: 2, 4, 6, 8, 10", "en": "Even: 2, 4, 6, 8, 10"},
    "rule2": {"vi": "Lẻ: 1, 3, 5, 7, 9", "en": "Odd: 1, 3, 5, 7, 9"},
    "last": {"vi": "Chữ số cuối 0, 2, 4, 6, 8 → số chẵn", "en": "Last digit 0, 2, 4, 6, 8 → even"},
    "last_cap": {"vi": "Nhìn chữ số cuối!", "en": "Look at the last digit!"},
}
for n in range(1, 11):
    assert (n % 2 == 0) == (n // 2 * 2 == n)


class EvenOdd(Scene):
    def construct(self):
        c = cap(TX["title"], 40)
        self.add(c)
        y0, dy = 4.7, 0.78
        x0 = -2.2
        rows = []
        for n in range(1, 11):
            y = y0 - (n - 1) * dy
            lab = T(str(n), 30, DIM).move_to([-3.5, y, 0])
            dots = VGroup(*[Dot([x0 + i * 0.52, y, 0], radius=0.17, color=SKY) for i in range(n)])
            rows.append((lab, dots, y))
        self.play(FadeIn(rows[0][0]), FadeIn(rows[0][1]), run_time=0.5)
        c = swap_cap(self, c, cap(TX["pair"], 36, SUN))
        for n in range(1, 11):
            lab, dots, y = rows[n - 1]
            if n > 1:
                self.play(FadeIn(lab), LaggedStart(*[FadeIn(d, scale=1.5) for d in dots], lag_ratio=0.08),
                          run_time=0.55 if n < 5 else 0.4)
            caps = VGroup()
            for p in range(n // 2):
                a, b = dots[2 * p], dots[2 * p + 1]
                caps.add(RoundedRectangle(corner_radius=0.22, width=1.0, height=0.44, color=MINT,
                                          stroke_width=3).move_to((a.get_center() + b.get_center()) / 2))
            anims = [Create(c_) for c_ in caps]
            if n % 2:
                dots[-1].set_color(PINK)
                tag = T(tr(TX["odd"]), 24, PINK)
                anims.append(dots[-1].animate.set_color(PINK))
            else:
                tag = T(tr(TX["even"]), 24, MINT)
            tag.move_to([3.4, y, 0])
            self.play(*anims, FadeIn(tag), run_time=0.45 if n < 5 else 0.3)
        self.wait(0.6)
        c = swap_cap(self, c, cap(TX["last_cap"], 38, SUN))
        r1 = fit(T(tr(TX["rule1"]), 34, MINT)).move_to([0, -4.0, 0])
        r2 = fit(T(tr(TX["rule2"]), 34, PINK)).move_to([0, -4.9, 0])
        r3 = fit(T(tr(TX["last"]), 28, WHITE)).move_to([0, -5.9, 0])
        for r in (r1, r2, r3):
            self.play(FadeIn(r, shift=UP * 0.2), run_time=0.7)
            self.wait(0.4)
        self.wait(4.0)

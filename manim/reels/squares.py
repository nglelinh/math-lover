from common import *

TX = {
    "title": {"vi": "Số chính phương", "en": "Square numbers"},
    "add": {"vi": "Thêm hình chữ L mỗi lần", "en": "Add an L-shape each time"},
    "sq": {"vi": "Sắp chấm thành hình vuông", "en": "Dots make a square"},
    "end": {"vi": "1, 4, 9, 16, 25, …", "en": "1, 4, 9, 16, 25, …"},
    "odd": {"vi": "Cộng các số lẻ liên tiếp!", "en": "Add the odd numbers in a row!"},
    "dots": {"vi": "chấm", "en": "dots"},
}
SP = 0.78
N = 5
assert [k * k for k in range(1, 6)] == [sum(2 * j - 1 for j in range(1, k + 1)) for k in range(1, 6)]


class Squares(Scene):
    def construct(self):
        c = cap(TX["title"], 44)
        self.add(c)
        cx, cy = 0.0, 2.7
        pos = lambda r, col: np.array([cx + (col - (N - 1) / 2) * SP, cy - (r - (N - 1) / 2) * SP, 0])
        grid = {(r, col): Dot(pos(r, col), radius=0.2, color=SKY) for r in range(N) for col in range(N)}
        c = swap_cap(self, c, cap(TX["add"], 36, SUN))
        eq_m = None
        for k in range(1, N + 1):
            new = [(k - 1, col) for col in range(k)] + [(r, k - 1) for r in range(k - 1)]
            assert len(new) == 2 * k - 1
            for key in new:
                grid[key].set_color(SUN)
            old = [(r, col) for r in range(k) for col in range(k) if (r, col) not in new]
            for key in old:
                grid[key].set_color(SKY)
            self.play(*[FadeIn(grid[key], scale=1.8) for key in new], run_time=0.9 if k < 3 else 0.7)
            frame = Square(k * SP, color=MINT, stroke_width=4).move_to(
                (pos(0, 0) + pos(k - 1, k - 1)) / 2)
            terms = " + ".join(str(2 * j - 1) for j in range(1, k + 1))
            line = fit(T("%s = %d" % (terms, k * k) if k > 1 else "1 = 1", 44, WHITE)).move_to([0, -0.8, 0])
            line2 = T("%d × %d = %d %s" % (k, k, k * k, tr(TX["dots"])), 36, MINT).move_to([0, -1.9, 0])
            grp = VGroup(line, line2)
            if eq_m is None:
                self.play(Create(frame), FadeIn(grp), run_time=0.7)
                eq_m = (frame, grp)
            else:
                self.play(ReplacementTransform(eq_m[0], frame), ReplacementTransform(eq_m[1], grp), run_time=0.7)
                eq_m = (frame, grp)
            self.wait(0.9 if k < 4 else 0.6)
        c = swap_cap(self, c, cap(TX["odd"], 34, MINT))
        seq = T(tr(TX["end"]), 56, SUN).move_to([0, -4.0, 0])
        self.play(Write(seq), run_time=1.2)
        self.wait(4.5)

from common import *

TX = {
    "title": {"vi": "Chiếc cân thăng bằng", "en": "The balanced scale"},
    "eq": {"vi": "? + 3 = 8", "en": "? + 3 = 8"},
    "bal": {"vi": "Hai bên bằng nhau", "en": "Both sides are equal"},
    "one": {"vi": "Lấy 3 khối chỉ ở bên trái…", "en": "Take 3 blocks from the left only…"},
    "tilt": {"vi": "Cân bị lệch!", "en": "The scale tips!"},
    "both": {"vi": "Lấy 3 khối ở cả hai bên", "en": "Take 3 blocks from BOTH sides"},
    "ok": {"vi": "Cân vẫn thăng bằng", "en": "Still balanced"},
    "ans": {"vi": "? = 5", "en": "? = 5"},
    "cap_mystery": {"vi": "Ô bí ẩn là số mấy?", "en": "What is in the mystery box?"},
    "cap_keep": {"vi": "Làm giống nhau cả hai bên", "en": "Do the same to both sides"},
}
assert 8 - 3 == 5


class Balance(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        pivot = np.array([0, 1.4, 0])
        L = 2.2
        th = ValueTracker(0.0)
        el = lambda: pivot + L * np.array([-np.cos(th.get_value()), np.sin(th.get_value()), 0])   # đầu trái
        er = lambda: pivot + L * np.array([np.cos(th.get_value()), -np.sin(th.get_value()), 0])  # đầu phải
        beam = always_redraw(lambda: Line(el(), er(), color=WHITE, stroke_width=10))
        stand = VGroup(Line(pivot, pivot + DOWN * 2.2, color=DIM, stroke_width=10),
                       Line(pivot + DOWN * 2.2 + LEFT * 1.0, pivot + DOWN * 2.2 + RIGHT * 1.0, color=DIM, stroke_width=12))
        tip = Dot(pivot, radius=0.16, color=SUN)

        def blk(color):
            return Square(0.42, color=color, fill_color=color, fill_opacity=1, stroke_width=0)
        # đồ vật trên hai đĩa: offset so với đầu đòn
        left_items = []
        box = VGroup(Square(0.8, color=PINK, fill_color=PINK, fill_opacity=0.9, stroke_width=0),
                     T("?", 44, WHITE)).set_z_index(3)
        left_items.append((box, np.array([-0.85, 0.45, 0])))
        for i in range(3):
            left_items.append((blk(SKY), np.array([0.0 + 0.5 * i, 0.33, 0])))
        right_items = []
        for i in range(8):
            r, k = divmod(i, 4)
            right_items.append((blk(MINT), np.array([(k - 1.5) * 0.5, 0.33 + 0.5 * r, 0])))
        for m, off in left_items:
            m.add_updater(lambda mm, dt=0, off=off: mm.move_to(el() + off))
        for m, off in right_items:
            m.add_updater(lambda mm, dt=0, off=off: mm.move_to(er() + off))
        pans = always_redraw(lambda: VGroup(
            Line(el() + LEFT * 1.3, el() + RIGHT * 1.3, color=ORANGE, stroke_width=8),
            Line(er() + LEFT * 1.3, er() + RIGHT * 1.3, color=ORANGE, stroke_width=8)))
        self.add(stand, beam, tip, pans)
        for m, _ in left_items + right_items:
            m.move_to(el() + _ if (m, _) in left_items else er() + _)
        self.play(*[FadeIn(m, scale=1.4) for m, _ in left_items + right_items], run_time=1.2)
        c = swap_cap(self, c, cap(TX["cap_mystery"], 38, SUN))
        eq = T(tr(TX["eq"]), 64, WHITE).move_to([0, -3.0, 0])
        msg = fit(T(tr(TX["bal"]), 34, MINT)).move_to([0, -4.2, 0])
        self.play(Write(eq), FadeIn(msg), run_time=1.0)
        self.wait(1.0)
        # lấy 3 khối bên trái: lệch
        c = swap_cap(self, c, cap(TX["cap_keep"], 38, WHITE))
        m1 = fit(T(tr(TX["one"]), 34, SUN)).move_to([0, -4.2, 0])
        self.play(Transform(msg, m1), run_time=0.5)
        cubes_l = [m for m, _ in left_items[1:]]
        self.play(*[FadeOut(m) for m in cubes_l], run_time=0.6)
        for m in cubes_l:
            m.clear_updaters()
        self.play(th.animate.set_value(0.16), run_time=1.0)
        m2 = fit(T(tr(TX["tilt"]), 36, PINK)).move_to([0, -4.2, 0])
        self.play(Transform(msg, m2), run_time=0.5)
        self.wait(1.0)
        # trả lại
        for m in cubes_l:
            m.set_opacity(1)
        for (m, off) in left_items[1:]:
            m.add_updater(lambda mm, dt=0, off=off: mm.move_to(el() + off))
        self.play(th.animate.set_value(0.0), *[FadeIn(m) for m in cubes_l], run_time=1.0)
        # lấy cả hai bên
        m3 = fit(T(tr(TX["both"]), 34, SUN)).move_to([0, -4.2, 0])
        self.play(Transform(msg, m3), run_time=0.5)
        cubes_r = [m for m, _ in right_items[:3]]
        self.play(*[FadeOut(m) for m in cubes_l + cubes_r], run_time=0.8)
        for m in cubes_l + cubes_r:
            m.clear_updaters()
        self.wait(0.3)
        m4 = fit(T(tr(TX["ok"]), 36, MINT)).move_to([0, -4.2, 0])
        self.play(Transform(msg, m4), run_time=0.5)
        ans = T(tr(TX["ans"]), 80, SUN).move_to([0, -3.0, 0])
        five = VGroup(*[m for m, _ in right_items[3:]])
        self.play(ReplacementTransform(eq, ans), Indicate(five, color=SUN, scale_factor=1.15), run_time=1.2)
        self.wait(4.0)

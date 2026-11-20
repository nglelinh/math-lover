from common import *

TX = {
    "title": {"vi": "Đếm bằng bóng đèn", "en": "Counting with light bulbs"},
    "rule": {"vi": "Sáng = 1, tắt = 0", "en": "On = 1, off = 0"},
    "ex": {"vi": "Ví dụ: 1011", "en": "Example: 1011"},
    "end": {"vi": "Máy tính chỉ dùng 0 và 1", "en": "Computers only use 0 and 1"},
    "dec": {"vi": "Số thường", "en": "Everyday number"},
    "cap_count": {"vi": "Đếm từ 0 đến 15", "en": "Count from 0 to 15"},
    "cap_read": {"vi": "Đọc bóng đèn", "en": "Reading the bulbs"},
}
VALS = [8, 4, 2, 1]
assert format(11, "04b") == "1011" and 8 + 2 + 1 == 11
assert all(sum(v for v, b in zip(VALS, format(n, "04b")) if b == "1") == n for n in range(16))


class Binary(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        n_tr = ValueTracker(0)
        N = lambda: int(round(n_tr.get_value()))
        xs = [-2.7, -0.9, 0.9, 2.7]
        by = 2.8
        bulbs, bits = [], []
        for i, (x, v) in enumerate(zip(xs, VALS)):
            b = Circle(radius=0.7, color=SUN, stroke_width=5, fill_color="#10121a", fill_opacity=1).move_to([x, by, 0])
            def upd(m, dt=0, i=i):
                on = format(N(), "04b")[i] == "1"
                m.set_fill(SUN if on else "#10121a", 1.0)
                m.set_stroke(SUN if on else DIM)
            b.add_updater(upd)
            bulbs.append(b)
            bit = Integer(0, font_size=48)
            def updb(m, dt=0, i=i, x=x):
                on = format(N(), "04b")[i] == "1"
                m.set_value(1 if on else 0)
                m.set_color(SUN if on else DIM)
                m.move_to([x, by - 1.3, 0])
            bit.add_updater(updb)
            bits.append(bit)
        vlab = VGroup(*[T(str(v), 34, SKY).move_to([x, by + 1.3, 0]) for x, v in zip(xs, VALS)])
        self.play(*[FadeIn(b) for b in bulbs], FadeIn(vlab), *[FadeIn(b) for b in bits], run_time=1.0)
        r = T(tr(TX["rule"]), 34, SUN).move_to([0, 0.2, 0])
        self.play(FadeIn(r), run_time=0.5)
        dec_lab = T(tr(TX["dec"]), 28, DIM).move_to([0, -1.2, 0])
        dec = Integer(0, font_size=110, color=WHITE)
        dec.add_updater(lambda m, dt=0: (m.set_value(N()), m.move_to([0, -2.6, 0])))
        self.play(FadeIn(dec_lab), FadeIn(dec), run_time=0.5)
        c = swap_cap(self, c, cap(TX["cap_count"], 40, SUN))
        steps = [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.35, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]
        for k in range(1, 16):
            n_tr.set_value(k)
            self.wait(steps[k - 1])
        self.wait(0.6)
        c = swap_cap(self, c, cap(TX["cap_read"], 40, SUN))
        n_tr.set_value(11)
        self.wait(0.8)
        ex = T(tr(TX["ex"]), 34, WHITE).move_to([0, -4.2, 0])
        self.play(FadeIn(ex), FadeOut(r), run_time=0.5)
        sums = MathTex(r"8+2+1=11", font_size=72, color=SUN).move_to([0, -5.3, 0])
        self.play(Write(sums), *[Indicate(bulbs[i], color=SUN, scale_factor=1.15) for i in (0, 2, 3)], run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(ex), FadeOut(sums), run_time=0.4)
        end = fit(T(tr(TX["end"]), 36, MINT)).move_to([0, -4.6, 0])
        self.play(FadeIn(end), run_time=0.6)
        self.wait(3.0)

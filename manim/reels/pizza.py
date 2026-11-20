from common import *
from math import pi

TX = {
    "title": {"vi": "Chia pizza công bằng", "en": "Sharing pizza fairly"},
    "whole": {"vi": "Cả cái pizza = 1", "en": "One whole pizza = 1"},
    "half": {"vi": "Cắt đôi: mỗi phần là một nửa", "en": "Cut in 2: each piece is a half"},
    "quarter": {"vi": "Cắt tiếp: mỗi phần là một phần tư", "en": "Cut again: each piece is a quarter"},
    "same": {"vi": "Một nửa bằng hai phần tư!", "en": "A half equals two quarters!"},
    "count": {"vi": "Đếm từng phần tư", "en": "Count the quarters"},
    "full": {"vi": "4 phần tư làm thành 1 cái pizza", "en": "4 quarters make 1 whole pizza"},
}


def sec(k, R, ctr, color, op=1.0):
    return Sector(radius=R, angle=pi / 2, start_angle=pi / 2 - (k + 1) * pi / 2, arc_center=ctr,
                  color=color, fill_opacity=op, stroke_width=0)


class Pizza(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        R = 2.3
        ctr = np.array([0, 2.2, 0])
        crust = Circle(radius=R, color="#c68642", stroke_width=10).move_to(ctr)
        base = Circle(radius=R - 0.05, color="#f2c14e", fill_opacity=1, stroke_width=0).move_to(ctr)
        pep = VGroup(*[Dot(ctr + np.array([x, y, 0]), radius=0.2, color="#d1495b") for x, y in
                       [(-1.0, 0.9), (0.9, 1.1), (-0.5, -0.6), (1.2, -0.7), (0.1, 0.2), (-1.3, -0.1), (0.5, -1.4)]])
        self.play(FadeIn(base), Create(crust), FadeIn(pep), run_time=1.0)
        t = fit(T(tr(TX["whole"]), 38, SUN)).move_to([0, -0.8, 0])
        self.play(FadeIn(t), run_time=0.5)
        self.wait(0.6)
        # cắt đôi
        cut1 = Line(ctr + UP * R, ctr + DOWN * R, color="#10121a", stroke_width=6)
        self.play(Create(cut1), run_time=0.7)
        t2 = fit(T(tr(TX["half"]), 34, WHITE)).move_to([0, -0.8, 0])
        half = VGroup(sec(0, R - 0.05, ctr, SUN, 0.45), sec(1, R - 0.05, ctr, SUN, 0.45))
        f1 = MathTex(r"\frac{1}{2}", font_size=96, color=SUN).move_to([0, -2.6, 0])
        self.play(Transform(t, t2), FadeIn(half), Write(f1), run_time=1.0)
        self.wait(1.2)
        # cắt tư
        cut2 = Line(ctr + LEFT * R, ctr + RIGHT * R, color="#10121a", stroke_width=6)
        self.play(Create(cut2), run_time=0.7)
        t3 = fit(T(tr(TX["quarter"]), 34, WHITE)).move_to([0, -0.8, 0])
        f2 = MathTex(r"\frac{1}{4}", font_size=96, color=SKY).move_to([0, -2.6, 0])
        self.play(Transform(t, t3), FadeOut(half), ReplacementTransform(f1, f2), run_time=0.8)
        self.wait(0.8)
        # nửa = hai phần tư
        t4 = fit(T(tr(TX["same"]), 34, SUN)).move_to([0, -0.8, 0])
        q01 = VGroup(sec(0, R - 0.05, ctr, SUN, 0.55), sec(1, R - 0.05, ctr, SUN, 0.55))
        eq = MathTex(r"\frac{1}{2}=\frac{2}{4}", font_size=88, color=SUN).move_to([0, -2.6, 0])
        self.play(Transform(t, t4), FadeIn(q01), ReplacementTransform(f2, eq), run_time=1.0)
        self.wait(1.8)
        # đếm từng phần tư
        t5 = fit(T(tr(TX["count"]), 34, WHITE)).move_to([0, -0.8, 0])
        self.play(Transform(t, t5), FadeOut(q01), FadeOut(eq), run_time=0.6)
        fr = [r"\frac{1}{4}", r"\frac{2}{4}", r"\frac{3}{4}", r"\frac{4}{4}=1"]
        shades = VGroup()
        cur = None
        for k in range(4):
            s = sec(k, R - 0.05, ctr, [SKY, MINT, PINK, SUN][k], 0.6)
            shades.add(s)
            nf = MathTex(fr[k], font_size=88, color=[SKY, MINT, PINK, SUN][k]).move_to([0, -2.6, 0])
            if cur is None:
                self.play(FadeIn(s), Write(nf), run_time=0.8)
            else:
                self.play(FadeIn(s), ReplacementTransform(cur, nf), run_time=0.8)
            cur = nf
            self.wait(0.6)
        t6 = fit(T(tr(TX["full"]), 34, SUN)).move_to([0, -0.8, 0])
        self.play(Transform(t, t6), run_time=0.6)
        self.wait(3.5)

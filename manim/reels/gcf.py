from common import *
from math import gcd

TX = {
    "title": {"vi": "Chia quà thật công bằng", "en": "Fair gift packs"},
    "q": {"vi": "12 bút và 18 vở", "en": "12 pens and 18 notebooks"},
    "q2": {"vi": "Chia thành các gói giống hệt nhau", "en": "Make identical packs, nothing left over"},
    "try4": {"vi": "Thử 4 gói", "en": "Try 4 packs"},
    "left": {"vi": "Vở bị dư 2 quyển!", "en": "2 notebooks left over!"},
    "try6": {"vi": "Thử 6 gói", "en": "Try 6 packs"},
    "ok": {"vi": "Vừa đủ: mỗi gói 2 bút + 3 vở", "en": "Perfect: 2 pens + 3 notebooks each"},
    "gcf": {"vi": "Số gói nhiều nhất = UCLN(12, 18) = 6", "en": "Most packs = GCF(12, 18) = 6"},
    "cap_fair": {"vi": "Số gói phải chia hết cho cả hai số", "en": "The number of packs divides both numbers"},
    "cap_big": {"vi": "Tìm số lớn nhất như vậy", "en": "Find the biggest one"},
}
PENS, BOOKS = 12, 18
assert gcd(PENS, BOOKS) == 6
assert [k for k in range(1, 19) if PENS % k == 0 and BOOKS % k == 0] == [1, 2, 3, 6]
assert BOOKS % 4 == 2 and PENS % 4 == 0


def pen():
    return RoundedRectangle(corner_radius=0.07, width=0.14, height=0.48, color=SUN, fill_color=SUN, fill_opacity=1, stroke_width=0)


def book():
    g = VGroup(Square(0.34, color=SKY, fill_color=SKY, fill_opacity=1, stroke_width=0),
               Line([-0.11, 0.0, 0], [0.11, 0.0, 0], color="#10121a", stroke_width=2))
    return g


class Gcf(Scene):
    def construct(self):
        c = cap(TX["title"], 42)
        self.add(c)
        pens = VGroup(*[pen() for _ in range(PENS)])
        books = VGroup(*[book() for _ in range(BOOKS)])
        pens.generate_target(); books.generate_target()
        def home():
            for i, p in enumerate(pens):
                p.home = np.array([(i - (PENS - 1) / 2) * 0.6, 4.2, 0])
            for i, b in enumerate(books):
                b.home = np.array([(i - (BOOKS - 1) / 2) * 0.42, 3.3, 0])
        home()
        for m in list(pens) + list(books):
            m.move_to(m.home)
            m.s = 1.0

        def go(m, pos, sc):
            a = m.animate.scale(sc / m.s).move_to(pos)
            m.s = sc
            return a
        q = T(tr(TX["q"]), 38, SUN).move_to([0, 5.2, 0])
        self.play(FadeIn(q), LaggedStart(*[FadeIn(p, scale=1.5) for p in pens], lag_ratio=0.05),
                  LaggedStart(*[FadeIn(b, scale=1.5) for b in books], lag_ratio=0.03), run_time=2.2)
        q2 = fit(T(tr(TX["q2"]), 28, DIM)).move_to([0, 2.0, 0])
        self.play(FadeIn(q2), run_time=0.6)
        self.wait(0.6)
        c = swap_cap(self, c, cap(TX["cap_fair"], 34, WHITE))

        def layout(k, y=2.2):
            """Vị trí: k gói; trả về (boxes, target_pos cho pens/books, dư)"""
            W = 7.6 / k
            boxes = VGroup()
            tp, tb, left = [], [], []
            per_p = PENS // k
            per_b = BOOKS // k
            for g in range(k):
                x = -3.8 + W * (g + 0.5)
                boxes.add(RoundedRectangle(corner_radius=0.15, width=W - 0.12, height=3.0, color=MINT,
                                           stroke_width=3).move_to([x, y, 0]))
                for i in range(per_p):
                    tp.append(np.array([x + (i - (per_p - 1) / 2) * 0.36, y + 0.9, 0]))
                for i in range(per_b):
                    r_, c_ = divmod(i, 2)
                    cols = 2 if (per_b - r_ * 2) >= 2 else 1
                    tb.append(np.array([x + (c_ - (cols - 1) / 2) * 0.58, y + 0.0 - r_ * 0.6, 0]))
            used_p = per_p * k
            used_b = per_b * k
            for i in range(used_p, PENS):
                left.append(("p", i))
            for i in range(used_b, BOOKS):
                left.append(("b", i))
            return boxes, tp, tb, left

        # --- thử 4 gói ---
        t4 = T(tr(TX["try4"]), 40, SUN).move_to([0, 5.2, 0])
        self.play(Transform(q, t4), FadeOut(q2), run_time=0.5)
        boxes, tp, tb, left = layout(4)
        moves = [go(pens[i], tp[i], 1.4) for i in range(len(tp))] + \
                [go(books[i], tb[i], 1.4) for i in range(len(tb))]
        lp = [go(books[i], [-0.35 + 0.7 * j, -0.5, 0], 1.4) for j, (_, i) in enumerate(left)]
        self.play(Create(boxes), *moves, *lp, run_time=1.8)
        warn = fit(T(tr(TX["left"]), 36, PINK)).move_to([0, -1.9, 0])
        ring = SurroundingRectangle(VGroup(*[books[i] for _, i in left]), color=PINK, buff=0.15, stroke_width=4)
        self.play(Create(ring), FadeIn(warn), run_time=0.8)
        self.wait(1.3)
        # --- trả về, thử 6 gói ---
        self.play(FadeOut(boxes), FadeOut(ring), FadeOut(warn),
                  *[go(m, m.home, 1.0) for m in list(pens) + list(books)], run_time=1.0)
        t6 = T(tr(TX["try6"]), 40, SUN).move_to([0, 5.2, 0])
        self.play(Transform(q, t6), run_time=0.4)
        boxes, tp, tb, left = layout(6)
        assert not left
        moves = [go(pens[i], tp[i], 1.4) for i in range(PENS)] + [go(books[i], tb[i], 1.4) for i in range(BOOKS)]
        self.play(Create(boxes), *moves, run_time=2.0)
        self.play(boxes.animate.set_color(SUN), run_time=0.5)
        ok = fit(T(tr(TX["ok"]), 34, MINT)).move_to([0, -0.9, 0])
        self.play(FadeIn(ok), run_time=0.7)
        self.wait(1.0)
        c = swap_cap(self, c, cap(TX["cap_big"], 36, SUN))
        res = fit(T(tr(TX["gcf"]), 34, SUN)).move_to([0, -2.3, 0])
        self.play(Write(res), run_time=1.0)
        facts = fit(T("12 = 6 × 2,   18 = 6 × 3", 38, WHITE)).move_to([0, -3.6, 0])
        self.play(FadeIn(facts), run_time=0.6)
        self.wait(4.0)

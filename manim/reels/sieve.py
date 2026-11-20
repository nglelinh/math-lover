from common import *

TX = {
    "title": {"vi": "Sàng số nguyên tố", "en": "Finding primes"},
    "cross": {"vi": "Gạch các bội của", "en": "Cross out multiples of"},
    "keep": {"vi": "Số còn lại là số nguyên tố", "en": "What is left are the primes"},
    "count": {"vi": "25 số nguyên tố nhỏ hơn 100", "en": "25 primes below 100"},
    "one": {"vi": "1 không phải số nguyên tố", "en": "1 is not prime"},
}
N = 100
sieve = [True] * (N + 1)
sieve[0] = sieve[1] = False
for i in range(2, 11):
    if sieve[i]:
        for j in range(i * i, N + 1, i):
            sieve[j] = False
PRIMES = [i for i in range(2, N + 1) if sieve[i]]
assert len(PRIMES) == 25 and PRIMES[-1] == 97


class Sieve(Scene):
    def construct(self):
        c = cap(TX["title"], 44)
        self.add(c)
        S = 0.72
        cx, cy = 0.0, 1.5
        cells = {}
        grid = VGroup()
        for n in range(1, N + 1):
            r, col = divmod(n - 1, 10)
            box = RoundedRectangle(corner_radius=0.08, width=S - 0.06, height=S - 0.06, color=DIM,
                                   stroke_width=1.5, fill_color=CARD, fill_opacity=1)
            t = T(str(n), 22 if n < 100 else 17)
            g = VGroup(box, t).move_to([cx + (col - 4.5) * S, cy + (4.5 - r) * S, 0])
            cells[n] = g
            grid.add(g)
        self.play(LaggedStart(*[FadeIn(g, scale=0.8) for g in grid], lag_ratio=0.012), run_time=2.0)
        note = fit(T(tr(TX["one"]), 28, DIM)).move_to([0, -2.9, 0])
        self.play(cells[1].animate.set_opacity(0.25), FadeIn(note), run_time=0.7)
        crossed = {1}
        for p in (2, 3, 5, 7):
            lab = fit(T("%s %d" % (tr(TX["cross"]), p), 36, SUN)).move_to([0, -3.9, 0])
            self.play(cells[p][0].animate.set_fill(SUN, 0.9).set_stroke(SUN, 3),
                      cells[p][1].animate.set_color(BLACK), *([FadeOut(note)] if p == 2 else []), run_time=0.6)
            note = lab
            self.play(FadeIn(lab), run_time=0.3)
            mult = [m for m in range(2 * p, N + 1, p) if m not in crossed]
            crossed.update(mult)
            self.play(LaggedStart(*[cells[m].animate.set_opacity(0.2) for m in mult], lag_ratio=0.05),
                      run_time=max(0.9, 0.08 * len(mult)))
            self.wait(0.3)
            self.play(FadeOut(lab), run_time=0.2)
        assert [n for n in range(1, N + 1) if n not in crossed] == PRIMES
        c = swap_cap(self, c, cap(TX["keep"], 34, MINT))
        self.play(*[cells[p][0].animate.set_fill(MINT, 0.9).set_stroke(MINT, 3) for p in PRIMES],
                  *[cells[p][1].animate.set_color(BLACK) for p in PRIMES], run_time=1.2)
        res = fit(T(tr(TX["count"]), 36, MINT)).move_to([0, -3.9, 0])
        self.play(FadeIn(res), run_time=0.6)
        plist = fit(T(", ".join(map(str, PRIMES[:10])) + ", …", 28, WHITE)).move_to([0, -5.0, 0])
        self.play(FadeIn(plist), run_time=0.6)
        self.wait(3.0)

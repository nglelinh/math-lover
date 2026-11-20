/**
 * Interactive explainers for math-lover (kids 8-12, touch friendly, EN + VI)
 *  - balance : "The balanced scale"  (chapter 03, equations)
 *  - binary  : "Light-bulb binary"   (chapter 07, binary codes)
 *  - jumper  : "LCM / GCF explorer"  (chapter 05; data-mode="lcm" | "gcf")
 * Usage in a lesson:  <div class="mlx-explainer" data-mlx="balance" data-lang="en"></div>
 * No dependencies; every explainer is a no-op if its container is missing.
 */
(function () {
    'use strict';

    var STYLE_ID = 'mlx-style';
    var CSS = [
        '.mlx{max-width:560px;margin:1.2rem auto;padding:14px;border-radius:16px;background:linear-gradient(135deg,#667eea 0%,#764ba2 100%);color:#fff;box-sizing:border-box;font-family:inherit;line-height:1.4}',
        '.mlx *{box-sizing:border-box}',
        '.mlx h4{margin:0 0 10px;text-align:center;font-size:1.15rem;color:#fff}',
        '.mlx-card{background:#fff;color:#2d3340;border-radius:12px;padding:12px;margin-bottom:10px;overflow:hidden}',
        '.mlx button{min-height:44px;min-width:44px;border:0;border-radius:10px;padding:8px 12px;font-size:1rem;font-weight:700;font-family:inherit;cursor:pointer;background:#667eea;color:#fff;touch-action:manipulation;-webkit-tap-highlight-color:transparent}',
        '.mlx button.alt{background:#eef0ff;color:#3f44a8}',
        '.mlx button:disabled{opacity:.4;cursor:not-allowed}',
        '.mlx button:focus-visible{outline:3px solid #ffd166;outline-offset:2px}',
        '.mlx-row{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;align-items:center}',
        '.mlx-msg{min-height:3.4em;text-align:center;font-weight:700;margin:6px 0 0;font-size:1rem}',
        '.mlx-ok{color:#1b8a3a}.mlx-bad{color:#c2410c}.mlx-info{color:#3f44a8}',
        '.mlx svg{display:block;width:100%;max-width:100%;height:auto;margin:0 auto}',
        '.mlx-eq{text-align:center;font-size:1.5rem;font-weight:800;margin:4px 0}',
        '.mlx-beam,.mlx-pan{transition:transform .6s ease}',
        /* binary */
        '.mlx-bulbs{display:flex;justify-content:center;gap:10px}',
        '.mlx-bcol{display:flex;flex-direction:column;align-items:center;gap:4px;flex:0 1 74px}',
        '.mlx-bval{font-weight:800;color:#3f44a8;font-size:1.1rem}',
        '.mlx button.mlx-bulb{width:100%;max-width:70px;min-height:56px;aspect-ratio:1/1;height:auto;border-radius:50%;border:4px solid #9aa1b5;background:#e6e8f0;color:#6b7186;padding:0;font-size:2rem;line-height:1;transition:background .2s,box-shadow .2s}',
        '.mlx button.mlx-bulb.on{background:#ffd166;border-color:#f4a300;color:#4a3300;box-shadow:0 0 18px 4px rgba(255,209,102,.9)}',
        '.mlx button.mlx-bulb.off{color:#9aa1b5;filter:grayscale(1)}',
        '.mlx-bbit{font-weight:700;color:#6b7186;font-size:1.1rem}',
        '.mlx-big{font-size:2.6rem;font-weight:800;text-align:center;color:#3f44a8;margin:2px 0}',
        /* jumper */
        '.mlx-stepper{display:flex;align-items:center;justify-content:center;gap:10px;margin:8px 0;flex-wrap:wrap}',
        '.mlx-stepper span.lab{flex:1 1 100%;text-align:center;font-weight:700}',
        '.mlx-stepper span.v{display:inline-block;min-width:2.2em;text-align:center;font-size:1.5rem;font-weight:800}',
        '.mlx-grid{display:grid;gap:3px;margin-top:6px}',
        '.mlx-cell{aspect-ratio:1/1;border-radius:6px;background:#eef0f6;color:#6b7186;font-size:clamp(10px,3.2vw,15px);display:flex;align-items:center;justify-content:center;font-weight:600;transition:opacity .2s;border:2px solid transparent}',
        '.mlx-cell.a{background:#bfe9fb;color:#0b4a66;border-color:#4cc9f0}',
        '.mlx-cell.b{background:#ffd0e6;color:#7a1b49;border-color:#ff7eb6}',
        '.mlx-cell.ab{background:#ffd166;color:#4a3300;border-color:#f4a300;font-weight:800}',
        '.mlx-cell.dim{opacity:.25}',
        '.mlx-cell.today{outline:3px solid #764ba2}',
        '.mlx-legend{display:flex;flex-wrap:wrap;gap:6px 12px;justify-content:center;font-size:.9rem;margin-top:8px}',
        '.mlx-legend i{display:inline-block;width:14px;height:14px;border-radius:4px;vertical-align:-2px;margin-right:4px;border:2px solid}',
        '.mlx-packs{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}',
        '.mlx-pack{display:flex;flex-wrap:wrap;gap:2px;padding:4px;border-radius:8px;border:2px solid;max-width:100%}',
        '.mlx-pack.good{border-color:#1b8a3a;background:#eafaf0}',
        '.mlx-left{display:flex;flex-wrap:wrap;gap:2px;padding:4px;border-radius:8px;border:2px dashed #c2410c;background:#fff1e8}',
        '.mlx-dot{width:12px;height:12px;border-radius:50%;display:inline-block}',
        '.mlx-dot.sq{border-radius:3px}'
    ].join('\n');

    var I18N = {
        en: {
            bal_title: 'The Balanced Scale', bal_intro: 'Find the mystery box. Take blocks away, but keep the scale balanced!',
            bal_l: 'Take 1 from LEFT', bal_r: 'Take 1 from RIGHT', bal_both: 'Take 1 from BOTH',
            bal_undo: 'Undo', bal_new: 'New puzzle', bal_reset: 'Start again',
            bal_tip: 'Tipped! The two sides are not equal. Undo, or take the same from the other side.',
            bal_ok: 'Balanced! The two sides are still equal.',
            bal_win: function (x, a, b) { return 'The mystery box is ' + x + '! Because ' + b + ' \u2212 ' + a + ' = ' + x + '.'; },
            bal_scale: 'A balance scale',
            bin_title: 'Light-Bulb Binary', bin_intro: 'Tap a bulb to turn it on or off. An ON bulb counts its number.',
            bin_plus: '+1', bin_reset: 'All off', bin_new: 'New challenge', bin_target: 'Challenge: make the number',
            bin_is: 'Everyday number', bin_ok: function (n, t) { return 'Yes! ' + t + ' = ' + n + ' \u2714'; },
            bin_try: 'Not yet. Keep trying!', bin_zero: 'All bulbs are off, so the number is 0.',
            bin_on: 'on', bin_off: 'off', bin_bulb: 'Bulb worth',
            lcm_title: 'Two Friends, One Library', lcm_a: 'Friend A visits every', lcm_b: 'Friend B visits every', days: 'days',
            lcm_play: '\u25B6 Watch the days', lcm_stop: '\u25A0 Stop', lcm_legend_a: 'A visits', lcm_legend_b: 'B visits', lcm_legend_ab: 'Both visit',
            lcm_res: function (a, b, l) { return 'They meet again on day ' + l + '. That is the least common multiple of ' + a + ' and ' + b + '.'; },
            lcm_list: function (n, arr) { return 'Every ' + n + ' days: ' + arr.join(', ') + ', \u2026'; },
            lcm_day: 'Day',
            gcf_title: 'Gift Packs', gcf_pens: 'Pens', gcf_books: 'Notebooks', gcf_size: 'Number of packs', gcf_best: 'Show me the most packs',
            gcf_line: function (name, per, r) { return name + ': ' + per + ' in each pack' + (r ? ', ' + r + ' left over' : ', none left over'); },
            gcf_good: 'Every pack is equal and nothing is left over!', gcf_bad: 'Something is left over. Try another number of packs.',
            gcf_great: function (g) { return 'The most packs that work: ' + g + '. That is the greatest common factor!'; },
            gcf_less: function (g) { return 'This works, but you can make even more packs. Try more!'; },
            minus: 'less', plus: 'more'
        },
        vi: {
            bal_title: 'Chi\u1EBFc c\u00E2n th\u0103ng b\u1EB1ng', bal_intro: 'H\u00E3y t\u00ECm \u00F4 b\u00ED \u1EA9n. L\u1EA5y b\u1EDBt kh\u1ED1i ra, nh\u01B0ng ph\u1EA3i gi\u1EEF c\u00E2n th\u0103ng b\u1EB1ng nh\u00E9!',
            bal_l: 'L\u1EA5y 1 \u1EDF b\u00EAn TR\u00C1I', bal_r: 'L\u1EA5y 1 \u1EDF b\u00EAn PH\u1EA2I', bal_both: 'L\u1EA5y 1 \u1EDF C\u1EA2 HAI b\u00EAn',
            bal_undo: 'Ho\u00E0n l\u1EA1i', bal_new: '\u0110\u1EC1 m\u1EDBi', bal_reset: 'L\u00E0m l\u1EA1i',
            bal_tip: 'C\u00E2n b\u1ECB l\u1EC7ch! Hai b\u00EAn kh\u00F4ng b\u1EB1ng nhau. H\u00E3y ho\u00E0n l\u1EA1i, ho\u1EB7c l\u1EA5y \u0111i s\u1ED1 kh\u1ED1i gi\u1ED1ng nh\u01B0 v\u1EADy \u1EDF b\u00EAn c\u00F2n l\u1EA1i.',
            bal_ok: 'C\u00E2n th\u0103ng b\u1EB1ng! Hai b\u00EAn v\u1EABn b\u1EB1ng nhau.',
            bal_win: function (x, a, b) { return '\u00D4 b\u00ED \u1EA9n l\u00E0 ' + x + '! V\u00EC ' + b + ' \u2212 ' + a + ' = ' + x + '.'; },
            bal_scale: 'M\u1ED9t chi\u1EBFc c\u00E2n th\u0103ng b\u1EB1ng',
            bin_title: 'Nh\u1ECB ph\u00E2n b\u1EB1ng b\u00F3ng \u0111\u00E8n', bin_intro: 'Ch\u1EA1m v\u00E0o b\u00F3ng \u0111\u00E8n \u0111\u1EC3 b\u1EADt ho\u1EB7c t\u1EAFt. B\u00F3ng S\u00C1NG s\u1EBD t\u00EDnh gi\u00E1 tr\u1ECB c\u1EE7a n\u00F3.',
            bin_plus: '+1', bin_reset: 'T\u1EAFt h\u1EBFt', bin_new: 'Th\u1EED th\u00E1ch m\u1EDBi', bin_target: 'Th\u1EED th\u00E1ch: t\u1EA1o ra s\u1ED1',
            bin_is: 'S\u1ED1 th\u01B0\u1EDDng', bin_ok: function (n, t) { return '\u0110\u00FAng r\u1ED3i! ' + t + ' = ' + n + ' \u2714'; },
            bin_try: 'Ch\u01B0a \u0111\u00FAng. Th\u1EED l\u1EA1i nh\u00E9!', bin_zero: 'T\u1EA5t c\u1EA3 b\u00F3ng \u0111\u1EC1u t\u1EAFt, n\u00EAn s\u1ED1 l\u00E0 0.',
            bin_on: 's\u00E1ng', bin_off: 't\u1EAFt', bin_bulb: 'B\u00F3ng c\u00F3 gi\u00E1 tr\u1ECB',
            lcm_title: 'Hai b\u1EA1n, m\u1ED9t th\u01B0 vi\u1EC7n', lcm_a: 'B\u1EA1n A c\u1EE9', lcm_b: 'B\u1EA1n B c\u1EE9', days: 'ng\u00E0y m\u1ED9t l\u1EA7n',
            lcm_play: '\u25B6 Xem t\u1EEBng ng\u00E0y', lcm_stop: '\u25A0 D\u1EEBng', lcm_legend_a: 'A \u0111\u1EBFn', lcm_legend_b: 'B \u0111\u1EBFn', lcm_legend_ab: 'C\u1EA3 hai \u0111\u1EBFn',
            lcm_res: function (a, b, l) { return 'Ng\u00E0y ' + l + ' hai b\u1EA1n g\u1EB7p l\u1EA1i. \u0110\u00F3 l\u00E0 b\u1ED9i chung nh\u1ECF nh\u1EA5t c\u1EE7a ' + a + ' v\u00E0 ' + b + '.'; },
            lcm_list: function (n, arr) { return 'C\u1EE9 ' + n + ' ng\u00E0y: ' + arr.join(', ') + ', \u2026'; },
            lcm_day: 'Ng\u00E0y',
            gcf_title: 'Chia qu\u00E0 th\u00E0nh t\u00FAi', gcf_pens: 'B\u00FAt', gcf_books: 'V\u1EDF', gcf_size: 'S\u1ED1 t\u00FAi', gcf_best: 'Cho t\u00F4i xem nhi\u1EC1u t\u00FAi nh\u1EA5t',
            gcf_line: function (name, per, r) { return name + ': m\u1ED7i t\u00FAi ' + per + (r ? ', c\u00F2n d\u01B0 ' + r : ', kh\u00F4ng d\u01B0 c\u00E1i n\u00E0o'); },
            gcf_good: 'C\u00E1c t\u00FAi \u0111\u1EC1u b\u1EB1ng nhau v\u00E0 kh\u00F4ng d\u01B0 c\u00E1i n\u00E0o!', gcf_bad: 'C\u00F2n d\u01B0 m\u1ED9t s\u1ED1 c\u00E1i. H\u00E3y th\u1EED s\u1ED1 t\u00FAi kh\u00E1c.',
            gcf_great: function (g) { return 'Chia \u0111\u01B0\u1EE3c nhi\u1EC1u t\u00FAi nh\u1EA5t l\u00E0 ' + g + ' t\u00FAi. \u0110\u00F3 l\u00E0 \u01B0\u1EDBc chung l\u1EDBn nh\u1EA5t!'; },
            gcf_less: function (g) { return 'C\u00E1ch n\u00E0y chia \u0111\u01B0\u1EE3c, nh\u01B0ng c\u00F2n chia \u0111\u01B0\u1EE3c nhi\u1EC1u t\u00FAi h\u01A1n. Th\u1EED th\u00EAm t\u00FAi nh\u00E9!'; },
            minus: 'gi\u1EA3m', plus: 't\u0103ng'
        }
    };

    function injectStyle() {
        if (document.getElementById(STYLE_ID)) return;
        var s = document.createElement('style');
        s.id = STYLE_ID;
        s.textContent = CSS;
        document.head.appendChild(s);
    }
    function gcd(a, b) { return b === 0 ? a : gcd(b, a % b); }
    function lcm(a, b) { return a / gcd(a, b) * b; }
    function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
    function btn(label, cls, onclick, aria) {
        var b = el('button', cls || '', label);
        b.type = 'button';
        if (aria) b.setAttribute('aria-label', aria);
        b.addEventListener('click', onclick);
        return b;
    }
    function NS(tag, attrs) {
        var e = document.createElementNS('http://www.w3.org/2000/svg', tag);
        for (var k in attrs) e.setAttribute(k, attrs[k]);
        return e;
    }
    function rand(n) { return Math.floor(Math.random() * n); }
    function shell(root, t, title) {
        root.innerHTML = '';
        root.classList.add('mlx');
        root.setAttribute('role', 'group');
        root.setAttribute('aria-label', title);
        root.appendChild(el('h4', '', title));
    }

    /* ---------------------------------------------------------- balance */
    var PUZZLES = [[3, 8], [2, 7], [4, 9], [5, 12], [1, 6], [4, 11]];

    function initBalance(root, t) {
        shell(root, t, '\u2696\uFE0F ' + t.bal_title);
        var card = el('div', 'mlx-card');
        var eq = el('div', 'mlx-eq');
        var svg = NS('svg', { viewBox: '0 0 360 270', role: 'img', 'aria-label': t.bal_scale });
        var msg = el('p', 'mlx-msg mlx-info');
        msg.setAttribute('aria-live', 'polite');
        card.appendChild(eq); card.appendChild(svg); card.appendChild(msg);
        var row1 = el('div', 'mlx-row'), row2 = el('div', 'mlx-row');
        row2.style.marginTop = '8px';
        root.appendChild(card);
        var bL = btn(t.bal_l, '', function () { act('l'); });
        var bR = btn(t.bal_r, '', function () { act('r'); });
        var bB = btn(t.bal_both, '', function () { act('b'); });
        var bU = btn(t.bal_undo, 'alt', undo);
        var bS = btn(t.bal_reset, 'alt', function () { start(cur); });
        var bN = btn(t.bal_new, 'alt', function () { start((cur + 1) % PUZZLES.length); });
        [bL, bR].forEach(function (b) { row1.appendChild(b); });
        row1.appendChild(bB);
        [bU, bS, bN].forEach(function (b) { row2.appendChild(b); });
        root.appendChild(row1); root.appendChild(row2);

        var cur = rand(PUZZLES.length), a, b, x, la, rb, hist, won;
        var PIV = { x: 180, y: 55 }, LEN = 108, HANG = 100;

        function start(i) {
            cur = i; a = PUZZLES[i][0]; b = PUZZLES[i][1]; x = b - a;
            la = a; rb = b; hist = []; won = false; build(); render(true);
        }
        function act(k) {
            if (won) return;
            hist.push([la, rb]);
            if (k === 'l' || k === 'b') la--;
            if (k === 'r' || k === 'b') rb--;
            render(false);
        }
        function undo() { if (hist.length && !won) { var h = hist.pop(); la = h[0]; rb = h[1]; render(false); } }

        var beam, panL, panR, itemsL, itemsR;
        function build() {
            while (svg.firstChild) svg.removeChild(svg.firstChild);
            svg.appendChild(NS('rect', { x: 130, y: 252, width: 100, height: 10, rx: 5, fill: '#7b8294' }));
            svg.appendChild(NS('rect', { x: PIV.x - 5, y: PIV.y, width: 10, height: 200, rx: 4, fill: '#9aa1b5' }));
            beam = NS('g', { 'class': 'mlx-beam' });
            beam.style.transformOrigin = PIV.x + 'px ' + PIV.y + 'px';
            beam.appendChild(NS('rect', { x: PIV.x - LEN - 6, y: PIV.y - 5, width: 2 * LEN + 12, height: 10, rx: 5, fill: '#2d3340' }));
            svg.appendChild(beam);
            panL = pan(); panR = pan();
            svg.appendChild(panL.g); svg.appendChild(panR.g);
            svg.appendChild(NS('circle', { cx: PIV.x, cy: PIV.y, r: 9, fill: '#ffd166', stroke: '#f4a300', 'stroke-width': 3 }));
        }
        function pan() {
            var g = NS('g', { 'class': 'mlx-pan' });
            g.appendChild(NS('line', { x1: 0, y1: 0, x2: -52, y2: HANG, stroke: '#7b8294', 'stroke-width': 2 }));
            g.appendChild(NS('line', { x1: 0, y1: 0, x2: 52, y2: HANG, stroke: '#7b8294', 'stroke-width': 2 }));
            g.appendChild(NS('rect', { x: -60, y: HANG, width: 120, height: 9, rx: 4, fill: '#ff9f43' }));
            var items = NS('g', {});
            g.appendChild(items);
            return { g: g, items: items };
        }
        function slots(n, side, solved) {
            var out = [], cols = 4, S = 28;
            for (var i = 0; i < n; i++) {
                var r = Math.floor(i / cols), c = i % cols, inRow = Math.min(cols, n - r * cols);
                out.push({ x: (c - (inRow - 1) / 2) * S, y: HANG - 15 - r * S });
            }
            return out;
        }
        function cube(p, fill, label, size) {
            var g = NS('g', { transform: 'translate(' + p.x + ',' + p.y + ')' });
            g.appendChild(NS('rect', { x: -size / 2, y: -size / 2, width: size, height: size, rx: 4, fill: fill, stroke: 'rgba(0,0,0,.25)', 'stroke-width': 1 }));
            if (label) { var tx = NS('text', { x: 0, y: 7, 'text-anchor': 'middle', 'font-size': 20, 'font-weight': 800, fill: '#fff' }); tx.textContent = label; g.appendChild(tx); }
            return g;
        }
        function render(first) {
            var diff = (x + la) - rb;
            var ang = -(diff > 0 ? 1 : diff < 0 ? -1 : 0) * Math.min(Math.abs(diff), 2) * 5;
            var rad = ang * Math.PI / 180;
            var lx = PIV.x - LEN * Math.cos(rad), ly = PIV.y - LEN * Math.sin(rad);
            var rx = PIV.x + LEN * Math.cos(rad), ry = PIV.y + LEN * Math.sin(rad);
            beam.style.transform = 'rotate(' + ang + 'deg)';
            panL.g.style.transform = 'translate(' + lx + 'px,' + ly + 'px)';
            panR.g.style.transform = 'translate(' + rx + 'px,' + ry + 'px)';
            if (first) { panL.g.style.transition = 'none'; panR.g.style.transition = 'none'; beam.style.transition = 'none'; void svg.getBoundingClientRect(); panL.g.style.transition = ''; panR.g.style.transition = ''; beam.style.transition = ''; }
            while (panL.items.firstChild) panL.items.removeChild(panL.items.firstChild);
            while (panR.items.firstChild) panR.items.removeChild(panR.items.firstChild);
            won = (la === 0 && diff === 0);
            var sl = slots(1 + la, 'l'), i;
            panL.items.appendChild(cube(sl[0], '#ff7eb6', won ? String(x) : '?', 26));
            for (i = 0; i < la; i++) panL.items.appendChild(cube(sl[i + 1], '#4cc9f0', '', 24));
            var sr = slots(rb, 'r');
            for (i = 0; i < rb; i++) panR.items.appendChild(cube(sr[i], '#80ed99', '', 24));
            eq.textContent = (won ? x : '?') + (la ? ' + ' + la : '') + ' = ' + rb;
            bL.disabled = won || la < 1; bR.disabled = won || rb < 1; bB.disabled = won || la < 1 || rb < 1;
            bU.disabled = won || !hist.length;
            if (won) { msg.className = 'mlx-msg mlx-ok'; msg.textContent = '\uD83C\uDF89 ' + t.bal_win(x, a, b); }
            else if (diff !== 0) { msg.className = 'mlx-msg mlx-bad'; msg.textContent = t.bal_tip; }
            else { msg.className = 'mlx-msg mlx-info'; msg.textContent = hist.length ? t.bal_ok : t.bal_intro; }
        }
        start(cur);
    }

    /* ----------------------------------------------------------- binary */
    function initBinary(root, t) {
        shell(root, t, '\uD83D\uDCA1 ' + t.bin_title);
        var VALS = [8, 4, 2, 1], bits = [0, 0, 0, 0], target = 0;
        var card = el('div', 'mlx-card');
        card.appendChild(el('p', 'mlx-msg mlx-info', t.bin_intro)).style.minHeight = '0';
        var bulbsRow = el('div', 'mlx-bulbs');
        var bulbs = [], bitEls = [];
        VALS.forEach(function (v, i) {
            var col = el('div', 'mlx-bcol');
            col.appendChild(el('div', 'mlx-bval', String(v)));
            var bb = el('button', 'mlx-bulb off', '\uD83D\uDCA1');
            bb.type = 'button';
            bb.addEventListener('click', function () { bits[i] = 1 - bits[i]; render(); });
            var bt = el('div', 'mlx-bbit', '0');
            col.appendChild(bb); col.appendChild(bt);
            bulbsRow.appendChild(col); bulbs.push(bb); bitEls.push(bt);
        });
        card.appendChild(bulbsRow);
        var sumEl = el('div', 'mlx-eq'); sumEl.style.fontSize = '1.2rem';
        var big = el('div', 'mlx-big');
        var lab = el('div', '', t.bin_is); lab.style.cssText = 'text-align:center;color:#6b7186;font-weight:700;margin-top:6px';
        card.appendChild(sumEl); card.appendChild(lab); card.appendChild(big);
        root.appendChild(card);
        var chal = el('div', 'mlx-card'); chal.style.textAlign = 'center';
        var tgt = el('div', 'mlx-eq'); tgt.style.color = '#764ba2';
        var msg = el('p', 'mlx-msg mlx-info'); msg.setAttribute('aria-live', 'polite');
        chal.appendChild(tgt); chal.appendChild(msg); root.appendChild(chal);
        var row = el('div', 'mlx-row');
        row.appendChild(btn(t.bin_plus, '', function () { var n = (val() + 1) % 16; for (var i = 0; i < 4; i++) bits[i] = (n >> (3 - i)) & 1; render(); }, '+1'));
        row.appendChild(btn(t.bin_reset, 'alt', function () { bits = [0, 0, 0, 0]; render(); }));
        row.appendChild(btn(t.bin_new, 'alt', function () { newTarget(); render(); }));
        root.appendChild(row);
        function val() { var n = 0; bits.forEach(function (b, i) { n += b * VALS[i]; }); return n; }
        function newTarget() { var n; do { n = 1 + rand(15); } while (n === target); target = n; }
        function render() {
            var n = val(), parts = [];
            bits.forEach(function (b, i) {
                bulbs[i].className = 'mlx-bulb ' + (b ? 'on' : 'off');
                bulbs[i].setAttribute('aria-pressed', b ? 'true' : 'false');
                bulbs[i].setAttribute('aria-label', t.bin_bulb + ' ' + VALS[i] + ': ' + (b ? t.bin_on : t.bin_off));
                bitEls[i].textContent = String(b);
                if (b) parts.push(VALS[i]);
            });
            sumEl.textContent = parts.length ? parts.join(' + ') + ' = ' + n : '0';
            big.textContent = String(n);
            tgt.textContent = t.bin_target + ' ' + target;
            if (n === target) { msg.className = 'mlx-msg mlx-ok'; msg.textContent = '\uD83C\uDF89 ' + t.bin_ok(n, parts.join(' + ')); }
            else if (n === 0) { msg.className = 'mlx-msg mlx-info'; msg.textContent = t.bin_zero; }
            else { msg.className = 'mlx-msg mlx-info'; msg.textContent = t.bin_try; }
        }
        newTarget(); render();
    }

    /* ----------------------------------------------------------- jumper */
    function stepper(label, tail, min, max, get, set) {
        var wrap = el('div', 'mlx-stepper');
        wrap.appendChild(el('span', 'lab', label));
        var m = btn('\u2212', 'alt', function () { if (get() > min) { set(get() - 1); } }, '');
        var MX = function () { return typeof max === 'function' ? max() : max; };
        var v = el('span', 'v', String(get()));
        var p = btn('+', 'alt', function () { if (get() < MX()) { set(get() + 1); } }, '');
        wrap.appendChild(m); wrap.appendChild(v); wrap.appendChild(p);
        if (tail) wrap.appendChild(el('span', '', tail));
        return { wrap: wrap, update: function () { v.textContent = String(get()); m.disabled = get() <= min; p.disabled = get() >= MX(); } };
    }

    function initLcm(root, t) {
        shell(root, t, '\uD83D\uDCDA ' + t.lcm_title);
        var A = 4, B = 6, N = 72, COLS = 9, day = 0, timer = null;
        var card = el('div', 'mlx-card');
        var sa, sb;
        sa = stepper(t.lcm_a, t.days, 2, 9, function () { return A; }, function (v) { A = v; reset(); });
        sb = stepper(t.lcm_b, t.days, 2, 9, function () { return B; }, function (v) { B = v; reset(); });
        card.appendChild(sa.wrap); card.appendChild(sb.wrap);
        var grid = el('div', 'mlx-grid'); grid.style.gridTemplateColumns = 'repeat(' + COLS + ',1fr)';
        var cells = [];
        for (var i = 1; i <= N; i++) { var c = el('div', 'mlx-cell', String(i)); grid.appendChild(c); cells.push(c); }
        card.appendChild(grid);
        var lg = el('div', 'mlx-legend');
        lg.innerHTML = '<span><i style="background:#bfe9fb;border-color:#4cc9f0"></i></span><span><i style="background:#ffd0e6;border-color:#ff7eb6"></i></span><span><i style="background:#ffd166;border-color:#f4a300"></i></span>';
        var ls = lg.querySelectorAll('span');
        ls[0].appendChild(document.createTextNode(t.lcm_legend_a)); ls[1].appendChild(document.createTextNode(t.lcm_legend_b)); ls[2].appendChild(document.createTextNode(t.lcm_legend_ab));
        card.appendChild(lg);
        var listA = el('p', 'mlx-msg mlx-info'); listA.style.minHeight = '0'; listA.style.margin = '8px 0 0'; listA.style.color = '#0b6b94';
        var listB = el('p', 'mlx-msg'); listB.style.minHeight = '0'; listB.style.margin = '2px 0 0'; listB.style.color = '#a3235f';
        var msg = el('p', 'mlx-msg mlx-ok'); msg.setAttribute('aria-live', 'polite');
        card.appendChild(listA); card.appendChild(listB); card.appendChild(msg);
        root.appendChild(card);
        var playBtn = btn(t.lcm_play, '', toggle);
        var row = el('div', 'mlx-row'); row.appendChild(playBtn); root.appendChild(row);

        function multiples(n, k) { var o = []; for (var i = 1; i <= k; i++) o.push(n * i); return o; }
        function paint(upTo) {
            var L = lcm(A, B);
            cells.forEach(function (c, idx) {
                var n = idx + 1, ia = n % A === 0, ib = n % B === 0;
                var cls = 'mlx-cell' + (ia && ib ? ' ab' : ia ? ' a' : ib ? ' b' : '');
                if (upTo !== null) { if (n > upTo) cls += ' dim'; if (n === upTo) cls += ' today'; }
                c.className = cls;
            });
            listA.textContent = t.lcm_list(A, multiples(A, 5));
            listB.textContent = t.lcm_list(B, multiples(B, 5));
        }
        function reset() { stop(); day = 0; sa.update(); sb.update(); paint(null); msg.textContent = t.lcm_res(A, B, lcm(A, B)); }
        function stop() { if (timer) { clearInterval(timer); timer = null; } playBtn.textContent = t.lcm_play; }
        function toggle() {
            if (timer) { stop(); paint(null); return; }
            var L = lcm(A, B); day = 0; playBtn.textContent = t.lcm_stop; msg.textContent = '';
            timer = setInterval(function () {
                day++; paint(day);
                var both = day % A === 0 && day % B === 0;
                msg.className = 'mlx-msg ' + (both ? 'mlx-ok' : 'mlx-info');
                msg.textContent = t.lcm_day + ' ' + day;
                if (day >= L) { stop(); paint(null); msg.className = 'mlx-msg mlx-ok'; msg.textContent = '\uD83C\uDF89 ' + t.lcm_res(A, B, L); }
            }, 320);
        }
        reset();
    }

    function initGcf(root, t) {
        shell(root, t, '\uD83C\uDF81 ' + t.gcf_title);
        var P = 12, Bk = 18, K = 6;
        var card = el('div', 'mlx-card');
        var sp = stepper(t.gcf_pens, '', 2, 24, function () { return P; }, function (v) { P = v; clampK(); render(); });
        var sbk = stepper(t.gcf_books, '', 2, 30, function () { return Bk; }, function (v) { Bk = v; clampK(); render(); });
        var sk = stepper(t.gcf_size, '', 1, function () { return Math.min(P, Bk); }, function () { return K; }, function (v) { K = v; render(); });
        card.appendChild(sp.wrap); card.appendChild(sbk.wrap); card.appendChild(sk.wrap);
        var l1 = el('div', 'mlx-msg'); l1.style.cssText = 'min-height:0;text-align:left;margin:8px 0 0;color:#0b6b94';
        var l2 = el('div', 'mlx-msg'); l2.style.cssText = 'min-height:0;text-align:left;margin:2px 0 0;color:#a3235f';
        var packs = el('div', 'mlx-packs');
        var msg = el('p', 'mlx-msg'); msg.setAttribute('aria-live', 'polite');
        [l1, l2, packs, msg].forEach(function (e) { card.appendChild(e); });
        root.appendChild(card);
        var row = el('div', 'mlx-row'); row.appendChild(btn(t.gcf_best, '', function () { K = gcd(P, Bk); render(); })); root.appendChild(row);
        function clampK() { var m = Math.min(P, Bk); if (K > m) K = m; if (K < 1) K = 1; }
        function dots(container, n, color, sq) {
            for (var j = 0; j < n; j++) { var d = el('span', 'mlx-dot' + (sq ? ' sq' : '')); d.style.background = color; container.appendChild(d); }
        }
        function render() {
            clampK(); sp.update(); sbk.update(); sk.update();
            var pp = Math.floor(P / K), pb = Math.floor(Bk / K), rp = P % K, rb = Bk % K, ok = rp === 0 && rb === 0;
            packs.innerHTML = '';
            for (var i = 0; i < K; i++) {
                var p = el('div', 'mlx-pack' + (ok ? ' good' : '')); if (!ok) p.style.borderColor = '#9aa1b5';
                dots(p, pp, '#4cc9f0', false); dots(p, pb, '#ff7eb6', true);
                packs.appendChild(p);
            }
            if (!ok) { var lf = el('div', 'mlx-left'); dots(lf, rp, '#4cc9f0', false); dots(lf, rb, '#ff7eb6', true); packs.appendChild(lf); }
            l1.textContent = t.gcf_line(t.gcf_pens, pp, rp);
            l2.textContent = t.gcf_line(t.gcf_books, pb, rb);
            var g = gcd(P, Bk);
            if (ok && K === g) { msg.className = 'mlx-msg mlx-ok'; msg.textContent = '\uD83C\uDF89 ' + t.gcf_great(g); }
            else if (ok) { msg.className = 'mlx-msg mlx-info'; msg.textContent = t.gcf_good + ' ' + t.gcf_less(g); }
            else { msg.className = 'mlx-msg mlx-bad'; msg.textContent = t.gcf_bad; }
        }
        render();
    }

    function initJumper(root, t) {
        if ((root.getAttribute('data-mode') || 'lcm') === 'gcf') initGcf(root, t); else initLcm(root, t);
    }

    var INIT = { balance: initBalance, binary: initBinary, jumper: initJumper };

    function initAll() {
        var nodes = document.querySelectorAll('.mlx-explainer');
        if (!nodes.length) return;
        injectStyle();
        for (var i = 0; i < nodes.length; i++) {
            var root = nodes[i], kind = root.getAttribute('data-mlx');
            var lang = root.getAttribute('data-lang') || document.documentElement.lang || 'en';
            var t = I18N[lang === 'vi' ? 'vi' : 'en'];
            if (INIT[kind] && !root.getAttribute('data-mlx-ready')) {
                root.setAttribute('data-mlx-ready', '1');
                INIT[kind](root, t);
            }
        }
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', initAll); else initAll();
})();

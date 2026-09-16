/**
 * Optional modern-application explorers for English enrichment lessons.
 * Each block no-ops unless its container id is present on the page.
 */
(function () {
    "use strict";

    function el(tag, attrs, html) {
        const node = document.createElement(tag);
        Object.keys(attrs || {}).forEach(function (key) {
            if (key === "style") {
                node.setAttribute("style", attrs[key]);
            } else {
                node[key] = attrs[key];
            }
        });
        if (html !== undefined) {
            node.innerHTML = html;
        }
        return node;
    }

    function boxWrap(title, innerHtml) {
        return (
            '<div class="interactive-box" style="background: linear-gradient(135deg, #38B8C5 0%, #7AA8FF 100%); padding: 20px; border-radius: 15px; color: white; max-width: 640px; margin: 20px auto;">' +
            '<h3 style="text-align:center;margin-top:0;">' + title + "</h3>" +
            '<div style="background:white;padding:18px;border-radius:12px;color:#223042;">' +
            innerHtml +
            "</div></div>"
        );
    }

    function initEvenBit() {
        const root = document.getElementById("apps-even-bit");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "On / Off Pair Tester",
            '<label for="apps-even-input"><strong>How many lights?</strong></label>' +
                '<input id="apps-even-input" type="range" min="1" max="16" value="8" style="width:100%;margin:10px 0;">' +
                '<p id="apps-even-count" style="font-weight:700;">8 lights</p>' +
                '<div id="apps-even-lights" style="display:flex;flex-wrap:wrap;gap:8px;min-height:48px;"></div>' +
                '<p id="apps-even-result" style="margin-top:12px;"></p>'
        );
        const input = document.getElementById("apps-even-input");
        const count = document.getElementById("apps-even-count");
        const lights = document.getElementById("apps-even-lights");
        const result = document.getElementById("apps-even-result");

        function render() {
            const n = parseInt(input.value, 10);
            count.textContent = n + " lights";
            lights.innerHTML = "";
            for (let i = 0; i < n; i += 1) {
                const on = i % 2 === 0;
                const lamp = el("span", {
                    style:
                        "width:28px;height:28px;border-radius:50%;display:inline-block;border:2px solid #223042;background:" +
                        (on ? "#F6C453" : "#E6E6E6") +
                        ";",
                });
                lights.appendChild(lamp);
            }
            const leftover = n % 2;
            result.textContent = leftover === 0
                ? "Complete pairs. This number is even — like a last computer switch set to 0."
                : "One light is left over. This number is odd — like a last computer switch set to 1.";
        }
        input.addEventListener("input", render);
        render();
    }

    function initSkipLoop() {
        const root = document.getElementById("apps-skip-loop");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "Repeat-Loop Skip Counter",
            '<label><strong>Start</strong></label><input id="apps-loop-start" type="number" value="0" min="0" max="40" style="width:100%;padding:8px;margin:6px 0 12px;">' +
                '<label><strong>Add each repeat</strong></label><input id="apps-loop-step" type="number" value="5" min="1" max="10" style="width:100%;padding:8px;margin:6px 0 12px;">' +
                '<label><strong>How many repeats?</strong></label><input id="apps-loop-times" type="range" min="1" max="8" value="4" style="width:100%;">' +
                '<p id="apps-loop-seq" style="font-size:20px;font-weight:700;margin-top:12px;"></p>' +
                "<p>This is the same idea as a Scratch <em>repeat</em> block.</p>"
        );
        const start = document.getElementById("apps-loop-start");
        const step = document.getElementById("apps-loop-step");
        const times = document.getElementById("apps-loop-times");
        const seq = document.getElementById("apps-loop-seq");

        function render() {
            let value = parseInt(start.value, 10) || 0;
            const jump = parseInt(step.value, 10) || 1;
            const n = parseInt(times.value, 10);
            const parts = [value];
            for (let i = 0; i < n; i += 1) {
                value += jump;
                parts.push(value);
            }
            seq.textContent = "repeat " + n + ": " + parts.join(" → ");
        }
        [start, step, times].forEach(function (node) {
            node.addEventListener("input", render);
        });
        render();
    }

    function initVariableBox() {
        const root = document.getElementById("apps-variable-box");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "Score Box Explorer",
            '<p><strong>score</strong> starts at 0. Catch a star or miss a cloud.</p>' +
                '<p id="apps-var-score" style="font-size:42px;font-weight:700;text-align:center;">0</p>' +
                '<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap;">' +
                '<button id="apps-var-star" type="button">Catch star +1</button>' +
                '<button id="apps-var-cloud" type="button">Miss cloud −1</button>' +
                '<button id="apps-var-reset" type="button">Reset</button>' +
                "</div>" +
                '<p id="apps-var-note" style="margin-top:12px;"></p>'
        );
        let score = 0;
        const display = document.getElementById("apps-var-score");
        const note = document.getElementById("apps-var-note");

        function show() {
            display.textContent = String(score);
            note.textContent = "The letter score is a mystery box. The number inside can change, just like n in n + 1 = 8.";
        }
        document.getElementById("apps-var-star").addEventListener("click", function () {
            score += 1;
            show();
        });
        document.getElementById("apps-var-cloud").addEventListener("click", function () {
            score -= 1;
            show();
        });
        document.getElementById("apps-var-reset").addEventListener("click", function () {
            score = 0;
            show();
        });
        show();
    }

    function initFractionBar() {
        const root = document.getElementById("apps-fraction-bar");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "Screen Progress Bar",
            '<label><strong>Filled parts</strong></label><input id="apps-frac-num" type="range" min="0" max="8" value="3" style="width:100%;">' +
                '<label><strong>Equal parts</strong></label><input id="apps-frac-den" type="range" min="2" max="8" value="4" style="width:100%;">' +
                '<div id="apps-frac-bar" style="display:flex;height:48px;border:3px solid #223042;border-radius:10px;overflow:hidden;margin:12px 0;"></div>' +
                '<p id="apps-frac-label" style="font-weight:700;"></p>'
        );
        const num = document.getElementById("apps-frac-num");
        const den = document.getElementById("apps-frac-den");
        const bar = document.getElementById("apps-frac-bar");
        const label = document.getElementById("apps-frac-label");

        function render() {
            let denominator = parseInt(den.value, 10);
            let numerator = parseInt(num.value, 10);
            if (numerator > denominator) {
                numerator = denominator;
                num.value = String(numerator);
            }
            bar.innerHTML = "";
            for (let i = 0; i < denominator; i += 1) {
                const cell = el("div", {
                    style:
                        "flex:1;background:" +
                        (i < numerator ? "#38B8C5" : "#FFF7ED") +
                        ";border-right:1px solid #223042;",
                });
                bar.appendChild(cell);
            }
            label.textContent = numerator + " / " + denominator + " of the screen is filled.";
        }
        num.addEventListener("input", render);
        den.addEventListener("input", render);
        render();
    }

    function initPrimeLock() {
        const root = document.getElementById("apps-prime-lock");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "When Do Two Loops Meet?",
            '<label><strong>Red sprite every</strong></label><input id="apps-lcm-a" type="number" min="2" max="12" value="4" style="width:100%;padding:8px;margin:6px 0 12px;">' +
                '<label><strong>Blue sprite every</strong></label><input id="apps-lcm-b" type="number" min="2" max="12" value="6" style="width:100%;padding:8px;margin:6px 0 12px;">' +
                '<p id="apps-lcm-out" style="font-weight:700;"></p>'
        );
        const a = document.getElementById("apps-lcm-a");
        const b = document.getElementById("apps-lcm-b");
        const out = document.getElementById("apps-lcm-out");

        function lcm(x, y) {
            let m = Math.max(x, y);
            while (m % x !== 0 || m % y !== 0) {
                m += 1;
            }
            return m;
        }

        function render() {
            const x = parseInt(a.value, 10) || 2;
            const y = parseInt(b.value, 10) || 2;
            const meet = lcm(x, y);
            out.textContent = "They first meet again on beat " + meet + ". That number is a multiple of both " + x + " and " + y + ".";
        }
        a.addEventListener("input", render);
        b.addEventListener("input", render);
        render();
    }

    function initMapScale() {
        const root = document.getElementById("apps-map-scale");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "Map Scale Lab",
            '<p>This map uses <strong>1 cm on paper = 100 m outside</strong>.</p>' +
                '<label><strong>Centimetres on the map</strong></label>' +
                '<input id="apps-map-cm" type="range" min="1" max="10" value="3" style="width:100%;">' +
                '<p id="apps-map-out" style="font-size:20px;font-weight:700;"></p>'
        );
        const cm = document.getElementById("apps-map-cm");
        const out = document.getElementById("apps-map-out");

        function render() {
            const paper = parseInt(cm.value, 10);
            const metres = paper * 100;
            out.textContent = paper + " cm on paper → " + metres + " metres to walk. Ratio 1 : 100 stays the same.";
        }
        cm.addEventListener("input", render);
        render();
    }

    function initChanceBits() {
        const root = document.getElementById("apps-chance-bits");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "Coin, Die, and Bit Lights",
            '<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center;">' +
                '<button id="apps-coin" type="button">Flip a coin</button>' +
                '<button id="apps-die" type="button">Roll a die</button>' +
                "</div>" +
                '<p id="apps-chance-out" style="font-weight:700;min-height:48px;margin-top:12px;"></p>' +
                '<p>A coin is 1 of 2. A die face is 1 of 6. A computer bit is also 1 of 2: off or on.</p>'
        );
        const out = document.getElementById("apps-chance-out");
        document.getElementById("apps-coin").addEventListener("click", function () {
            const face = Math.random() < 0.5 ? "heads" : "tails";
            out.textContent = "Coin: " + face + ". Fair chance is 1 out of 2.";
        });
        document.getElementById("apps-die").addEventListener("click", function () {
            const face = 1 + Math.floor(Math.random() * 6);
            out.textContent = "Die: " + face + ". Fair chance for that face is 1 out of 6.";
        });
    }

    function initComboCount() {
        const root = document.getElementById("apps-combo-count");
        if (!root) {
            return;
        }
        root.innerHTML = boxWrap(
            "Character Creator Counter",
            '<label><strong>Hat choices</strong></label><input id="apps-hat" type="range" min="1" max="5" value="2" style="width:100%;">' +
                '<label><strong>Shirt choices</strong></label><input id="apps-shirt" type="range" min="1" max="5" value="3" style="width:100%;">' +
                '<label><strong>Shoe choices</strong></label><input id="apps-shoe" type="range" min="1" max="5" value="2" style="width:100%;">' +
                '<p id="apps-combo-out" style="font-size:20px;font-weight:700;"></p>'
        );
        const hat = document.getElementById("apps-hat");
        const shirt = document.getElementById("apps-shirt");
        const shoe = document.getElementById("apps-shoe");
        const out = document.getElementById("apps-combo-out");

        function render() {
            const h = parseInt(hat.value, 10);
            const s = parseInt(shirt.value, 10);
            const z = parseInt(shoe.value, 10);
            out.textContent = h + " × " + s + " × " + z + " = " + (h * s * z) + " different characters. More choices make a longer list.";
        }
        [hat, shirt, shoe].forEach(function (node) {
            node.addEventListener("input", render);
        });
        render();
    }

    function initAll() {
        initEvenBit();
        initSkipLoop();
        initVariableBox();
        initFractionBar();
        initPrimeLock();
        initMapScale();
        initChanceBits();
        initComboCount();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", initAll);
    } else {
        initAll();
    }
}());

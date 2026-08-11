/**
 * Vietnamese interactive lesson bundle.
 * Activates reusable interactive blocks for Vietnamese lesson pages only.
 */

(function() {
    'use strict';

    const QUESTION_SETS = [
        {
            question: 'Dãy số 4, 8, 12, 16 đang tăng thêm bao nhiêu mỗi bước?',
            choices: ['1', '2', '4'],
            answerIndex: 2,
            explanation: 'Mỗi bước đều cộng thêm 4.'
        },
        {
            question: 'Nếu 3 hộp có 12 chiếc bút như nhau, mỗi hộp có bao nhiêu chiếc bút?',
            choices: ['3', '4', '6'],
            answerIndex: 1,
            explanation: '12 chia đều cho 3 bằng 4.'
        },
        {
            question: 'Phân số nào lớn hơn?',
            choices: ['1/2', '1/4', 'Bằng nhau'],
            answerIndex: 0,
            explanation: 'Cùng một cái bánh thì chia 2 phần cho miếng lớn hơn chia 4 phần.'
        },
        {
            question: 'Số nào là số nguyên tố?',
            choices: ['9', '11', '15'],
            answerIndex: 1,
            explanation: '11 chỉ có hai ước là 1 và 11.'
        },
        {
            question: 'Số tiếp theo của dãy 3, 6, 9, 12 là gì?',
            choices: ['13', '15', '18'],
            answerIndex: 1,
            explanation: 'Mỗi bước cộng thêm 3 nên số tiếp theo là 15.'
        }
    ];

    function escapeHtml(value) {
        return String(value || '')
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    function clamp(value, min, max) {
        return Math.min(max, Math.max(min, value));
    }

    function gcd(a, b) {
        let x = Math.abs(a);
        let y = Math.abs(b);
        while (y !== 0) {
            const temp = x % y;
            x = y;
            y = temp;
        }
        return x || 1;
    }

    function divisors(n) {
        const abs = Math.abs(n);
        if (abs === 0) {
            return [];
        }

        const result = [];
        for (let value = 1; value <= abs; value += 1) {
            if (abs % value === 0) {
                result.push(value);
            }
        }
        return result;
    }

    function ensureStyles() {
        if (document.getElementById('vi-interactive-styles')) {
            return;
        }

        const style = document.createElement('style');
        style.id = 'vi-interactive-styles';
        style.textContent = `
            .vi-card {
                background: #ffffff;
                border: 1px solid #d7e6f5;
                border-radius: 18px;
                box-shadow: 0 16px 30px rgba(15, 76, 129, 0.08);
                overflow: hidden;
            }
            .vi-card__header {
                padding: 1rem 1.25rem 0.75rem;
                background: linear-gradient(135deg, #0f4c81 0%, #1d7cb8 100%);
                color: #ffffff;
            }
            .vi-card__title {
                margin: 0;
                font-size: 1.2rem;
            }
            .vi-card__subtitle {
                margin: 0.35rem 0 0;
                font-size: 0.95rem;
                opacity: 0.95;
            }
            .vi-card__body {
                padding: 1rem 1.25rem 1.25rem;
            }
            .vi-controls,
            .vi-metrics,
            .vi-bars,
            .vi-chip-row,
            .vi-choice-row {
                display: grid;
                gap: 0.75rem;
            }
            .vi-path-graph-shell {
                margin: 0.5rem 0 1rem;
                padding: 0.75rem;
                border: 1px solid #d7e6f5;
                border-radius: 16px;
                background: #fbfdff;
                overflow-x: auto;
            }
            .vi-path-graph {
                width: 100%;
                min-width: 320px;
                height: auto;
                display: block;
            }
            .vi-path-line--branch {
                opacity: 0.82;
                transition: stroke-width 0.15s ease, opacity 0.15s ease;
            }
            .vi-path-line--branch:hover {
                opacity: 1;
                stroke-width: 6;
            }
            .vi-path-line--active {
                opacity: 1;
                stroke-width: 7;
                filter: drop-shadow(0 0 4px rgba(15, 76, 129, 0.35));
            }
            .vi-controls {
                grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
                margin-bottom: 1rem;
            }
            .vi-metrics {
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                margin-top: 1rem;
            }
            .vi-field {
                display: flex;
                flex-direction: column;
                gap: 0.45rem;
                font-size: 0.95rem;
                color: #234864;
            }
            .vi-field__head {
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 0.75rem;
            }
            .vi-field input,
            .vi-field select,
            .vi-button,
            .vi-answer-input {
                font: inherit;
            }
            .vi-field input[type="number"],
            .vi-field select,
            .vi-answer-input {
                padding: 0.7rem 0.8rem;
                border: 1px solid #c5d9ed;
                border-radius: 12px;
                background: #ffffff;
                color: #17364d;
            }
            .vi-field input[type="range"] {
                width: 100%;
                margin: 0;
            }
            .vi-range-shell {
                position: relative;
                padding-top: 2rem;
            }
            .vi-range-badge {
                position: absolute;
                top: 0;
                left: 12px;
                transform: translateX(-50%);
                min-width: 2.75rem;
                padding: 0.2rem 0.55rem;
                border-radius: 999px;
                background: #0f4c81;
                color: #ffffff;
                font-size: 0.82rem;
                font-weight: 700;
                text-align: center;
                box-shadow: 0 8px 18px rgba(15, 76, 129, 0.16);
                pointer-events: none;
            }
            .vi-range-badge::after {
                content: "";
                position: absolute;
                left: 50%;
                bottom: -6px;
                width: 10px;
                height: 10px;
                background: #0f4c81;
                transform: translateX(-50%) rotate(45deg);
            }
            .vi-button,
            .vi-choice {
                border: none;
                border-radius: 12px;
                padding: 0.75rem 1rem;
                background: #0f4c81;
                color: #ffffff;
                cursor: pointer;
                font-weight: 600;
                transition: transform 0.15s ease, opacity 0.15s ease;
            }
            .vi-button:hover,
            .vi-choice:hover {
                transform: translateY(-1px);
                opacity: 0.96;
            }
            .vi-button--secondary,
            .vi-choice--secondary {
                background: #d7e9f8;
                color: #174263;
            }
            .vi-metric {
                padding: 0.9rem;
                border-radius: 14px;
                background: #f5f9fd;
                border: 1px solid #dbeaf7;
            }
            .vi-metric__label {
                display: block;
                color: #4e6d86;
                font-size: 0.85rem;
            }
            .vi-metric__value {
                display: block;
                margin-top: 0.25rem;
                font-size: 1.15rem;
                font-weight: 700;
                color: #143c58;
            }
            .vi-output,
            .vi-note {
                margin-top: 1rem;
                padding: 1rem;
                border-radius: 14px;
                background: #f5f9fd;
                border: 1px solid #dbeaf7;
                color: #17364d;
                line-height: 1.6;
            }
            .vi-dot-grid {
                display: flex;
                flex-wrap: wrap;
                gap: 0.45rem;
                margin-top: 1rem;
            }
            .vi-dot {
                width: 18px;
                height: 18px;
                border-radius: 999px;
                background: #1d7cb8;
            }
            .vi-dot--muted {
                background: #a3c8e3;
            }
            .vi-chip-row {
                grid-template-columns: repeat(auto-fit, minmax(68px, max-content));
                align-items: start;
            }
            .vi-chip {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.45rem 0.75rem;
                border-radius: 999px;
                background: #eef6fd;
                border: 1px solid #cddff0;
                color: #184564;
                font-size: 0.92rem;
                min-width: 52px;
            }
            .vi-bar-list {
                display: grid;
                gap: 0.7rem;
                margin-top: 1rem;
            }
            .vi-bar-row {
                display: grid;
                grid-template-columns: 72px 1fr 64px;
                align-items: center;
                gap: 0.6rem;
            }
            .vi-bar-track {
                height: 14px;
                border-radius: 999px;
                background: #dcebf8;
                overflow: hidden;
            }
            .vi-bar-fill {
                height: 100%;
                border-radius: 999px;
                background: linear-gradient(90deg, #1d7cb8 0%, #4fb3ff 100%);
            }
            .vi-segments {
                display: grid;
                grid-auto-flow: column;
                gap: 0.35rem;
                margin-top: 1rem;
            }
            .vi-segment {
                min-height: 34px;
                border-radius: 10px;
                border: 1px solid #c6dbee;
                background: #f4f9fd;
            }
            .vi-segment--active {
                background: linear-gradient(135deg, #21a1df 0%, #0f4c81 100%);
            }
            .vi-array-shell {
                margin-top: 1rem;
                overflow-x: auto;
                padding-bottom: 0.35rem;
            }
            .vi-array-board {
                display: grid;
                gap: 0.5rem;
                justify-content: start;
                width: max-content;
                max-width: 100%;
                margin: 0 auto;
            }
            .vi-array-cell {
                width: 30px;
                height: 30px;
                border-radius: 10px;
                background: linear-gradient(135deg, #77c7f2 0%, #1d7cb8 100%);
                border: 1px solid #8cc6ec;
                box-shadow: 0 4px 10px rgba(29, 124, 184, 0.16);
                position: relative;
            }
            .vi-array-cell--alt {
                background: linear-gradient(135deg, #ffd27a 0%, #ff9f45 100%);
                border-color: #f1be7c;
                box-shadow: 0 4px 10px rgba(255, 159, 69, 0.18);
            }
            .vi-array-cell::after {
                content: "";
                position: absolute;
                inset: 8px;
                border-radius: 999px;
                background: rgba(255, 255, 255, 0.88);
            }
            .vi-array-caption {
                margin-top: 0.75rem;
                color: #315874;
                text-align: center;
                line-height: 1.6;
            }
            .vi-svg {
                width: 100%;
                max-width: 320px;
                display: block;
                margin: 1rem auto;
            }
            .vi-equation {
                font-size: 1.35rem;
                font-weight: 700;
                color: #0f4c81;
                text-align: center;
                margin-bottom: 1rem;
            }
            .vi-choice-row {
                grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
                margin-top: 1rem;
            }
            .vi-feedback {
                margin-top: 1rem;
                padding: 1rem;
                border-radius: 14px;
                background: #eef8f1;
                color: #195a2a;
                border: 1px solid #cfe9d8;
            }
            .vi-feedback--warn {
                background: #fff7ec;
                border-color: #f1debb;
                color: #805417;
            }
            @media (max-width: 640px) {
                .vi-card__body {
                    padding: 1rem;
                }
                .vi-bar-row {
                    grid-template-columns: 64px 1fr 56px;
                }
            }
        `;

        document.head.appendChild(style);
    }

    function cardShell(title, subtitle, bodyHtml) {
        return `
            <div class="vi-card">
                <div class="vi-card__header">
                    <h3 class="vi-card__title">${escapeHtml(title)}</h3>
                    <p class="vi-card__subtitle">${escapeHtml(subtitle)}</p>
                </div>
                <div class="vi-card__body">
                    ${bodyHtml}
                </div>
            </div>
        `;
    }

    function barsHtml(labels, values) {
        const max = Math.max.apply(null, values.concat([1]));
        return `
            <div class="vi-bar-list">
                ${labels.map(function(label, index) {
                    const width = (values[index] / max) * 100;
                    return `
                        <div class="vi-bar-row">
                            <strong>${escapeHtml(label)}</strong>
                            <div class="vi-bar-track">
                                <div class="vi-bar-fill" style="width: ${width}%;"></div>
                            </div>
                            <span>${values[index]}</span>
                        </div>
                    `;
                }).join('')}
            </div>
        `;
    }

    function formatRangeValue(input) {
        const numericValue = Number(input.value);
        if (Number.isNaN(numericValue)) {
            return input.value;
        }

        if (Math.abs(numericValue) >= 1000 || input.step === '1000') {
            return numericValue.toLocaleString('vi-VN');
        }

        if (Number.isInteger(numericValue)) {
            return String(numericValue);
        }

        return numericValue.toLocaleString('vi-VN', {
            maximumFractionDigits: 2
        });
    }

    function refreshRangeBadges(container) {
        if (!container) {
            return;
        }

        container.querySelectorAll('.vi-range-shell').forEach(function(shell) {
            const input = shell.querySelector('input[type="range"]');
            const badge = shell.querySelector('.vi-range-badge');
            if (!input || !badge) {
                return;
            }

            const min = parseFloat(input.min || '0');
            const max = parseFloat(input.max || '100');
            const value = parseFloat(input.value || '0');
            const ratio = max === min ? 0 : (value - min) / (max - min);
            const usableWidth = Math.max(input.clientWidth - 24, 0);
            const offset = 12 + usableWidth * ratio;

            badge.textContent = formatRangeValue(input);
            badge.style.left = `${offset}px`;
        });
    }

    function enhanceRangeInputs(container) {
        if (!container) {
            return;
        }

        container.querySelectorAll('label.vi-field').forEach(function(field) {
            const labelText = field.firstElementChild && field.firstElementChild.tagName === 'SPAN'
                ? field.firstElementChild
                : null;
            if (labelText && !labelText.classList.contains('vi-field__head')) {
                labelText.classList.add('vi-field__head');
            }
        });

        container.querySelectorAll('input[type="range"]').forEach(function(input, index) {
            let shell = input.parentElement;
            if (!shell || !shell.classList.contains('vi-range-shell')) {
                shell = document.createElement('div');
                shell.className = 'vi-range-shell';
                input.parentNode.insertBefore(shell, input);
                shell.appendChild(input);
            }

            let badge = shell.querySelector('.vi-range-badge');
            if (!badge) {
                badge = document.createElement('output');
                badge.className = 'vi-range-badge';
                badge.setAttribute('aria-hidden', 'true');
                shell.insertBefore(badge, input);
            }

            if (!input.id) {
                input.id = `vi-range-${container.dataset.viTemplate || 'lesson'}-${index}`;
            }
            badge.htmlFor = input.id;
        });

        if (container.dataset.viRangeBound !== 'true') {
            container.addEventListener('input', function() {
                refreshRangeBadges(container);
            });
            window.addEventListener('resize', function() {
                refreshRangeBadges(container);
            });
            container.dataset.viRangeBound = 'true';
        }

        window.requestAnimationFrame(function() {
            refreshRangeBadges(container);
        });
    }

    function renderPathOrCountLab(container) {
        container.innerHTML = cardShell(
            'Đồ thị đường đi',
            'Chỉ đi một đường: hoặc đường A hoặc đường B. Mỗi lối nhỏ là một cách — tổng số lối bằng phép cộng.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Đường A — số lối nhỏ</span>
                        <input class="vi-paths-a" type="range" min="1" max="6" value="2" />
                    </label>
                    <label class="vi-field">
                        <span>Đường B — số lối nhỏ</span>
                        <input class="vi-paths-b" type="range" min="1" max="6" value="3" />
                    </label>
                </div>
                <div class="vi-path-graph-shell" aria-live="polite"></div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const pathsAInput = container.querySelector('.vi-paths-a');
        const pathsBInput = container.querySelector('.vi-paths-b');
        const graphShell = container.querySelector('.vi-path-graph-shell');
        const output = container.querySelector('.vi-output');
        let activePathId = '';

        function yForIndex(index, count, top, bottom) {
            if (count === 1) {
                return (top + bottom) / 2;
            }
            return top + ((bottom - top) * index) / (count - 1);
        }

        function buildGraph(countA, countB) {
            const width = 500;
            const height = 220;
            const homeX = 42;
            const forkX = 130;
            const mergeX = 360;
            const schoolX = 458;
            const midY = height / 2;
            const paths = [];
            let svgPaths = '';

            svgPaths += `<line x1="${homeX + 14}" y1="${midY}" x2="${forkX}" y2="${midY}" class="vi-path-line vi-path-line--trunk" data-path-id="trunk"></line>`;
            svgPaths += `<circle cx="${homeX}" cy="${midY}" r="16" fill="#8dd0f5" stroke="#0f4c81" stroke-width="3"></circle>`;
            svgPaths += `<text x="${homeX}" y="${midY + 4}" text-anchor="middle" font-size="11" fill="#17364d">Nhà</text>`;
            svgPaths += `<circle cx="${schoolX}" cy="${midY}" r="16" fill="#ffe8d6" stroke="#0f4c81" stroke-width="3"></circle>`;
            svgPaths += `<text x="${schoolX}" y="${midY + 4}" text-anchor="middle" font-size="11" fill="#17364d">Trường</text>`;
            svgPaths += `<text x="${forkX + 8}" y="28" font-size="12" fill="#1d7cb8" font-weight="700">Đường A</text>`;
            svgPaths += `<text x="${forkX + 8}" y="${height - 18}" font-size="12" fill="#ff7b54" font-weight="700">Đường B</text>`;

            for (let index = 0; index < countA; index += 1) {
                const y = yForIndex(index, countA, 42, midY - 18);
                const pathId = `a-${index + 1}`;
                paths.push({
                    id: pathId,
                    label: `A${index + 1}`,
                    group: 'A',
                    labelY: y,
                    d: `M ${forkX} ${midY} L ${forkX + 24} ${y} L ${mergeX} ${y} L ${schoolX - 16} ${midY}`
                });
            }

            for (let index = 0; index < countB; index += 1) {
                const y = yForIndex(index, countB, midY + 18, height - 42);
                const pathId = `b-${index + 1}`;
                paths.push({
                    id: pathId,
                    label: `B${index + 1}`,
                    group: 'B',
                    labelY: y,
                    d: `M ${forkX} ${midY} L ${forkX + 24} ${y} L ${mergeX} ${y} L ${schoolX - 16} ${midY}`
                });
            }

            paths.forEach(function(path) {
                const tone = path.group === 'A' ? '#1d7cb8' : '#ff7b54';
                const active = activePathId === path.id ? ' vi-path-line--active' : '';
                svgPaths += `<path d="${path.d}" class="vi-path-line vi-path-line--branch${active}" data-path-id="${path.id}" data-path-group="${path.group}" stroke="${tone}" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"></path>`;
                svgPaths += `<text x="${mergeX + 12}" y="${path.labelY + 4}" font-size="11" fill="#17364d">${path.label}</text>`;
            });

            graphShell.innerHTML = `
                <svg class="vi-path-graph" viewBox="0 0 ${width} ${height}" role="img" aria-label="Đồ thị đường đi từ nhà đến trường">
                    ${svgPaths}
                </svg>
            `;

            graphShell.querySelectorAll('.vi-path-line--branch').forEach(function(line) {
                line.style.cursor = 'pointer';
                line.addEventListener('click', function() {
                    activePathId = line.dataset.pathId;
                    update();
                });
            });

            return paths;
        }

        function update() {
            const countA = parseInt(pathsAInput.value, 10);
            const countB = parseInt(pathsBInput.value, 10);
            const total = countA + countB;
            const paths = buildGraph(countA, countB);
            const active = paths.find(function(item) {
                return item.id === activePathId;
            });

            const listHtml = paths.map(function(path) {
                return `<span class="vi-chip" style="background:${path.group === 'A' ? '#d9ecfb' : '#ffe8d6'};">${path.label}</span>`;
            }).join('');

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Lối đường A</span>
                        <span class="vi-metric__value">${countA}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Lối đường B</span>
                        <span class="vi-metric__value">${countB}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Tổng lối đi</span>
                        <span class="vi-metric__value">${total}</span>
                    </div>
                </div>
                <p class="vi-note">
                    Em chọn <strong>hoặc</strong> một lối thuộc đường A <strong>hoặc</strong> một lối thuộc đường B,
                    nên tổng số cách là <strong>${countA} + ${countB} = ${total}</strong> (nguyên lý cộng).
                </p>
                <div class="vi-chip-row">${listHtml}</div>
                <p class="vi-note">${active
                    ? `Em đang chọn lối <strong>${active.label}</strong> thuộc đường <strong>${active.group}</strong>.`
                    : 'Em hãy bấm một đường trên sơ đồ để tô sáng lối đi đó.'}</p>
            `;
        }

        pathsAInput.addEventListener('input', function() {
            activePathId = '';
            update();
        });
        pathsBInput.addEventListener('input', function() {
            activePathId = '';
            update();
        });
        update();
    }

    function renderPathAndCountLab(container) {
        container.innerHTML = cardShell(
            'Đồ thị hai bước — Nguyên lý nhân',
            'Em chọn áo rồi chọn quần (hai bước liên tiếp). Mỗi cặp áo–quần là một đường đi — tổng số đường bằng phép nhân.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Bước 1 — số áo</span>
                        <input class="vi-step-a" type="range" min="1" max="5" value="3" />
                    </label>
                    <label class="vi-field">
                        <span>Bước 2 — số quần</span>
                        <input class="vi-step-b" type="range" min="1" max="5" value="2" />
                    </label>
                </div>
                <div class="vi-path-graph-shell" aria-live="polite"></div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const stepAInput = container.querySelector('.vi-step-a');
        const stepBInput = container.querySelector('.vi-step-b');
        const graphShell = container.querySelector('.vi-path-graph-shell');
        const output = container.querySelector('.vi-output');
        let activePathId = '';

        function yForIndex(index, count, top, bottom) {
            if (count === 1) {
                return (top + bottom) / 2;
            }
            return top + ((bottom - top) * index) / (count - 1);
        }

        function buildGraph(countA, countB) {
            const width = 520;
            const height = Math.max(200, 56 + countA * countB * 6);
            const cappedHeight = Math.min(height, 280);
            const homeX = 42;
            const shirtX = 145;
            const pantX = 310;
            const schoolX = 468;
            const midY = cappedHeight / 2;
            const paths = [];
            let svgPaths = '';

            svgPaths += `<circle cx="${homeX}" cy="${midY}" r="16" fill="#8dd0f5" stroke="#0f4c81" stroke-width="3"></circle>`;
            svgPaths += `<text x="${homeX}" y="${midY + 4}" text-anchor="middle" font-size="11" fill="#17364d">Nhà</text>`;
            svgPaths += `<circle cx="${schoolX}" cy="${midY}" r="16" fill="#ffe8d6" stroke="#0f4c81" stroke-width="3"></circle>`;
            svgPaths += `<text x="${schoolX}" y="${midY + 4}" text-anchor="middle" font-size="11" fill="#17364d">Trường</text>`;
            svgPaths += `<text x="${shirtX - 18}" y="24" font-size="12" fill="#1d7cb8" font-weight="700">Bước 1: áo</text>`;
            svgPaths += `<text x="${pantX - 24}" y="24" font-size="12" fill="#6b4bb8" font-weight="700">Bước 2: quần</text>`;
            svgPaths += `<line x1="${homeX + 16}" y1="${midY}" x2="${shirtX - 20}" y2="${midY}" stroke="#94a3b8" stroke-width="3" stroke-dasharray="6 4"></line>`;

            for (let shirt = 0; shirt < countA; shirt += 1) {
                const shirtY = yForIndex(shirt, countA, 42, cappedHeight - 42);
                svgPaths += `<circle cx="${shirtX}" cy="${shirtY}" r="10" fill="#d9ecfb" stroke="#1d7cb8" stroke-width="2"></circle>`;
                svgPaths += `<text x="${shirtX}" y="${shirtY + 4}" text-anchor="middle" font-size="10" fill="#17364d">Á${shirt + 1}</text>`;

                for (let pant = 0; pant < countB; pant += 1) {
                    const spread = Math.min(36, 12 + countB * 4);
                    const pantY = shirtY + (pant - (countB - 1) / 2) * (spread / Math.max(countB - 1, 1));
                    const pathId = `s${shirt + 1}-p${pant + 1}`;
                    const active = activePathId === pathId ? ' vi-path-line--active' : '';
                    const tone = shirt % 2 === 0 ? '#1d7cb8' : '#4f86c6';
                    const d = `M ${shirtX + 10} ${shirtY} L ${pantX - 14} ${pantY} L ${schoolX - 16} ${midY}`;
                    paths.push({
                        id: pathId,
                        label: `Á${shirt + 1}·Q${pant + 1}`,
                        shirt: shirt + 1,
                        pant: pant + 1,
                        d: d
                    });
                    svgPaths += `<path d="${d}" class="vi-path-line vi-path-line--branch${active}" data-path-id="${pathId}" stroke="${tone}" fill="none" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"></path>`;
                    svgPaths += `<circle cx="${pantX}" cy="${pantY}" r="7" fill="#ebe4ff" stroke="#6b4bb8" stroke-width="2"></circle>`;
                }
            }

            graphShell.innerHTML = `
                <svg class="vi-path-graph" viewBox="0 0 ${width} ${cappedHeight}" role="img" aria-label="Đồ thị hai bước chọn áo rồi chọn quần">
                    ${svgPaths}
                </svg>
            `;

            graphShell.querySelectorAll('.vi-path-line--branch').forEach(function(line) {
                line.style.cursor = 'pointer';
                line.addEventListener('click', function() {
                    activePathId = line.dataset.pathId;
                    update();
                });
            });

            return paths;
        }

        function update() {
            const countA = parseInt(stepAInput.value, 10);
            const countB = parseInt(stepBInput.value, 10);
            const total = countA * countB;
            const paths = buildGraph(countA, countB);
            const active = paths.find(function(item) {
                return item.id === activePathId;
            });

            const listHtml = paths.map(function(path) {
                return `<span class="vi-chip" style="background:#eef6fd;">${path.label}</span>`;
            }).join('');

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Số áo (bước 1)</span>
                        <span class="vi-metric__value">${countA}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Số quần (bước 2)</span>
                        <span class="vi-metric__value">${countB}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Tổng bộ đồ</span>
                        <span class="vi-metric__value">${total}</span>
                    </div>
                </div>
                <p class="vi-note">
                    Em chọn <strong>một áo</strong> rồi <strong>một quần</strong> — hai bước nối tiếp.
                    Mỗi áo ghép với mọi quần nên có <strong>${countA} × ${countB} = ${total}</strong> đường đi (nguyên lý nhân).
                </p>
                <div class="vi-chip-row">${listHtml}</div>
                <p class="vi-note">${active
                    ? `Em đang xem đường <strong>${active.label}</strong> (áo ${active.shirt}, quần ${active.pant}).`
                    : 'Em hãy bấm một đường trên sơ đồ để tô sáng bộ áo–quần đó.'}</p>
            `;
        }

        stepAInput.addEventListener('input', function() {
            activePathId = '';
            update();
        });
        stepBInput.addEventListener('input', function() {
            activePathId = '';
            update();
        });
        update();
    }

    function renderOrCountLab(container) {
        container.innerHTML = cardShell(
            'Trạm chọn HOẶC — Nguyên lý cộng',
            'Em chỉ chọn một nhóm (súp hoặc salad, đường A hoặc đường B). Đổi số lựa chọn rồi cộng hai nhóm.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Nhóm A — số lựa chọn (ví dụ: súp)</span>
                        <input class="vi-group-a" type="range" min="1" max="10" value="2" />
                    </label>
                    <label class="vi-field">
                        <span>Nhóm B — số lựa chọn (ví dụ: salad)</span>
                        <input class="vi-group-b" type="range" min="1" max="10" value="3" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const groupAInput = container.querySelector('.vi-group-a');
        const groupBInput = container.querySelector('.vi-group-b');
        const output = container.querySelector('.vi-output');

        function renderChips(count, label, tone) {
            const chips = Array.from({ length: count }, function(_, index) {
                return `<span class="vi-chip" style="background:${tone}; color:#17364d; border-color:#cddff0;">${label} ${index + 1}</span>`;
            }).join('');
            return `<div class="vi-chip-row">${chips}</div>`;
        }

        function update() {
            const countA = parseInt(groupAInput.value, 10);
            const countB = parseInt(groupBInput.value, 10);
            const total = countA + countB;

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Nhóm A</span>
                        <span class="vi-metric__value">${countA}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Nhóm B</span>
                        <span class="vi-metric__value">${countB}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Tổng cách chọn</span>
                        <span class="vi-metric__value">${total}</span>
                    </div>
                </div>
                <p class="vi-note">
                    Vì em chỉ chọn <strong>một</strong> món trong <strong>hai nhóm loại trừ nhau</strong>,
                    ta <strong>cộng</strong>: <strong>${countA} + ${countB} = ${total}</strong> cách.
                    Đây là <strong>nguyên lý cộng</strong> (chọn HOẶC A HOẶC B).
                </p>
                <div>
                    <strong>Nhóm A</strong>
                    ${renderChips(countA, 'A', '#d9ecfb')}
                </div>
                <div style="margin-top:0.75rem;">
                    <strong>hoặc</strong>
                </div>
                <div style="margin-top:0.75rem;">
                    <strong>Nhóm B</strong>
                    ${renderChips(countB, 'B', '#ffe8d6')}
                </div>
                <p class="vi-note" style="margin-top:0.75rem;">
                    Không nhân ${countA} × ${countB} vì em không chọn cùng lúc một món A và một món B trong bài này.
                </p>
            `;
        }

        groupAInput.addEventListener('input', update);
        groupBInput.addEventListener('input', update);
        update();
    }

    function renderNumberLab(container, mode, options) {
        if (mode === 'path-or-count') {
            renderPathOrCountLab(container);
            return;
        }
        if (mode === 'path-and-count') {
            renderPathAndCountLab(container);
            return;
        }
        if (mode === 'or-count') {
            renderOrCountLab(container);
            return;
        }

        const config = options || {};
        const isSigned = mode === 'signed';
        const min = typeof config.min === 'number' ? config.min : (isSigned ? -20 : 0);
        const max = typeof config.max === 'number' ? config.max : (mode === 'square' ? 50 : 100);
        const startValue = typeof config.startValue === 'number' ? config.startValue : (isSigned ? -4 : 12);

        container.innerHTML = cardShell(
            config.cardTitle || 'Máy soi con số',
            config.subtitle || 'Thử nhiều giá trị rồi quan sát quy luật của số.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Chọn số</span>
                        <input class="vi-number-input" type="number" min="${min}" max="${max}" value="${startValue}" />
                    </label>
                    <label class="vi-field">
                        <span>Kéo nhanh</span>
                        <input class="vi-range-input" type="range" min="${min}" max="${max}" value="${startValue}" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const numberInput = container.querySelector('.vi-number-input');
        const rangeInput = container.querySelector('.vi-range-input');
        const output = container.querySelector('.vi-output');

        function sync(value) {
            numberInput.value = value;
            rangeInput.value = value;
        }

        function renderDots(total) {
            const count = clamp(Math.abs(total), 0, 24);
            return `
                <div class="vi-dot-grid">
                    ${Array.from({ length: count }, function(_, index) {
                        return `<span class="vi-dot${index % 2 === 1 ? ' vi-dot--muted' : ''}"></span>`;
                    }).join('')}
                </div>
            `;
        }

        function update() {
            const parsed = parseInt(numberInput.value, 10);
            const value = clamp(Number.isNaN(parsed) ? startValue : parsed, min, max);
            sync(value);

            const factorValues = divisors(value);
            const factorHtml = factorValues.length
                ? factorValues.map(function(item) {
                    return `<span class="vi-chip">${item}</span>`;
                }).join('')
                : '<span class="vi-chip">mọi số</span>';

            let summary = '';
            if (mode === 'prime') {
                const prime = value > 1 && factorValues.length === 2;
                summary = prime
                    ? `${value} là số nguyên tố vì chỉ có hai ước là 1 và ${value}.`
                    : `${value} chưa phải số nguyên tố vì có nhiều hơn hai ước số hoặc nhỏ hơn 2.`;
            } else if (mode === 'square') {
                const root = Math.sqrt(Math.abs(value));
                const perfect = Number.isInteger(root);
                summary = perfect
                    ? `${value} là số chính phương vì ${root} × ${root} = ${value}.`
                    : `${value} chưa phải số chính phương. Em thử tìm hai số giống nhau nhân với nhau xem có ra ${value} không nhé.`;
            } else if (mode === 'signed') {
                if (value === 0) {
                    summary = '0 là điểm mốc ở giữa trục số: không dương và cũng không âm.';
                } else if (value > 0) {
                    summary = `${value} là số dương vì nằm bên phải số 0 trên trục số.`;
                } else {
                    summary = `${value} là số âm vì nằm bên trái số 0 trên trục số.`;
                }
            } else {
                const even = value % 2 === 0;
                summary = even
                    ? `${value} ghép thành từng cặp đều nhau nên là số chẵn.`
                    : `${value} luôn còn thừa 1 khi ghép cặp nên là số lẻ.`;
            }

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Giá trị đang xét</span>
                        <span class="vi-metric__value">${value}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Phân loại nhanh</span>
                        <span class="vi-metric__value">${
                            mode === 'signed'
                                ? (value === 0 ? 'Mốc 0' : (value > 0 ? 'Số dương' : 'Số âm'))
                                : (value % 2 === 0 ? 'Số chẵn' : 'Số lẻ')
                        }</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Số ước</span>
                        <span class="vi-metric__value">${factorValues.length || '∞'}</span>
                    </div>
                </div>
                <p class="vi-note">${summary}</p>
                <div>
                    <strong>Các ước dễ thấy:</strong>
                    <div class="vi-chip-row">${factorHtml}</div>
                </div>
                ${renderDots(value)}
            `;
        }

        numberInput.addEventListener('input', update);
        rangeInput.addEventListener('input', function() {
            numberInput.value = rangeInput.value;
            update();
        });

        update();
    }

    function renderArrayLab(container, mode) {
        if (mode === 'multiplication') {
            container.innerHTML = cardShell(
                'Trạm xếp hàng và cột',
                'Kéo thanh trượt để nhìn phép nhân như một sơ đồ đồ vật được xếp theo hàng và cột.',
                `
                    <div class="vi-controls">
                        <label class="vi-field">
                            <span>Số hàng</span>
                            <input class="vi-rows" type="range" min="1" max="6" value="3" />
                        </label>
                        <label class="vi-field">
                            <span>Số cột</span>
                            <input class="vi-columns" type="range" min="1" max="8" value="4" />
                        </label>
                    </div>
                    <div class="vi-output" aria-live="polite"></div>
                `
            );

            const rowsInput = container.querySelector('.vi-rows');
            const columnsInput = container.querySelector('.vi-columns');
            const output = container.querySelector('.vi-output');

            function updateMultiplication() {
                const rows = parseInt(rowsInput.value, 10);
                const columns = parseInt(columnsInput.value, 10);
                const total = rows * columns;
                const repeatedAddition = Array.from({ length: rows }, function() {
                    return columns;
                }).join(' + ');
                const board = Array.from({ length: total }, function(_, index) {
                    const rowIndex = Math.floor(index / columns);
                    return `<span class="vi-array-cell${rowIndex % 2 === 1 ? ' vi-array-cell--alt' : ''}"></span>`;
                }).join('');

                output.innerHTML = `
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Số hàng</span>
                            <span class="vi-metric__value">${rows}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Số cột</span>
                            <span class="vi-metric__value">${columns}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Tổng số đồ vật</span>
                            <span class="vi-metric__value">${total}</span>
                        </div>
                    </div>
                    <p class="vi-note">
                        Có <strong>${rows}</strong> hàng và <strong>${columns}</strong> cột nên
                        <strong>${rows} × ${columns} = ${total}</strong>.
                        Nếu em nhìn theo cột trước thì cũng thấy <strong>${columns} × ${rows} = ${total}</strong>.
                    </p>
                    <div class="vi-chip-row">
                        ${Array.from({ length: rows }, function() {
                            return `<span class="vi-chip">${columns}</span>`;
                        }).join('')}
                    </div>
                    <p class="vi-array-caption">${repeatedAddition} = ${total}</p>
                    <div class="vi-array-shell">
                        <div class="vi-array-board" style="grid-template-columns: repeat(${columns}, 30px);">
                            ${board}
                        </div>
                    </div>
                    <p class="vi-array-caption">Mỗi ô là 1 đồ vật. Đổi số hàng hoặc số cột để xem tích thay đổi ngay trên sơ đồ.</p>
                `;
            }

            rowsInput.addEventListener('input', updateMultiplication);
            columnsInput.addEventListener('input', updateMultiplication);
            updateMultiplication();
            return;
        }

        container.innerHTML = cardShell(
            'Bảng xếp nhóm',
            'Đổi số lượng và cách xếp để xem phép nhân, phép chia và phần dư.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Tổng số đồ vật</span>
                        <input class="vi-total" type="range" min="1" max="48" value="18" />
                    </label>
                    <label class="vi-field">
                        <span>Số đồ vật trong mỗi hàng</span>
                        <input class="vi-group" type="range" min="1" max="12" value="3" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const totalInput = container.querySelector('.vi-total');
        const groupInput = container.querySelector('.vi-group');
        const output = container.querySelector('.vi-output');

        function update() {
            const total = parseInt(totalInput.value, 10);
            const group = parseInt(groupInput.value, 10);
            const rows = Math.floor(total / group);
            const remainder = total % group;
            const grid = Array.from({ length: total }, function(_, index) {
                const active = index < rows * group;
                return `<span class="vi-dot${active ? '' : ' vi-dot--muted'}"></span>`;
            }).join('');

            let summary = `${total} = ${group} × ${rows}`;
            if (remainder > 0) {
                summary += ` và còn dư ${remainder}.`;
            } else {
                summary += '. Không còn dư nên em có một phép chia hết.';
            }

            if (mode === 'factors' && remainder === 0) {
                summary = `${group} là một ước của ${total} vì xếp được ${rows} hàng bằng nhau.`;
            }

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Số hàng đầy đủ</span>
                        <span class="vi-metric__value">${rows}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Phần dư</span>
                        <span class="vi-metric__value">${remainder}</span>
                    </div>
                </div>
                <p class="vi-note">${summary}</p>
                <div class="vi-dot-grid">${grid}</div>
            `;
        }

        totalInput.addEventListener('input', update);
        groupInput.addEventListener('input', update);
        update();
    }

    function renderFractionLab(container, mode) {
        container.innerHTML = cardShell(
            'Xưởng phân số',
            'Tô màu từng phần để nhìn thấy phân số, số thập phân và phần trăm.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>${mode === 'probability' ? 'Số kết quả thuận lợi' : 'Số phần được tô'}</span>
                        <input class="vi-numerator" type="range" min="0" max="4" value="2" />
                    </label>
                    <label class="vi-field">
                        <span>${mode === 'probability' ? 'Tổng số kết quả' : 'Tổng số phần bằng nhau'}</span>
                        <input class="vi-denominator" type="range" min="2" max="10" value="4" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const numeratorInput = container.querySelector('.vi-numerator');
        const denominatorInput = container.querySelector('.vi-denominator');
        const output = container.querySelector('.vi-output');

        function update() {
            const denominator = parseInt(denominatorInput.value, 10);
            numeratorInput.max = denominator;
            if (parseInt(numeratorInput.value, 10) > denominator) {
                numeratorInput.value = denominator;
            }

            const numerator = parseInt(numeratorInput.value, 10);
            const decimal = numerator / denominator;
            const percent = Math.round(decimal * 100);
            const simple = gcd(numerator, denominator);
            const reduced = `${numerator / simple}/${denominator / simple}`;

            let note = `Phân số đang tạo là ${numerator}/${denominator}.`;
            if (mode === 'decimal') {
                note += ` Viết dưới dạng số thập phân là ${decimal.toFixed(2)}.`;
            } else if (mode === 'percent') {
                note += ` Đổi sang phần trăm được ${percent}%.`;
            } else if (mode === 'equivalent') {
                note += ` Dạng rút gọn là ${reduced}.`;
            } else if (mode === 'probability') {
                note += ` Nếu thử rất nhiều lần, em có thể mong đợi khoảng ${percent}% kết quả thuận lợi.`;
            } else {
                note += ` Dạng rút gọn là ${reduced}.`;
            }

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Phân số</span>
                        <span class="vi-metric__value">${numerator}/${denominator}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Số thập phân</span>
                        <span class="vi-metric__value">${decimal.toFixed(2)}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Phần trăm</span>
                        <span class="vi-metric__value">${percent}%</span>
                    </div>
                </div>
                <div class="vi-segments">
                    ${Array.from({ length: denominator }, function(_, index) {
                        return `<span class="vi-segment${index < numerator ? ' vi-segment--active' : ''}"></span>`;
                    }).join('')}
                </div>
                <p class="vi-note">${note}</p>
            `;
        }

        numeratorInput.addEventListener('input', update);
        denominatorInput.addEventListener('input', update);
        update();
    }

    function renderMeasurementLab(container, mode) {
        let body = '';
        if (mode === 'time') {
            body = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Giờ</span>
                        <input class="vi-hours" type="range" min="0" max="12" value="2" />
                    </label>
                    <label class="vi-field">
                        <span>Phút</span>
                        <input class="vi-minutes" type="range" min="0" max="55" step="5" value="30" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `;
        } else if (mode === 'money') {
            body = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Số tiền (đồng)</span>
                        <input class="vi-amount" type="range" min="1000" max="200000" step="1000" value="56000" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `;
        } else if (mode === 'ratio') {
            body = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Lượng A</span>
                        <input class="vi-a" type="range" min="1" max="24" value="6" />
                    </label>
                    <label class="vi-field">
                        <span>Lượng B</span>
                        <input class="vi-b" type="range" min="1" max="24" value="9" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `;
        } else {
            body = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Độ dài (cm)</span>
                        <input class="vi-length" type="range" min="10" max="500" value="125" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `;
        }

        container.innerHTML = cardShell(
            'Phòng đo lường',
            'Đổi đơn vị hoặc thay đổi đại lượng để thấy các con số liên hệ với nhau.',
            body
        );

        const output = container.querySelector('.vi-output');

        function update() {
            if (mode === 'time') {
                const hours = parseInt(container.querySelector('.vi-hours').value, 10);
                const minutes = parseInt(container.querySelector('.vi-minutes').value, 10);
                const totalMinutes = hours * 60 + minutes;
                const totalSeconds = totalMinutes * 60;

                output.innerHTML = `
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Thời gian đang chọn</span>
                            <span class="vi-metric__value">${hours} giờ ${minutes} phút</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Tổng số phút</span>
                            <span class="vi-metric__value">${totalMinutes}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Tổng số giây</span>
                            <span class="vi-metric__value">${totalSeconds}</span>
                        </div>
                    </div>
                    <p class="vi-note">Khi đổi đơn vị, giá trị đo không đổi. Chỉ có cách viết thay đổi thôi.</p>
                `;
                return;
            }

            if (mode === 'money') {
                const amount = parseInt(container.querySelector('.vi-amount').value, 10);
                const notes = [50000, 20000, 10000, 5000, 2000, 1000];
                let remaining = amount;
                const breakdown = notes.map(function(note) {
                    const count = Math.floor(remaining / note);
                    remaining -= count * note;
                    return { note: note, count: count };
                }).filter(function(item) {
                    return item.count > 0;
                });

                output.innerHTML = `
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Số tiền</span>
                            <span class="vi-metric__value">${amount.toLocaleString('vi-VN')}đ</span>
                        </div>
                    </div>
                    <div class="vi-chip-row">
                        ${breakdown.map(function(item) {
                            return `<span class="vi-chip">${item.count} × ${item.note.toLocaleString('vi-VN')}đ</span>`;
                        }).join('')}
                    </div>
                    <p class="vi-note">Em có thể cộng các tờ tiền lại để kiểm tra tổng tiền nhận được.</p>
                `;
                return;
            }

            if (mode === 'ratio') {
                const a = parseInt(container.querySelector('.vi-a').value, 10);
                const b = parseInt(container.querySelector('.vi-b').value, 10);
                const factor = gcd(a, b);

                output.innerHTML = `
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Tỉ số A:B</span>
                            <span class="vi-metric__value">${a}:${b}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Dạng rút gọn</span>
                            <span class="vi-metric__value">${a / factor}:${b / factor}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Tổng hai lượng</span>
                            <span class="vi-metric__value">${a + b}</span>
                        </div>
                    </div>
                    <p class="vi-note">Nếu cùng nhân cả hai số với 2, 3 hoặc 4 thì em sẽ được các tỉ lệ tương đương.</p>
                `;
                return;
            }

            const length = parseInt(container.querySelector('.vi-length').value, 10);
            const meters = Math.floor(length / 100);
            const centimeters = length % 100;

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Độ dài đang xét</span>
                        <span class="vi-metric__value">${length} cm</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Viết theo mét</span>
                        <span class="vi-metric__value">${meters} m ${centimeters} cm</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Viết theo milimét</span>
                        <span class="vi-metric__value">${length * 10} mm</span>
                    </div>
                </div>
                <p class="vi-note">Em hãy thử tăng thêm 10 cm mỗi lần để xem các đơn vị thay đổi như thế nào.</p>
            `;
        }

        container.querySelectorAll('input').forEach(function(input) {
            input.addEventListener('input', update);
        });
        update();
    }

    function renderGeometryLab(container, mode) {
        let controls = '';
        let description = 'Kéo các kích thước để thấy chu vi, diện tích hoặc thể tích thay đổi ra sao.';

        if (mode === 'angle') {
            description = 'Đổi số đo rồi quan sát xem góc thuộc loại nào.';
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Số đo góc</span>
                        <input class="vi-angle" type="range" min="0" max="360" step="1" value="90" />
                    </label>
                </div>
            `;
        } else if (mode === 'triangle') {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Đáy</span>
                        <input class="vi-base" type="range" min="2" max="14" value="8" />
                    </label>
                    <label class="vi-field">
                        <span>Chiều cao</span>
                        <input class="vi-height" type="range" min="2" max="12" value="6" />
                    </label>
                </div>
            `;
        } else if (mode === 'solid') {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Dài</span>
                        <input class="vi-length" type="range" min="2" max="10" value="6" />
                    </label>
                    <label class="vi-field">
                        <span>Rộng</span>
                        <input class="vi-width" type="range" min="2" max="10" value="4" />
                    </label>
                    <label class="vi-field">
                        <span>Cao</span>
                        <input class="vi-height" type="range" min="2" max="10" value="5" />
                    </label>
                </div>
            `;
        } else if (mode === 'circle') {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Bán kính</span>
                        <input class="vi-radius" type="range" min="2" max="10" value="5" />
                    </label>
                </div>
            `;
        } else {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Chiều rộng</span>
                        <input class="vi-width" type="range" min="2" max="14" value="8" />
                    </label>
                    <label class="vi-field">
                        <span>Chiều cao</span>
                        <input class="vi-height" type="range" min="2" max="12" value="5" />
                    </label>
                </div>
            `;
        }

        container.innerHTML = cardShell(
            'Xưởng hình học',
            description,
            controls + '<div class="vi-output" aria-live="polite"></div>'
        );

        const output = container.querySelector('.vi-output');

        function update() {
            if (mode === 'angle') {
                const angle = parseInt(container.querySelector('.vi-angle').value, 10);
                const radians = angle * Math.PI / 180;
                const startX = 110;
                const startY = 120;
                const rayLength = 82;
                const endX = startX + Math.cos(radians) * rayLength;
                const endY = startY - Math.sin(radians) * rayLength;
                let angleType = 'Góc không';
                let note = 'Góc không có số đo bằng 0°.';

                if (angle > 0 && angle < 90) {
                    angleType = 'Góc nhọn';
                    note = 'Góc này lớn hơn 0° và nhỏ hơn 90° nên là góc nhọn.';
                } else if (angle === 90) {
                    angleType = 'Góc vuông';
                    note = 'Góc vuông có số đo đúng bằng 90°.';
                } else if (angle > 90 && angle < 180) {
                    angleType = 'Góc tù';
                    note = 'Góc này lớn hơn 90° nhưng nhỏ hơn 180° nên là góc tù.';
                } else if (angle === 180) {
                    angleType = 'Góc bẹt';
                    note = 'Góc bẹt tạo thành một đường thẳng và có số đo 180°.';
                } else if (angle > 180 && angle < 360) {
                    angleType = 'Góc phản';
                    note = 'Góc này lớn hơn 180° nhưng chưa tròn một vòng nên là góc phản.';
                } else if (angle === 360) {
                    angleType = 'Góc tròn';
                    note = 'Góc tròn quay đủ một vòng và có số đo 360°.';
                }

                output.innerHTML = `
                    <svg class="vi-svg" viewBox="0 0 320 240" aria-hidden="true">
                        <line x1="${startX}" y1="${startY}" x2="${startX + rayLength + 40}" y2="${startY}" stroke="#0f4c81" stroke-width="5" stroke-linecap="round"></line>
                        <line x1="${startX}" y1="${startY}" x2="${endX.toFixed(1)}" y2="${endY.toFixed(1)}" stroke="#1d7cb8" stroke-width="5" stroke-linecap="round"></line>
                        ${renderAngleArc(startX, startY, 34, angle)}
                        <circle cx="${startX}" cy="${startY}" r="6" fill="#17364d"></circle>
                    </svg>
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Số đo góc</span>
                            <span class="vi-metric__value">${angle}°</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Phân loại</span>
                            <span class="vi-metric__value">${angleType}</span>
                        </div>
                    </div>
                    <p class="vi-note">${note}</p>
                `;
                return;
            }

            if (mode === 'triangle') {
                const base = parseInt(container.querySelector('.vi-base').value, 10);
                const height = parseInt(container.querySelector('.vi-height').value, 10);
                const area = (base * height) / 2;

                output.innerHTML = `
                    <svg class="vi-svg" viewBox="0 0 320 220" aria-hidden="true">
                        <polygon points="40,190 280,190 160,${190 - (height * 10)}" fill="#6ec5f3" stroke="#0f4c81" stroke-width="4"></polygon>
                    </svg>
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Đáy</span>
                            <span class="vi-metric__value">${base}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Chiều cao</span>
                            <span class="vi-metric__value">${height}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Diện tích</span>
                            <span class="vi-metric__value">${area}</span>
                        </div>
                    </div>
                    <p class="vi-note">Diện tích tam giác bằng đáy × chiều cao rồi chia 2.</p>
                `;
                return;
            }

            if (mode === 'solid') {
                const length = parseInt(container.querySelector('.vi-length').value, 10);
                const width = parseInt(container.querySelector('.vi-width').value, 10);
                const height = parseInt(container.querySelector('.vi-height').value, 10);
                const volume = length * width * height;

                output.innerHTML = `
                    <svg class="vi-svg" viewBox="0 0 320 220" aria-hidden="true">
                        <polygon points="70,90 220,90 260,60 110,60" fill="#d7ecfb" stroke="#0f4c81" stroke-width="3"></polygon>
                        <polygon points="70,90 70,170 220,170 220,90" fill="#8dd0f5" stroke="#0f4c81" stroke-width="3"></polygon>
                        <polygon points="220,90 220,170 260,140 260,60" fill="#4aa9dd" stroke="#0f4c81" stroke-width="3"></polygon>
                    </svg>
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Kích thước</span>
                            <span class="vi-metric__value">${length} × ${width} × ${height}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Thể tích</span>
                            <span class="vi-metric__value">${volume}</span>
                        </div>
                    </div>
                    <p class="vi-note">Mỗi lần tăng một chiều, em đang thêm một lớp khối hộp mới.</p>
                `;
                return;
            }

            if (mode === 'circle') {
                const radius = parseInt(container.querySelector('.vi-radius').value, 10);
                const area = (Math.PI * radius * radius).toFixed(1);
                const circumference = (2 * Math.PI * radius).toFixed(1);

                output.innerHTML = `
                    <svg class="vi-svg" viewBox="0 0 320 220" aria-hidden="true">
                        <circle cx="160" cy="110" r="${radius * 10}" fill="#a5def8" stroke="#0f4c81" stroke-width="4"></circle>
                        <line x1="160" y1="110" x2="${160 + radius * 10}" y2="110" stroke="#ff7b54" stroke-width="4"></line>
                    </svg>
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Bán kính</span>
                            <span class="vi-metric__value">${radius}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Chu vi</span>
                            <span class="vi-metric__value">${circumference}</span>
                        </div>
                        <div class="vi-metric">
                            <span class="vi-metric__label">Diện tích</span>
                            <span class="vi-metric__value">${area}</span>
                        </div>
                    </div>
                    <p class="vi-note">Khi bán kính lớn hơn, cả chu vi và diện tích đều tăng lên.</p>
                `;
                return;
            }

            const width = parseInt(container.querySelector('.vi-width').value, 10);
            const height = parseInt(container.querySelector('.vi-height').value, 10);
            const area = width * height;
            const perimeter = 2 * (width + height);

            output.innerHTML = `
                <svg class="vi-svg" viewBox="0 0 320 220" aria-hidden="true">
                    <rect x="50" y="40" width="${width * 16}" height="${height * 16}" fill="#8dd0f5" stroke="#0f4c81" stroke-width="4" rx="10"></rect>
                </svg>
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Chiều rộng</span>
                        <span class="vi-metric__value">${width}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Chiều cao</span>
                        <span class="vi-metric__value">${height}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Chu vi</span>
                        <span class="vi-metric__value">${perimeter}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Diện tích</span>
                        <span class="vi-metric__value">${area}</span>
                    </div>
                </div>
                <p class="vi-note">Hãy thử giữ nguyên chiều cao rồi tăng chiều rộng để xem diện tích thay đổi như thế nào.</p>
            `;
        }

        container.querySelectorAll('input').forEach(function(input) {
            input.addEventListener('input', update);
        });
        update();
    }

    function buildAngleArcPath(centerX, centerY, radius, angleInDegrees) {
        if (angleInDegrees <= 0) {
            return '';
        }

        const segments = Math.max(8, Math.ceil(angleInDegrees / 8));
        const points = [];

        for (let step = 0; step <= segments; step += 1) {
            const portion = angleInDegrees * step / segments;
            const radians = portion * Math.PI / 180;
            points.push({
                x: centerX + Math.cos(radians) * radius,
                y: centerY - Math.sin(radians) * radius
            });
        }

        return `M ${points.map(function(point) {
            return `${point.x.toFixed(1)} ${point.y.toFixed(1)}`;
        }).join(' L ')}`;
    }

    function renderAngleArc(centerX, centerY, radius, angleInDegrees) {
        if (angleInDegrees === 360) {
            return `<circle cx="${centerX}" cy="${centerY}" r="${radius}" fill="none" stroke="#ff7b54" stroke-width="4"></circle>`;
        }

        const pathData = buildAngleArcPath(centerX, centerY, radius, angleInDegrees);

        if (!pathData) {
            return '';
        }

        return `<path d="${pathData}" fill="none" stroke="#ff7b54" stroke-width="4"></path>`;
    }

    function renderDataLab(container, mode) {
        if (mode === 'probability') {
            container.innerHTML = cardShell(
                'Phòng thí nghiệm xác suất',
                'Mô phỏng nhiều lần rồi so sánh kết quả thật với điều em dự đoán.',
                `
                    <div class="vi-controls">
                        <label class="vi-field">
                            <span>Thí nghiệm</span>
                            <select class="vi-experiment">
                                <option value="coin">Đồng xu</option>
                                <option value="dice">Xúc xắc</option>
                                <option value="spinner">Vòng quay 4 màu</option>
                            </select>
                        </label>
                        <label class="vi-field">
                            <span>Số lần thử</span>
                            <input class="vi-trials" type="range" min="10" max="120" step="10" value="40" />
                        </label>
                    </div>
                    <button class="vi-button" type="button">Mô phỏng</button>
                    <div class="vi-output" aria-live="polite"></div>
                `
            );

            const experimentInput = container.querySelector('.vi-experiment');
            const trialsInput = container.querySelector('.vi-trials');
            const button = container.querySelector('.vi-button');
            const output = container.querySelector('.vi-output');

            function runSimulation() {
                const experiment = experimentInput.value;
                const trials = parseInt(trialsInput.value, 10);
                let labels;
                let counts;

                if (experiment === 'coin') {
                    labels = ['Ngửa', 'Sấp'];
                    counts = [0, 0];
                    for (let i = 0; i < trials; i += 1) {
                        counts[Math.random() < 0.5 ? 0 : 1] += 1;
                    }
                } else if (experiment === 'dice') {
                    labels = ['1', '2', '3', '4', '5', '6'];
                    counts = [0, 0, 0, 0, 0, 0];
                    for (let i = 0; i < trials; i += 1) {
                        counts[Math.floor(Math.random() * 6)] += 1;
                    }
                } else {
                    labels = ['Đỏ', 'Xanh', 'Vàng', 'Tím'];
                    counts = [0, 0, 0, 0];
                    for (let i = 0; i < trials; i += 1) {
                        counts[Math.floor(Math.random() * 4)] += 1;
                    }
                }

                output.innerHTML = `
                    <p class="vi-note">Sau ${trials} lần thử, em hãy xem kết quả có gần với dự đoán ban đầu của em không.</p>
                    ${barsHtml(labels, counts)}
                `;
            }

            button.addEventListener('click', runSimulation);
            trialsInput.addEventListener('input', runSimulation);
            experimentInput.addEventListener('change', runSimulation);
            runSimulation();
            return;
        }

        container.innerHTML = cardShell(
            'Bảng dữ liệu trực quan',
            'Đổi số liệu của ba nhóm rồi đọc tổng, nhóm lớn nhất và biểu đồ cột.',
            `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Nhóm A</span>
                        <input class="vi-a" type="range" min="0" max="20" value="8" />
                    </label>
                    <label class="vi-field">
                        <span>Nhóm B</span>
                        <input class="vi-b" type="range" min="0" max="20" value="12" />
                    </label>
                    <label class="vi-field">
                        <span>Nhóm C</span>
                        <input class="vi-c" type="range" min="0" max="20" value="5" />
                    </label>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const output = container.querySelector('.vi-output');

        function update() {
            const values = [
                parseInt(container.querySelector('.vi-a').value, 10),
                parseInt(container.querySelector('.vi-b').value, 10),
                parseInt(container.querySelector('.vi-c').value, 10)
            ];
            const total = values[0] + values[1] + values[2];
            const maxValue = Math.max.apply(null, values);
            const biggest = ['Nhóm A', 'Nhóm B', 'Nhóm C'][values.indexOf(maxValue)];

            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Tổng số liệu</span>
                        <span class="vi-metric__value">${total}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Nhóm lớn nhất</span>
                        <span class="vi-metric__value">${biggest}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Giá trị trung bình</span>
                        <span class="vi-metric__value">${(total / 3).toFixed(1)}</span>
                    </div>
                </div>
                ${barsHtml(['Nhóm A', 'Nhóm B', 'Nhóm C'], values)}
            `;
        }

        container.querySelectorAll('input').forEach(function(input) {
            input.addEventListener('input', update);
        });
        update();
    }

    function renderSequenceLab(container, mode) {
        let controls = '';
        if (mode === 'binary') {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Số thập phân</span>
                        <input class="vi-decimal" type="range" min="0" max="31" value="13" />
                    </label>
                </div>
            `;
        } else if (mode === 'fibonacci') {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Số đầu tiên</span>
                        <input class="vi-first" type="range" min="1" max="8" value="1" />
                    </label>
                    <label class="vi-field">
                        <span>Số thứ hai</span>
                        <input class="vi-second" type="range" min="1" max="8" value="1" />
                    </label>
                </div>
            `;
        } else if (mode === 'pascal') {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Chọn hàng</span>
                        <input class="vi-row" type="range" min="0" max="7" value="4" />
                    </label>
                </div>
            `;
        } else {
            controls = `
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Số bắt đầu</span>
                        <input class="vi-start" type="range" min="0" max="20" value="2" />
                    </label>
                    <label class="vi-field">
                        <span>Bước nhảy</span>
                        <input class="vi-step" type="range" min="1" max="10" value="3" />
                    </label>
                </div>
            `;
        }

        container.innerHTML = cardShell(
            'Máy tạo quy luật',
            'Đổi số bắt đầu hoặc quy tắc để xem dãy số được tạo ra.',
            controls + '<div class="vi-output" aria-live="polite"></div>'
        );

        const output = container.querySelector('.vi-output');

        function update() {
            if (mode === 'binary') {
                const decimal = parseInt(container.querySelector('.vi-decimal').value, 10);
                const binary = decimal.toString(2);
                const powers = binary.split('').map(function(bit, index) {
                    const power = Math.pow(2, binary.length - index - 1);
                    return `${bit}×${power}`;
                });

                output.innerHTML = `
                    <div class="vi-metrics">
                        <div class="vi-metric">
                            <span class="vi-metric__label">Số nhị phân</span>
                            <span class="vi-metric__value">${binary}</span>
                        </div>
                    </div>
                    <div class="vi-chip-row">
                        ${powers.map(function(item) {
                            return `<span class="vi-chip">${item}</span>`;
                        }).join('')}
                    </div>
                    <p class="vi-note">Mỗi chữ số 0 hoặc 1 cho biết em có dùng giá trị của một lũy thừa 2 hay không.</p>
                `;
                return;
            }

            if (mode === 'fibonacci') {
                let first = parseInt(container.querySelector('.vi-first').value, 10);
                let second = parseInt(container.querySelector('.vi-second').value, 10);
                const sequence = [first, second];
                while (sequence.length < 8) {
                    sequence.push(sequence[sequence.length - 1] + sequence[sequence.length - 2]);
                }

                output.innerHTML = `
                    <div class="vi-chip-row">
                        ${sequence.map(function(item) {
                            return `<span class="vi-chip">${item}</span>`;
                        }).join('')}
                    </div>
                    <p class="vi-note">Mỗi số mới bằng tổng của hai số ngay trước nó.</p>
                `;
                return;
            }

            if (mode === 'pascal') {
                const rowIndex = parseInt(container.querySelector('.vi-row').value, 10);
                let row = [1];
                for (let rowNumber = 0; rowNumber < rowIndex; rowNumber += 1) {
                    const next = [1];
                    for (let index = 0; index < row.length - 1; index += 1) {
                        next.push(row[index] + row[index + 1]);
                    }
                    next.push(1);
                    row = next;
                }

                output.innerHTML = `
                    <div class="vi-chip-row">
                        ${row.map(function(item) {
                            return `<span class="vi-chip">${item}</span>`;
                        }).join('')}
                    </div>
                    <p class="vi-note">Mỗi số ở giữa bằng tổng của hai số ngay phía trên nó.</p>
                `;
                return;
            }

            const start = parseInt(container.querySelector('.vi-start').value, 10);
            const step = parseInt(container.querySelector('.vi-step').value, 10);
            const sequence = Array.from({ length: 8 }, function(_, index) {
                return start + step * index;
            });
            const next = start + step * 8;

            output.innerHTML = `
                <div class="vi-chip-row">
                    ${sequence.map(function(item) {
                        return `<span class="vi-chip">${item}</span>`;
                    }).join('')}
                </div>
                <p class="vi-note">Mỗi bước cộng thêm ${step}. Em đoán số tiếp theo là ${next} không?</p>
            `;
        }

        container.querySelectorAll('input').forEach(function(input) {
            input.addEventListener('input', update);
        });
        update();
    }

    function randomEquation() {
        const addend = 2 + Math.floor(Math.random() * 8);
        const answer = 3 + Math.floor(Math.random() * 10);
        return {
            addend: addend,
            total: addend + answer,
            answer: answer
        };
    }

    function renderBalanceLab(container) {
        container.innerHTML = cardShell(
            'Cân bằng phương trình',
            'Tìm số bí mật sao cho hai vế bằng nhau.',
            `
                <div class="vi-equation"></div>
                <div class="vi-controls">
                    <label class="vi-field">
                        <span>Giá trị em đoán</span>
                        <input class="vi-guess" type="range" min="0" max="20" value="5" />
                    </label>
                </div>
                <button class="vi-button vi-button--secondary" type="button">Bài mới</button>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const equationEl = container.querySelector('.vi-equation');
        const guessInput = container.querySelector('.vi-guess');
        const button = container.querySelector('.vi-button');
        const output = container.querySelector('.vi-output');
        let current = randomEquation();

        function update() {
            const guess = parseInt(guessInput.value, 10);
            equationEl.textContent = `x + ${current.addend} = ${current.total}`;

            const difference = current.total - (guess + current.addend);
            const correct = difference === 0;
            output.innerHTML = `
                <div class="vi-metrics">
                    <div class="vi-metric">
                        <span class="vi-metric__label">Vế trái</span>
                        <span class="vi-metric__value">${guess + current.addend}</span>
                    </div>
                    <div class="vi-metric">
                        <span class="vi-metric__label">Vế phải</span>
                        <span class="vi-metric__value">${current.total}</span>
                    </div>
                </div>
                <div class="vi-feedback${correct ? '' : ' vi-feedback--warn'}">
                    ${
                        correct
                            ? `Chính xác. x = ${guess}. Hai vế đã cân bằng.`
                            : `Chưa cân bằng. Em cần điều chỉnh thêm ${difference} để hai vế bằng nhau.`
                    }
                </div>
            `;
        }

        guessInput.addEventListener('input', update);
        button.addEventListener('click', function() {
            current = randomEquation();
            guessInput.value = current.answer;
            update();
            refreshRangeBadges(container);
        });
        update();
    }

    function renderChallengeLab(container) {
        container.innerHTML = cardShell(
            'Thử thách nhanh',
            'Đọc kỹ câu hỏi, dự đoán trước rồi mới bấm chọn đáp án.',
            `
                <div class="vi-output" aria-live="polite"></div>
                <div class="vi-choice-row"></div>
                <button class="vi-button vi-button--secondary" type="button">Câu khác</button>
            `
        );

        const output = container.querySelector('.vi-output');
        const choices = container.querySelector('.vi-choice-row');
        const nextButton = container.querySelector('.vi-button');
        let currentQuestion = QUESTION_SETS[0];

        function pickQuestion() {
            currentQuestion = QUESTION_SETS[Math.floor(Math.random() * QUESTION_SETS.length)];
            output.innerHTML = `<p class="vi-note"><strong>Câu hỏi:</strong> ${escapeHtml(currentQuestion.question)}</p>`;
            choices.innerHTML = currentQuestion.choices.map(function(choice, index) {
                return `<button class="vi-choice" type="button" data-index="${index}">${escapeHtml(choice)}</button>`;
            }).join('');

            choices.querySelectorAll('.vi-choice').forEach(function(button) {
                button.addEventListener('click', function() {
                    const selected = parseInt(button.dataset.index, 10);
                    const correct = selected === currentQuestion.answerIndex;
                    output.innerHTML = `
                        <p class="vi-note"><strong>Câu hỏi:</strong> ${escapeHtml(currentQuestion.question)}</p>
                        <div class="vi-feedback${correct ? '' : ' vi-feedback--warn'}">
                            ${
                                correct
                                    ? 'Em trả lời đúng rồi.'
                                    : 'Chưa đúng. Hãy đọc lại gợi ý và thử câu khác nhé.'
                            }
                            ${escapeHtml(currentQuestion.explanation)}
                        </div>
                    `;
                });
            });
        }

        nextButton.addEventListener('click', pickQuestion);
        pickQuestion();
    }

    function renderLegacyPatternRecognizer(container) {
        container.innerHTML = cardShell(
            'Bảng tìm số chẵn',
            'Hãy đoán trước các số chẵn rồi bấm để kiểm tra dự đoán của em.',
            `
                <div class="vi-dot-grid" style="justify-content: center;">
                    ${Array.from({ length: 20 }, function(_, index) {
                        const value = index + 1;
                        return `<button class="vi-choice vi-choice--secondary" type="button" data-number="${value}">${value}</button>`;
                    }).join('')}
                </div>
                <div class="vi-choice-row">
                    <button class="vi-button" type="button">Hiện số chẵn</button>
                    <button class="vi-button vi-button--secondary" type="button">Làm lại</button>
                </div>
                <div class="vi-output" aria-live="polite"></div>
            `
        );

        const buttons = container.querySelectorAll('.vi-choice[data-number]');
        const reveal = container.querySelectorAll('.vi-button')[0];
        const reset = container.querySelectorAll('.vi-button')[1];
        const output = container.querySelector('.vi-output');

        function paint(showAll) {
            buttons.forEach(function(button) {
                const value = parseInt(button.dataset.number, 10);
                if (showAll && value % 2 === 0) {
                    button.style.background = '#1d7cb8';
                    button.style.color = '#ffffff';
                } else {
                    button.style.background = '#d7e9f8';
                    button.style.color = '#174263';
                }
            });
            output.innerHTML = showAll
                ? '<p class="vi-note">Các số chẵn xuất hiện cách nhau đúng 2 đơn vị.</p>'
                : '<p class="vi-note">Em hãy tự chọn vài số rồi dự đoán trước khi bấm "Hiện số chẵn".</p>';
        }

        reveal.addEventListener('click', function() {
            paint(true);
        });
        reset.addEventListener('click', function() {
            paint(false);
        });
        paint(false);
    }

    function initContainer(container) {
        if (!container || container.dataset.viInitialized === 'true') {
            return;
        }

        const template = container.dataset.viTemplate;
        const mode = container.dataset.viMode;

        if (template === 'number-lab') {
            renderNumberLab(container, mode);
        } else if (template === 'array-lab') {
            renderArrayLab(container, mode);
        } else if (template === 'fraction-lab') {
            renderFractionLab(container, mode);
        } else if (template === 'measurement-lab') {
            renderMeasurementLab(container, mode);
        } else if (template === 'geometry-lab') {
            renderGeometryLab(container, mode);
        } else if (template === 'data-lab') {
            renderDataLab(container, mode);
        } else if (template === 'sequence-lab') {
            renderSequenceLab(container, mode);
        } else if (template === 'balance-lab') {
            renderBalanceLab(container);
        } else {
            renderChallengeLab(container);
        }

        enhanceRangeInputs(container);
        container.dataset.viInitialized = 'true';
    }

    function initLegacyCompat() {
        const evenExplorer = document.getElementById('even-number-explorer');
        if (evenExplorer && evenExplorer.dataset.viInitialized !== 'true') {
            renderNumberLab(evenExplorer, 'parity', {
                cardTitle: 'Trình khám phá số chẵn',
                subtitle: 'Đổi số rồi quan sát xem có ghép thành từng cặp đều nhau không.'
            });
            enhanceRangeInputs(evenExplorer);
            evenExplorer.dataset.viInitialized = 'true';
        }

        const patternRecognizer = document.getElementById('pattern-recognizer');
        if (patternRecognizer && patternRecognizer.dataset.viInitialized !== 'true') {
            renderLegacyPatternRecognizer(patternRecognizer);
            patternRecognizer.dataset.viInitialized = 'true';
        }
    }

    function init() {
        ensureStyles();
        document.querySelectorAll('.vi-interactive-root').forEach(initContainer);
        initLegacyCompat();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();

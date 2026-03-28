/**
 * Interactive Fractions Explorer
 * Allows children to explore halves (1/2) and quarters (1/4) visually
 * Chapter 04: Halves and Quarters - Sharing Fairly
 */

(function() {
    'use strict';

    /**
     * Initialize the Pizza Fraction Cutter
     */
    function initPizzaCutter() {
        const container = document.getElementById('pizza-fraction-cutter');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 15px; color: white; max-width: 700px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">🍕 Pizza Fraction Cutter</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333;">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <label style="font-weight: bold; display: block; margin-bottom: 10px;">
                            How many people need to share the pizza?
                        </label>
                        <div style="margin: 15px 0;">
                            <button class="people-btn" data-people="2" style="margin: 5px; padding: 12px 30px; font-size: 16px; border: 3px solid #667eea; background: white; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                2 People
                            </button>
                            <button class="people-btn" data-people="4" style="margin: 5px; padding: 12px 30px; font-size: 16px; border: 3px solid #667eea; background: white; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                4 People
                            </button>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: center; margin: 30px 0;">
                        <svg id="pizza-svg" width="300" height="300" style="border: 3px solid #8B4513; border-radius: 50%; background: white;">
                            <!-- Pizza will be drawn here -->
                        </svg>
                    </div>

                    <div id="fraction-info" style="padding: 15px; background: #e7f3ff; border-radius: 8px; text-align: center;">
                        <p style="margin: 0; font-weight: bold; color: #0066cc;">
                            Click a button to cut the pizza!
                        </p>
                    </div>
                </div>
            </div>
        `;

        const pizzaSvg = document.getElementById('pizza-svg');
        const fractionInfo = document.getElementById('fraction-info');
        const peopleButtons = document.querySelectorAll('.people-btn');

        function drawPizza(numPeople) {
            const centerX = 150;
            const centerY = 150;
            const radius = 130;

            pizzaSvg.innerHTML = '';

            // Draw full pizza background
            const pizzaCircle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            pizzaCircle.setAttribute('cx', centerX);
            pizzaCircle.setAttribute('cy', centerY);
            pizzaCircle.setAttribute('r', radius);
            pizzaCircle.setAttribute('fill', '#FFD700');
            pizzaSvg.appendChild(pizzaCircle);

            // Draw slices
            const colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A'];
            const sliceAngle = 360 / numPeople;

            for (let i = 0; i < numPeople; i++) {
                const startAngle = (i * sliceAngle - 90) * Math.PI / 180;
                const endAngle = ((i + 1) * sliceAngle - 90) * Math.PI / 180;

                const x1 = centerX + radius * Math.cos(startAngle);
                const y1 = centerY + radius * Math.sin(startAngle);
                const x2 = centerX + radius * Math.cos(endAngle);
                const y2 = centerY + radius * Math.sin(endAngle);

                const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
                const largeArcFlag = sliceAngle > 180 ? 1 : 0;
                const pathData = `M ${centerX} ${centerY} L ${x1} ${y1} A ${radius} ${radius} 0 ${largeArcFlag} 1 ${x2} ${y2} Z`;
                path.setAttribute('d', pathData);
                path.setAttribute('fill', colors[i % colors.length]);
                path.setAttribute('opacity', '0.8');
                path.setAttribute('stroke', '#8B4513');
                path.setAttribute('stroke-width', '3');
                pizzaSvg.appendChild(path);

                // Add fraction label in the middle of each slice
                const middleAngle = (startAngle + endAngle) / 2;
                const labelRadius = radius * 0.6;
                const labelX = centerX + labelRadius * Math.cos(middleAngle);
                const labelY = centerY + labelRadius * Math.sin(middleAngle);

                const text = document.createElementNS('http://www.w3.org/2000/svg', 'text');
                text.setAttribute('x', labelX);
                text.setAttribute('y', labelY);
                text.setAttribute('text-anchor', 'middle');
                text.setAttribute('dominant-baseline', 'middle');
                text.setAttribute('fill', 'white');
                text.setAttribute('font-size', '24');
                text.setAttribute('font-weight', 'bold');
                text.setAttribute('stroke', '#333');
                text.setAttribute('stroke-width', '1');
                text.textContent = `1/${numPeople}`;
                pizzaSvg.appendChild(text);

                // Add dividing line
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', centerX);
                line.setAttribute('y1', centerY);
                line.setAttribute('x2', x1);
                line.setAttribute('y2', y1);
                line.setAttribute('stroke', '#8B4513');
                line.setAttribute('stroke-width', '3');
                pizzaSvg.appendChild(line);
            }

            // Add pepperoni decorations
            for (let i = 0; i < 12; i++) {
                const angle = (Math.random() * 360) * Math.PI / 180;
                const distance = Math.random() * (radius - 30) + 20;
                const pepX = centerX + distance * Math.cos(angle);
                const pepY = centerY + distance * Math.sin(angle);

                const pepperoni = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
                pepperoni.setAttribute('cx', pepX);
                pepperoni.setAttribute('cy', pepY);
                pepperoni.setAttribute('r', '8');
                pepperoni.setAttribute('fill', '#8B0000');
                pizzaSvg.appendChild(pepperoni);
            }

            // Update info
            const fractionName = numPeople === 2 ? 'halves (1/2)' : 'quarters (1/4)';
            fractionInfo.innerHTML = `
                <p style="margin: 0 0 10px 0; font-weight: bold; color: #0066cc; font-size: 18px;">
                    Pizza cut into ${numPeople} equal pieces!
                </p>
                <p style="margin: 0; color: #333;">
                    Each person gets <strong style="color: #ff6b6b; font-size: 20px;">1/${numPeople}</strong> (${fractionName}) of the pizza.
                </p>
            `;
        }

        // Event listeners for buttons
        peopleButtons.forEach(btn => {
            btn.addEventListener('click', function() {
                const numPeople = parseInt(this.dataset.people);
                
                // Update button styles
                peopleButtons.forEach(b => {
                    b.style.background = 'white';
                    b.style.color = '#333';
                });
                this.style.background = '#667eea';
                this.style.color = 'white';

                drawPizza(numPeople);
            });
        });

        // Initial pizza (2 slices)
        peopleButtons[0].style.background = '#667eea';
        peopleButtons[0].style.color = 'white';
        drawPizza(2);
    }

    /**
     * Initialize the Fraction Comparison game
     */
    function initFractionComparison() {
        const container = document.getElementById('fraction-comparison');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 15px; color: white; max-width: 800px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">⚖️ Which is Bigger?</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333;">
                    <div style="display: flex; justify-content: space-around; align-items: center; margin: 20px 0; flex-wrap: wrap;">
                        <div style="text-align: center; margin: 10px;">
                            <svg id="half-circle" width="200" height="200">
                                <!-- Half circle will be drawn here -->
                            </svg>
                            <div style="font-size: 24px; font-weight: bold; margin-top: 10px; color: #667eea;">1/2</div>
                        </div>

                        <div style="font-size: 48px; font-weight: bold; color: #667eea;">VS</div>

                        <div style="text-align: center; margin: 10px;">
                            <svg id="quarter-circle" width="200" height="200">
                                <!-- Quarter circle will be drawn here -->
                            </svg>
                            <div style="font-size: 24px; font-weight: bold; margin-top: 10px; color: #667eea;">1/4</div>
                        </div>
                    </div>

                    <div style="text-align: center; margin: 30px 0;">
                        <button id="half-bigger-btn" style="margin: 5px; padding: 15px 30px; font-size: 18px; background: #4ECDC4; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                            1/2 is Bigger
                        </button>
                        <button id="quarter-bigger-btn" style="margin: 5px; padding: 15px 30px; font-size: 18px; background: #FF6B6B; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                            1/4 is Bigger
                        </button>
                        <button id="equal-btn" style="margin: 5px; padding: 15px 30px; font-size: 18px; background: #FFA07A; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                            They're Equal
                        </button>
                    </div>

                    <div id="comparison-result" style="padding: 15px; border-radius: 8px; display: none;">
                        <!-- Result will appear here -->
                    </div>
                </div>
            </div>
        `;

        const halfCircle = document.getElementById('half-circle');
        const quarterCircle = document.getElementById('quarter-circle');
        const comparisonResult = document.getElementById('comparison-result');
        const halfBiggerBtn = document.getElementById('half-bigger-btn');
        const quarterBiggerBtn = document.getElementById('quarter-bigger-btn');
        const equalBtn = document.getElementById('equal-btn');

        function drawComparisonCircles() {
            const centerX = 100;
            const centerY = 100;
            const radius = 80;

            // Draw half circle
            halfCircle.innerHTML = '';
            
            // Full circle outline
            const halfOutline = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            halfOutline.setAttribute('cx', centerX);
            halfOutline.setAttribute('cy', centerY);
            halfOutline.setAttribute('r', radius);
            halfOutline.setAttribute('fill', 'none');
            halfOutline.setAttribute('stroke', '#ddd');
            halfOutline.setAttribute('stroke-width', '2');
            halfOutline.setAttribute('stroke-dasharray', '5,5');
            halfCircle.appendChild(halfOutline);

            // Half filled
            const halfPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            const halfPathData = `M ${centerX} ${centerY} L ${centerX} ${centerY - radius} A ${radius} ${radius} 0 0 1 ${centerX} ${centerY + radius} Z`;
            halfPath.setAttribute('d', halfPathData);
            halfPath.setAttribute('fill', '#4ECDC4');
            halfPath.setAttribute('opacity', '0.8');
            halfPath.setAttribute('stroke', '#2eb3aa');
            halfPath.setAttribute('stroke-width', '3');
            halfCircle.appendChild(halfPath);

            // Draw quarter circle
            quarterCircle.innerHTML = '';
            
            // Full circle outline
            const quarterOutline = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
            quarterOutline.setAttribute('cx', centerX);
            quarterOutline.setAttribute('cy', centerY);
            quarterOutline.setAttribute('r', radius);
            quarterOutline.setAttribute('fill', 'none');
            quarterOutline.setAttribute('stroke', '#ddd');
            quarterOutline.setAttribute('stroke-width', '2');
            quarterOutline.setAttribute('stroke-dasharray', '5,5');
            quarterCircle.appendChild(quarterOutline);

            // Quarter filled
            const quarterPath = document.createElementNS('http://www.w3.org/2000/svg', 'path');
            const quarterPathData = `M ${centerX} ${centerY} L ${centerX + radius} ${centerY} A ${radius} ${radius} 0 0 1 ${centerX} ${centerY - radius} Z`;
            quarterPath.setAttribute('d', quarterPathData);
            quarterPath.setAttribute('fill', '#FF6B6B');
            quarterPath.setAttribute('opacity', '0.8');
            quarterPath.setAttribute('stroke', '#ff5252');
            quarterPath.setAttribute('stroke-width', '3');
            quarterCircle.appendChild(quarterPath);
        }

        function checkAnswer(answer) {
            comparisonResult.style.display = 'block';
            
            if (answer === 'half') {
                comparisonResult.style.background = '#d4edda';
                comparisonResult.style.color = '#155724';
                comparisonResult.innerHTML = `
                    <p style="margin: 0; font-weight: bold; font-size: 18px;">
                        ✓ Correct! 1/2 is BIGGER than 1/4
                    </p>
                    <p style="margin: 10px 0 0 0;">
                        When you cut something into fewer pieces, each piece is bigger!
                        1/2 means 2 pieces (bigger), 1/4 means 4 pieces (smaller).
                    </p>
                `;
            } else {
                comparisonResult.style.background = '#f8d7da';
                comparisonResult.style.color = '#721c24';
                comparisonResult.innerHTML = `
                    <p style="margin: 0; font-weight: bold; font-size: 18px;">
                        ✗ Not quite! 1/2 is BIGGER than 1/4
                    </p>
                    <p style="margin: 10px 0 0 0;">
                        Look at the circles above - 1/2 (half) is a larger piece than 1/4 (quarter).
                        The MORE pieces you cut something into, the SMALLER each piece becomes!
                    </p>
                `;
            }
        }

        halfBiggerBtn.addEventListener('click', () => checkAnswer('half'));
        quarterBiggerBtn.addEventListener('click', () => checkAnswer('quarter'));
        equalBtn.addEventListener('click', () => checkAnswer('equal'));

        drawComparisonCircles();
    }

    /**
     * Initialize the Fraction Builder
     */
    function initFractionBuilder() {
        const container = document.getElementById('fraction-builder');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 20px; border-radius: 15px; color: white; max-width: 700px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">🧩 Fraction Builder</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333;">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <p style="font-weight: bold; font-size: 18px; margin-bottom: 15px;">
                            Build a whole by adding fractions!
                        </p>
                        
                        <div style="margin: 20px 0;">
                            <button class="add-half-btn" style="margin: 5px; padding: 12px 25px; font-size: 16px; background: #4ECDC4; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                + Add 1/2
                            </button>
                            <button class="add-quarter-btn" style="margin: 5px; padding: 12px 25px; font-size: 16px; background: #FF6B6B; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                + Add 1/4
                            </button>
                            <button id="reset-fractions-btn" style="margin: 5px; padding: 12px 25px; font-size: 16px; background: #6c757d; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold;">
                                Reset
                            </button>
                        </div>
                    </div>

                    <div style="display: flex; justify-content: center; margin: 30px 0;">
                        <svg id="fraction-builder-svg" width="300" height="300" style="border: 3px solid #667eea; border-radius: 10px; background: #f8f9fa;">
                            <!-- Fraction visualization will be drawn here -->
                        </svg>
                    </div>

                    <div id="fraction-total" style="padding: 15px; background: #e7f3ff; border-radius: 8px; text-align: center;">
                        <p style="margin: 0; font-weight: bold; color: #0066cc; font-size: 20px;">
                            Total: <span id="total-fraction">0/4</span>
                        </p>
                        <p style="margin: 10px 0 0 0; color: #333;" id="completion-message">
                            Start adding fractions!
                        </p>
                    </div>
                </div>
            </div>
        `;

        const builderSvg = document.getElementById('fraction-builder-svg');
        const totalFraction = document.getElementById('total-fraction');
        const completionMessage = document.getElementById('completion-message');
        const addHalfBtn = document.querySelector('.add-half-btn');
        const addQuarterBtn = document.querySelector('.add-quarter-btn');
        const resetBtn = document.getElementById('reset-fractions-btn');

        let totalQuarters = 0; // Track in quarters (out of 4)

        function drawFractionBar() {
            builderSvg.innerHTML = '';
            
            const barWidth = 250;
            const barHeight = 60;
            const startX = 25;
            const startY = 120;

            // Draw empty rectangle
            const emptyRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            emptyRect.setAttribute('x', startX);
            emptyRect.setAttribute('y', startY);
            emptyRect.setAttribute('width', barWidth);
            emptyRect.setAttribute('height', barHeight);
            emptyRect.setAttribute('fill', 'white');
            emptyRect.setAttribute('stroke', '#333');
            emptyRect.setAttribute('stroke-width', '3');
            builderSvg.appendChild(emptyRect);

            // Draw filled portion
            const filledWidth = (totalQuarters / 4) * barWidth;
            const filledRect = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
            filledRect.setAttribute('x', startX);
            filledRect.setAttribute('y', startY);
            filledRect.setAttribute('width', filledWidth);
            filledRect.setAttribute('height', barHeight);
            filledRect.setAttribute('fill', '#4ECDC4');
            filledRect.setAttribute('opacity', '0.7');
            builderSvg.appendChild(filledRect);

            // Draw quarter divisions
            for (let i = 1; i < 4; i++) {
                const x = startX + (barWidth / 4) * i;
                const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
                line.setAttribute('x1', x);
                line.setAttribute('y1', startY);
                line.setAttribute('x2', x);
                line.setAttribute('y2', startY + barHeight);
                line.setAttribute('stroke', '#999');
                line.setAttribute('stroke-width', '2');
                line.setAttribute('stroke-dasharray', '5,5');
                builderSvg.appendChild(line);
            }

            // Label
            const label = document.createElementNS('http://www.w3.org/2000/svg', 'text');
            label.setAttribute('x', startX + barWidth / 2);
            label.setAttribute('y', startY + barHeight / 2);
            label.setAttribute('text-anchor', 'middle');
            label.setAttribute('dominant-baseline', 'middle');
            label.setAttribute('fill', totalQuarters > 0 ? 'white' : '#999');
            label.setAttribute('font-size', '24');
            label.setAttribute('font-weight', 'bold');
            label.textContent = `${totalQuarters}/4`;
            builderSvg.appendChild(label);

            // Update display
            totalFraction.textContent = `${totalQuarters}/4`;
            
            if (totalQuarters === 0) {
                completionMessage.textContent = 'Start adding fractions!';
                completionMessage.style.color = '#333';
            } else if (totalQuarters < 4) {
                completionMessage.textContent = `You need ${4 - totalQuarters} more quarter(s) to make a whole!`;
                completionMessage.style.color = '#0066cc';
            } else if (totalQuarters === 4) {
                completionMessage.innerHTML = '🎉 <strong>Perfect! You made 1 whole!</strong> (4/4 = 1)';
                completionMessage.style.color = '#28a745';
            } else {
                completionMessage.innerHTML = `⚠️ Oops! You went over 1 whole. You have ${totalQuarters}/4 = ${totalQuarters / 4} wholes!`;
                completionMessage.style.color = '#dc3545';
            }
        }

        addHalfBtn.addEventListener('click', function() {
            totalQuarters += 2; // 1/2 = 2/4
            drawFractionBar();
        });

        addQuarterBtn.addEventListener('click', function() {
            totalQuarters += 1; // 1/4 = 1/4
            drawFractionBar();
        });

        resetBtn.addEventListener('click', function() {
            totalQuarters = 0;
            drawFractionBar();
        });

        // Initial draw
        drawFractionBar();
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            initPizzaCutter();
            initFractionComparison();
            initFractionBuilder();
        });
    } else {
        initPizzaCutter();
        initFractionComparison();
        initFractionBuilder();
    }
})();

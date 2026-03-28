/**
 * Interactive Even Numbers Explorer
 * Allows children to explore even and odd numbers by testing different values
 * Chapter 01: Discovering Even Numbers
 */

(function() {
    'use strict';

    /**
     * Initialize the Even Number Explorer
     */
    function initEvenNumberExplorer() {
        const container = document.getElementById('even-number-explorer');
        if (!container) return;

        // Create the HTML structure
        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 20px; border-radius: 15px; color: white; max-width: 600px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">🔢 Even Number Explorer</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333; margin-bottom: 15px;">
                    <label for="number-input" style="font-weight: bold; display: block; margin-bottom: 10px;">
                        Pick a number (1-100):
                    </label>
                    <input 
                        type="number" 
                        id="number-input" 
                        min="1" 
                        max="100" 
                        value="8" 
                        style="width: 100%; padding: 10px; font-size: 18px; border: 2px solid #667eea; border-radius: 5px; box-sizing: border-box;"
                    />
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 12px; margin-bottom: 8px;">
                        <span style="font-weight: bold; color: #667eea;">Slider value</span>
                        <span id="number-slider-value" style="display: inline-flex; align-items: center; justify-content: center; min-width: 52px; padding: 6px 12px; border-radius: 999px; background: #667eea; color: white; font-weight: bold;">8</span>
                    </div>
                    <input 
                        type="range" 
                        id="number-slider" 
                        min="1" 
                        max="100" 
                        value="8" 
                        style="width: 100%; margin-top: 10px;"
                    />
                </div>

                <div id="result-display" style="background: white; padding: 20px; border-radius: 10px; color: #333; min-height: 200px;">
                    <!-- Results will be displayed here -->
                </div>

                <div style="background: rgba(255,255,255,0.2); padding: 15px; border-radius: 10px; margin-top: 15px;">
                    <p style="margin: 0; font-size: 14px; text-align: center;">
                        💡 <strong>Tip:</strong> Try different numbers and see the pattern!
                    </p>
                </div>
            </div>
        `;

        // Get elements
        const numberInput = document.getElementById('number-input');
        const numberSlider = document.getElementById('number-slider');
        const numberSliderValue = document.getElementById('number-slider-value');
        const resultDisplay = document.getElementById('result-display');

        /**
         * Update the display when number changes
         */
        function updateDisplay() {
            const num = parseInt(numberInput.value);
            numberSliderValue.textContent = numberSlider.value;
            
            if (isNaN(num) || num < 1 || num > 100) {
                resultDisplay.innerHTML = '<p style="color: red; text-align: center;">Please enter a number between 1 and 100</p>';
                return;
            }

            const isEven = num % 2 === 0;
            const halfNum = Math.floor(num / 2);
            const remainder = num % 2;

            // Generate visual representation (circles)
            let circlesHTML = '<div style="margin: 15px 0;">';
            
            // Left group
            circlesHTML += '<div style="display: inline-block; margin-right: 20px; vertical-align: top;">';
            circlesHTML += '<div style="font-weight: bold; margin-bottom: 5px;">Group 1:</div>';
            for (let i = 0; i < halfNum; i++) {
                circlesHTML += '<span style="display: inline-block; width: 30px; height: 30px; background: #4ECDC4; border-radius: 50%; margin: 3px; border: 2px solid #333;"></span>';
                if ((i + 1) % 5 === 0) circlesHTML += '<br>';
            }
            circlesHTML += '</div>';

            // Right group
            circlesHTML += '<div style="display: inline-block; vertical-align: top;">';
            circlesHTML += '<div style="font-weight: bold; margin-bottom: 5px;">Group 2:</div>';
            for (let i = 0; i < halfNum; i++) {
                circlesHTML += '<span style="display: inline-block; width: 30px; height: 30px; background: #FF6B6B; border-radius: 50%; margin: 3px; border: 2px solid #333;"></span>';
                if ((i + 1) % 5 === 0) circlesHTML += '<br>';
            }
            circlesHTML += '</div>';

            // Leftover circle if odd
            if (remainder === 1) {
                circlesHTML += '<div style="margin-top: 15px; padding: 10px; background: #FFF3CD; border-radius: 5px; border: 2px dashed #FFB100;">';
                circlesHTML += '<div style="font-weight: bold; color: #856404; margin-bottom: 5px;">Leftover:</div>';
                circlesHTML += '<span style="display: inline-block; width: 30px; height: 30px; background: gold; border-radius: 50%; margin: 3px; border: 3px solid #FFB100;"></span>';
                circlesHTML += '</div>';
            }
            
            circlesHTML += '</div>';

            // Build result HTML
            let resultHTML = `
                <div style="text-align: center; margin-bottom: 20px;">
                    <h2 style="margin: 0; font-size: 48px; color: ${isEven ? '#28a745' : '#dc3545'};">
                        ${num}
                    </h2>
                    <div style="font-size: 24px; font-weight: bold; color: ${isEven ? '#28a745' : '#dc3545'}; margin-top: 5px;">
                        ${isEven ? '✓ EVEN' : '✗ ODD'}
                    </div>
                </div>

                <div style="background: ${isEven ? '#d4edda' : '#f8d7da'}; padding: 15px; border-radius: 8px; margin-bottom: 15px;">
                    <p style="margin: 0; font-weight: bold; color: ${isEven ? '#155724' : '#721c24'};">
                        ${num} ÷ 2 = ${halfNum}${remainder === 1 ? ' remainder 1' : ''}
                    </p>
                </div>

                ${circlesHTML}

                <div style="margin-top: 20px; padding: 15px; background: #e7f3ff; border-radius: 8px; border-left: 4px solid #0066cc;">
                    <p style="margin: 0; font-weight: bold; color: #0066cc;">
                        ${isEven 
                            ? `🎉 ${num} splits perfectly into 2 equal groups of ${halfNum}!` 
                            : `💡 ${num} can't split evenly. You get 2 groups of ${halfNum} with 1 left over!`
                        }
                    </p>
                </div>
            `;

            resultDisplay.innerHTML = resultHTML;
        }

        // Event listeners
        numberInput.addEventListener('input', function() {
            numberSlider.value = this.value;
            updateDisplay();
        });

        numberSlider.addEventListener('input', function() {
            numberInput.value = this.value;
            updateDisplay();
        });

        // Initial display
        updateDisplay();
    }

    /**
     * Initialize pattern recognizer (find even numbers in a range)
     */
    function initPatternRecognizer() {
        const container = document.getElementById('pattern-recognizer');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 20px; border-radius: 15px; color: white; max-width: 800px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">🎯 Pattern Finder</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333;">
                    <div id="number-grid" style="display: grid; grid-template-columns: repeat(10, 1fr); gap: 10px; max-width: 600px; margin: 0 auto;">
                        <!-- Numbers will be generated here -->
                    </div>
                    
                    <div style="margin-top: 20px; text-align: center;">
                        <button id="reveal-btn" style="background: #667eea; color: white; border: none; padding: 12px 30px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold;">
                            Reveal Even Numbers
                        </button>
                        <button id="reset-btn" style="background: #6c757d; color: white; border: none; padding: 12px 30px; font-size: 16px; border-radius: 8px; cursor: pointer; margin-left: 10px; font-weight: bold;">
                            Reset
                        </button>
                    </div>

                    <div id="pattern-message" style="margin-top: 20px; padding: 15px; background: #e7f3ff; border-radius: 8px; display: none;">
                        <!-- Message will appear here -->
                    </div>
                </div>
            </div>
        `;

        const numberGrid = document.getElementById('number-grid');
        const revealBtn = document.getElementById('reveal-btn');
        const resetBtn = document.getElementById('reset-btn');
        const patternMessage = document.getElementById('pattern-message');

        // Generate number grid (1-20)
        function generateGrid() {
            numberGrid.innerHTML = '';
            for (let i = 1; i <= 20; i++) {
                const numBox = document.createElement('div');
                numBox.className = 'number-box';
                numBox.textContent = i;
                numBox.style.cssText = `
                    background: #f0f0f0;
                    border: 2px solid #999;
                    border-radius: 8px;
                    padding: 15px;
                    text-align: center;
                    font-size: 20px;
                    font-weight: bold;
                    cursor: pointer;
                    transition: all 0.3s;
                `;
                numBox.dataset.number = i;
                
                numBox.addEventListener('click', function() {
                    const num = parseInt(this.dataset.number);
                    if (num % 2 === 0) {
                        this.style.background = '#4ECDC4';
                        this.style.color = 'white';
                        this.style.borderColor = '#2eb3aa';
                    } else {
                        this.style.background = '#FF6B6B';
                        this.style.color = 'white';
                        this.style.borderColor = '#ff5252';
                    }
                });

                numberGrid.appendChild(numBox);
            }
        }

        revealBtn.addEventListener('click', function() {
            const boxes = numberGrid.querySelectorAll('.number-box');
            boxes.forEach(box => {
                const num = parseInt(box.dataset.number);
                if (num % 2 === 0) {
                    box.style.background = '#4ECDC4';
                    box.style.color = 'white';
                    box.style.borderColor = '#2eb3aa';
                    box.style.transform = 'scale(1.1)';
                    setTimeout(() => {
                        box.style.transform = 'scale(1)';
                    }, 300);
                }
            });

            patternMessage.style.display = 'block';
            patternMessage.innerHTML = `
                <p style="margin: 0; font-weight: bold; color: #0066cc;">
                    🔍 Pattern discovered! Even numbers are: 2, 4, 6, 8, 10, 12, 14, 16, 18, 20<br>
                    Notice: They all end in 0, 2, 4, 6, or 8!
                </p>
            `;
        });

        resetBtn.addEventListener('click', function() {
            generateGrid();
            patternMessage.style.display = 'none';
        });

        // Initial grid
        generateGrid();
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            initEvenNumberExplorer();
            initPatternRecognizer();
        });
    } else {
        initEvenNumberExplorer();
        initPatternRecognizer();
    }
})();

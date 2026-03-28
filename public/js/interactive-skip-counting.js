/**
 * Interactive Skip Counting by 2s Explorer
 * Allows children to practice skip counting with visual feedback
 * Chapter 02: Skip Counting by 2s
 */

(function() {
    'use strict';

    /**
     * Initialize the Number Line Jump game
     */
    function initNumberLineJump() {
        const container = document.getElementById('number-line-jump');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); padding: 20px; border-radius: 15px; color: white; max-width: 900px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">🦘 Number Line Jump Game</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333; position: relative;">
                    <div id="number-line-canvas" style="height: 150px; position: relative; margin: 20px 0;">
                        <!-- Number line will be drawn here -->
                    </div>

                    <div style="text-align: center; margin-top: 20px;">
                        <div style="margin-bottom: 15px;">
                            <span style="font-weight: bold; font-size: 18px;">Current Position: </span>
                            <span id="current-position" style="font-size: 32px; font-weight: bold; color: #667eea;">0</span>
                        </div>
                        
                        <button id="jump-btn" style="background: #667eea; color: white; border: none; padding: 15px 40px; font-size: 18px; border-radius: 8px; cursor: pointer; font-weight: bold; margin: 0 5px;">
                            Jump +2
                        </button>
                        <button id="reset-jump-btn" style="background: #6c757d; color: white; border: none; padding: 15px 40px; font-size: 18px; border-radius: 8px; cursor: pointer; font-weight: bold; margin: 0 5px;">
                            Reset
                        </button>
                    </div>

                    <div id="jump-sequence" style="margin-top: 20px; padding: 15px; background: #e7f3ff; border-radius: 8px;">
                        <div style="font-weight: bold; margin-bottom: 10px; color: #0066cc;">Skip Counting Sequence:</div>
                        <div id="sequence-display" style="font-size: 20px; font-weight: bold; color: #333;">0</div>
                    </div>
                </div>
            </div>
        `;

        const canvas = document.getElementById('number-line-canvas');
        const currentPositionDisplay = document.getElementById('current-position');
        const jumpBtn = document.getElementById('jump-btn');
        const resetJumpBtn = document.getElementById('reset-jump-btn');
        const sequenceDisplay = document.getElementById('sequence-display');

        let position = 0;
        let sequence = [0];
        const maxPosition = 20;

        function drawNumberLine() {
            canvas.innerHTML = '';
            const canvasWidth = canvas.offsetWidth;
            const spacing = canvasWidth / maxPosition;

            // Draw the line
            const line = document.createElement('div');
            line.style.cssText = `
                position: absolute;
                bottom: 60px;
                left: 0;
                width: 100%;
                height: 4px;
                background: #333;
            `;
            canvas.appendChild(line);

            // Draw tick marks and numbers
            for (let i = 0; i <= maxPosition; i++) {
                const tick = document.createElement('div');
                const isEven = i % 2 === 0;
                
                tick.style.cssText = `
                    position: absolute;
                    bottom: ${isEven ? '52px' : '56px'};
                    left: ${i * spacing}px;
                    width: 2px;
                    height: ${isEven ? '20px' : '12px'};
                    background: ${isEven ? '#333' : '#999'};
                    transform: translateX(-1px);
                `;
                canvas.appendChild(tick);

                // Number labels (only for even numbers)
                if (isEven) {
                    const label = document.createElement('div');
                    label.textContent = i;
                    label.style.cssText = `
                        position: absolute;
                        bottom: 25px;
                        left: ${i * spacing}px;
                        transform: translateX(-50%);
                        font-weight: bold;
                        font-size: 14px;
                        color: #333;
                    `;
                    canvas.appendChild(label);
                }
            }

            // Draw jumping frog/character
            const frog = document.createElement('div');
            frog.id = 'jumping-frog';
            frog.textContent = '🦘';
            frog.style.cssText = `
                position: absolute;
                bottom: 70px;
                left: ${position * spacing}px;
                transform: translateX(-50%);
                font-size: 40px;
                transition: left 0.5s ease-in-out, bottom 0.25s ease-in-out;
            `;
            canvas.appendChild(frog);
        }

        function jump() {
            if (position >= maxPosition) {
                alert('🎉 You reached the end! Click Reset to try again.');
                return;
            }

            const canvasWidth = canvas.offsetWidth;
            const spacing = canvasWidth / maxPosition;
            const frog = document.getElementById('jumping-frog');

            // Animate jump (go up then move right)
            frog.style.bottom = '120px';
            
            setTimeout(() => {
                position += 2;
                frog.style.left = `${position * spacing}px`;
                sequence.push(position);
                
                setTimeout(() => {
                    frog.style.bottom = '70px';
                    updateDisplay();
                }, 250);
            }, 250);
        }

        function updateDisplay() {
            currentPositionDisplay.textContent = position;
            sequenceDisplay.textContent = sequence.join(', ');
        }

        function reset() {
            position = 0;
            sequence = [0];
            drawNumberLine();
            updateDisplay();
        }

        jumpBtn.addEventListener('click', jump);
        resetJumpBtn.addEventListener('click', reset);

        // Initial setup
        reset();
        
        // Redraw on window resize
        window.addEventListener('resize', drawNumberLine);
    }

    /**
     * Initialize Skip Counting Practice
     */
    function initSkipCountingPractice() {
        const container = document.getElementById('skip-counting-practice');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #fa709a 0%, #fee140 100%); padding: 20px; border-radius: 15px; color: white; max-width: 700px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0;">🎯 Skip Counting Challenge</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; color: #333;">
                    <div style="text-align: center; margin-bottom: 20px;">
                        <div style="font-weight: bold; margin-bottom: 10px;">What number comes next?</div>
                        <div id="question-display" style="font-size: 28px; font-weight: bold; color: #667eea; margin: 15px 0;">
                            2, 4, 6, 8, ?
                        </div>
                    </div>

                    <div id="answer-options" style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; margin-bottom: 20px;">
                        <!-- Options will be generated here -->
                    </div>

                    <div id="feedback-message" style="padding: 15px; border-radius: 8px; text-align: center; font-weight: bold; display: none;">
                        <!-- Feedback will appear here -->
                    </div>

                    <div style="margin-top: 20px; text-align: center;">
                        <button id="new-question-btn" style="background: #667eea; color: white; border: none; padding: 12px 30px; font-size: 16px; border-radius: 8px; cursor: pointer; font-weight: bold;">
                            New Question
                        </button>
                    </div>

                    <div style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px;">
                        <div style="text-align: center;">
                            <span style="font-weight: bold;">Score: </span>
                            <span id="score-display" style="font-size: 24px; color: #28a745;">0</span>
                            <span style="margin: 0 10px;">/</span>
                            <span style="font-weight: bold;">Attempts: </span>
                            <span id="attempts-display" style="font-size: 24px; color: #6c757d;">0</span>
                        </div>
                    </div>
                </div>
            </div>
        `;

        const questionDisplay = document.getElementById('question-display');
        const answerOptions = document.getElementById('answer-options');
        const feedbackMessage = document.getElementById('feedback-message');
        const newQuestionBtn = document.getElementById('new-question-btn');
        const scoreDisplay = document.getElementById('score-display');
        const attemptsDisplay = document.getElementById('attempts-display');

        let score = 0;
        let attempts = 0;
        let currentAnswer = 0;

        function generateQuestion() {
            // Generate a random skip counting sequence
            const startNum = Math.floor(Math.random() * 3) * 2; // 0, 2, or 4
            const length = 4 + Math.floor(Math.random() * 3); // 4-6 numbers
            
            let sequence = [];
            for (let i = 0; i < length; i++) {
                sequence.push(startNum + i * 2);
            }

            currentAnswer = startNum + length * 2;
            
            // Display sequence with ? at the end
            questionDisplay.textContent = sequence.join(', ') + ', ?';

            // Generate options (correct answer + 2 wrong answers)
            const options = [currentAnswer];
            
            // Add wrong answers
            const wrongAnswers = [];
            wrongAnswers.push(currentAnswer - 1); // Odd number before
            wrongAnswers.push(currentAnswer + 1); // Odd number after
            if (currentAnswer > 2) {
                wrongAnswers.push(currentAnswer - 2); // Previous even
            } else {
                wrongAnswers.push(currentAnswer + 2); // Next even
            }

            // Pick 2 random wrong answers
            const shuffledWrong = wrongAnswers.sort(() => Math.random() - 0.5).slice(0, 2);
            options.push(...shuffledWrong);

            // Shuffle all options
            options.sort(() => Math.random() - 0.5);

            // Display options
            answerOptions.innerHTML = '';
            options.forEach(opt => {
                const button = document.createElement('button');
                button.textContent = opt;
                button.style.cssText = `
                    padding: 20px;
                    font-size: 24px;
                    font-weight: bold;
                    background: #f0f0f0;
                    border: 3px solid #999;
                    border-radius: 8px;
                    cursor: pointer;
                    transition: all 0.2s;
                `;
                
                button.addEventListener('click', function() {
                    checkAnswer(parseInt(this.textContent));
                });

                button.addEventListener('mouseenter', function() {
                    this.style.background = '#e0e0e0';
                    this.style.transform = 'scale(1.05)';
                });

                button.addEventListener('mouseleave', function() {
                    this.style.background = '#f0f0f0';
                    this.style.transform = 'scale(1)';
                });

                answerOptions.appendChild(button);
            });

            feedbackMessage.style.display = 'none';
        }

        function checkAnswer(answer) {
            attempts++;
            attemptsDisplay.textContent = attempts;

            const buttons = answerOptions.querySelectorAll('button');
            buttons.forEach(btn => btn.disabled = true);

            if (answer === currentAnswer) {
                score++;
                scoreDisplay.textContent = score;
                
                feedbackMessage.style.display = 'block';
                feedbackMessage.style.background = '#d4edda';
                feedbackMessage.style.color = '#155724';
                feedbackMessage.textContent = `🎉 Correct! ${currentAnswer} is the next number in the sequence!`;
            } else {
                feedbackMessage.style.display = 'block';
                feedbackMessage.style.background = '#f8d7da';
                feedbackMessage.style.color = '#721c24';
                feedbackMessage.textContent = `Try again! The correct answer is ${currentAnswer}. Keep practicing!`;
            }
        }

        newQuestionBtn.addEventListener('click', generateQuestion);

        // Initial question
        generateQuestion();
    }

    /**
     * Initialize Multiplication Connection visualizer
     */
    function initMultiplicationConnection() {
        const container = document.getElementById('multiplication-connection');
        if (!container) return;

        container.innerHTML = `
            <div class="interactive-box" style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); padding: 20px; border-radius: 15px; color: #333; max-width: 600px; margin: 20px auto;">
                <h3 style="text-align: center; margin-top: 0; color: #667eea;">🔢 Skip Counting = Multiplication!</h3>
                
                <div style="background: white; padding: 20px; border-radius: 10px; border: 3px solid #667eea;">
                    <label for="groups-input" style="font-weight: bold; display: block; margin-bottom: 10px;">
                        How many groups of 2?
                    </label>
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                        <span style="font-weight: bold; color: #667eea;">Slider value</span>
                        <span id="groups-slider-value" style="display: inline-flex; align-items: center; justify-content: center; min-width: 52px; padding: 6px 12px; border-radius: 999px; background: #667eea; color: white; font-weight: bold;">5</span>
                    </div>
                    <input 
                        type="range" 
                        id="groups-input" 
                        min="1" 
                        max="10" 
                        value="5" 
                        style="width: 100%; margin-bottom: 10px;"
                    />
                    <div style="text-align: center; font-size: 24px; font-weight: bold; color: #667eea; margin-bottom: 20px;">
                        <span id="groups-display">5</span> groups
                    </div>

                    <div id="visual-groups" style="margin: 20px 0; min-height: 150px;">
                        <!-- Visual groups will be displayed here -->
                    </div>

                    <div style="background: #e7f3ff; padding: 15px; border-radius: 8px; margin-top: 20px;">
                        <div style="font-weight: bold; color: #0066cc; margin-bottom: 10px;">Skip Counting:</div>
                        <div id="skip-count-display" style="font-size: 18px; color: #333; margin-bottom: 10px;">
                            2, 4, 6, 8, 10
                        </div>
                        
                        <div style="font-weight: bold; color: #0066cc; margin-bottom: 10px;">Multiplication:</div>
                        <div id="multiplication-display" style="font-size: 20px; font-weight: bold; color: #333;">
                            5 × 2 = 10
                        </div>
                    </div>
                </div>
            </div>
        `;

        const groupsInput = document.getElementById('groups-input');
        const groupsDisplay = document.getElementById('groups-display');
        const groupsSliderValue = document.getElementById('groups-slider-value');
        const visualGroups = document.getElementById('visual-groups');
        const skipCountDisplay = document.getElementById('skip-count-display');
        const multiplicationDisplay = document.getElementById('multiplication-display');

        function updateDisplay() {
            const numGroups = parseInt(groupsInput.value);
            groupsDisplay.textContent = numGroups;
            groupsSliderValue.textContent = numGroups;

            // Draw visual groups
            let groupsHTML = '';
            for (let g = 0; g < numGroups; g++) {
                groupsHTML += '<div style="display: inline-block; margin: 5px; padding: 8px; border: 2px dashed #667eea; border-radius: 8px; background: #f8f9fa;">';
                for (let i = 0; i < 2; i++) {
                    groupsHTML += '<span style="display: inline-block; width: 20px; height: 20px; background: #4ECDC4; border-radius: 50%; margin: 2px; border: 2px solid #2eb3aa;"></span>';
                }
                groupsHTML += '</div>';
            }
            visualGroups.innerHTML = groupsHTML;

            // Generate skip counting sequence
            let skipSequence = [];
            for (let i = 1; i <= numGroups; i++) {
                skipSequence.push(i * 2);
            }
            skipCountDisplay.textContent = skipSequence.join(', ');

            // Show multiplication
            const total = numGroups * 2;
            multiplicationDisplay.textContent = `${numGroups} × 2 = ${total}`;
        }

        groupsInput.addEventListener('input', updateDisplay);

        // Initial display
        updateDisplay();
    }

    // Initialize when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            initNumberLineJump();
            initSkipCountingPractice();
            initMultiplicationConnection();
        });
    } else {
        initNumberLineJump();
        initSkipCountingPractice();
        initMultiplicationConnection();
    }
})();

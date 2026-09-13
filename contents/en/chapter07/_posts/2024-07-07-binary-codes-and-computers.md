---
layout: post
title: Binary Codes - How Computers Count
chapter: '07'
order: 7
owner: Math-Lover Team
lang: en
categories: [chapter07]
lesson_type: required
---
## Hook

A light switch has two states: off and on.

A computer is a city of tiny switches. Off means 0. On means 1. Every photo, song, and game is a long message written with only those two digits.

![A binary on-off scene]({{ site.baseurl }}/img/chapter_img/chapter07/09_binary.svg)

---

## Objectives

By the end of this lesson, learners can:

- explain that binary uses only 0 and 1
- convert a small whole number from decimal to binary
- convert a short binary string back to decimal
- say why computers like two states

---

## What We Already Know

You already know place value in base ten: ones, tens, hundreds.

$$237 = 2 \times 100 + 3 \times 10 + 7 \times 1$$

Today the places become ones, twos, fours, eights, … — powers of two instead of powers of ten.

![A powers chart — each step multiplies by 2](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Powers_chart.png/960px-Powers_chart.png)

*Image: Wikimedia Commons — math diagram*

---

## Discovery Puzzle

How would you write the number 13 if you were only allowed the digits 0 and 1?

Try building 13 from the blocks 8, 4, 2, and 1. Which blocks do you need? Which do you skip?

The pattern of “need” and “skip” *is* the binary number.

---

## Core Idea

**Binary** (base two) uses only the digits 0 and 1.

### A small dictionary

| Decimal | Binary |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 10 |
| 3 | 11 |
| 4 | 100 |
| 5 | 101 |
| 6 | 110 |
| 7 | 111 |
| 8 | 1000 |
| 9 | 1001 |
| 10 | 1010 |

Notice the jump at 2, 4, and 8 — each new place is worth twice the one before it.

### Decimal to binary: divide by 2, keep the remainders

Convert 13.

- $$13 \div 2 = 6$$ remainder $$1$$
- $$6 \div 2 = 3$$ remainder $$0$$
- $$3 \div 2 = 1$$ remainder $$1$$
- $$1 \div 2 = 0$$ remainder $$1$$

Read the remainders **upward**: $$1101$$.

Check with places:

$$1 \times 8 + 1 \times 4 + 0 \times 2 + 1 \times 1 = 13$$

![Binary decomposition of a number into powers of two](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Binary_decomposition.png/960px-Binary_decomposition.png)

*Image: Wikimedia Commons — math diagram*

### Why machines use binary

Electric circuits are happy with two clear states:

- current flowing: $$1$$
- current off: $$0$$

Ten different voltages would be easier to confuse. Two voltages are sturdy.

---

## Guided Discovery Activities

### Activity 1: To binary

Convert:

- 7 → $$111$$ ($$4 + 2 + 1$$)
- 10 → $$1010$$ ($$8 + 2$$)

### Activity 2: Back to decimal

Convert:

- $$100$$ → $$4$$
- $$1111$$ → $$15$$ ($$8 + 4 + 2 + 1$$)

### Activity 3: Bits and a byte

A **bit** is one binary digit.

Eight bits make one **byte**.

One byte can store any whole number from 0 to 255, because

$$2^{8} = 256$$

different patterns (including 00000000).

![Programming code as a reminder that machines store messages in bits](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/960px-Programming_code.jpg)

*Image: Wikimedia Commons*

---

## Example Walkthrough

### Example 1

Convert 5.

Remainders of dividing by 2: 1, then 0, then 1. Read upward: $$101$$.

$$4 + 1 = 5$$.

### Example 2

Convert 12.

$$12 = 8 + 4$$, so the eights and fours lights are on: $$1100$$.

### Example 3

Convert $$101$$ to decimal.

$$1 \times 4 + 0 \times 2 + 1 \times 1 = 5$$.

---

## Math Through Time

**Gottfried Leibniz** (1646–1716) wrote about a number system that needed only 0 and 1.

**George Boole** (1815–1864) built an algebra of true and false — another pair, like 1 and 0. Modern computers stand on both ideas.

Today every image is a grid of tiny lights, each stored with bits. A black-and-white pixel is almost a single bit: dark or bright.

---

## Challenge Ladder

Level 1: Convert 5, 12, and 20 to binary.

Level 2: Convert $$101$$, $$1100$$, and $$10000$$ to decimal.

Level 3: What is the smallest number of bits you need to write 20? Prove it by listing the place values.

Level 4: If one extra bit doubles the number of patterns, how many patterns can 4 bits make? How many can 5 bits make?

---

## Watch and Learn

Popular educational videos to reinforce this lesson:

1. [Introduction to number systems and binary — Khan Academy](https://www.youtube.com/watch?v=ku4KOFQ-bB4) — Khan Academy
2. [The binary number system — Khan Academy](https://www.youtube.com/watch?v=sXxwr66Y79Y) — Khan Academy
3. [Decimal Place Value — Math Antics](https://www.youtube.com/watch?v=KG6ILNOiMgM) — Math Antics

*Videos: YouTube — educational channels suitable for ages 8–10*

---

## Parent Corner

This is an applications lesson: the same place-value idea, with 2 playing the role of 10.

Helpful prompts:

- "Which power-of-two blocks do we need?"
- "Did we read the remainders from the last one back to the first?"
- "What does a single bit mean in a light-switch story?"

You can play “on/off cards” with four cards labeled 8, 4, 2, and 1. Flip cards face-up to build numbers from 0 to 15.

---

## Thinking Questions

1. Why is 2 written as $$10$$ in binary, not as “2”?
2. How is a computer’s 0 and 1 like a light switch?
3. If every extra bit doubles the patterns, why do photos take so many bytes?

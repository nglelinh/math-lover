---
layout: post
title: Optional — Even and Odd Inside Computers
chapter: '01'
order: 90
owner: Math-Lover Team
lang: en
categories: [chapter01]
lesson_type: optional
modern_apps: true
---
## Hook

A night-light is either **on** or **off**. There is no “a little bit on.”

Computers are built from millions of tiny night-lights. Each one stores a yes-or-no. That simple pair is the same pairing idea you already used with socks.

![Even and odd numbers on a number line](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/EvenOddNumberLine.svg/960px-EvenOddNumberLine.svg.png)

*Image: Wikimedia Commons — math diagram*

---

## Objectives

By the end of this optional note, learners can:

- connect even numbers to complete pairs, and odd numbers to one leftover
- explain a computer **bit** as an on/off switch
- notice that the last switch being off or on matches even or odd

---

## What We Already Know

You already know the pair test: 8 stickers make two equal groups; 9 leaves one leftover.

Today we look at the same rule hiding inside phones, games, and school tablets.

![On and off computer switches in pairs]({{ site.baseurl }}/img/chapter_img/chapter01/90_even_odd_computer.svg)

---

## Discovery Puzzle

Draw four lamps in a row. Turn them on, off, on, off.

- How many lamps are on?
- How many lamps are off?
- If you add one more lamp, can you still make perfect on/off pairs?

Do not name “binary” yet. Just sort: complete pairs, or one leftover.

---

## Core Idea

A **bit** is a computer’s smallest yes-or-no. People write it as $$0$$ (off) or $$1$$ (on).

The [CS Unplugged binary cards](https://www.csunplugged.org/en/topics/binary-numbers/) show the same idea with paper cards: each card is a double of the one before it.

When a whole number of bits is even, the last leftover test is “off.” When it is odd, the last leftover test is “on.”

$$8 = 2 \times 4 \quad \text{(even, last switch 0)}$$

$$9 = 2 \times 4 + 1 \quad \text{(odd, last switch 1)}$$

That is not a new rule. It is the sock rule written in computer language.

Sound on/off, dark mode on/off, and “two-player turn” are all pair stories. A list of 16 tiny switches can make many patterns, but each switch still has only two jobs. The wonder is not a new operation — it is noticing that pairing scales from socks to screens.

![Binary place values as on/off cards](https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Binary_decomposition.png/960px-Binary_decomposition.png)

*Image: Wikimedia Commons — math diagram*

---

## Try the Explorer

Move the slider. Watch the lights pair up.

<div id="apps-even-bit"></div>

Guided questions:

- What changes from 8 to 9?
- Why does 10 look “tidy” again?

---

## Guided Discovery Activities

### Activity 1: Paper bits

Cut four cards labeled 8, 4, 2, and 1 (the CS Unplugged sizes). Show 6 by turning on 4 and 2. Is 6 even? Are the on cards a complete pair story?

### Activity 2: Two-player turns

Many coding games (see [Code.org Hour of Code](https://hourofcode.com/) and [Scratch](https://scratch.mit.edu/)) take turns: player 1, player 2, player 1… Turn numbers are odd or even. Who moves on turn 7?

### Activity 3: House numbers

Street numbers still use even/odd sides. A computer listing those houses only needs the last bit to sort left and right.

![House numbers along a street](https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Coltman_Street%2C_Hull_-_geograph.org.uk_-_1194325.jpg/960px-Coltman_Street%2C_Hull_-_geograph.org.uk_-_1194325.jpg)

*Image: Wikimedia Commons*

---

## Example Walkthrough

Is 14 even for a computer?

$$14 \div 2 = 7$$ leftover $$0$$. Last switch off. Even.

Is 15 even?

$$15 \div 2 = 7$$ leftover $$1$$. Last switch on. Odd.

---

## Watch and Learn

Popular educational videos to reinforce this lesson:

1. [Introduction to even and odd numbers — Khan Academy](https://www.youtube.com/watch?v=SFRTTUtAjg4)
2. [The binary number system — Khan Academy](https://www.youtube.com/watch?v=sXxwr66Y79Y)
3. [Even and Odd Numbers — Math for Kids](https://www.youtube.com/watch?v=eF_FxSW8QwY)

*Videos: YouTube — educational channels suitable for ages 8–10*

---

## Thinking Questions

1. Why is a leftover of 1 enough to call a number odd?
2. If a game stores “sound on / sound off,” is that more like 2 or like 100?
3. Can you invent a dance that is even steps only?

---

## Challenge

Using cards 8, 4, 2, and 1, make 11. Is 11 odd? How does the 1-card tell you without dividing?

---

## Parent Corner

This note does not teach programming. It shows that pairing is a tool computers still use. Praise “I can show the leftover,” not memorizing the word *bit*. If the child wants more, try CS Unplugged cards or a free Hour of Code puzzle — no account required for many activities.

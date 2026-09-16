---
layout: post
title: Optional — Skip Counting Is a Coding Loop
chapter: '02'
order: 90
owner: Math-Lover Team
lang: en
categories: [chapter02]
lesson_type: optional
modern_apps: true
---
## Hook

A cartoon cat takes 5 steps, then 5 more, then 5 more.

A child could write: 5, 10, 15, 20.

A computer writes the same idea as **repeat 4 times: add 5**.

That is skip counting wearing a green “start” flag.

![Number line showing even and odd steps](https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/EvenOddNumberLine.svg/960px-EvenOddNumberLine.svg.png)

*Image: Wikimedia Commons — math diagram*

---

## Objectives

By the end of this optional note, learners can:

- see a **repeat** block as skip counting
- predict the next value after $$n$$ jumps of size $$k$$
- try the idea in a kid coding playground without needing a full programming course

---

## What We Already Know

You already skip count by 2s, 5s, and 10s. You know that $$4 \times 5 = 20$$ is four groups of five.

Today those groups become a loop: same jump, again and again.

![Skip counting drawn as a repeat loop]({{ site.baseurl }}/img/chapter_img/chapter02/90_skip_loop.svg)

---

## Discovery Puzzle

Start at 0. Jump +5 four times.

Write every landing: ?, ?, ?, ?, ?

Now start at 2 and jump +5 four times. What changes? What stays the same?

---

## Core Idea

A **loop** is a polite way to say “do this jump a chosen number of times.”

If you start at $$s$$ and add $$k$$ each time, after $$n$$ repeats you land on:

$$s + n \times k$$

Example: start 0, jump 5, repeat 4:

$$0 + 4 \times 5 = 20$$

The list 0, 5, 10, 15, 20 is the story. The formula is the shortcut.

![Arithmetic jumps along a path](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Academ_Arithmetic_progressions_along_a_knotted_loop.svg/960px-Academ_Arithmetic_progressions_along_a_knotted_loop.svg.png)

*Image: Wikimedia Commons — math diagram*

Scratch (from the MIT Scratch Team) uses a purple **repeat** block for exactly this. [Code.org](https://code.org/) dance and game puzzles use the same “move, then do it again” idea. You do not need to finish a whole course — one puzzle is enough to feel the loop.

Notice the two jobs in a loop: **what to repeat** (the jump size) and **how many times**. Mix them up and the path changes. A clock that skip-counts by 5s is a loop that always uses the same jump; a dance that hops 2, then 2, then 2 is the same structure with a smaller $$k$$.

---

## Try the Explorer

Change the start, the jump, and the number of repeats.

<div id="apps-skip-loop"></div>

Guided questions:

- If you only change “repeats,” which numbers stay in the list?
- How is this like counting coins of the same value?

---

## Guided Discovery Activities

### Activity 1: Clap loop

Clap every 2 counts up to 20. That is a repeat loop you can hear.

### Activity 2: Animation frames

Many cartoons draw a wing every 2 frames. Count 2, 4, 6, 8… The picture “flaps” because the computer skip-counts frames.

### Activity 3: Try a playground

Open [Scratch Getting Started](https://scratch.mit.edu/) or an [Hour of Code](https://hourofcode.com/) maze. Find a block that means “do this again.” Predict the path before you press start.

![Lines of programming as repeated instructions](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/960px-Programming_code.jpg)

*Image: Wikimedia Commons*

---

## Example Walkthrough

A sprite starts at step 10 and hops +10 three times.

List: 10, 20, 30, 40.

Shortcut: $$10 + 3 \times 10 = 40$$.

That is skip counting by 10s, the “magic zero” pattern, written as a loop.

---

## Watch and Learn

Popular educational videos to reinforce this lesson:

1. [Getting Started with Scratch — Scratch Team](https://www.youtube.com/watch?v=9jTPZfhuVro)
2. [Intro to multiplication — Khan Academy](https://www.youtube.com/watch?v=RNxwasijbAo)
3. [Number Patterns — Math Antics](https://www.youtube.com/watch?v=vV7C7bXm4VI)

*Videos: YouTube — educational channels suitable for ages 8–10*

---

## Thinking Questions

1. Why does changing the start move the whole list, but keep the gaps?
2. Is “repeat 0 times” a sensible loop? What list do you get?
3. How is skip counting by 10s secretly a place-value loop?

---

## Challenge

A dance puzzle repeats “move 3 steps” eight times from 0. Where does the dancer finish? Can you show it two ways: a list and a multiplication?

---

## Parent Corner

The goal is the *aha*: computers are not magicians; they are patient skip-counters. Stay with one short puzzle. Ask “What will happen if we repeat one more time?” before pressing the green flag.

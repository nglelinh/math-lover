---
layout: post
title: "Optional — The Mystery Box Is a Game Score"
chapter: '03'
order: 90
owner: Math-Lover Team
lang: en
categories: [chapter03]
lesson_type: optional
---
## Hook

In the mystery-box lesson, a letter hid a number: $$n + 3 = 7$$.

In a coding game, a box labeled **score** hides a number too. Catch a star, and the box changes. That is the same idea — a name that remembers a value.

![Balance scale for hidden numbers](https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Balance_scale.svg/960px-Balance_scale.svg.png)

*Image: Wikimedia Commons — math diagram*

---

## Objectives

By the end of this optional note, learners can:

- treat a game **score** or **lives** box as a variable
- update the box with +1 or −1 and say the new value
- see why programmers pick names instead of rewriting every number

---

## What We Already Know

You already solved $$n + 5 = 12$$ by asking “what number makes this true?”

Today the number can change while you play, but the *name* stays the same.

![A score box that remembers a changing number]({{ site.baseurl }}/img/chapter_img/chapter03/90_score_variable.svg)

---

## Discovery Puzzle

A cat has `lives = 3`.

It bumps a cactus: lives become 2.
It finds a heart: lives become 3 again.

Which thing changed — the name, or the number inside?

If someone writes `lives + 1 = 4`, what is `lives` now?

---

## Core Idea

A **variable** is a labeled box. In algebra the label might be $$n$$. In [Scratch](https://scratch.mit.edu/) the official tutorial calls it a variable that can hold a score or a word.

When you catch a star:

$$\text{score} \leftarrow \text{score} + 1$$

Read that as “put the old score plus one back into the same box.”

Harvard’s [CS50 Scratch notes](https://cs50.harvard.edu/scratch/notes/7/) use the same picture: make a variable, set it, then change it.

You do not need adult machine-learning words. You only need: **name, value, change**.

A second common box is `x` or `y` for where a sprite stands on the screen. Move right, and `x` grows. That is still the mystery-box habit: the letter stays, the number updates. If two sprites each have their own `score`, the names look the same but the boxes are different — like two envelopes both labeled “stars.”

![Lines of code as named instructions](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/Programming_code.jpg/960px-Programming_code.jpg)

*Image: Wikimedia Commons*

---

## Try the Explorer

Catch stars and miss clouds. Watch the box.

<div id="apps-variable-box"></div>

Guided questions:

- After three stars, what equation is true: $$\text{score} = ?$$
- If score is 4 and you want 7, what change do you need?

---

## Guided Discovery Activities

### Activity 1: Paper scoreboard

Write `score` on an envelope. Put 0 inside. Each time a sock lands in a basket, replace the paper with a new number. The envelope name never changes.

### Activity 2: Scratch peek

Open Scratch, click **Variables → Make a Variable**, name it `score`. The orange blocks “set score to 0” and “change score by 1” are algebra you can click.

### Activity 3: Two boxes

Make `stars` and `clouds`. If stars = 5 and clouds = 2, what is stars − clouds? Two mystery boxes at once.

---

## Example Walkthrough

Start: $$\text{score} = 0$$.

Three stars: $$0 + 1 + 1 + 1 = 3$$.

One miss: $$3 - 1 = 2$$.

The sentence “score is 2” is the same kind of sentence as “$$n = 2$$.”

---

## Watch and Learn

Popular educational videos to reinforce this lesson:

1. [What Are Variables and Lists in Scratch? — Scratch Team](https://www.youtube.com/watch?v=kRJ37shzFp0)
2. [What Is Algebra? — Math Antics](https://www.youtube.com/watch?v=NybHckSEQBI)
3. [How to Make a Jumping Game in Scratch — Scratch Team](https://www.youtube.com/watch?v=1jHvXakt1qw)

*Videos: YouTube — educational channels suitable for ages 8–10*

---

## Thinking Questions

1. Why is a name useful if the number keeps changing?
2. Could two different names hold the same number? Give a game example.
3. What happens if you forget to set score back to 0 at the start?

---

## Challenge

A jumping game starts with `score = 0` and `level = 1`. Every 5 stars, level increases by 1. After 12 stars, what is level? Use a table, not a guess.

---

## Parent Corner

This is optional enrichment, not a new algebra chapter. If Vietnamese Chapter 3 already has programming stories, this English note is only a short bridge: mystery box ↔ score box. Celebrate clear “the box now holds…” sentences.

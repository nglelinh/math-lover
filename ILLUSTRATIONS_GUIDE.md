# Illustrations Guide for Math-Lover Lessons

This guide explains how to add illustrations (both static Python-generated images and interactive JavaScript components) to your math lessons.

## Overview

We've created two types of illustrations to enhance learning:

1. **Static Visualizations** - Python-generated SVG or PNG images showing mathematical concepts
2. **Interactive Components** - JavaScript-powered interactive explorers and games

---

## 📁 File Structure

```
math-lover/
├── scripts/illustrations/          # Python scripts to generate images
│   ├── generate_even_numbers.py
│   ├── generate_skip_counting.py
│   └── generate_fractions.py
│   ├── generate_child_friendly_svgs.py
│   └── update_lesson_image_refs.py
├── img/chapter_img/                # Generated images stored here
│   ├── chapter01/
│   ├── chapter02/
│   └── chapter04/
└── public/js/                      # Interactive JavaScript components
    ├── interactive-even-numbers.js
    ├── interactive-skip-counting.js
    └── interactive-fractions.js
```

---

## 🐍 Generating Static Visualizations

### Visual Style for Children

Pictures for children should be:

- clear at a glance
- bold in shape, color, and contrast
- focused on one main idea per picture
- free from clutter, tiny labels, and too many competing elements

If a concept needs several parts, prefer multiple simple pictures over one crowded picture.

### Step 1: Run Python Scripts

Navigate to the scripts directory and run the generators:

```bash
cd scripts/illustrations
python3 generate_even_numbers.py
python3 generate_skip_counting.py
python3 generate_fractions.py
python3 generate_child_friendly_svgs.py
python3 update_lesson_image_refs.py
```

This creates the lesson illustration files inside `img/chapter_img/chapter##/`.
For the current bilingual lessons, prefer the child-friendly SVG workflow because it is:

- easier to keep clear and bold for children
- lighter to load locally and on GitHub Pages
- simpler to update consistently across many lessons

### Step 2: Add Images to Markdown Lessons

In your lesson markdown files, reference images with `{{ site.baseurl }}/img` so they work both locally and on GitHub Pages:

```markdown
## Core Idea

Even numbers split perfectly into 2 equal groups!

![Even Number Pattern]({{ site.baseurl }}/img/chapter_img/chapter01/03_even_vs_odd.svg)

As you can see from the visualization above...
```

For the simplified lesson visuals, prefer `.svg` references whenever a matching file exists.

---

## Available Static Visualizations

### Chapter 01: Even Numbers

| File | Description |
|------|-------------|
| `01_even_number_pattern.png` | Number line showing even numbers highlighted |
| `02_even_pairs.png` | Visual showing even numbers as pairs of objects |
| `03_even_vs_odd.png` | Side-by-side comparison of even and odd |
| `04_double_pattern.png` | Bar chart showing doubling pattern |

**Example usage in lesson:**

```markdown
![Even vs Odd Comparison]({{ site.baseurl }}/img/chapter_img/chapter01/03_even_vs_odd.png)

Notice how even numbers split perfectly, while odd numbers always have one left over!
```

### Chapter 02: Skip Counting by 2s

| File | Description |
|------|-------------|
| `01_number_line_jumps.png` | Number line with jump arcs showing +2 pattern |
| `02_towers_of_two.png` | Visual stacks showing counting by 2s |
| `03_socks_pairs.png` | Real-world example with socks |
| `04_skip_count_pattern.png` | Grid showing skip counting sequence |
| `05_multiplication_connection.png` | Shows skip counting = multiplication |

**Example usage in lesson:**

```markdown
## Guided Discovery Activity

![Number Line Jumps]({{ site.baseurl }}/img/chapter_img/chapter02/01_number_line_jumps.png)

Start at 0 and jump forward 2 spaces each time. Where do you land?
```

### Chapter 04: Fractions (Halves and Quarters)

| File | Description |
|------|-------------|
| `01_halves_shapes.png` | Different shapes divided into halves |
| `02_quarters_shapes.png` | Different shapes divided into quarters |
| `03_half_vs_quarter.png` | Size comparison of 1/2 vs 1/4 |
| `04_fractions_adding.png` | Visual showing how fractions add up |
| `05_real_world_fractions.png` | Clocks, money, sports examples |

**Example usage in lesson:**

```markdown
## Core Idea

### Halves (1/2)

![Shapes Divided into Halves]({{ site.baseurl }}/img/chapter_img/chapter04/01_halves_shapes.png)

When you split something into 2 equal parts, each part is called one-half or 1/2.
```

---

## 🎮 Adding Interactive Components

### Vietnamese Lesson Workflow (Required)

Vietnamese lesson posts now use a shared interactive bundle and a central mapping file. You should not add chapter-specific script tags inside Vietnamese markdown files.

#### Step 1: Add a mapping entry

Create or update the matching entry in [`_data/vi_interactive_lessons.json`](/Users/nguyenlelinh/teaching/math-lover/_data/vi_interactive_lessons.json). The key must be the lesson source path.

```json
"contents/vi/chapter04/_posts/2026-03-28-vi-du-bai-moi.md": {
  "template": "fraction-lab",
  "mode": "fractions",
  "container_id": "vi-interactive-2026-03-28-vi-du-bai-moi",
  "guidance": "Em hãy đổi số phần được tô rồi so sánh phần đang chọn với cả hình ban đầu."
}
```

Available reusable templates:

- `number-lab`
- `array-lab`
- `fraction-lab`
- `measurement-lab`
- `geometry-lab`
- `data-lab`
- `sequence-lab`
- `balance-lab`
- `challenge-lab`

#### Step 2: Add the include marker to the lesson markdown

Insert the standard include near the end of the lesson, usually before `## Góc cha mẹ`:

```markdown
<!-- vi-interactive:start -->
{% include vi-interactive-lesson.html %}
<!-- vi-interactive:end -->
```

#### Step 3: Run the required coverage check

```bash
python3 scripts/check_vi_interactive_coverage.py
```

This check fails when a published Vietnamese lesson is missing the include marker or a mapping entry.

### Legacy English / Chapter-Specific Components

English lessons still use the older chapter-specific JavaScript files. Those components remain available below for legacy content and English-only pages.

---

## Available Interactive Components

### Chapter 01: Even Numbers

**1. Even Number Explorer** - Test if numbers are even or odd

```markdown
<div id="even-number-explorer"></div>
```

**2. Pattern Recognizer** - Click numbers to reveal the pattern

```markdown
<div id="pattern-recognizer"></div>
```

**Example in lesson:**

```markdown
## Guided Discovery Activity

### Activity 1: The Even Number Explorer

<div id="even-number-explorer"></div>

Pick any number between 1 and 100. The explorer will:
- Show you if it's even or odd
- Split it into two groups visually
- Help you understand WHY it's even or odd
```

### Chapter 02: Skip Counting by 2s

**1. Number Line Jump** - Animated frog jumping by 2s

```markdown
<div id="number-line-jump"></div>
```

**2. Skip Counting Practice** - Quiz game

```markdown
<div id="skip-counting-practice"></div>
```

**3. Multiplication Connection** - Shows skip counting = multiplication

```markdown
<div id="multiplication-connection"></div>
```

**Example in lesson:**

```markdown
## Guided Discovery Activity

### Activity 1: The Number Line Jump Game

<div id="number-line-jump"></div>

Watch the kangaroo jump by 2s! Each jump moves forward exactly 2 spaces on the number line.

---

### Activity 2: Practice Your Skills

<div id="skip-counting-practice"></div>

Can you figure out what number comes next in the sequence?
```

### Chapter 04: Fractions

**1. Pizza Fraction Cutter** - Cut pizza into halves or quarters

```markdown
<div id="pizza-fraction-cutter"></div>
```

**2. Fraction Comparison** - Which is bigger, 1/2 or 1/4?

```markdown
<div id="fraction-comparison"></div>
```

**3. Fraction Builder** - Add fractions to make a whole

```markdown
<div id="fraction-builder"></div>
```

**Example in lesson:**

```markdown
## Guided Discovery Activity

### Activity 1: Pizza Party!

<div id="pizza-fraction-cutter"></div>

How should we cut the pizza if 2 people want to share? What about 4 people?

---

### Activity 2: Which Piece is Bigger?

<div id="fraction-comparison"></div>

If you could choose between 1/2 of a pizza or 1/4 of the same pizza, which would you pick?
```

---

## 🎨 Combining Static and Interactive

For the best learning experience, combine both types:

```markdown
## Core Idea

Even numbers split perfectly into 2 equal groups!

![Even vs Odd Comparison]({{ site.baseurl }}/img/chapter_img/chapter01/03_even_vs_odd.png)

The image above shows how even numbers (like 4, 6, 8) can be split into two equal groups with nothing left over. Odd numbers (like 3, 5, 7) always have one left over.

---

## Guided Discovery Activity

Now try it yourself with any number you like:

<div id="even-number-explorer"></div>

Pick different numbers and watch how they split. Can you predict if a number will be even or odd just by looking at it?
```

---

## 📝 Best Practices

### When to Use Static Images

✅ **Use static images for:**
- Explaining concepts clearly
- Showing patterns at a glance
- Comparing multiple examples side-by-side
- Historical or real-world examples
- Step-by-step visual walkthroughs

### When to Use Interactive Components

✅ **Use interactive components for:**
- Hands-on exploration and experimentation
- Practice and skill-building
- Testing predictions
- Games and challenges
- Discovery-based learning activities

### Placement Tips

1. **Introduction section**: Start with a static image showing the concept
2. **Core Idea section**: Use static visualizations to explain
3. **Guided Discovery Activity**: Add interactive components here!
4. **Example Exploration**: Mix static images with interactive practice
5. **Challenge Ladder**: Use interactive components for all levels

### Responsive Design

Both static images and interactive components are responsive:
- Images automatically scale to fit the screen
- Interactive components adjust to mobile/tablet screens
- Test on different devices to ensure good experience

---

## 🔧 Customizing Illustrations

### Modifying Python Scripts

Edit the Python scripts in `scripts/illustrations/` to:
- Change colors (update the `colors` array)
- Adjust sizes and layouts
- Add new visualization types
- Change number ranges

After editing, regenerate:

```bash
cd scripts/illustrations
python3 generate_even_numbers.py
```

### Customizing JavaScript

Edit files in `public/js/` to:
- Change color schemes (look for hex colors like `#667eea`)
- Adjust difficulty levels
- Add new features
- Modify animations

Changes to JavaScript are immediately reflected (just refresh the page).

---

## 🌐 Bilingual Support

When adding illustrations to both English and Vietnamese lessons:

1. **Static images** work for both languages (they're visual)
2. **English interactive components** can continue using the legacy chapter-specific files
3. **Vietnamese lesson pages** must use the shared include plus `_data/vi_interactive_lessons.json`

For Vietnamese versions:
- add the `vi-interactive-lesson.html` include marker
- add or update the matching entry in [`_data/vi_interactive_lessons.json`](/Users/nguyenlelinh/teaching/math-lover/_data/vi_interactive_lessons.json)
- rely on `_layouts/post.html` to load `public/js/interactive-vi-lessons.js` automatically when `page.lang == 'vi'`
- run `python3 scripts/check_vi_interactive_coverage.py`

---

## 📦 Example: Complete Lesson with Illustrations

Here's a complete example showing both types:

```markdown
---
layout: post
title: Discovering Even Numbers
chapter: '01'
order: 1
lang: en
---

## Hook

Have you ever tried sharing candy with a friend? Some numbers share perfectly—others don't!

## Core Idea

![Even Number Pattern]({{ site.baseurl }}/img/chapter_img/chapter01/01_even_number_pattern.png)

Even numbers are special because they split into 2 equal groups. Look at the pattern above—do you notice something?

---

## Guided Discovery Activity

### Activity 1: Test Any Number

<div id="even-number-explorer"></div>

Try numbers like 8, 15, 24, and 37. What pattern do you notice?

---

### Activity 2: Find All Even Numbers

<div id="pattern-recognizer"></div>

Click on numbers from 1 to 20. Can you find all the even ones? Then click "Reveal" to check!

---

## Example Exploration

![Even vs Odd Comparison]({{ site.baseurl }}/img/chapter_img/chapter01/03_even_vs_odd.png)

Look closely at this comparison. What's the difference?

---

## Extension Activity

![Double Pattern]({{ site.baseurl }}/img/chapter_img/chapter01/04_double_pattern.png)

Here's a bonus discovery: Every even number is double of another number! Can you figure out the pattern?
```

---

## ✅ Checklist for Adding Illustrations

When adding illustrations to a lesson:

- [ ] Generate static images using Python scripts
- [ ] Verify images are saved to correct `chapter_img/chapter##/` folder
- [ ] Add image references using `{{ site.baseurl }}/img` in markdown
- [ ] For Vietnamese lessons, add the standard `vi-interactive-lesson.html` include marker
- [ ] For Vietnamese lessons, add a matching entry in `_data/vi_interactive_lessons.json`
- [ ] For English legacy lessons, verify the chapter-specific interactive container IDs still match the JavaScript file
- [ ] Test locally with `bundle exec jekyll serve`
- [ ] Verify images load correctly
- [ ] Verify interactive components work (desktop and mobile)
- [ ] Run `python3 scripts/check_vi_interactive_coverage.py` after Vietnamese lesson changes
- [ ] Add bilingual content if needed
- [ ] Commit images and code to repository

---

## 🚀 Next Steps

1. Review existing lessons (Chapter 01, 02, 04)
2. Add illustrations using this guide
3. Generate images for other chapters using similar Python scripts
4. Reuse the Vietnamese shared templates before creating new bespoke interactive widgets
5. Test with children to see what works best!

---

**Happy illustrating!** 🎨📊🎮

For questions or issues, check:
- `.cursor/rules/illustration-rule.mdc` for pedagogical guidelines
- Python script comments for technical details
- JavaScript comments for implementation notes

# Math-Lover: A Discovery-Based Math Course for Children (Ages 8-12)

A multilingual (English/Vietnamese) mathematics course website for children ages 8-12, built on Jekyll and GitHub Pages. This course emphasizes discovery-based learning, pattern recognition, and mathematical thinking rather than rote memorization.

## 🎯 Key Features

- ✅ Bilingual support (English/Vietnamese)
- ✅ Chapter-based content structure
- ✅ Responsive, child-friendly design
- ✅ MathJax support for mathematical formulas
- ✅ Automatic deployment to GitHub Pages
- ✅ Custom Jekyll plugins for multilingual support
- ✅ Discovery-based learning approach
- ✅ Parent-child guidance sections

**Target Audience:** Children ages 8-12 with parents/educators as guides

## 🚀 Getting Started

> 📖 **See detailed setup instructions in [SETUP.md](./SETUP.md) and [AGENTS.md](./AGENTS.md)**

### Step 1: Configure the Course

Edit `_config.yml`:

```yaml
# Setup
title:               "Math-Lover: Discovering Numbers"
description:         'A discovery-based math course for children ages 8-12'
url:                 https://nglelinh.github.io
baseurl:             '/math-lover'
imgurl:              /math-lover/img

# About/contact
author:
  name:              Your Name
  email:             your.email@example.com
```

### Step 2: Configure GitHub Pages

1. Go to **Settings > Pages**
2. Select **Source**: "GitHub Actions"
3. Workflows automatically run when you push code

### Step 3: Create Lesson Content

Edit homepage content in `home/_posts/`:
- `21-01-20-introduction.md` - Course introduction
- `21-01-20-contents.md` - Course outline
- `21-02-03-makers.md` - Creator information

Create chapter content in `contents/en/` and `contents/vi/`:

```
contents/
├── en/
│   ├── chapter01/
│   │   └── _posts/
│   │       └── 2024-01-01-discovering-numbers.md
│   ├── chapter02/
│   │   └── _posts/
│   │       └── 2024-01-15-patterns-and-sequences.md
│   └── ...
└── vi/
    ├── chapter01/
    │   └── _posts/
    │       └── 2024-01-01-kham-pha-con-so.md
    └── ...
```

**Lesson Format (Child-Friendly):**

```markdown
---
layout: post
title: Discovering Even and Odd Numbers
chapter: '01'
order: 1
owner: Your Name
lang: en
categories: [chapter01]
lesson_type: required  # or optional
---

## Objectives
What will children discover in this lesson...

## Introduction
A relatable story or scenario...

## Core Idea
Gradual explanation with concrete examples...

## Guided Discovery Activity
Short parent-child activities using objects or drawings...

## Example Exploration
Step-by-step walkthrough with numbers...

## Parent Insight
Mathematical ideas and cognitive skills being developed...

## Thinking Questions
Open-ended questions encouraging exploration...

## Extension Activity
Optional challenge for curious learners...

Use math formulas for clarity: $$2, 4, 6, 8, \ldots$$
```

## 📁 Cấu trúc thư mục

```
.
├── _config.yml              # Cấu hình Jekyll
├── _includes/               # Các component tái sử dụng
│   ├── head.html
│   └── sidebar.html
├── _layouts/                # Layouts cho pages
│   ├── default.html
│   ├── page.html
│   └── post.html
├── _plugins/                # Custom Jekyll plugins
│   ├── multilang.rb         # Hỗ trợ đa ngôn ngữ
│   ├── multilang_post_url.rb
│   ├── redirect_generator.rb
├── contents/                # Nội dung khóa học
│   ├── en/                  # Nội dung tiếng Anh
│   │   ├── chapter00/
│   │   ├── chapter01/
│   │   └── ...
│   └── vi/                  # Nội dung tiếng Việt
│       ├── chapter00/
│       ├── chapter01/
│       └── ...
├── home/                    # Trang chủ
│   └── _posts/
├── img/                     # Hình ảnh
│   └── chapter_img/
├── public/                  # CSS, JS, assets
│   ├── css/
│   ├── js/
│   └── logo.png
├── Gemfile                  # Ruby dependencies
├── index.html               # Trang chủ
└── README.md                # Hướng dẫn dự án
```

## 🛠️ Development

### Setup

```bash
# Install Ruby dependencies
bundle install

# Run Jekyll local server (with live reload)
bundle exec jekyll serve --livereload

# Access the site at
http://127.0.0.1:4000/your-baseurl/
```

### Adding New Chapters

1. Create directories: `contents/en/chapterXX/` and `contents/vi/chapterXX/`
2. Create `_posts/` subdirectories
3. Add markdown files: `YYYY-MM-DD-title.md`
4. Ensure complete front matter (chapter, order, lang, etc.)

### Adding Images

1. Place images in `img/chapter_img/`
2. Reference in markdown:

```markdown
![Alt text]({{ site.baseurl }}/img/chapter_img/your-image.png)
```

### Important: Bilingual Content

**Every lesson must be created in BOTH English and Vietnamese:**
- Add to `contents/en/chapterXX/_posts/` with `lang: en`
- Add to `contents/vi/chapterXX/_posts/` with `lang: vi`
- Use similar file names with translated titles

## 📚 Content Philosophy

### Age-Appropriate Learning Progression

- **Ages 8-9**: Number sense, place value, basic operations, simple fractions, shapes, patterns
- **Ages 9-10**: Multiplicative thinking, logic puzzles, fraction fluency, measurement
- **Ages 10-12**: Decimals, ratios, geometry, data, probability, introductory algebraic thinking

### Discovery-Based Approach

Each lesson follows a progression:
1. **Play & Exploration** - Children discover through hands-on activities
2. **Reasoning** - Guide children to notice patterns and ask questions
3. **Explanation** - Formalize the mathematical idea

Emphasize the "why" not the "what"—help children develop deep intuition.

## 🎨 Customization

### CSS

Edit files in `public/css/`:
- `lanyon.css` - Main layout
- `poole.css` - Base styles
- `syntax.css` - Code highlighting

### JavaScript

Edit files in `public/js/`:
- `script.js` - General functionality
- `multilang.js` - Language switching

## 📝 Mathematical Content

The course uses MathJax for mathematical formulas:

```markdown
Simple equation: $$2 + 3 = 5$$

Pattern notation: $$2, 4, 6, 8, \ldots$$

Multi-line equations:
$$
\begin{align}
\text{Length} &= 5 \text{ units} \\
\text{Width} &= 3 \text{ units} \\
\text{Area} &= 5 \times 3 = 15 \text{ square units}
\end{align}
$$
```

**Keep formulas minimal and child-friendly**—avoid complex notation that obscures concepts.

## 🌐 Multilingual Support

### Using Translation Tags

In templates:

```liquid
{% t home %}           <!-- Shows "Home" or "Trang chủ" -->
{% language_switch %}  <!-- Language switcher button -->
```

### Configure Translations

In `_config.yml`:

```yaml
t:
  en:
    title: "Math-Lover"
    home: "Home"
    chapters: "Chapters"
  vi:
    title: "Tình Yêu Toán Học"
    home: "Trang chủ"
    chapters: "Các chương"
```

## 📖 Documentation

- **[AGENTS.md](./AGENTS.md)** - Developer guidelines for contributing
- **[SETUP.md](./SETUP.md)** - Detailed setup instructions
- **[CONTRIBUTING.md](./CONTRIBUTING.md)** - Contribution guidelines
- **[Cursor Rules](./cursor/rules/)** - AI assistant guidelines

## 🤝 Contributing

To contribute lessons:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/chapter-XX-topic`
3. Add content to **BOTH** `contents/en/` and `contents/vi/`
4. Test locally: `bundle exec jekyll serve`
5. Submit a Pull Request

Please follow the [Lesson Writing Guidelines](./AGENTS.md) for age-appropriate, discovery-based content.

## 📄 License

This course template uses the Lanyon theme and is developed for educational purposes.

## 🙏 Credits

- **Theme**: [Lanyon](https://github.com/poole/lanyon) by Mark Otto
- **Jekyll**: Static site generator
- **MathJax**: Mathematical formula rendering
- **Inspiration**: Mathematical circles and discovery-based learning

## 📞 Support

If you encounter issues:
1. Check [Issues](../../issues)
2. Create a new issue if needed
3. See contact info in `_config.yml`

---

**Happy Teaching and Discovering! 🎓✨**

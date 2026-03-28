<!-- OPENSPEC:START -->
# OpenSpec Instructions

These instructions are for AI assistants working in this project.

Always open `@/openspec/AGENTS.md` when the request:
- Mentions planning or proposals (words like proposal, spec, change, plan)
- Introduces new capabilities, breaking changes, architecture shifts, or big performance/security work
- Sounds ambiguous and you need the authoritative spec before coding

Use `@/openspec/AGENTS.md` to learn:
- How to create and apply change proposals
- Spec format and conventions
- Project structure and guidelines

Keep this managed block so 'openspec update' can refresh the instructions.

<!-- OPENSPEC:END -->

# AGENTS.md
Operational guide for coding agents working in `math-lover`.

## Project Snapshot
- Stack: Jekyll (Ruby), Liquid templates, vanilla JavaScript, Markdown content, optional Python scripts.
- Domain: bilingual (English/Vietnamese) math course content for children.
- Deployment: GitHub Pages via `.github/workflows/jekyll.yml`.
- Primary quality gate: successful Jekyll build plus manual content checks.

## Rule Files To Apply
Cursor rules in `.cursor/rules/`:
1. `lecture-notes-rule.mdc`
2. `math-formula-rule.mdc`
3. `course-books-rule.mdc`
4. `illustration-rule.mdc`

Copilot rules:
- `.github/copilot-instructions.md` is not present in this repository.

If rules conflict, prioritize repository-specific bilingual and pedagogical requirements.

## Repository Layout
- `contents/en/`, `contents/vi/`: lesson content and chapter posts.
- `_plugins/`: custom Jekyll Ruby plugins.
- `_layouts/`, `_includes/`: Liquid templates.
- `public/js/`, `public/css/`: front-end assets.
- `img/chapter_img/`: lesson illustrations.
- `scripts/illustrations/`: Python generators for static images.
- `_config.yml`: site config, translations, URL settings.

## Setup Commands
```bash
bundle install
bundle exec jekyll clean
bundle exec jekyll serve --livereload
```

Docker alternative:
```bash
docker-compose up
```

## Build, Lint, and Test Commands
### Build
```bash
# Development build
bundle exec jekyll build

# Production-like build
JEKYLL_ENV=production bundle exec jekyll build

# CI-like Pages build (matches workflow)
bundle exec jekyll build --baseurl "/math-lover"
```

### Lint / Static Validation
No dedicated lint frameworks are configured (`rubocop`, `eslint`, `pytest` are absent).
Use syntax checks:
```bash
# Ruby plugin syntax
ruby -c _plugins/multilang.rb
ruby -c _plugins/multilang_post_url.rb
ruby -c _plugins/redirect_generator.rb
ruby -c _plugins/search_generator.rb

# Python script syntax
python3 -m py_compile scripts/illustrations/generate_even_numbers.py
python3 -m py_compile scripts/illustrations/generate_skip_counting.py
python3 -m py_compile scripts/illustrations/generate_fractions.py
```

### Test / Validation
Automated unit tests are not present. Main validation:
```bash
bundle exec jekyll build
bundle exec jekyll serve --livereload
```

Manual browser checks after serving:
- pages load without Liquid/build errors
- EN/VI language switch works
- search overlay and result navigation work
- images resolve via `{{ site.baseurl }}/img`
- MathJax formulas render
- mobile and desktop responsiveness look correct

### Running a Single Test (Important)
There is no true single-test runner. Use nearest equivalents:
```bash
# Check one Ruby file
ruby -c _plugins/search_generator.rb

# Check one Python file
python3 -m py_compile scripts/illustrations/generate_fractions.py

# Check one content page manually
bundle exec jekyll serve --livereload
# then open the specific page URL in browser
```

## Content and Bilingual Requirements
- New lessons must be added in both `contents/en/` and `contents/vi/`.
- Post filename pattern: `YYYY-MM-DD-title.md`.
- Front matter should include: `layout`, `title`, `chapter`, `order`, `owner`, `lang`, `categories`.
- Categories should use chapter format like `chapter01`.
- Keep heading hierarchy clean (H1/H2/H3).

## Math and Markdown Conventions
- Use `$$...$$` for math blocks; avoid inline `$...$` in this repo.
- Use `\begin{align}` for multi-line equations.
- Keep math age-appropriate and explanation-first.
- Separate paragraphs with blank lines.
- Use fenced code blocks with language identifiers.

## Code Style Guidelines
### General
- Follow existing style per file; avoid unrelated refactors.
- Keep diffs small and task-focused.
- Preserve bilingual and pedagogical tone in lesson content.
- Avoid adding dependencies unless clearly justified.

### Imports and Dependencies
- Ruby: require only what is used (existing plugins use `json`, `fileutils`).
- JavaScript: no bundler/module system; scripts run in browser globals.
- Python: explicit imports (`matplotlib`, `numpy`, `os`, patches); remove dead imports.

### Formatting
- Ruby: 2-space indentation; plugin classes under `module Jekyll`.
- JavaScript: prefer `const`/`let`; existing legacy IIFEs may still use `var`.
- Python: PEP 8 style, descriptive function names, docstrings for generator functions.
- Markdown: short readable paragraphs for children and parents.

### Types and Data Shapes
- JavaScript: no TypeScript; add runtime guards for missing DOM nodes and null values.
- Ruby: handle missing front matter/config keys safely.
- Python: keep numeric logic explicit and deterministic for repeatable outputs.

### Naming Conventions
- Files: kebab-case for JS, snake_case for Ruby/Python.
- Ruby methods: snake_case.
- JavaScript identifiers: camelCase.
- CSS classes: follow existing utility/theme naming patterns.

### Error Handling and Resilience
- Ruby plugins: guard nil paths and log warnings with `Jekyll.logger.warn`.
- JavaScript: use `try/catch` for async operations and fail gracefully when targets are absent.
- Python scripts: ensure output directories exist before writing files.
- Prefer actionable warnings/errors over silent failures.

### Frontend and Accessibility
- Use vanilla DOM APIs; avoid jQuery.
- Keep interactions keyboard-usable when practical.
- Preserve responsive behavior and readable text sizes for child audiences.

## Agent Workflow Expectations
- Run `bundle exec jekyll build` before finalizing when possible.
- For JS interaction changes, run local server and sanity-check affected pages.
- For content changes, verify EN/VI parity and logical linking.
- Do not commit `_site/` artifacts.
- Keep search index generation behavior intact (`search-index.json`, `search-index-vi.json`).

## PR Readiness Checklist
- Scope is limited to the requested change.
- Jekyll build passes.
- Manual checks completed for affected features/pages.
- Bilingual parity maintained where content changed.
- Cursor rule expectations remain satisfied.

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workflow Rules

1. Plan Mode Default
- Enter plan mode for ANY non-trivial task (3+ steps or architectural decisions)
- If something goes sideways, STOP and re-plan immediately — don’t keep pushing
- Use plan mode for verification steps, not just building
- Write detailed specs upfront to reduce ambiguity

2. Subagent Strategy
- Use subagents liberally to keep the main context window clean
- Offload research, exploration, and parallel analysis to subagents
- For complex problems, throw more compute at it via subagents
- One task per subagent for focused execution

3. Self-Improvement Loop
- After ANY correction from the user, update tasks/lessons.md with the pattern
- Write rules for yourself that prevent the same mistake
- Ruthlessly iterate on these lessons until the mistake rate drops
- Review lessons at the session start for the relevant project

4. Verification Before Done
- Never mark a task complete without proving it works
- Diff behavior between main and your changes when relevant
- Ask yourself: “Would a staff engineer approve this?”
- Run tests, check logs, demonstrate correctness

5. Demand Elegance (Balanced)
- For non-trivial changes: pause and ask, “Is there a more elegant way?”
- If a fix feels hacky: “Knowing everything I know now, implement the elegant solution.”
- Skip this for simple, obvious fixes — don’t over-engineer
- Challenge your own work before presenting it

6. Autonomous Bug Fixing
- When given a bug report: just fix it. Don’t ask for hand-holding
- Point at logs, errors, failing tests — then resolve them
- Zero context switching is required from the user
- Go fix failing CI tests without being told how

Task Management
- Plan First: Write a plan for tasks/todo.md with checkable items
- Verify Plan: Check in before starting implementation
- Track Progress: Mark items complete as you go
- Explain Changes: High-level summary at each step
- Document Results: Add review section to tasks/todo.md
- Capture Lessons: Update tasks/lessons.md after corrections

Core Principles
- Simplicity First: Make every change as simple as possible. Impact minimal code.
- No Laziness: Find root causes. No temporary fixes. Senior developer standards.
- Minimal Impact: Changes should only touch what's necessary. Avoid introducing bugs.

## Project Overview

Educational materials for AI courses taught by **Giorgi Basilaia** at Smart Academy. All content is static HTML — no build tools, no bundlers, no npm.

### Course Programs

| Program | Directory | Language | Sessions |
|---------|-----------|----------|----------|
| **AI in Practice** (Adults) | Root (`./`) | Georgian | 12 lectures, 24 hours |
| **AI for Teens** | `teens/` | Georgian | 8 lectures, 20 hours |
| **GIPA AI Intensive** (University) | `gipa/` | Bilingual KA/EN | 2-day masterclass |
| **Corporate AI Training** | `corporate-training.html` | Georgian | Customizable packages |

Registration: https://smartacademy.ge/trainings/587-AI-In-Practice

### Main Course Lecture Sequence (12 Lectures)

1. Introduction to Generative Intelligence and ChatGPT Basics
2. Prompt Engineering
3. Text Generation and Style
4. Creative Ideation and Innovation
5. Information Processing and Research
6. Professional Applications and Workflows
7. Visual Content and Presentations
8. Audio, Voice, and Video Generation
9. Automation and No-Code Tools
10. Security, Ethics, and Responsible Use
11. Custom AI Assistants
12. AI Playbook and Future Development

**Note**: Lecture 8 was inserted during a restructuring. Former lectures 8-11 became 9-12.

## File Naming Conventions

Each lecture has a consistent multi-format structure:

| Pattern | Description |
|---------|-------------|
| `lecture-X-slides.html` | Interactive slide-based presentation (primary teaching material) |
| `lecture-X-summary.html` | Comprehensive summary with key concepts |
| `lecture-X-study-guide.html` | Student study guide with learning objectives |
| `lecture-X-quick-ref.html` | Quick reference card |
| `lecture-X-exercises.html` | Practical hands-on activities |
| `lecture-X-lesson-plan.html` | Instructor's 120-minute teaching guide |
| `homework-X.html` | Homework assignment (~4-5 points each) |

## Key Pages

| Page | Purpose |
|------|---------|
| `index.html` | Course hub with lecture cards, progress tracking (localStorage), navigation |
| `index nolinks.html` | Public-facing course page (no lecture links, redirects to registration). SEO-optimized with Schema.org, OG tags, 40+ AI tool keywords |
| `landing.html` | Gateway splash page — "choose your path" between individual course and corporate training. Dark cinematic design with two portal cards |
| `corporate-training.html` | B2B corporate training page with packages, departments (15 industries), contact form (formsubmit.co), FAQ |
| `course-info.html` | Grading system (100-point scale) and course policies |
| `course-description.html` | Marketing-focused course description |
| `ai-tools.html` | AI tools reference guide (40+ tools across categories) |
| `teens/index.html` | Teen course hub |

### GIPA Masterclass Pages (`gipa/`)

| Page | Purpose |
|------|---------|
| `gipa/index.html` | Masterclass hub: day cards, learning path, resources, checklist, tools |
| `gipa/day1.html` | Day 1: AI Foundations & Curriculum Design (sidebar navigation, 11 topics) |
| `gipa/day2.html` | Day 2: Research, Feedback & Ethics (sidebar navigation, 9 topics) |
| `gipa/faq.html` | FAQ with collapsible accordion (3 categories) |
| `gipa/glossary.html` | AI terminology dictionary (Georgian explanations) |
| `gipa/prompts.html` | Prompt collection with copy functionality |
| `gipa/practice_day1.html` | Day 1 hands-on lab |
| `gipa/practice_day2.html` | Day 2 hands-on lab |
| `gipa/action-plan.html` | 30-day post-masterclass action plan |
| `gipa/ai-matrix.html` | AI integration matrix by faculty/department |
| `gipa/instructor.html` | Instructor profile |

**GIPA password protection**: `gipa/index.html` gates Day 1/Day 2 links behind password `aigipa` (sessionStorage, one-time per session).

## Architecture

### Slide-Based Presentation System (Main Course)

All lecture slides are standalone HTML with embedded CSS/JavaScript. Only external dependency: FiraGO font CDN.

```html
<html lang="ka">
<head>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <div class="slide"><!-- ... --></div>
    </div>
</body>
```

**CSS Components**: `.slide`, `.highlight-box` (blue), `.warning-box` (orange), `.key-points` (green), `.example-box` (gray), `.two-column`, `.interactive-section`

**JS Functions**: `toggleAdditionalInfo()` (collapsible sections), `showAnswer()` (quiz reveal)

**Slide flow**: Title → Objectives → Content → Examples → Practice → Summary → Navigation (prev/next)

### Color Schemes

**Main course slides**: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)` with accents Purple (#667eea), Blue (#2196f3), Orange (#ff9800), Green (#4caf50)

**index.html / landing.html / corporate-training.html** (dark theme): `--dark-bg: #0f172a`, `--primary-color: #6366f1`, `--accent-color: #ec4899`, `--card-bg: #1e293b`

**GIPA pages**: Navy palette with Tailwind CSS (via CDN). `navy-900: #003366` through `navy-50: #e6f0fa`

### GIPA Pages Architecture

Uses Tailwind CSS CDN + custom navy color extension. Features:

- **Dark mode toggle** (`#gipaControls`): Fixed bottom-right panel with dark/light, A-/A+, EN/KA buttons. State persisted in `localStorage` (`gipa-dark`, `gipa-fontsize`).
- **Language toggle**: Bilingual KA/EN content via `data-ka`/`data-en` attributes on elements. `setLanguage()` function swaps content.
- **Sidebar navigation** (day1/day2): Collapsible sidebar with topic links, module groupings, time badges.
- **Dark mode CSS pattern** (injected via JS `<style>`):
  ```css
  body.dark .bg-white { background: #1e293b !important }
  body.dark .text-navy-900 { color: #93c5fd !important }
  body.dark .text-emerald-900 { color: #6ee7b7 !important }
  body.dark .text-green-900 { color: #86efac !important }
  /* etc. — dark colors become their light counterparts */
  ```

**Known dark mode pitfall**: When adding dark mode overrides for Tailwind hover classes (like `hover:bg-gray-50`), escaped selectors (`hover\:bg-gray-50`) don't work in JS-injected styles. Use structural selectors instead (e.g., `body.dark .faq-item button:hover`).

### Landing & Corporate Pages

- **`landing.html`**: Standalone dark page, floating particle canvas animation, two portal cards with hover glow effects. Has light/dark toggle and KA/EN language toggle.
- **`corporate-training.html`**: Packages (Awareness 2-3h, Essentials 3-6h, Professional 6-12h, Custom), 15 industry departments, contact form via formsubmit.co, FAQPage schema, night mode, language toggle.

Both have comprehensive SEO: meta description/keywords (150+ keywords with AI tool names), Open Graph, Twitter Cards, Schema.org JSON-LD.

## Development Guidelines

### Language Rules
- **Primary**: Georgian (ქართული) with UTF-8 encoding
- **Technical terms**: Keep in English when Georgian translation is unclear (ChatGPT, prompt, API, workflow, etc.)
- **Font**: FiraGO from CDN, fallback to 'Segoe UI'

### Creating New Materials
1. Follow naming pattern: `lecture-X-[type].html`
2. Copy CSS from an existing file for consistency
3. Add navigation links to previous/next lectures
4. Preserve Georgian text exactly when modifying existing content
5. All files must be standalone (no external dependencies beyond FiraGO CDN or Tailwind CDN for GIPA)

### Critical Rules
- Never break UTF-8 encoding when editing Georgian text
- Never remove or modify standard CSS class names
- Always update `index.html` when adding new lectures
- Always update navigation links in adjacent lectures when inserting/reordering
- Keep all files standalone — no build tools, no bundlers, no npm
- When adding dark mode overrides: always test that `text-navy-*`, `text-blue-*`, `text-emerald-*`, `text-green-*` classes have light counterparts in `body.dark` rules

## Grading System (course-info.html)

### Main Course
- **Homework**: 50 points (homework-1 through homework-10, ~4-5 points each)
- **Quizzes**: 30 points (3 quizzes × 10 points)
- **Participation**: 20 points (attendance 8, discussion 6, exercises 6)
- **Passing grade**: 61 points minimum

### Teen Course
- Participation 30%, Mini-assignments 30%, Final project 40%

## Course Completion Status

**Complete (slides + summary + study-guide + quick-ref + exercises)**: Lectures 1-12
**Lesson plans completed**: Lectures 1-7, 9 | **Missing**: 8, 10, 11, 12
**Homework files**: homework-1 through homework-10

### Teen Course
All 8 lecture slides complete. `index.html`, `syllabus.html`, `course-info.html` complete.

### GIPA Masterclass
All pages complete: index, day1, day2, faq, glossary, prompts, practice labs, action-plan, ai-matrix, instructor.

## Directory Structure

- `archive/` — Old versions of security and playbook lectures (pre-restructuring)
- `teens/` — Teen course (8 sessions)
- `gipa/` — GIPA university masterclass (2-day intensive)
- `.serena/` — Serena MCP integration with project memories

## Viewing Materials

```cmd
start index.html
start lecture-1-slides.html
start gipa/index.html
start landing.html
```

## Instructor

**Giorgi Basilaia** — 25+ years technology experience, university professor, 14 scientific papers (3388 citations), 18 international research projects (NATO, USAID, ERASMUS)

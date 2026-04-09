# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Workflow Rules

1. **Plan Mode Default** — Enter plan mode for any non-trivial task (3+ steps). Stop and re-plan if something goes sideways.
2. **Subagent Strategy** — Use subagents for research, exploration, and parallel analysis to keep main context clean.
3. **Verification Before Done** — Never mark complete without proving it works.
4. **Simplicity First** — Minimal impact. Only touch what's necessary.

## Git Workflow

No build tools. The only workflow command is:
```bat
push.bat        # stages all, commits with timestamp, pushes to GitHub
```
Remote: `https://github.com/basilaia123/ai2026` (branch: `master`)

If push fails with "Duplicate header" error, the local git config has a stale `http.extraHeader`. Fix:
```bash
git config --local --unset http.extraHeader
```

## Project Overview

Static HTML educational materials for AI courses by **Giorgi Basilaia** (Smart Academy). No build tools, no bundlers, no npm. Every file is standalone HTML with embedded CSS/JS.

### Course Programs

| Program | Directory | Language | Format |
|---------|-----------|----------|--------|
| **AI in Practice** (Adults) | `lectures/` | Georgian | 12 lectures, scrollable |
| **AI for Teens** | `ai4teens/` | Georgian | 8 lectures, scrollable |
| **GIPA AI Intensive** | `gipa/` | Bilingual KA/EN | 2-day masterclass, sidebar nav |
| **Tempo Holding** (Corporate) | `tempo/` | Georgian | 6 sessions, fullscreen slides |
| **Cascade / Art Direction** | `art/` | Georgian | 1-day workshop, sidebar nav |
| **OPPA** (Corporate) | `oppa/` | Georgian | Workshop, sidebar nav |
| **chatgpt.ge** | `chatgpt.ge/` | Georgian | Marketing/landing pages |

## Architecture

### Two Distinct HTML Patterns

**Pattern A — Fullscreen Slide Deck** (`tempo/lecture-X-slides.html`)
- `body { overflow: hidden }`, `100vw × 100vh` slides
- Navigation: arrow keys + nav buttons, progress bar at bottom
- Font sizing: `clamp()` + `vw` units for Full HD scaling
- Detail panels: fixed right-side drawer toggled per-slide (`toggleDetail(id)`)
- Charts: Chart.js via CDN, initialized in `window.onload`
- Colors: amber/gold (`#d97706`, `#fbbf24`) on dark (`#0f172a`)

**Pattern B — Scrollable Reference Page** (`gipa/day1.html`, `art/art-direction-training.html`, `oppa/oppa-training.html`)
- Tailwind CSS CDN + custom navy color extension
- Fixed sidebar (`w-72`, collapsible on mobile), main content scrolls
- Active nav link highlighting via IntersectionObserver
- Font size controls (`A-`/`A+`) stored in `localStorage`
- Dark mode via JS-injected `<style>` block (not Tailwind dark: prefix)
- **Known pitfall**: Tailwind hover escaped selectors (`hover\:bg-gray-50`) don't work in JS-injected styles — use structural selectors instead

### Main Course Slides (`lectures/`)
- Standalone HTML, FiraGO font CDN only
- CSS components: `.slide`, `.highlight-box`, `.warning-box`, `.key-points`, `.example-box`, `.two-column`
- JS: `toggleAdditionalInfo()` (collapsible), `showAnswer()` (quiz reveal)
- Color: purple gradient `#667eea → #764ba2`

### GIPA Password Gate
`gipa/index.html` gates Day 1/Day 2 behind password `aigipa` (sessionStorage, one-time per session).

### Tempo Detail Panel System
Each slide can have an expandable detail drawer:
```html
<button class="detail-btn" id="btn-SLIDEID" onclick="toggleDetail('SLIDEID')">📖 დეტალები</button>
<div class="detail-panel" id="detail-SLIDEID">
  <div class="dp-header">...</div>
  <div class="dp-body">...</div>
</div>
```
`toggleDetail()` manages `.open` class on both panel and overlay, and `.visible` on button.

## Language Rules

- **Primary**: Georgian (ქართული), UTF-8 encoding — never break encoding when editing
- **Technical terms**: Keep in English (ChatGPT, prompt, API, workflow, ROI, etc.)
- **Font**: FiraGO CDN (`https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css`), fallback `'Segoe UI'`

## Directory Map

| Directory | Contents |
|-----------|----------|
| `lectures/` | Main adult course: 12 lectures × 6 file types each |
| `ai4teens/` | Teen course: 8 lectures |
| `gipa/` | University masterclass: day1, day2, faq, glossary, prompts, labs, action-plan, ai-matrix |
| `tempo/` | Tempo Holding corporate: index, 6 session slides (only session 1 complete) |
| `art/` | Cascade art direction workshop: training HTML + prompt templates |
| `oppa/` | OPPA corporate workshop |
| `chatgpt.ge/` | Marketing site templates (agriculture, construction, corporate) |
| `dead_offers/` | Archived proposals — do not modify |

## Lecture File Naming (`lectures/`)

`lecture-X-[type].html` where type ∈ `slides`, `summary`, `study-guide`, `quick-ref`, `exercises`, `lesson-plan`
`homework-X.html` — assignments (homework-1 through homework-10)

## Tempo Session Status

| Session | Topic | Slides |
|---------|-------|--------|
| 1 | AI საფუძვლები + პრომპტ-ინჟინერია | ✅ Complete (34 slides) |
| 2 | ელფოსტა, ბიზნეს-კომუნიკაცია | ❌ Missing |
| 3 | პრეზენტაციები (Gamma) + SOP | ❌ Missing |
| 4 | სოციალური მედია + მულტიმედია | ❌ Missing |
| 5 | გაყიდვები: სკრიპტები, Follow-up | ❌ Missing |
| 6 | AI ასისტენტები, ავტომატიზაცია + ROI | ❌ Missing |

## Instructor

**Giorgi Basilaia** — 25+ years technology experience, university professor, 14 scientific papers (3388 citations), 18 international research projects (NATO, USAID, ERASMUS). Teaches at Smart Academy, Tbilisi.

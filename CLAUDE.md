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

Commit history uses short operational subjects like `update <timestamp>`, plus occasional `CHECKPOINT:` messages for larger restructures — follow one of those two styles. Testing is manual: after edits, open the affected HTML file in a browser and verify layout, slide/section navigation, and any inline JS (collapsibles, timers, copy buttons, quiz reveals). If you touch `gipa/`, re-check the password-gate flow on `gipa/index.html`.

## Project Overview

Static HTML educational and proposal materials for AI courses and corporate trainings by **Giorgi Basilaia** (Smart Academy). No build tools, no bundlers, no npm for the course content — every page is standalone HTML with embedded CSS/JS. A couple of unrelated app subfolders (see below) are real npm/Next.js projects with their own `CLAUDE.md`/`AGENTS.md` — their rules override this file when working inside them.

### Course & Proposal Programs

| Program | Directory | Language | Format |
|---------|-----------|----------|--------|
| **AI in Practice** (Adults) | `lectures/` | Georgian | 12 lectures, scrollable |
| **AI for Teens** | `ai4teens/` | Georgian | 8 lectures, scrollable |
| **GIPA AI Intensive** | `gipa/` | Bilingual KA/EN | 2-day masterclass, sidebar nav |
| **Tempo Holding** (Corporate) | `tempo/` | Georgian | 6 sessions, fullscreen slides |
| **Cascade / Art Direction** | `art/` | Georgian | 1-day workshop, sidebar nav |
| **OPPA** (Corporate) | `oppa/` | Georgian | Workshop, sidebar nav |
| **Green School** | `Green/` | Georgian | Multi-session, sidebar nav |
| **Megalab** | `megalab/` | Georgian | Multi-day (`day-X-slides.html`), sidebar nav |
| **Mardi Holding** (Corporate) | `mardi/` | Georgian | Multi-lecture, sidebar nav |
| **Eurodrug Georgia** (Corporate) | `eurodrug/` | Georgian | Proposal + sidebar-nav sessions |
| **chatgpt.ge** | `chatgpt.ge/` | Georgian | Marketing/landing pages |

Many other top-level folders (`caritas`/`caritas_georgia`/`caritasgeorgia`, `credo`, `GITA`, `orbi`, `mof`, `mcdonalds`, `job26`, `labtechnology`, `loialte_ebrd`, `openday`, `award`, `unlimited`, `gh`) are one-off client proposals or event pages following the same standalone-HTML conventions as above; check each folder's own `index.html` before assuming a shared structure. `dead_offers/` holds archived proposals — treat as read-only unless explicitly asked.

## Architecture

### Two Distinct HTML Patterns

**Pattern A — Fullscreen Slide Deck** (`tempo/lecture-X-slides.html`)
- `body { overflow: hidden }`, `100vw × 100vh` slides
- Navigation: arrow keys + nav buttons, progress bar at bottom
- Font sizing: `clamp()` + `vw` units for Full HD scaling
- Detail panels: fixed right-side drawer toggled per-slide (`toggleDetail(id)`)
- Charts: Chart.js via CDN, initialized in `window.onload`
- Colors: amber/gold (`#d97706`, `#fbbf24`) on dark (`#0f172a`)

**Pattern B — Scrollable Reference Page** (`gipa/day1.html`, `art/art-direction-training.html`, `oppa/oppa-training.html`, and now the default for newer corporate decks: `Green/lecture-X.html`, `megalab/day-X-slides.html`, `mardi/lecture-X-slides.html`, `eurodrug/day-X-slides.html`)
- Tailwind CSS CDN (or hand-rolled equivalent) + a client-specific color palette defined as CSS custom properties / `tailwind.config` extension (e.g. Megalab blue/pink, Eurodrug navy/cyan, Green School forest green)
- Fixed sidebar (`~280px` / `w-72`, collapsible on mobile via `toggleSidebar()`/`toggleMenu()`), main content scrolls
- Active nav link highlighting on `scroll` (offsetTop comparison) or IntersectionObserver
- Shared component kit across these decks: `.badge` (`badge-theory`/`badge-practice`/`badge-demo`), `.card`, `.two-column`/`.three-column` grids, `.highlight-box`/`.warning-box`/`.success-box`, `.prompt-blueprint` (dark code block with a `.pb-copy`/`.copy-btn` button wired to `copyText(btn)`, which reads `.code-content` and calls `navigator.clipboard.writeText`), and a countdown `startTimer(elementId, minutes)` for timed practice exercises
- Font size controls (`A-`/`A+`) stored in `localStorage` (where present)
- Dark mode via JS-injected `<style>` block (not Tailwind `dark:` prefix)
- **Known pitfall**: Tailwind hover escaped selectors (`hover\:bg-gray-50`) don't work in JS-injected styles — use structural selectors instead
- When asked to build a new lecture/session for one of these clients "in the format of" an existing one, treat the referenced file as the literal template: copy its section skeleton (agenda → block header → topic sections → practice → summary), its CSS variable names, and its JS helpers, then swap in the client's palette and subject-matter content — don't invent a new layout.

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

### Nested Real App Projects (not static HTML)
- `investment-app/` — a Next.js/TypeScript app (React 19, Tailwind, recharts, yahoo-finance2) with its own `package.json`, `CLAUDE.md`, and `AGENTS.md`. Use `npm run dev`/`build`/`lint` inside that folder; its rules take precedence there.
- `chat-app/` — standalone static HTML pages only (no build step), despite the name.

## Language Rules

- **Primary**: Georgian (ქართული), UTF-8 encoding — never break encoding when editing
- **Technical terms**: Keep in English (ChatGPT, prompt, API, workflow, ROI, etc.)
- **Font**: FiraGO CDN (`https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css`), fallback `'Segoe UI'`
- **Georgian QA**: after generating or editing Georgian content, run it past the `gramma` subagent (or the `georgian-proofreader` skill/rules in `skill_rules.md`) — it checks spelling, morphology, postpositions, verb conjugation, and flags common AI-generated calques (e.g. banned em/en-dashes, forbidden abbreviations, corporate loanword barbarisms).

## Directory Map

| Directory | Contents |
|-----------|----------|
| `lectures/` | Main adult course: 12 lectures × 6 file types each |
| `ai4teens/` | Teen course: 8 lectures |
| `gipa/` | University masterclass: day1, day2, faq, glossary, prompts, labs, action-plan, ai-matrix |
| `tempo/` | Tempo Holding corporate: index + 6 sessions (slides/summary/exercises each), all complete |
| `art/` | Cascade art direction workshop: training HTML + prompt templates |
| `oppa/` | OPPA corporate workshop |
| `Green/` | Green School: lecture-X.html sessions, dashboard, offer/schedule generators |
| `megalab/` | Megalab corporate training: day-X-slides/summary/exercises, homework, Notion guide |
| `mardi/` | Mardi Holding corporate training: lecture-X-slides + day-X pages, prompt library, survey |
| `eurodrug/` | Eurodrug Georgia proposal (`index.html`) + `day-X-slides.html` sessions |
| `chatgpt.ge/` | Marketing site templates (agriculture, construction, corporate) |
| `investment-app/` | Standalone Next.js app — see its own `CLAUDE.md` |
| `dead_offers/` | Archived proposals — do not modify |

## Lecture File Naming (`lectures/`)

`lecture-X-[type].html` where type ∈ `slides`, `summary`, `study-guide`, `quick-ref`, `exercises`, `lesson-plan`
`homework-X.html` — assignments (homework-1 through homework-10)

Newer corporate decks (`Green/`, `megalab/`, `mardi/`, `eurodrug/`) instead use `lecture-X.html` or `day-X-slides.html`/`day-X-summary.html`/`day-X-exercises.html` — check the target directory's existing files for its actual convention before creating a new one.

## Instructor

**Giorgi Basilaia** — 25+ years technology experience, university professor, 14 scientific papers (3388 citations), 18 international research projects (NATO, USAID, ERASMUS). Teaches at Smart Academy, Tbilisi.

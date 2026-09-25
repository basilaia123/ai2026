# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This directory contains a comprehensive Georgian language course on "AI ასისტენტები, აგენტები და No-Code ავტომატიზაცია" (AI Assistants, Agents, and No-Code Automation). The course is structured as 11 sessions (8 online + 3 physical workshops, 22 hours total) covering Custom GPTs, Claude Projects, Make.com, Zapier, n8n, API integration, and RAG systems.

**Course Hub Files:**
- **index.html**: Course landing page with syllabus, session schedule, pricing, and registration
- **agents.txt**: Detailed course plan with all 11 sessions, learning objectives, grading system
- **getsmart.html**: Smart Academy course catalog portal (separate interface)

**Lecture Materials (per lecture):**
- **lecture-X-slides.html**: Main slide-based presentation for teaching
- **lecture-X-summary.html**: Condensed summary of lecture content
- **lecture-X-quick-ref.html**: Quick reference guide with tables and key concepts
- **lecture-X-exercises.html**: Hands-on practice exercises
- **lecture-X-study-guide.html**: Comprehensive study guide for students

**Homework Assignments:**
- **homework-X.html**: Standalone homework assignments (30-40 minutes each)

## Architecture

### File Naming Convention

All lecture materials follow consistent naming:
- Slides: `lecture-X-slides.html`
- Summary: `lecture-X-summary.html`
- Quick Reference: `lecture-X-quick-ref.html`
- Exercises: `lecture-X-exercises.html`
- Study Guide: `lecture-X-study-guide.html`
- Homework: `homework-X.html`

Where X = lecture number (1, 2, 3, etc.)

### Navigation System

All lecture-related files include a consistent navigation bar linking to:
- 🏠 Main course hub (index.html)
- 📊 Lecture slides
- 📚 Summary
- 📋 Quick reference
- 💪 Exercises
- 📖 Study guide (when applicable)

The `.nav-link.current` class highlights the active page.

### Slide-Based Presentation System

**Core Components:**
- `.slide` div: Each slide is a standalone section (min-height: 80vh)
- `.slide-content`: Main content area with consistent typography
- `.two-column`: Grid layout for side-by-side content (2 columns on desktop, stacks on mobile)

**Content Boxes:**
- `.highlight-box`: Blue background (#e3f2fd) with blue border-left (#2196f3)
- `.warning-box`: Orange background (#fff3e0) with orange border-left (#ff9800)
- `.key-points`: Key takeaways section
- `.info-box`: Info callouts (landing page)
- `.success-box`: Success/completion indicators (homework)

**Interactive Elements:**
- Collapsible sections with `toggleAdditionalInfo()` function
- Quiz answers with `showAnswer()` function (exercises)
- Session details toggle with `toggleSession(button)` (index.html)
- Homework toggle with `toggleHomework(button)` (index.html)
- FAQ accordion with `toggleFAQ(element)` (index.html)

### Color Scheme & Typography

**Primary Gradients:**
- Purple gradient: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)` - used in headers
- Blue gradient: `linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%)` - used in index.html header
- Card backgrounds: `linear-gradient(135deg, #dbeafe 0%, #bfdbfe 100%)`

**Accent Colors:**
- Green CTA buttons: #10b981 (hover: #059669)
- Text: #2c3e50 (primary), #333 (body)
- Background: #f8f9fa, linear gradients for pages

**Typography:**
- Font: FiraGO (loaded via CDN from jsdelivr.net or fonts.google.com)
- Encoding: UTF-8 (required for Georgian characters)
- Headings: h1 (2.5rem), h2 (2rem), h3 (1.5rem)

### Responsive Design

**Breakpoints:**
- Desktop: > 1024px (auto-expand sessions, full grid layouts)
- Tablet: 768px - 1024px (2-column grids, adjusted padding)
- Mobile: < 768px (1-column, accordion behavior, stacked layouts)

**Grid Patterns:**
- 6-column → 3-column → 2-column → 1-column (landing page highlights)
- 2-column → 1-column (session cards, two-column content)
- Flexbox for navigation links with wrapping

### Course Landing Page (index.html)

**Sections:**
1. Header: Course title, duration, lecturer, meta badges
2. Course highlights: 6-card grid (AI assistants, automation, API, agents, projects, certificate)
3. Target audience: Feature cards for different user groups
4. Session schedule: 11 session cards (online/workshop types)
5. FAQ: Accordion-style questions
6. Stats & learning outcomes

**JavaScript Functions:**
- `toggleSession(button)`: Mobile-only accordion for session details (auto-open on desktop >1024px)
- `toggleHomework(button)`: Show/hide homework within session cards
- `toggleFAQ(element)`: Expand/collapse FAQ items
- Window resize listener: Auto-expand sessions on desktop

### Smart Academy Portal (getsmart.html)

Advanced course catalog with filtering, search, favorites, and infinite scroll:
- External API: smartacademy.ge/api/courses
- Filter system: price range, duration, categories, tags
- Voice search (Chrome/Safari)
- Grid/list view toggle
- Star ratings and favorites (localStorage)
- QR codes and course recommendations
- Dark/light theme toggle

Requires CORS proxy for API access.

## Development Guidelines

### Content Updates

**IMPORTANT:** Use Serena agent for content updates to save tokens when modifying course materials.

### Georgian Language Rules

- All course content in Georgian (UTF-8 encoding)
- Technical terms kept in English: AI, API, workflow, automation, Make.com, Zapier, n8n, RAG, prompt, token, LLM, etc.
- Tone: Professional business language for landing page, educational/instructional for lectures
- Georgian quotes: „text" (not "text")

### Adding New Lecture Materials

**Complete lecture set requires 5 files:**

1. **lecture-X-slides.html**: Main presentation
   - Include `.slide` divs for each topic
   - Add navigation at top and bottom
   - Use `.highlight-box` and `.warning-box` for callouts

2. **lecture-X-summary.html**: Condensed content
   - Summary of key points per section
   - Shorter than slides, focus on essentials

3. **lecture-X-quick-ref.html**: Reference tables
   - Use `<table>` with styled headers
   - Include terminology, comparisons, cheat sheets
   - `.key-box` and `.tip-box` for highlights

4. **lecture-X-exercises.html**: Practice activities
   - Number exercises clearly
   - Include solution sections with `showAnswer()` toggle
   - `.exercise-card` divs for structure

5. **lecture-X-study-guide.html**: Comprehensive guide
   - Combine all content for student review
   - Include learning objectives, key concepts, practice questions

**Naming must be consistent** - use hyphens, not underscores.

### Adding Homework Assignments

Create `homework-X.html` with:
- Header with assignment title and points badge
- `.info-box`, `.warning-box`, `.success-box` for different message types
- Task sections with clear numbering
- Submission instructions and grading criteria
- Link back to course hub

### Updating Course Landing Page

**Adding a session:**
1. Add `.session-card` to `.schedule` grid
2. Include `.session-header` with number and type (online/workshop)
3. Add topics as `<ul>` in `.session-content`
4. Optional: Add homework section with toggle button
5. Update total session count in header
6. Update agents.txt with detailed session plan

**Updating FAQ:**
- Add `.faq-item` with `.faq-question` (onclick handler) and `.faq-answer`
- Use ❓ emoji prefix for consistency

**Modifying course metadata:**
- Duration: `.meta-item` in header
- Pricing: Header and stats section
- Highlights: `.highlight-card` grid (maintain 6 cards)

### HTML Pattern Examples

**Session card structure:**
```html
<div class="session-card">
    <div class="session-header">
        <span class="session-number">შეხვედრა X</span>
        <span class="session-type online">ონლაინ ლექცია</span>
    </div>
    <h3>Session Title</h3>
    <button class="toggle-btn" onclick="toggleSession(this)">დეტალები ▼</button>
    <div class="session-content">
        <ul>
            <li>Topic 1</li>
            <li>Topic 2</li>
        </ul>
    </div>
</div>
```

**Navigation pattern (all lecture files):**
```html
<nav class="nav-links">
    <a href="index.html" class="nav-link">🏠 მთავარი</a>
    <a href="lecture-X-slides.html" class="nav-link">📊 ლექცია</a>
    <a href="lecture-X-summary.html" class="nav-link">📚 შეჯამება</a>
    <a href="lecture-X-quick-ref.html" class="nav-link current">📋 სწრაფი ცნობარი</a>
    <a href="lecture-X-exercises.html" class="nav-link">💪 სავარჯიშოები</a>
    <a href="lecture-X-study-guide.html" class="nav-link">📖 სასწავლო გზამკვლევი</a>
</nav>
```

**Content boxes:**
```html
<div class="highlight-box">
    <p>Important information highlighted in blue</p>
</div>

<div class="warning-box">
    <p>Warning or caution in orange</p>
</div>

<div class="key-points">
    <h3>მთავარი დასკვნები</h3>
    <ul>
        <li>Key point 1</li>
        <li>Key point 2</li>
    </ul>
</div>
```

## File Organization

```
agents/
├── index.html                    # Course landing page (main hub)
├── agents.txt                    # Detailed course plan
├── getsmart.html                 # Smart Academy catalog portal
│
├── lecture-1-slides.html         # Lecture 1: AI Assistants Fundamentals
├── lecture-1-summary.html
├── lecture-1-quick-ref.html
├── lecture-1-exercises.html
├── lecture-1-study-guide.html
│
├── lecture-2-slides.html         # Lecture 2
├── lecture-3-slides.html         # Lecture 3
│
├── homework-1.html               # Homework 1: Prompting Skills
├── homework-2.html               # Homework 2
├── homework-3.html               # Homework 3
│
├── index.html.backup             # Backup file
├── temp-head.txt                 # Temporary file
├── .vscode/sftp.json            # SFTP configuration
└── CLAUDE.md                     # This file
```

## Testing

**Manual browser testing required:**
- Navigation links between all lecture materials
- Session/homework accordion behavior (mobile vs desktop)
- FAQ accordion expansion/collapse
- Georgian text rendering (FiraGO font loading)
- Responsive grid layouts at all breakpoints
- Interactive toggles and show/hide functionality
- Smooth scrolling and page anchors

**Smart Academy portal testing:**
- API connectivity and CORS handling
- Filter combinations (price, duration, tags, categories)
- Infinite scroll loading
- Voice search (Chrome/Safari only)
- LocalStorage (favorites, ratings, search history)
- Theme switching (dark/light)

## Notes

- Static HTML site with no build process
- All dependencies (fonts, icons) via CDN
- Cross-browser compatible (modern browsers)
- Mobile-first responsive design
- No server-side functionality (except getsmart.html API)
- Consistent styling patterns across all lecture materials
- Uses slide-based architecture similar to CompTIA and IB Psychology courses in parent directories

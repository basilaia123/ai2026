# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an AI training course website for Gastronome.ge managers - a 6-hour intensive training program (2 days × 3 hours) focused on practical AI usage in management roles.

**Target Audience:** 5 manager roles at Gastronome.ge
- 📦 Warehouse Managers
- 🍽️ Restaurant Managers
- 🚚 Distribution Managers
- ⚙️ Operations Managers
- 🏪 Store Managers

**Course Structure:**
- Day 1 (3 hours): AI fundamentals, ChatGPT mastery, automation, decision-making
- Day 2 (3 hours): Visual content creation, custom GPTs, advanced workflows, capstone project
- 9 modules total covering practical AI applications for management

## File Structure

```
gastronome/
├── index.html                              # Main course hub with navigation
├── day1.html                               # Day 1 overview page
├── day2.html                               # Day 2 overview page
├── module1.html                            # Module 1: AI Introduction
├── module2.html                            # Module 2: ChatGPT for Managers
├── module3.html                            # Module 3: Automation
├── module4.html                            # Module 4: Problem Solving & Decision Making
├── module5.html                            # Module 5: Homework Review
├── module6.html                            # Module 6: Visual Content Creation
├── module7.html                            # Module 7: Advanced AI Workflows
├── module8.html                            # Module 8: Capstone Project
├── module9.html                            # Module 9: AI Strategy & Long-term Vision
└── gastronome_ai_training_managers_v2.md  # Complete course curriculum (Georgian)
```

## Architecture

### Slide-based Presentation System
All module HTML files follow a consistent slide-based architecture:
- Each `.slide` div represents one presentation slide
- JavaScript-powered navigation (keyboard arrows, prev/next buttons)
- Slide counter shows progress (e.g., "3 / 6")
- Home button links back to index.html
- Responsive design for mobile/desktop viewing

### Design Pattern
```html
<div class="slide active">           <!-- First slide is .active -->
    <div class="slide-content">
        <!-- Content here -->
    </div>
</div>
```

### Navigation System
- **Prev/Next buttons:** Fixed at bottom center
- **Slide counter:** Fixed at top right
- **Home button:** Fixed at top left (links to index.html)
- **Keyboard navigation:** Arrow keys for prev/next
- **Last slide behavior:** "Next" button becomes "შემდეგი მოდული →" and links to next module

### Styling Components
- `.highlight-box` - Purple gradient boxes for key messages
- `.key-points` - Gray boxes with bullet lists
- `.example-box` - Light blue boxes with left border (for examples)
- `.comparison-box` - Monospace font boxes (for before/after comparisons)
- `.tool-card` - White cards with purple border (for tool descriptions)

### Color Scheme
- Primary gradient: `linear-gradient(135deg, #667eea 0%, #764ba2 100%)`
- Day 2 gradient: `linear-gradient(135deg, #11998e 0%, #38ef7d 100%)`
- Accent colors: Purple (#667eea), violet (#764ba2), dark gray (#2c3e50)

## Development Workflow

### Creating a New Module Page

1. **Copy template structure** from existing module (e.g., module1.html)
2. **Update navigation:**
   - Adjust total slide count in `<span id="totalSlides">X</span>`
   - Update last slide "Next" button to link to correct next module
   - Update home button link if needed
3. **Content structure:**
   - Slide 1: Module title and duration
   - Middle slides: Content with appropriate styling components
   - Last slide: Summary with key learnings and next module teaser
4. **Maintain consistency:**
   - Use established CSS classes
   - Keep gradient backgrounds consistent
   - Follow Georgian language conventions

### Editing Existing Content

- Content is in **Georgian language** (UTF-8 encoding)
- English technical terms are used where Georgian translation is unclear
- Each module targets specific manager roles with role-specific examples
- Maintain the practical, hands-on approach with real Gastronome.ge scenarios

### Testing Checklist

- [ ] Navigation works (prev/next buttons, keyboard arrows)
- [ ] Slide counter displays correctly
- [ ] Home button returns to index.html
- [ ] Last slide links to correct next module
- [ ] Georgian text renders properly
- [ ] Responsive design works on mobile
- [ ] All styling components display correctly

## Content Guidelines

### Language and Tone
- **Primary language:** Georgian (ქართული)
- **Technical terms:** English when clearer (e.g., "ChatGPT", "prompt engineering", "ROI")
- **Tone:** Professional but accessible, practical and action-oriented
- **Audience:** Mid-level managers with varying technical backgrounds

### Module Content Pattern
Each module follows this pattern:
1. **Introduction slide** - Module title, emoji, duration
2. **Concept slides** - Theory with real statistics and examples
3. **Practice slides** - Role-specific examples for each of 5 manager types
4. **Summary slide** - Key learnings and next steps

### Role-Specific Content
When creating examples, include variations for all 5 roles:
- 📦 Warehouse: Inventory, forecasting, supplier management
- 🍽️ Restaurant: Menu planning, scheduling, customer feedback
- 🚚 Distribution: Route optimization, delivery tracking, logistics
- ⚙️ Operations: SOPs, KPIs, process documentation
- 🏪 Store: Sales analysis, merchandising, customer service

## Key Course Concepts

### Learning Objectives (from course description)
1. Accelerate decision-making with data-driven AI insights
2. Automate administrative burden (reports, emails, documentation)
3. Improve team management with AI-powered tools
4. Create professional presentations, analytics, strategic documents
5. Increase department productivity by 40-60%

### Core AI Tools Covered
- **ChatGPT/Claude** - Main AI assistant ($20/month)
- **Notion AI** - Documentation and knowledge management
- **Canva AI** - Presentations and visuals
- **Google Workspace AI** - Daily office tasks
- **Microsoft Copilot** - Office 365 integration

### Prompt Engineering Formula
```
[ROLE] + [CONTEXT] + [TASK] + [FORMAT] + [CONSTRAINTS] = Perfect response
```

This formula is central to Module 2 and referenced throughout the course.

## Notes for AI Development

- The complete curriculum is documented in `gastronome_ai_training_managers_v2.md` (2,143 lines)
- This is a **completed training course** (all 9 modules exist as HTML)
- Day overview pages (day1.html, day2.html) summarize content for each day
- Index.html serves as the main navigation hub with grid layout of all modules

## Maintenance

When updating content:
1. Keep navigation links synchronized across all pages
2. Maintain consistent styling with existing modules
3. Preserve Georgian language quality and technical accuracy
4. Ensure role-specific examples are relevant to Gastronome.ge operations
5. Test slide navigation after any JavaScript changes
6. Verify mobile responsiveness for all new content

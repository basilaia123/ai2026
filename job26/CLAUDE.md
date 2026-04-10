# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static HTML website containing job hunting training materials in Georgian language. The project consists of standalone HTML files with embedded CSS styling and uses the FiraGO font family for Georgian text rendering.

## Project Structure

- `index.html` - Main presentation file (17 slides) about AI in job searching - comprehensive training materials
- `cv-samples.html` - CV sample templates (IT student and business student examples)
- `job-hunting-training-lesson-plan.html` - Training lesson plan for trainers
- `job-hunting-training-60min-quick-ref.html` - 60-minute quick reference guide
- `job-hunting-training-60min-exercises.html` - 60-minute exercises

## Development

This is a simple static website with no build process, package manager, or testing framework. Files can be opened directly in a web browser for viewing and testing.

### Viewing the site
Open any HTML file directly in a web browser to view the content.

### Making changes
- Edit HTML files directly
- CSS is embedded within each HTML file in `<style>` tags
- Uses external FiraGO font from CDN: `https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css`

## Architecture Notes

### Design System
- All files are self-contained with embedded styling
- Responsive design using CSS Grid and Flexbox
- Georgian language content requires proper font support (FiraGO)
- Clean, modern design with gradient backgrounds and card-based layouts

### Common UI Components
- `.slide` - Main content container with white background and shadow
- `.highlight-box` - Blue boxes for key information (border-left: #2196f3)
- `.warning-box` - Orange boxes for warnings and cautions (border-left: #ff9800)
- `.key-points` - Green boxes for important takeaways (border-left: #4caf50)
- `.example-box` - Gray boxes for examples (border-left: #757575)
- `.demo-box` - Yellow boxes for demonstrations/prompts (border-left: #ffc107)
- `.two-column` - CSS Grid layout for side-by-side content

### Navigation System
- Top sticky navigation bar (`.top-nav`) linking between all pages
- Bottom navigation for returning to main page
- Active page highlighting in navigation

### Content Structure
- Slide-based presentation format (numbered slides like "1/17")
- CV samples use specialized styling (`.cv-sample`, `.cv-header`, `.cv-section`)
- Skill tags displayed as colored badges (`.cv-skill-tag`)
- Consistent spacing and typography throughout
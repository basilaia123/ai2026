---
name: tempo-course-generator
description: Generates high-quality, premium Tempo Holding course materials, slides, summaries, and exercises in HTML format using the established GIPA/Tempo layout. Use this skill when asked to create a new lecture, module, or presentation for the Tempo Holding AI Training.
---

# Tempo Course Generator

This skill enables Gemini CLI to generate beautifully formatted, interactive HTML presentations and course materials tailored to the **Tempo Holding** premium brand identity. 

## When to use this skill

Activate this workflow whenever the user requests:
- "Create lecture 2 for the Tempo course"
- "Generate slides for a new module"
- "Make a summary or exercise file for the Tempo training"

## Workflows



### 1. Generating Presentation Slides

The main delivery format for Tempo courses is the interactive HTML presentation (GIPA-style layout with sidebar).

**CRITICAL DESIGN RULES FOR SLIDES:**
1. **Consolidate Content:** NEVER create a slide that only has a prompt without context. ALWAYS combine the theoretical explanation (Why/How) and the practical prompt (Code Block) on the same single slide. This reduces slide bloat and improves readability.
2. **Data Visualization:** Whenever presenting percentages, time savings, or comparative statistics, use **Chart.js** (Bar charts, Doughnut charts) instead of plain text bullets. (See `references/components.md` for examples).

1. **Understand the Content:** Analyze the provided topic, agenda, or raw notes from the user. Break the content down into logical "Blocks" and individual "Topics" (Slides).
2. **Apply the Template:** Read the template file located at \`assets/slide-template.html\`. This file contains the complete CSS (Tailwind + custom styles), JavaScript logic for navigation and copy buttons, and the base layout structure.
3. **Populate the Sidebar:** Generate the \`<aside id="sidebar">\` navigation links. Remember to group them by blocks (e.g., "ბლოკი 1: თეორია").
4. **Populate the Main Content:** For each topic, create a \`<section id="topic-X" class="min-h-[85vh] flex flex-col justify-center mb-0 scroll-mt-10 border-b border-gray-200 py-10">\`.
   - Use \`<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>Title</h3>\` for slide titles.
   - Use rich visual elements: Do not just output plain lists. Use the components defined in \`references/components.md\` (e.g., grids, warning boxes, code blocks).
5. **Write the File:** Save the generated output to the user's workspace (e.g., \`lecture-2-slides.html\`).

### 2. Generating Summaries or Exercises

If the user asks for a summary or an exercise file:
1. Refer to existing files in the project (like \`lecture-1-summary.html\` or \`lecture-1-exercises.html\`) to understand the exact structure.
2. The style for these is typically a continuous document with a \`container\` class, a dark \`header\` block, and white \`content-section\` or \`exercise-card\` blocks.
3. Maintain the color palette: \`--sky: #C5A059\`, \`--deep: #1A1A1A\`, \`--bg: #FAFAFA\`.
4. Ensure the \`FiraGO\` and \`Playfair Display\` fonts are imported.

## Brand Guidelines & Tone

- **Tone:** Premium, professional, authoritative, but accessible. 
- **Colors:** Deep Charcoal/Black (\`#1A1A1A\`, \`#2C2C2C\`) and Gold/Champagne (\`#C5A059\`, \`#E6D5B3\`).
- **Terminology:** Avoid generic AI buzzwords where possible. Relate concepts back to real estate, investments, and development.

## Bundled Resources

- \`assets/slide-template.html\`: The base HTML structure for generating new slide presentations. Contains the core layout, sidebar mechanics, and CSS.
- \`references/components.md\`: A reference guide containing HTML snippets for rich visual components (Warning boxes, Grid comparisons, Code blocks with copy buttons) to use within the slides.

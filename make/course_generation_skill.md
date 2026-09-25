# AI Course Generation Skill (2026 Enterprise Standard)

**Skill Name**: `course_generator`
**Purpose**: Use this skill when the user says "მინდა ახალი კურსის შექმნა" (I want to create a new course) or explicitly requests the course generator.

## 1. Initial Clarification (The Intake)
When activated, do not generate anything immediately. First, ask the user for:
1. **Course Title & Goal**: (e.g., "Advanced AI Agents for Fintech")
2. **Number of Lectures**: (Standard is 6)
3. **Core Technologies**: (e.g., n8n, Ollama, Make.com)
4. **Lecture Breakdown**: Ask for a brief 1-sentence topic for each lecture if they have one.

## 2. Linguistic & Tone Policy (STRICT)
- **Language**: Professional Georgian.
- **Zero Abbreviations**: Replace jargon with full Georgian terms where possible, or use professional English terms without Georgian suffixes (e.g. `n8n-ის` is fine, but avoid `ჯიპიტი-ები`).
- **Typography**: Use Georgian quotation marks `„...“` and long em-dashes `—`.
- **Tone**: "Enterprise 2026". Focus on "Zero Data Leakage", "ROI", "Human-in-the-Loop", and "Deterministic Logic". 
- **Banned Words**: Never mention "Zapier" (use n8n instead) or "Voice AI" (unless explicitly requested). 

## 3. Workflow & Generation Order
Once the user provides the inputs, generate the course in this exact order:

### Step 1: The Manifest (`index.html`)
Generate a brutalist/FiraGO landing page. It MUST include:
- **AEO (Answer Engine Optimization)**: `<script type="application/ld+json">` for Course and FAQ schemas.
- **FAQ Section**: Must use semantic `<details itemscope itemtype="https://schema.org/Question">` tags.
- **Curriculum Section**: Generate `<div class="session-card">` elements for each lecture.

### Step 2: The Presentation Slides (`lecture-[N]-slides.html`)
For each lecture, generate a single HTML file containing all slides.
**Template**:
```html
<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="utf-8"/>
    <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
    <title>ლექცია N: სათაური</title>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet"/>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'FiraGO', sans-serif; line-height: 1.6; color: #2c3e50; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); min-height: 100vh; }
        .container { width: 100%; margin: 0 auto; padding: 1rem; }
        .slide { background: #ffffff; padding: 2rem; border-radius: 15px; margin-bottom: 2rem; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border-left: 5px solid #667eea; min-height: 80vh; position: relative; }
        .slide h1 { color: #2c3e50; margin-bottom: 1.5rem; font-size: 2.5rem; text-align: center; border-bottom: 3px solid #667eea; padding-bottom: 1rem; }
    </style>
</head>
<body>
    <div class="container">
        <!-- Slide 1 -->
        <div class="slide">
            <h1>ლექცია 1: სათაური</h1>
            <p>ტექსტი</p>
        </div>
    </div>
</body>
</html>
```

### Step 3: Supplementary Files Generator
Do NOT write the supplementary files manually. Write a Python script (e.g., `build_supplements.py`) using the official CSS template to batch-generate 4 files per lecture:
1. `lecture-[N]-summary.html`
2. `lecture-[N]-study-guide.html`
3. `lecture-[N]-quick-ref.html`
4. `lecture-[N]-exercises.html`

**Python Generation Script Template:**
```python
import os

CSS_STYLE = \"\"\"
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'FiraGO', sans-serif; line-height: 1.6; color: #2c3e50; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); min-height: 100vh; padding: 2rem 1rem; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 3px solid #667eea; font-size: 2.5rem; }
        h2 { color: #667eea; margin-top: 2.5rem; margin-bottom: 1.5rem; font-size: 2rem; }
        .highlight-box { background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3; margin: 1.5rem 0; }
        .nav-links { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 10px; display: flex; justify-content: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem; }
        .nav-link { color: white; text-decoration: none; padding: 0.7rem 1.5rem; border-radius: 8px; font-weight: 500; }
        .nav-link.current { background: white; color: #667eea; font-weight: 600; }
        .section-summary { background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0; border-left: 4px solid #667eea; }
\"\"\"

def generate_html(title, current_page, content, lecture_num):
    nav_links = {
        "index.html": "🏠 მთავარი",
        f"lecture-{lecture_num}-slides.html": "📊 სლაიდები",
        f"lecture-{lecture_num}-summary.html": "📚 შეჯამება",
        f"lecture-{lecture_num}-quick-ref.html": "📋 სწრაფი ცნობარი",
        f"lecture-{lecture_num}-exercises.html": "💪 სავარჯიშოები",
        f"lecture-{lecture_num}-study-guide.html": "📖 სასწავლო გზამკვლევი"
    }
    
    nav_html = '<nav class="nav-links">\\n'
    for link, text in nav_links.items():
        css_class = 'nav-link current' if link == current_page else 'nav-link'
        nav_html += f'        <a href="{link}" class="{css_class}">{text}</a>\\n'
    nav_html += '    </nav>'

    return f\"\"\"<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet"/>
    <style>{CSS_STYLE}</style>
</head>
<body>
    {nav_html}
    <div class="container">
        {content}
    </div>
</body>
</html>\"\"\"

# Add logic here to iterate over lectures and write files
```

## 4. Final Review
Always verify that the generated HTML files open correctly and that the JavaScript (e.g. for toggles or password protection `checkPasswordWithCookie`) is free of syntax errors.

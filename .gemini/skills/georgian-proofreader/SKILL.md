---
name: georgian-proofreader
description: Automates grammar, spelling, and terminology checks for Georgian web pages (HTML/MD), ensuring high-quality language and consistency with Tempo Holding branding and technical standards. Use when asked to proofread, fix grammar, or localize Georgian materials.
---

# Georgian Proofreader Skill

This skill provides a standardized workflow for proofreading and correcting Georgian content in the "AI - Generative Intelligence Practical Course" project.

## Workflow

1. **Full Content Audit**:
   - Read the **entire** file carefully.
   - Scan for English terms in: body text, placeholders, UI mocks (Email Subjects, CTAs), and button labels.

2. **Terminology Sweep**:
   - Refer to [terminology.md](references/terminology.md) for every identified technical term.
   - Use Georgian primary terms but keep original English in parentheses if it's critical for technical understanding (e.g., მითითება (Prompt)).

3. **Grammar & Tone Check**:
   - Apply **Tempo Holding** branding: elite, professional, responsible.
   - Check for: "ბულეტები" -> "პუნქტები", "თავის მართლება" -> "პასუხისმგებლობის აღება".
   - Ensure consistent punctuation and verb forms.

4. **Surgical Replacement**:
   - Apply changes using the `replace` tool.
   - After each replacement, re-scan surrounding text for context consistency.

## Priority Terminology
- **CTA** -> მოწოდება მოქმედებისკენ (CTA)
- **Subject Line** -> წერილის თემა
- **Action Items** -> სამოქმედო გეგმა / პუნქტები
- **Bullet Points** -> პუნქტობრივი ჩამონათვალი
- **Prompt** -> მითითება (პრომპტი)

For full terminology and branding guidelines, see [references/terminology.md](references/terminology.md).

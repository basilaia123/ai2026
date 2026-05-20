import re

def reorder_day2_html():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-slides.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Split the document by the section header comments
    sections_raw = re.split(r'(?=<!-- ═══ [A-Z ]+ ═══ -->)', html)

    section_dict = {}
    for i, sect in enumerate(sections_raw):
        match = re.search(r'<!-- ═══ ([A-Z ]+) ═══ -->', sect)
        if match:
            name = match.group(1).strip()
            section_dict[name] = sect
        else:
            section_dict[f'PART_{i}'] = sect

    print('Found blocks:', list(section_dict.keys()))

    # Desired logical order based on our discussion
    desired_order = [
        'PART_0',               # Header, Menu, Navigation, Title
        'AGENDA',
        'BLOCK I HEADER',       # კრეატიული აზროვნება, ინოვაცია და SOP-ების მართვა
        'THINKING PARTNER',     # 🧠 AI — Thinking Partner
        'BRAINSTORM',           # 💡 ბრეინშტორმინგი AI-სთან
        'REVERSE BRAINSTORM',   # 🔄 შებრუნებული აზროვნება
        'RISK',                 # 🔒 რისკი და კონფიდენციალობა (Moved here, after ideation, before saving to SOP)
        'NOTION INTRO',         # 📋 Notion
        'NOTION SOP',           # 📄 Notion AI + SOP
        'BREAK',                # ☕ შესვენება
        'BLOCK II HEADER',      # კვლევა, მონაცემთა ანალიზი და გადაწყვეტილებები
        'PERPLEXITY',           # 🔍 Perplexity.ai
        'NOTEBOOKLM',           # 📚 NotebookLM
        'DATA ANALYTICS',       # 📊 მონაცემთა ანალიტიკა
        'ROWS AI',              # 📊 Rows AI / Claude for Excel
        'BLOCK III HEADER',     # კრეატიული AI — ვიზუალები და იდეები (Leftovers)
        'BRAINSTORMING',        # 💡 იდეების გენერაცია (Brainstorming - micro task)
        'IMAGE PROMPTS',        # 🖼️ AI ვიზუალების გენერაცია
        'IMAGE PRACTICE',       # 🎨 მიკრო-დავალება სურათზე
        'SUMMARY'               # ✅ შეჯამება
    ]

    new_html = ""
    for name in desired_order:
        if name in section_dict:
            new_html += section_dict[name]
        else:
            print(f"WARNING: Missing section {name}")

    # Now update the Sidebar Navigation HTML to match this new order
    nav_old = '''<div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — 75 წთ</div>
        <a href="#thinking-partner" class="nav-link">🧠 AI — Thinking Partner</a>
        <a href="#few-shot" class="nav-link">🎯 Few-Shot Prompting</a>
        <a href="#risk" class="nav-link">🔒 რისკი და კონფიდენციალობა</a>
        <a href="#brainstorm" class="nav-link">💡 ბრეინშტორმინგი AI-სთან</a>
        <a href="#reverse" class="nav-link">🔄 შებრუნებული აზროვნება</a>
        <a href="#notion-intro" class="nav-link">📋 Notion — კორპორატიული მეხსიერება</a>
        <a href="#notion-sop" class="nav-link">📄 Notion AI + SOP-ების შექმნა</a>
        <a href="#practice1" class="nav-link">✏️ პრაქტიკა 1: Notion დოკუმენტი</a>'''

    nav_new = '''<div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — 75 წთ</div>
        <a href="#thinking-partner" class="nav-link">🧠 AI — Thinking Partner</a>
        <a href="#brainstorm" class="nav-link">💡 ბრეინშტორმინგი AI-სთან</a>
        <a href="#reverse" class="nav-link">🔄 შებრუნებული აზროვნება</a>
        <a href="#risk" class="nav-link">🔒 რისკი და კონფიდენციალობა</a>
        <a href="#notion-intro" class="nav-link">📋 Notion — კორპორატიული მეხსიერება</a>
        <a href="#notion-sop" class="nav-link">📄 Notion AI + SOP-ების შექმნა</a>
        <a href="#practice1" class="nav-link">✏️ პრაქტიკა 1: Notion დოკუმენტი</a>'''

    new_html = new_html.replace(nav_old, nav_new)

    # Note: the "Few-Shot Prompting" section was somehow missing from the HTML comments split or merged with something else.
    # We will check if it exists and clean it up if needed.

    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-slides.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Day 2 perfectly reordered.")

if __name__ == '__main__':
    reorder_day2_html()
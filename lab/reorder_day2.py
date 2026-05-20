import re

def reorder_slides():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Get IDs
    ids = re.findall(r'<section id=\"([^\"]+)\"', content)
    print("Found IDs:", ids)
    
    # We will use regex to capture each section.
    # Note: there are also Block headers (the div with class="py-8 border-b...") that we might need to move.
    
    # Let's rebuild the nav first
    nav_old = '''<div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — 75 წთ</div>
        <a href="#thinking-partner" class="nav-link">🧠 AI — Thinking Partner</a>
        <a href="#few-shot" class="nav-link">🎯 Few-Shot Prompting</a>
        <a href="#risk" class="nav-link">🔒 რისკი და კონფიდენციალობა</a>
        <a href="#brainstorm" class="nav-link">💡 ბრეინშტორმინგი AI-სთან</a>
        <a href="#reverse" class="nav-link">🔄 შებრუნებული აზროვნება</a>
        <a href="#notion-intro" class="nav-link">📋 Notion — კორპორატიული მეხსიერება</a>
        <a href="#notion-sop" class="nav-link">📄 Notion AI + SOP-ების შექმნა</a>
        <a href="#practice1" class="nav-link">✏️ პრაქტიკა 1: Notion დოკუმენტი</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">☕ შესვენება 10 წთ</div>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი II — 95 წთ</div>
        <a href="#perplexity" class="nav-link">🔍 Perplexity.ai — კვლევა</a>
        <a href="#notebooklm" class="nav-link">📚 NotebookLM — ცოდნის ბაზა</a>
        <a href="#practice2" class="nav-link">✏️ პრაქტიკა 2: NotebookLM</a>
        <a href="#data-analytics" class="nav-link">📊 მონაცემთა ანალიტიკა</a>
        <a href="#rows-ai" class="nav-link" style="padding-left:2rem;">Rows AI / Claude for Excel</a>
        <a href="#brainstorm-visual" class="nav-link">💡 Brainstorming — AI-სთან</a>
        <a href="#image-prompts" class="nav-link">🖼️ AI ვიზუალების გენერაცია</a>
        <a href="#image-practice" class="nav-link">🎨 მიკრო-დავალება: სოციალური მედია</a>
        <a href="#summary" class="nav-link">✅ შეჯამება და Q&amp;A</a>'''
        
    nav_new = '''<div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — 75 წთ</div>
        <a href="#thinking-partner" class="nav-link">🧠 AI — Thinking Partner</a>
        <a href="#brainstorm" class="nav-link">💡 ბრეინშტორმინგი AI-სთან</a>
        <a href="#reverse" class="nav-link">🔄 შებრუნებული აზროვნება</a>
        <a href="#few-shot" class="nav-link">🎯 Few-Shot Prompting</a>
        <a href="#risk" class="nav-link">🔒 რისკი და კონფიდენციალობა</a>
        <a href="#notion-intro" class="nav-link">📋 Notion — კორპორატიული მეხსიერება</a>
        <a href="#notion-sop" class="nav-link">📄 Notion AI + SOP-ების შექმნა</a>
        <a href="#practice1" class="nav-link">✏️ პრაქტიკა 1: Notion დოკუმენტი</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">☕ შესვენება 10 წთ</div>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი II — 95 წთ</div>
        <a href="#perplexity" class="nav-link">🔍 Perplexity.ai — კვლევა</a>
        <a href="#notebooklm" class="nav-link">📚 NotebookLM — ცოდნის ბაზა</a>
        <a href="#practice2" class="nav-link">✏️ პრაქტიკა 2: NotebookLM</a>
        <a href="#data-analytics" class="nav-link">📊 მონაცემთა ანალიტიკა</a>
        <a href="#rows-ai" class="nav-link" style="padding-left:2rem;">Rows AI / Claude for Excel</a>
        <a href="#brainstorm-visual" class="nav-link">💡 Brainstorming — AI-სთან</a>
        <a href="#image-prompts" class="nav-link">🖼️ AI ვიზუალების გენერაცია</a>
        <a href="#image-practice" class="nav-link">🎨 მიკრო-დავალება: სოციალური მედია</a>
        <a href="#summary" class="nav-link">✅ შეჯამება და Q&amp;A</a>'''
        
    content = content.replace(nav_old, nav_new)
    
    # We need to extract the HTML blocks of sections
    # It's safer to read line by line and construct blocks.
    lines = content.split('\\n')
    
    blocks = {}
    current_block_id = None
    current_lines = []
    
    # We will identify sections by `<section id="xxx"` or Block headers
    # Block 1 header is: <!-- ═══ BLOCK I HEADER ═══ -->
    # Block 2 header is: <!-- ═══ BLOCK II HEADER ═══ -->
    # Block 3 header is: <!-- ═══ BLOCK III HEADER ═══ --> (Visuals)
    
    in_section = False
    
    for line in lines:
        pass
        
    # Regex approach for the body is cleaner
    # Separate the header/nav from the body
    main_start = content.find('<div class="max-w-5xl pl-16 pr-6 md:pl-24 md:pr-10 py-10">')
    main_end = content.find('</main>')
    
    if main_start == -1 or main_end == -1:
        print("Could not find main content bounds")
        return
        
    pre_main = content[:main_start + len('<div class="max-w-5xl pl-16 pr-6 md:pl-24 md:pr-10 py-10">')]
    main_content = content[main_start + len('<div class="max-w-5xl pl-16 pr-6 md:pl-24 md:pr-10 py-10">'):main_end]
    post_main = content[main_end:]
    
    # Extract sections using non-greedy regex
    sections_raw = re.split(r'(?=<!-- ═══ [^═]+ ═══ -->)', main_content)
    
    # To debug what we split into
    section_dict = {}
    for sect in sections_raw:
        match = re.search(r'<!-- ═══ ([^═]+) ═══ -->', sect)
        if match:
            name = match.group(1).strip()
            section_dict[name] = sect
        else:
            if sect.strip():
                section_dict['INTRO_AGENDA'] = sect

    # Check if we got everything
    print("Found section comments:", section_dict.keys())
    
    # Rebuild in the desired order
    desired_order = [
        'INTRO_AGENDA',
        'BLOCK I HEADER',
        'THINKING PARTNER',
        'BRAINSTORM',
        'REVERSE BRAINSTORMING',
        'FEW-SHOT',
        'RISK',
        'NOTION INTRO',
        'NOTION SOP',
        'PRACTICE 1',
        'BLOCK II HEADER',
        'PERPLEXITY',
        'NOTEBOOK LM',
        'PRACTICE 2',
        'DATA ANALYTICS',
        'ROWS AI',
        'BLOCK III HEADER',
        'BRAINSTORMING', # Note: 'BRAINSTORMING' is #brainstorm-visual
        'IMAGE PROMPTS',
        'IMAGE PRACTICE',
        'SUMMARY'
    ]
    
    new_main_content = ""
    for name in desired_order:
        if name in section_dict:
            new_main_content += section_dict[name]
        else:
            print(f"WARNING: Missing section {name} from parsed blocks")
            
    final_content = pre_main + new_main_content + post_main
    
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-slides.html', 'w', encoding='utf-8') as f:
        f.write(final_content)
        
    print("Reordered successfully!")

if __name__ == '__main__':
    reorder_slides()
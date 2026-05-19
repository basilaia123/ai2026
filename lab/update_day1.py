import re

with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replace_code_block(match):
    full_match = match.group(0)
    button_match = match.group(1)
    inner_text = match.group(2).strip()
    
    # If the block has a copy button OR has multiple lines, we style it as a Blueprint
    if button_match or '\n' in inner_text:
        return f'''<div class=\"relative rounded-lg p-6 text-sm text-gray-300 group hover:border-[#2196F3]/30 border border-transparent transition-all shadow-lg\" style=\"background:#0f1f2e; margin-top:1rem;\">
    <div class=\"flex items-center justify-between mb-4\">
        <span class=\"text-[10px] uppercase tracking-widest font-bold\" style=\"color:#2196F3;\">Prompt Blueprint</span>
        <button class=\"copy-btn px-3 py-1 rounded transition-all border\" style=\"background:rgba(33,150,243,0.1); color:#2196F3; border-color:rgba(33,150,243,0.2); font-size:10px;\" onmouseover=\"this.style.background='#2196F3'; this.style.color='white';\" onmouseout=\"this.style.background='rgba(33,150,243,0.1)'; this.style.color='#2196F3';\" onclick=\"copyText(this)\">კოპირება</button>
    </div>
    <pre class=\"font-mono leading-relaxed text-gray-200 whitespace-pre-wrap\">{inner_text}</pre>
</div>'''
    
    # Otherwise return original
    return full_match

# Find <div class="code-block" ...> ... </div>
pattern = re.compile(r'<div class=\"code-block\"[^>]*>(?:\s*(<button[^>]*>.*?<\/button>)\s*)?(.*?)<\/div>', re.DOTALL)

new_content = pattern.sub(replace_code_block, content)

with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Done. Replaced code blocks.')

import re

def update_day1():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the JS copy function so it handles the new structure properly
    old_js = """function copyText(btn) {
    const codeBlock = btn.parentElement;
    const text = codeBlock.innerText.replace('კოპირება', '').trim();
    navigator.clipboard.writeText(text).then(() => {
        btn.textContent = '✓ დაკოპირდა';
        setTimeout(() => btn.textContent = 'კოპირება', 2000);
    });
}"""
    
    new_js = """function copyText(btn) {
    const codeBlock = btn.closest('.code-block, .prompt-blueprint');
    const contentNode = codeBlock.querySelector('.code-content');
    let text = '';
    if (contentNode) {
        text = contentNode.innerText.trim();
    } else {
        text = codeBlock.innerText.replace('კოპირება', '').replace('Prompt Blueprint', '').trim();
    }
    navigator.clipboard.writeText(text).then(() => {
        btn.textContent = '✓ დაკოპირდა';
        setTimeout(() => btn.textContent = 'კოპირება', 2000);
    });
}"""
    
    if old_js in html:
        html = html.replace(old_js, new_js)
    else:
        print("Warning: Could not find original JS copyText function. It might have been modified.")

    # 2. Replace all code-blocks with a unified Prompt Blueprint / Code Snippet design
    def replacer(match):
        full_tag = match.group(1) # <div class="code-block" style="...">
        inner_content = match.group(2)
        
        # Check if there's a button
        has_button = False
        button_match = re.search(r'<button[^>]*>.*?<\/button>', inner_content)
        if button_match:
            has_button = True
            inner_content = inner_content.replace(button_match.group(0), '').strip()
            
        inner_content = inner_content.strip()
        
        # Standardized design
        return f'''<div class="prompt-blueprint" style="background: #0f1f2e; border: 1px solid rgba(33,150,243,0.3); border-radius: 8px; padding: 1.25rem 1.5rem; margin: 1rem 0; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">
        <span style="color: #2196F3; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">Prompt Blueprint</span>
        <button class="copy-btn" style="position: static; font-size: 0.7rem; background: rgba(33,150,243,0.1); color: #2196F3; border: 1px solid rgba(33,150,243,0.3); padding: 0.2rem 0.5rem; border-radius: 4px; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#2196F3'; this.style.color='#fff';" onmouseout="this.style.background='rgba(33,150,243,0.1)'; this.style.color='#2196F3';" onclick="copyText(this)">კოპირება</button>
    </div>
    <div class="code-content" style="font-family: 'Courier New', monospace; font-size: 0.85rem; color: #e2e8f0; white-space: pre-wrap; line-height: 1.6;">{inner_content}</div>
</div>'''

    # Find all <div class="code-block"...>...</div>
    pattern = re.compile(r'(<div[^>]*class=\"[^\"]*code-block[^\"]*\"[^>]*>)(.*?)<\/div>', re.DOTALL)
    
    new_html = pattern.sub(replacer, html)
    
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    
    print("Successfully standardized all code blocks.")

if __name__ == '__main__':
    update_day1()

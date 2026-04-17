import os
import re

print("Starting quick-ref processing...")

renames = {
    'lecture-7-quick-ref.html': 'lecture-5.temp.html',
    'lecture-8-quick-ref.html': 'lecture-6.temp.html',
    'lecture-9-quick-ref.html': 'lecture-7.temp.html',
    'lecture-6-quick-ref.html': 'lecture-8.temp.html',
    'lecture-10-quick-ref.html': 'lecture-9.temp.html'
}

for old, new in renames.items():
    if os.path.exists(old):
        os.rename(old, new)

temps = {
    'lecture-5.temp.html': 'lecture-5-quick-ref.html',
    'lecture-6.temp.html': 'lecture-6-quick-ref.html',
    'lecture-7.temp.html': 'lecture-7-quick-ref.html',
    'lecture-8.temp.html': 'lecture-8-quick-ref.html',
    'lecture-9.temp.html': 'lecture-9-quick-ref.html'
}

for old, new in temps.items():
    if os.path.exists(old):
        if os.path.exists(new):
            os.remove(new)
        os.rename(old, new)

# Delete orphans
orphans = ['lecture-11-quick-ref.html', 'lecture-12-quick-ref.html']
for orphan in orphans:
    if os.path.exists(orphan):
        os.remove(orphan)

# Update content
for i in range(1, 10):
    fname = f'lecture-{i}-quick-ref.html'
    if not os.path.exists(fname): continue
    
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # Title & H1
    content = re.sub(r'<title>.*?</title>', f'<title>ლექცია {i} - მოკლე ცნობარი (Quick Reference)</title>', content)
    content = re.sub(r'<h1>ლექცია \d+ - მოკლე ცნობარი</h1>', f'<h1>ლექცია {i} - მოკლე ცნობარი</h1>', content)

    # Nav Menu
    old_nav = r'<div class="nav-menu">.*?</div>'
    new_nav = f'''<div class="nav-menu">
            <a href="index.html">🏠 მთავარი გვერდი</a>
            <a href="v2-lecture-{i}-slides.html">📊 სლაიდები</a>
            <a href="lecture-{i}-exercises.html">✏️ სავარჯიშოები</a>
            <a href="lecture-{i}-summary.html">📚 შეჯამება</a>
        </div>'''
    content = re.sub(old_nav, new_nav, content, flags=re.DOTALL)

    # Models
    content = content.replace('GPT-4o', 'GPT-5.4')
    content = content.replace('GPT-4', 'GPT-5.4')
    content = content.replace('Midjourney v6', 'Midjourney v7')
    content = content.replace('Claude 3.5', 'Claude 4.6')
    content = content.replace('Claude 3', 'Claude 4.6')
    content = content.replace('DALL-E 3', 'Flux.1 Pro')
    content = content.replace('Sora (OpenAI)', 'Sora 2.0')
    content = content.replace('Google Veo', 'Veo 3')
    
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)

print("Quick-refs mapped, updated and finalized.")

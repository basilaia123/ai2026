# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================== PARSING eu4dialogue/pm/index.html ====================")
with open('eu4dialogue/pm/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find each session card by finding <div class="session-card
cards = re.findall(r'<div class="session-card(.*?)</div>\s*</div>\s*</div>\s*(?:</div>|\n\s*<!-- Module|\n\s*<!-- Day|\n\s*</div>\s*<!--)', text, re.DOTALL)
print(f"Total session cards parsed: {len(cards)}")

# Better yet, regex find session headers and content
headers = re.findall(r'<div class="session-num-badge"[^>]*>(\d+)</div>\s*<div>\s*<div class="session-title"[^>]*>(.*?)</div>\s*</div>\s*</div>\s*<div class="session-badge"[^>]*>(.*?)</div>', text)
for num, title, badge in headers:
    print(f"\n[Module {num}] {badge.strip()}\nTitle: {title.strip()}")
    # Find block titles under this
    # Let's extract slice of text from this module to next
    pos = text.find(f'>{num}</div>')
    next_pos = text.find(f'>{int(num)+1:02d}</div>') if int(num) < 8 else text.find('class="interactive-syllabus"', pos)
    mod_chunk = text[pos:next_pos] if next_pos != -1 else text[pos:pos+3000]
    
    block_titles = re.findall(r'<div class="session-block-title"[^>]*>(.*?)</div>', mod_chunk)
    for bt in block_titles:
        print(f"   ► {bt.strip()}")
    
    # Also tasks and polls
    tasks = re.findall(r'<div class="session-task-box"[^>]*>(.*?)</div>', mod_chunk, re.DOTALL)
    for t in tasks:
        clean_t = re.sub(r'<.*?>', '', t).strip()
        print(f"   🔧 TASK: {clean_t[:120]}...")

    polls = re.findall(r'<div class="session-poll-box"[^>]*>(.*?)</div>', mod_chunk, re.DOTALL)
    for p in polls:
        clean_p = re.sub(r'<.*?>', '', p).strip()
        print(f"   📊 POLL: {clean_p[:120]}...")

print("\n\n==================== PARSING eu4dialogue/pm/proposal.md ====================")
with open('eu4dialogue/pm/proposal.md', 'r', encoding='utf-8') as f:
    ptext = f.read()

# Find modules in markdown
for m in re.finditer(r'### მოდული (\d+): (.*?)\n(.*?)(?=\n### მოდული|\n## |$)', ptext, re.DOTALL):
    print(f"\n[MD Module {m.group(1)}] {m.group(2).strip()}")
    for line in m.group(3).strip().split('\n')[:8]:
        if line.strip():
            print(f"   {line.strip()}")

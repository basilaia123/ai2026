# -*- coding: utf-8 -*-
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('eu4dialogue/pm/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract sessions
cards = re.findall(r'<div class="session-card.*?>(.*?)</div>\s*</div>\s*</div>\s*</div>', text, re.DOTALL)
print(f"Cards found: {len(cards)}")

# Or let's parse session-title, session-badge, and topics
day_matches = re.split(r'<!-- DAY \d+ HEADING -->', text)
print(f"Days split: {len(day_matches)}")

for day_idx, day_content in enumerate(day_matches[1:], 1):
    print(f"\n==================== DAY {day_idx} ====================")
    sessions = re.findall(r'<div class="session-card.*?<div class="session-num-badge">(\d+)</div>.*?<div class="session-title">(.*?)</div>.*?<div class="session-badge">(.*?)</div>(.*?)</div>\s*</div>\s*</div>', day_content, re.DOTALL)
    for num, title, badge, body in sessions:
        print(f"\n--- Module {num}: {title.strip()} [{badge.strip()}] ---")
        topics = re.findall(r'<li.*?>(.*?)</li>', body)
        for t in topics:
            clean_t = re.sub(r'<.*?>', '', t).strip()
            print(f"   * {clean_t}")

import json
from collections import Counter

d1 = json.load(open(r'C:\Users\GBASILAIA\claude\ai2026\GITA\Pre-Acceleration\2026-5h-AI-for-Startups\day1-slides.json', encoding='utf-8'))
d2 = json.load(open(r'C:\Users\GBASILAIA\claude\ai2026\GITA\Pre-Acceleration\2026-5h-AI-for-Startups\day2-slides.json', encoding='utf-8'))

print('=== DAY 1 sample ===')
for i in [0, 1, 7, 8, 9, 22, 46]:
    if i < len(d1):
        s = d1[i]
        print(f"  [{s['index']:2d}] kind={s['kind']:10s} title={s['title'][:60]}")
        for b in s['blocks'][:3]:
            t = b.get('type', '?')
            txt = (b.get('text') or b.get('class') or '')[:80]
            print(f"      - {t}: {txt}")

print()
print('=== DAY 2 sample ===')
for i in [0, 1, 7, 8, 41]:
    if i < len(d2):
        s = d2[i]
        print(f"  [{s['index']:2d}] kind={s['kind']:10s} title={s['title'][:60]}")
        for b in s['blocks'][:3]:
            t = b.get('type', '?')
            txt = (b.get('text') or b.get('class') or '')[:80]
            print(f"      - {t}: {txt}")

print()
print(f"Day 1 kinds: {Counter(s['kind'] for s in d1)}")
print(f"Day 2 kinds: {Counter(s['kind'] for s in d2)}")
print(f"Day 1 total blocks: {sum(len(s['blocks']) for s in d1)}")
print(f"Day 2 total blocks: {sum(len(s['blocks']) for s in d2)}")
print(f"Day 1 avg blocks/slide: {sum(len(s['blocks']) for s in d1)/len(d1):.1f}")
print(f"Day 2 avg blocks/slide: {sum(len(s['blocks']) for s in d2)/len(d2):.1f}")
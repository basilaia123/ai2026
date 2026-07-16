import json
d = json.load(open(r'C:\Users\GBASILAIA\claude\ai2026\GITA\Pre-Acceleration\2026-5h-AI-for-Startups\day2-slides.json', encoding='utf-8'))
s = d[8]  # slide 9
print(f"=== Day 2 Slide 9 (Ideogram) ===")
def walk(b, depth=0):
    pad = "  " * depth
    t = b.get('type')
    cls = b.get('class','')
    print(f"{pad}- {t} class={cls!r}")
    if 'text' in b:
        print(f"{pad}  text={b['text'][:100]!r}")
    if 'blocks' in b:
        for sb in b['blocks']:
            walk(sb, depth+1)
for b in s['blocks']:
    walk(b)

print()
print('=== Day 1 Slide 23 (Convergent Thinking) ===')
d = json.load(open(r'C:\Users\GBASILAIA\claude\ai2026\GITA\Pre-Acceleration\2026-5h-AI-for-Startups\day1-slides.json', encoding='utf-8'))
s = d[22]
for b in s['blocks']:
    walk(b)
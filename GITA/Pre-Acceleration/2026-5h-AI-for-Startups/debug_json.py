import json
d = json.load(open(r'C:\Users\GBASILAIA\claude\ai2026\GITA\Pre-Acceleration\2026-5h-AI-for-Startups\day1-slides.json', encoding='utf-8'))
print(f'Total slides: {len(d)}')
print(f'Numbers: {[s["number"] for s in d]}')
print(f'Titles:')
for s in d:
    print(f'  [{s["number"]:2d}] {s["title"][:60]}')
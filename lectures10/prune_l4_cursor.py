import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-4-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

slides = soup.find_all('div', class_='slide')

deleted_count = 0
for slide in slides:
    t = slide.find(['h1', 'h2'])
    if t:
        text = t.get_text(strip=True)
        if re.search(r'Cursor', text) or re.search(r'ახალი სტანდარტი', text):
            slide.decompose()
            deleted_count += 1
            break

# Re-number slides
slides = soup.find_all('div', class_='slide')
total = len(slides)
for i, slide in enumerate(slides, 1):
    span = slide.find('span', class_='slide-number')
    if span:
        span.string = f"{i}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print(f"Total deleted: {deleted_count}. New slide count: {total}")

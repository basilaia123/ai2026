import os
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-10-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

slides = soup.find_all('div', class_='slide')
removed = 0

for slide in slides:
    title_tags = slide.find_all(['h1', 'h2'])
    for t in title_tags:
        if 'პრეზენტაციების რიგი' in t.text:
            slide.decompose()
            removed += 1
            break # move to next slide

# Renumber remaining slides
current_slides = soup.find_all('div', class_='slide')
total = len(current_slides)

for idx, slide in enumerate(current_slides, 1):
    sn = slide.find(class_='slide-number')
    if sn:
        sn.string = f"{idx}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Removed {removed} 'Presentation Order' slides. Total slides now: {total}.")

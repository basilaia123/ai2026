import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-4-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

slides = soup.find_all('div', class_='slide')

def find_all_slides(pattern):
    results = []
    for s in soup.find_all('div', class_='slide'):
        t = s.find(['h1', 'h2'])
        if t and re.search(pattern, t.get_text()):
            results.append(s)
    return results

# 1. Marketing Prompts
mrkt = find_all_slides(r'მარკეტინგული Prompt-|მარკეტინგული პრომპტების')
for s in mrkt:
    s.decompose()

# 2. Dry stats
stats_patterns = [
    r'სტატისტიკა',
    r'ავტომატიზაციის ბაზარი',
    r'ინდუსტრიული AI'
]
for pat in stats_patterns:
    st = find_all_slides(pat)
    for s in st:
        s.decompose()

# 3. Duplicate Best Practices
prac = find_all_slides(r'საუკეთესო პრაქტიკა|საუკეთესო პრაქტიკები')
if len(prac) > 1:
    prac[0].decompose() # Delete the first occurrence, keep the last one

# Re-number slides properly
slides = soup.find_all('div', class_='slide')
total = 0
for slide in slides:
    nav = slide.find('div', class_='navigation')
    t = slide.find(['h1', 'h2'])
    if t or not nav:
        total += 1

slide_index = 1
for slide in slides:
    nav = slide.find('div', class_='navigation')
    t = slide.find(['h1', 'h2'])
    
    if t or not nav:
        num_tag = slide.find(class_='slide-number')
        if num_tag:
            num_tag.string = f"{slide_index}/{total}"
        slide_index += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print(f"Final pruning done. Total slides: {total}")

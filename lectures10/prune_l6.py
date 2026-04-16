import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-6-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def find_all_slides(pattern):
    results = []
    for s in soup.find_all('div', class_='slide'):
        t = s.find(['h1', 'h2'])
        if t and re.search(pattern, t.get_text()):
            results.append(s)
    return results

# 1. Delete QA
qa_slides = find_all_slides(r'კითხვები და პასუხები')
for s in qa_slides:
    s.decompose()

# 2. Merge Ethics and Copyright
ethics = find_all_slides(r'ეთიკური საკითხები')
copyr = find_all_slides(r'საავტორო უფლებები')
if ethics and copyr:
    eth = ethics[0]
    cp = copyr[0]
    # rename eth
    t = eth.find(['h1', 'h2'])
    if t:
        t.string = "⚖️ ეთიკურ-სამართლებრივი საკითხები (Copyright)"
    
    # create two columns or just append cp content
    container = soup.new_tag('div')
    container['class'] = 'two-column'
    container['style'] = 'margin-top: 1rem;'
    
    col1 = soup.new_tag('div')
    eth_content = eth.find('div', class_='key-points') or eth.find('div', class_='warning-box')
    if eth_content:
        col1.append(eth_content.extract())
        
    col2 = soup.new_tag('div')
    cp_content = cp.find('div', class_='key-points') or cp.find('div', class_='warning-box')
    if cp_content:
        col2.append(cp_content.extract())
        
    container.append(col1)
    container.append(col2)
    eth.append(container)
    cp.decompose()

# 3. Merge Captions and Platform Optimization
caps = find_all_slides(r'სუბტიტრები')
opt = find_all_slides(r'პლატფორმებისთვის ოპტიმიზაცია')
if caps and opt:
    c = caps[0]
    o = opt[0]
    t = c.find(['h1', 'h2'])
    if t:
        t.string = "📝 სუბტიტრები და პლატფორმებისთვის ოპტიმიზაცია"
        
    container = soup.new_tag('div')
    container['class'] = 'two-column'
    container['style'] = 'margin-top: 1rem;'
    
    col1 = soup.new_tag('div')
    c_content = c.find('div', class_='key-points') or c.find('div', class_='highlight-box')
    if c_content:
        col1.append(c_content.extract())
        
    col2 = soup.new_tag('div')
    o_content = o.find('div', class_='key-points') or o.find('div', class_='highlight-box')
    if o_content:
        col2.append(o_content.extract())
        
    container.append(col1)
    container.append(col2)
    c.append(container)
    o.decompose()

# Renumber slides
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
    
print(f"L6 pruned successfully. New slide count: {total}")

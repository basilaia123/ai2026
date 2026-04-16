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

def find_and_delete(pattern, keep_last=False):
    found = find_all_slides(pattern)
    if not found: return
    if keep_last:
        for s in found[:-1]:
            s.decompose()
    else:
        for s in found:
            s.decompose()

# 1. Structural Duplicates
# "სასწავლო მიზნები"
find_and_delete(r'სასწავლო მიზნები', keep_last=False) # Wait, we must keep the first one!
# Actually, find_all_slides returns in order.
objs = find_all_slides(r'სასწავლო მიზნები')
if len(objs) > 1:
    for s in objs[1:]:
        s.decompose()

# "ძირითადი დასკვნები" or "დასკვნები"
concl = find_all_slides(r'ძირითადი დასკვნები')
if len(concl) > 1:
    concl[0].decompose() # Delete the one in the middle

# Middle QA & Resources
find_and_delete(r'^❓ კითხვა-პასუხი$')
find_and_delete(r'^🧭 სასარგებლო მასალები$')
find_and_delete(r'^ჩვენი მოგზაურობა ხელოვნური ინტელექტის სამყაროში$')

# 2. Mistakes and Best Practices
errs = find_all_slides(r'შეცდომები')
if len(errs) > 1:
    errs[0].decompose() # Delete early instance

prac = find_all_slides(r'საუკეთესო პრაქტიკა')
if len(prac) > 1:
    prac[0].decompose() # Delete early instance
    
# 3. Industry / Use-Case Bloat
industry_patterns = [
    r'ხელოვნური ინტელექტი მარკეტინგში',
    r'მარკეტინგული პრომპტების შაბლონები',
    r'ადამიანურ რესურსებსა',
    r'ადამიანური რესურსების პრომპტების',
    r'პროგრამული უზრუნველყოფის შემუშავებაში',
    r'დეველოპმენტის Prompt',
    r'^AI ფინანსებში',
    r'ფინანსური Prompt',
    r'^AI ჯანდაცვაში',
    r'ჯანდაცვის Prompt',
    r'^AI მარკეტინგში',
    r'^AI გაყიდვებში',
    r'გაყიდვების Prompt',
    r'^AI ადამიანურ რესურსებში',
    r'HR Prompt',
    r'^AI განათლებაში',
    r'განათლების Prompt',
    r'^AI პროექტების მართვაში',
    r'პროექტების მართვის Prompt',
    r'ყოველდღიური გამოყენება'
]

for pat in industry_patterns:
    find_and_delete(pat)

# 4. Merge Practical Exercises
# We have 3 exercises. We will keep the last one and append the first two into it.
exercises = find_all_slides(r'პრაქტიკული')
if len(exercises) > 1:
    main_ex = exercises[-1]
    title = main_ex.find(['h1', 'h2'])
    if title:
        title.string = "კომპლექსური პრაქტიკული სავარჯიშო (ინფორმაციის მოძიება + კვლევა)"
    
    # Create two columns layout
    container = soup.new_tag('div')
    container['class'] = 'two-column'
    container['style'] = 'margin-top: 1rem;'
    
    # Take the content of the FIRST exercise
    ex1_content = exercises[0].find('div', class_='key-points') or exercises[0].find('div', class_='highlight-box')
    if ex1_content:
        col1 = soup.new_tag('div')
        h3 = soup.new_tag('h4')
        h3.string = "ნაწილი 1: მონაცემთა მოძიება"
        col1.append(h3)
        ex1_content.extract()
        col1.append(ex1_content)
        container.append(col1)
        
    # Take the content of the LAST (main) exercise
    ex2_content = main_ex.find('div', class_='key-points') or main_ex.find('div', class_='highlight-box')
    if ex2_content:
        col2 = soup.new_tag('div')
        h3 = soup.new_tag('h4')
        h3.string = "ნაწილი 2: პროფესიული ქეისი"
        col2.append(h3)
        # Move actual items
        items = main_ex.find_all(['ol', 'ul', 'p'])
        for item in items:
            # check if it is direct child of slide-content or main_ex to avoid moving the entire slide text
            if item.parent == main_ex or 'key-points' in (item.parent.get('class') or []):
                i_clone = item.extract()
                col2.append(i_clone)
        container.append(col2)
        
    main_ex.append(container)
    
    # delete the early exercises
    for ex in exercises[:-1]:
        ex.decompose()

# Delete empty trailing navigation if present
current_slides = soup.find_all('div', class_='slide')
for slide in current_slides:
    nav = slide.find('div', class_='navigation')
    t = slide.find(['h1', 'h2'])
    if nav and not t:
        slide.decompose()

# Renumber
slides = soup.find_all('div', class_='slide')
total = len(slides)
for i, slide in enumerate(slides, 1):
    span = slide.find('span', class_='slide-number')
    if span:
        span.string = f"{i}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print(f"File updated. New slide count: {total}")

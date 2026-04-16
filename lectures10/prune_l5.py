import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-5-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

def find_all_slides(pattern):
    results = []
    for s in soup.find_all('div', class_='slide'):
        t = s.find(['h1', 'h2'])
        if t and re.search(pattern, t.get_text()):
            results.append(s)
    return results

# 1. Delete Video Generation Slides
video_slides = find_all_slides(r'ვიდეო გენერაცია|ვიდეო კონტენტის|ვიდეო გენერაციის პრომპტები|ვიდეოს დამატებითი')
for s in video_slides:
    s.decompose()

# 2. Prune fluff
fluff_slides = find_all_slides(r'სურათების ზომები|კითხვები და პასუხები')
for s in fluff_slides:
    s.decompose()

# 3. Merge Tool Overviews
# Slide 4: სურათების გენერაცია - ლიდერები
# Slide 8: სურათების გენერირების ინსტრუმენტები
tool_slides = find_all_slides(r'სურათების გენერაცია - ლიდერები|სურათების გენერირების ინსტრუმენტები')
if len(tool_slides) > 1:
    # Delete the latter one
    tool_slides[1].decompose()

# 4. Merge Practical Exercises
exercises = find_all_slides(r'პრაქტიკული სავარჯიშო|საკლასო დავალება')
if len(exercises) > 1:
    main_ex = exercises[-1]
    title = main_ex.find(['h1', 'h2'])
    if title:
        title.string = "კომპლექსური პრაქტიკული სავარჯიშო (ვიზუალური გენერაცია)"
    
    # Create two columns layout
    container = soup.new_tag('div')
    container['class'] = 'two-column'
    container['style'] = 'margin-top: 1rem;'
    
    # Take the content of the FIRST exercise
    ex1_content = exercises[0].find('div', class_='key-points') or exercises[0].find('div', class_='highlight-box') or exercises[0].find('div', class_='exercise-box')
    if ex1_content:
        col1 = soup.new_tag('div')
        h3 = soup.new_tag('h4')
        h3.string = "ნაწილი 1: პრომპტების შექმნა"
        col1.append(h3)
        ex1_content.extract()
        col1.append(ex1_content)
        container.append(col1)
        
    # Take the content of the LAST (main) exercise
    ex2_content = main_ex.find('div', class_='key-points') or main_ex.find('div', class_='highlight-box') or main_ex.find('div', class_='exercise-box')
    if ex2_content:
        col2 = soup.new_tag('div')
        h3 = soup.new_tag('h4')
        h3.string = "ნაწილი 2: პრაქტიკული გენერაცია"
        col2.append(h3)
        # Move actual items
        items = main_ex.find_all(['ol', 'ul', 'p'])
        for item in items:
            if item.parent == main_ex or 'key-points' in (item.parent.get('class') or []) or 'exercise-box' in (item.parent.get('class') or []):
                i_clone = item.extract()
                col2.append(i_clone)
        container.append(col2)
        
    # Appending to main_ex
    # remove old stuff
    for el in main_ex.find_all('div', recursive=False):
        if el.get('class') != ['slide-number'] and el.name != 'h2':
            if el != container:
                el.decompose()
                
    main_ex.append(container)
    
    # Add a time box at the end
    time_box = soup.new_tag('div')
    time_box['class'] = 'warning-box'
    time_box['style'] = 'margin-top: 2rem;'
    h4_time = soup.new_tag('h4')
    h4_time.string = "⏱️ სრული დავალების დრო: 20 წუთი"
    time_box.append(h4_time)
    main_ex.append(time_box)
    
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
    span = slide.find(class_='slide-number')
    if span:
        span.string = f"{i}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print(f"L5 pruned successfully. New slide count: {total}")

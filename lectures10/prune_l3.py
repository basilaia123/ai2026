import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-3-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

slides = soup.find_all('div', class_='slide')

def find_slide(text_pattern):
    for slide in slides:
        h12 = slide.find_all(['h1', 'h2'])
        for h in h12:
            if re.search(text_pattern, h.get_text()):
                return slide
    return None

# Merge logic for "ხშირი შეცდომები" (Old 56 into 22)
err_slide1 = find_slide(r'ხშირი შეცდომები$')  # Slide 22 has no emoji
err_slide2 = find_slide(r'❌ ხშირი შეცდომები')

if err_slide1 and err_slide2:
    idx2 = slides.index(err_slide2)
    # Extract list items from err_slide2 and append to err_slide1
    ul1 = err_slide1.find('ul')
    ul2 = err_slide2.find('ul')
    if ul1 and ul2:
        for li in ul2.find_all('li'):
            ul1.append(li)
    err_slide2.decompose()

# Merge logic for "საუკეთესო პრაქტიკები"
best_slide1 = find_slide(r'^საუკეთესო პრაქტიკები$')
best_slide2 = find_slide(r'⭐ საუკეთესო პრაქტიკები')

if best_slide1 and best_slide2:
    ul1 = best_slide1.find('ul')
    ul2 = best_slide2.find('ul')
    if ul1 and ul2:
        for li in ul2.find_all('li'):
            ul1.append(li)
    best_slide2.decompose()

# 2. Extract Brainstorming frameworks (Slides 32-36) into Slide 31
brainstorm_main = find_slide(r'ბრეინშტორმინგის ტექნიკები AI-ით')
patterns_to_merge = [
    r'SCAMPER', r'What If', r'ანალოგიური აზროვნება', 
    r'შებრუნებული ბრეინშტორმინგი', r'შემთხვევითი მონაცემების'
]

if brainstorm_main:
    # Create a new container to hold these summaries in brainstorm_main
    container = soup.new_tag('div')
    container['class'] = 'two-column'
    container['style'] = 'margin-top: 15px;'
    
    for pat in patterns_to_merge:
        s = find_slide(pat)
        if s:
            t = s.find(['h2', 'h3', 'h4'])
            if t:
                # take first paragraph or list
                desc = s.find(['p', 'ul'])
                box = soup.new_tag('div')
                box['class'] = 'highlight-box'
                new_h4 = soup.new_tag('h4')
                new_h4.string = t.get_text()
                box.append(new_h4)
                if desc:
                    box.append(desc) # moves it
                container.append(box)
            s.decompose()
    
    brainstorm_main.append(container)


# 3. Simple deletions
to_delete_patterns = [
    r'^ძირითადი დასკვნები$', # Slide 27
    r'^📚 სწავლის მიზნები$', # Slide 28
    r'^💡 რა არის შემოქმედებითი იდეაცია\?$', # Slide 29
    r'^🧱 შემოქმედებითი ბლოკების დაძლევა$', # Slide 44
    r'^💪 პრაქტიკული სავარჯიშო$', # Slide 52
    r'^⏱️ 10-წუთიანი პრაქტიკული დავალება$', # Slide 53
    r'^🎮 ბონუსი: SCAMPER ინტერაქტიული თამაში$', # Slide 54
    r'^📚 შემდეგი ნაბიჯები$' # Slide 58
]

for pat in to_delete_patterns:
    s = find_slide(pat)
    if s:
        s.decompose()

# Delete Slide 60 (Empty or No Title)
# Sometimes the last slide is empty or has no h1/h2
# Let's cleanly check slides again
current_slides = soup.find_all('div', class_='slide')
for s in current_slides:
    titles = s.find_all(['h1', 'h2'])
    if not titles:
        # Check if it has any meaningful content
        content = s.get_text(strip=True)
        if len(content) < 10 or 'No title' in content:  # Often just a number
            s.decompose()

# Finally, re-number the slides
current_slides = soup.find_all('div', class_='slide')
total = len(current_slides)
for i, slide in enumerate(current_slides, 1):
    span = slide.find(class_='slide-number')
    if span:
        span.string = f"{i}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"Done! New slide count: {total}")

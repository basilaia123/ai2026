import os
import re
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-7-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Bump dates
text = re.sub(r'2024', '2025', text)
text = re.sub(r'2025', '2026', text)

soup = BeautifulSoup(text, 'html.parser')

def find_all_slides(pattern):
    results = []
    for s in soup.find_all('div', class_='slide'):
        t = s.find(['h1', 'h2'])
        if t and re.search(pattern, t.get_text()):
            results.append(s)
    return results

# 2. QA delete
qas = find_all_slides(r'კითხვები და პასუხები')
for q in qas:
    q.decompose()

# 3. Merge Thank You into Summary or Resources
thx = find_all_slides(r'გმადლობთ ყურადღებისთვის')
summs = find_all_slides(r'ლექციის შეჯამება')
if thx and summs:
    s = summs[-1]
    t_slide = thx[0]
    
    # Append the nice emoji text to summary
    p = soup.new_tag('p')
    p['style'] = "font-size: 1.2rem; margin-top: 2rem; color: #666; text-align: center;"
    p.string = "გმადლობთ ყურადღებისთვის! 🙏"
    
    # put it before navigation
    nav = s.find('div', class_='navigation')
    if nav:
        nav.insert_before(p)
    else:
        s.append(p)
        
    t_slide.decompose()

# 4. Format Slide 19 as the Practical Exercise
# Pattern was "თქვენი პირველი ავტომატიზაციის შექმნა"
exs = find_all_slides(r'თქვენი პირველი ავტომატიზაციის შექმნა')
if exs:
    ex = exs[0]
    h2 = ex.find(['h1', 'h2'])
    if h2:
        h2.string = "💪 პრაქტიკული სავარჯიშო: თქვენი პირველი ავტომატიზაცია"
        
    # Append time box if it doesn't have warning-box with time already
    if not ex.find('div', class_='warning-box'):
        time_box = soup.new_tag('div')
        time_box['class'] = 'warning-box'
        time_box['style'] = 'margin-top: 2rem;'
        h4_time = soup.new_tag('h4')
        h4_time.string = "⏱️ სავარჯიშოს დრო: 15 წუთი"
        time_box.append(h4_time)
        
        nav = ex.find('div', class_='navigation')
        if nav:
            nav.insert_before(time_box)
        else:
            ex.append(time_box)

# Delete empty trailing navigation if present
current_slides = soup.find_all('div', class_='slide')
for slide in current_slides:
    nav = slide.find('div', class_='navigation')
    t = slide.find(['h1', 'h2'])
    if nav and not t:
        slide.decompose()

# Renumber slides
slides = soup.find_all('div', class_='slide')
total = len(slides)
slide_index = 1
for slide in slides:
    num_tag = slide.find(class_='slide-number')
    if num_tag:
        num_tag.string = f"{slide_index}/{total}"
    slide_index += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"L7 processed successfully. New slide count: {total}")

import os
import re
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-5-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace all occurrences of 2025 with 2026 (Except in URLs if any, but fine to just regex safely)
text = re.sub(r'2025-2026', '2026', text)
text = re.sub(r'2025/2026', '2026', text)
text = re.sub(r'2025', '2026', text)
text = re.sub(r'2024', '2025', text) # Any 2024 push to 2025 or 2026 (let's do 2026 for old prompts)
# Replace specific 2024 string in prompt
text = text.replace('Marketing Trends 2025', 'Marketing Trends 2026')

soup = BeautifulSoup(text, 'html.parser')

# Update "რას ისწავლით ამ ლექციაში"
slides = soup.find_all('div', class_='slide')
for slide in slides:
    t = slide.find(['h1', 'h2'])
    if t and 'რას ისწავლით' in t.text:
        ul = slide.find('ul')
        if ul:
            ul.clear()
            li1 = soup.new_tag('li')
            li1.string = 'ვიზუალური კონტენტის გენერაციის საფუძვლები'
            li2 = soup.new_tag('li')
            li2.string = 'სურათების გენერირების წამყვანი პლატფორმების გამოყენება (Midjourney v7)'
            li3 = soup.new_tag('li')
            li3.string = 'პროფესიული AI პრეზენტაციების შექმნა წამებში (Gamma AI, Visual Suite)'
            li4 = soup.new_tag('li')
            li4.string = 'ინფოგრაფიკებისა და ბრენდინგის ვიზუალური იდენტობის შექმნა'
            ul.append(li1)
            ul.append(li2)
            ul.append(li3)
            ul.append(li4)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("L5 updated strictly to 2026 parameters and Learning Objectives fixed.")

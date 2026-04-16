import os
import re
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

count = 0
for i in range(1, 11):
    file_path = os.path.join(cwd, f'v2-lecture-{i}-slides.html')
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Remove ALL <a> tags containing these keywords
    for a in soup.find_all('a'):
        text = a.get_text(strip=True).lower()
        if 'წინა' in text or 'შემდეგი' in text or 'მთავარი' in text:
            a.decompose()
            count += 1

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print(f"Removed {count} orphaned links matching 'წინა', 'მთავარი', 'შემდეგი' across v2-*.html.")

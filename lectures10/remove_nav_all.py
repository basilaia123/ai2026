import os
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

for i in range(1, 11):
    file_path = os.path.join(cwd, f'v2-lecture-{i}-slides.html')
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')

    # Remove ALL navigation blocks
    navs = soup.find_all('div', class_='navigation')
    for nav in navs:
        nav.decompose()

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

print("All bottom navigation buttons removed from all files.")

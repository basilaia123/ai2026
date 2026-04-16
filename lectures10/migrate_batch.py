import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

def load_soup(filename):
    with open(os.path.join(cwd, filename), 'r', encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def migrate(old_name, new_name, old_num, new_num):
    soup = load_soup(old_name)
    
    # 1. Update text "ლექცია N"
    for text_node in soup.find_all(string=re.compile(f"ლექცია {old_num}")):
        text_node.replace_with(text_node.replace(f"ლექცია {old_num}", f"ლექცია {new_num}"))
        
    for text_node in soup.find_all(string=re.compile("120 წუთი")):
        text_node.replace_with(text_node.replace("120 წუთი", "150 წუთი"))

    # Update nav links
    nav_links = soup.find_all('a', class_='top-nav-link')
    for link in nav_links:
        if old_name in link.get('href', ''):
            link['href'] = link['href'].replace(old_name, new_name)

    html = str(soup)
    
    # Save v2-lecture-X-slides.html
    with open(os.path.join(cwd, new_name), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Migrated {old_name} to {new_name}")

migrate('lecture-7-slides.html', 'v2-lecture-5-slides.html', 7, 5)
migrate('lecture-8-slides.html', 'v2-lecture-6-slides.html', 8, 6)
migrate('lecture-9-slides.html', 'v2-lecture-7-slides.html', 9, 7)
migrate('lecture-10-slides.html', 'v2-lecture-8-slides.html', 10, 8)
print("Done batch migrating 7->5, 8->6, 9->7, 10->8")

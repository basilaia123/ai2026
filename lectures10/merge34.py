import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

def load_soup(filename):
    with open(os.path.join(cwd, filename), 'r', encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def merge_l3_l4():
    soup3 = load_soup('lecture-3-slides.html')
    soup4 = load_soup('lecture-4-slides.html')
    
    container = soup3.find('div', class_='container')
    
    # Skip the first slide of L4 (it's just a title slide) and append the rest
    l4_slides = soup4.find_all('div', class_='slide')
    for slide in l4_slides[1:]:
        container.append(slide)

    # 1. Update Title / Header
    soup3.title.string = "ლექცია 3: ტექსტის გენერაცია, იდეაცია და სოციალური მედია"
    h1 = soup3.find('h1')
    if h1:
        h1.string = "ლექცია 3: ტექსტის გენერაცია, იდეაცია და სოციალური მედია"
        
    # Replace 120 minutes with 150 minutes in the whole document text if accessible
    for td in soup3.find_all(string=re.compile("120 წუთი")):
        td.replace_with(td.replace("120 წუთი", "150 წუთი"))

    # Update slide numbers
    slides = soup3.find_all('div', class_='slide')
    total = len(slides)
    for i, slide in enumerate(slides, 1):
        span = slide.find(class_='slide-number')
        if span:
            span.string = f"{i}/{total}"

    # Update nav links to point to v2-lecture-3-slides.html
    nav_links = soup3.find_all('a', class_='top-nav-link')
    for link in nav_links:
        if 'lecture-3-slides.html' in link.get('href', ''):
            link['href'] = link['href'].replace('lecture-3-slides.html', 'v2-lecture-3-slides.html')

    html = str(soup3)
    
    # Save v2-lecture-3-slides.html
    with open(os.path.join(cwd, 'v2-lecture-3-slides.html'), 'w', encoding='utf-8') as f:
        f.write(html)

merge_l3_l4()
print("Merged 3 and 4 successfully.")

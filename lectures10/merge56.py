import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

def load_soup(filename):
    with open(os.path.join(cwd, filename), 'r', encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def merge_l5_l6():
    soup5 = load_soup('lecture-5-slides.html')
    soup6 = load_soup('lecture-6-slides.html')
    
    # In L5 and L6, slides are direct children of body!
    # Let's find all slides in L5
    slides5 = soup5.find_all('div', class_='slide')
    
    # We append slides from L6 to the end of L5's body
    slides6 = soup6.find_all('div', class_='slide')
    
    body5 = soup5.body
    
    # Append all slides from L6 to L5 (skip the first title slide of L6)
    for slide in slides6[1:]:
        body5.append(slide)

    # 1. Update Title / Header
    soup5.title.string = "ლექცია 4: ინფორმაციის დამუშავება, კვლევა და პროფესიული გამოყენება"
    h1 = soup5.find('h1')
    if h1:
        h1.string = "ლექცია 4: ინფორმაციის დამუშავება, კვლევა და პროფესიული გამოყენება"
        
    # Also update the title slide h2, etc if needed.
    # Replace "ლექცია 5" with "ლექცია 4" globally or specific known spots
    for text_node in soup5.find_all(string=re.compile("ლექცია 5")):
        text_node.replace_with(text_node.replace("ლექცია 5", "ლექცია 4"))
        
    for text_node in soup5.find_all(string=re.compile("120 წუთი")):
        text_node.replace_with(text_node.replace("120 წუთი", "150 წუთი"))

    # Update slide numbers
    slides = soup5.find_all('div', class_='slide')
    total = len(slides)
    for i, slide in enumerate(slides, 1):
        span = slide.find(class_='slide-number')
        if span:
            span.string = f"{i}/{total}"
        else:
            span = soup5.new_tag('div', attrs={'class': 'slide-number'})
            span.string = f"{i}/{total}"
            slide.insert(0, span)

    # Update nav links
    nav_links = soup5.find_all('a', class_='top-nav-link')
    for link in nav_links:
        if 'lecture-5-slides.html' in link.get('href', ''):
            link['href'] = link['href'].replace('lecture-5-slides.html', 'v2-lecture-4-slides.html')

    html = str(soup5)
    
    # Save v2-lecture-4-slides.html
    with open(os.path.join(cwd, 'v2-lecture-4-slides.html'), 'w', encoding='utf-8') as f:
        f.write(html)

merge_l5_l6()
print("Merged 5 and 6 successfully into v2-lecture-4.")

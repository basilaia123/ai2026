import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

def load_soup(filename):
    with open(os.path.join(cwd, filename), 'r', encoding='utf-8') as f:
        return BeautifulSoup(f.read(), 'html.parser')

def create_l9():
    soup11 = load_soup('lecture-11-slides.html')
    soup12 = load_soup('lecture-12-slides.html')
    
    # Target L9: Custom AI + Security/Ethics (Old 11 + parts of 12)
    # Get container of 11
    container11 = soup11.find('div', class_='container')
    
    # Get all slides from 12
    slides12 = soup12.find_all('div', class_='slide')
    
    # Slides 2-10 (Security & Ethics) are index 1 to 9
    # Slide 19 (Organizational AI Policy) is index 18
    # Slide 20 (GDPR) is index 19
    # Slide 21 (Data Privacy Checklist) is index 20
    
    def append_slide(slide):
        # We need to maintain the DOM structure.
        container11.append(slide)

    # Optional: Append the Section 1 divider as well
    dividers = soup12.find_all('div', class_='section-divider')
    if dividers:
        container11.append(dividers[0]) # Section 1: Security & Ethics
        
    for i in range(1, 10):
        if i < len(slides12):
            append_slide(slides12[i])
            
    # Maybe add a custom divider for GDPR?
    if len(slides12) > 20:
        append_slide(slides12[18])
        append_slide(slides12[19])
        append_slide(slides12[20])
    
    # Update title
    soup11.title.string = "ლექცია 9: მორგებული AI ასისტენტები და უსაფრთხოება"
    h1 = soup11.find('h1')
    if h1:
        h1.string = "🤖 მორგებული AI ასისტენტები და უსაფრთხოება"
        
    # Replace texts
    for text_node in soup11.find_all(string=re.compile("ლექცია 11")):
        text_node.replace_with(text_node.replace("ლექცია 11", "ლექცია 9"))
    for text_node in soup11.find_all(string=re.compile("120 წუთი")):
        text_node.replace_with(text_node.replace("120 წუთი", "150 წუთი"))

    # Update slide numbers
    slides = soup11.find_all('div', class_='slide')
    total = len(slides)
    for i, slide in enumerate(slides, 1):
        span = slide.find(class_='slide-number')
        if span:
            span.string = f"{i}/{total}"

    # Update nav links
    nav_links = soup11.find_all('a', class_='top-nav-link')
    for link in nav_links:
        if 'lecture-11-slides.html' in link.get('href', ''):
            link['href'] = link['href'].replace('lecture-11-slides.html', 'v2-lecture-9-slides.html')

    with open(os.path.join(cwd, 'v2-lecture-9-slides.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup11))
    print("Created v2-lecture-9-slides.html")

def create_l10():
    soup12 = load_soup('lecture-12-slides.html')
    
    container12 = soup12.find('div', class_='container')
    
    # We want to KEEP:
    # Title slide (0)
    # Dividers for Section 2 and 3
    # Slides 11-15 (Playbook) -> index 10-14
    # Slides 16-18 (Presentations) -> index 15-17
    # Slides 22-25 (Resources, etc) -> index 21-24
    
    # Build a list of elements to delete
    # Delete Slides 1-9 (index 1 to 9)
    # Delete Slide 19-21 (index 18 to 20)
    # Delete Section 1 Divider
    
    slides12 = soup12.find_all('div', class_='slide')
    dividers = soup12.find_all('div', class_='section-divider')
    
    to_delete = []
    
    # dividers[0] is Section 1
    if dividers:
        to_delete.append(dividers[0])
        
    for i in range(1, 10):
        if i < len(slides12):
            to_delete.append(slides12[i])
            
    for i in range(18, 21):
        if i < len(slides12):
            to_delete.append(slides12[i])
            
    for el in to_delete:
        el.decompose()
        
    # Update title
    soup12.title.string = "ლექცია 10: AI Playbook და დასკვნითი პრეზენტაციები"
    
    title_slide = soup12.find('div', class_='slide')
    if title_slide:
        h1 = title_slide.find('h1')
        if h1:
            h1.string = "ლექცია 10: დასკვნითი შეხვედრა"
        p = title_slide.find('p')
        if p and "უსაფრთხოება" in p.text:
            p.string = "AI Playbook და პროექტების პრეზენტაცია"
            
        cards = title_slide.find_all('div', class_='tool-card')
        # Maybe remove the first card (section 1) or rename it
        if len(cards) >= 3:
            cards[0].decompose()
            # Update the other two
            cards[1].find('h4').string = "ნაწილი 1 (1 სთ)"
            cards[2].find('h4').string = "ნაწილი 2 (2 სთ)"
            
    # Replace texts
    for text_node in soup12.find_all(string=re.compile("ლექცია 12")):
        text_node.replace_with(text_node.replace("ლექცია 12", "ლექცია 10"))

    # Update slide numbers
    slides = soup12.find_all('div', class_='slide')
    total = len(slides)
    for i, slide in enumerate(slides, 1):
        span = slide.find(class_='slide-number')
        if span:
            span.string = f"{i}/{total}"

    # Update nav links
    nav_links = soup12.find_all('a', class_='top-nav-link')
    for link in nav_links:
        if 'lecture-12-slides.html' in link.get('href', ''):
            link['href'] = link['href'].replace('lecture-12-slides.html', 'v2-lecture-10-slides.html')

    with open(os.path.join(cwd, 'v2-lecture-10-slides.html'), 'w', encoding='utf-8') as f:
        f.write(str(soup12))
    print("Created v2-lecture-10-slides.html")

create_l9()
create_l10()

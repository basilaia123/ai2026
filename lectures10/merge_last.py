import os
from bs4 import BeautifulSoup
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-3-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

slides = soup.find_all('div', class_='slide')

# Find and delete 'ვიზუალური იდეაცია AI-ით'
for slide in slides:
    t = slide.find(['h1', 'h2'])
    if t and 'ვიზუალური იდეაცია AI-ით' in t.get_text():
        slide.decompose()
        break
        
# Re-fetch slides to find the last 3 content slides
slides = soup.find_all('div', class_='slide')

# Ignore the trailing navigation block if it's considered a slide
content_slides = []
for slide in slides:
    t = slide.find(['h1', 'h2'])
    if t:
        content_slides.append(slide)

last_3 = content_slides[-3:]

if len(last_3) == 3:
    s1, s2, s3 = last_3
    
    # We will merge s2 and s3 into s1.
    # To save vertical space, we can put s2 (Takeaways) and s3 (Closing) next to each other.
    
    # Extract s2 content
    s2_key_points = s2.find('div', class_='key-points')
    
    # Extract s3 content
    s3_center = s3.find('div', class_='center')
    
    # We will rename the title of s1
    title = s1.find(['h1', 'h2'])
    if title:
        title.string = "ბრენდინგის იდეები & შეჯამება"
        
    s1.append(soup.new_tag('hr', style='margin: 2rem 0; opacity: 0.2;'))
    
    # Create two columns for the takeaways and closing
    two_col = soup.new_tag('div')
    two_col['class'] = 'two-column'
    
    if s2_key_points:
        col1 = soup.new_tag('div')
        # Add heading
        h3 = soup.new_tag('h3')
        h3.string = "🎯 მთავარი დასკვნები"
        col1.append(h3)
        # Move key points
        s2_key_points.extract()
        col1.append(s2_key_points)
        two_col.append(col1)
        
    if s3_center:
        col2 = soup.new_tag('div')
        s3_center.extract()
        
        # Remove massive top margins or center class to fit better
        s3_center['style'] = "display: flex; flex-direction: column; justify-content: center; height: 100%; text-align: center; background: rgba(99, 102, 241, 0.1); border-radius: 12px; padding: 1rem;"
        
        col2.append(s3_center)
        two_col.append(col2)
        
    s1.append(two_col)
    
    # Delete s2 and s3 from DOM
    s2.decompose()
    s3.decompose()

# Re-number slides
slides = soup.find_all('div', class_='slide')
total = 0
for slide in slides:
    nav = slide.find('div', class_='navigation')
    if not nav:
        total += 1

slide_index = 1
for slide in slides:
    nav = slide.find('div', class_='navigation')
    span = slide.find('span', class_='slide-number')
    if not nav:
        if span:
            span.string = f"{slide_index}/{total}"
        slide_index += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("Successfully deleted Visual Ideation and merged last 3 slides.")

import os
import glob

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
files = glob.glob(os.path.join(cwd, '*.html')) + glob.glob(os.path.join(cwd, '*.md'))

count = 0
for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    original_text = text
    
    # Target specific variations of the course title
    text = text.replace("AI - გენერატიული ინტელექტი პრაქტიკაში", "AI - ხელოვნური ინტელექტი პრაქტიკაში")
    text = text.replace("AI - გენერატიული ინტელექტის პრაქტიკაში", "AI - ხელოვნური ინტელექტის პრაქტიკაში")
    text = text.replace("AI - გენერატიული ინტელექტის პრაქტიკული კურსი", "AI - ხელოვნური ინტელექტის პრაქტიკული კურსი")
    
    # Case with quotes
    text = text.replace('"AI - გენერატიული ინტელექტი პრაქტიკაში"', '"AI - ხელოვნური ინტელექტი პრაქტიკაში"')
    
    if text != original_text:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        count += 1

print(f"Course title updated in {count} files.")

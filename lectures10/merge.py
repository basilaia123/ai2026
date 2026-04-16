import os

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'

def process_file(old_name, new_name, title_replacement=None):
    with open(os.path.join(cwd, old_name), 'r', encoding='utf-8') as f:
        content = f.read()

    # Update 120 minutes -> 150 minutes
    content = content.replace('120 წუთი', '150 წუთი')
    
    # Update navigation links (self-referential)
    content = content.replace(f'href="{old_name}"', f'href="{new_name}"')
    
    if title_replacement:
        content = content.replace(title_replacement[0], title_replacement[1])
        
    with open(os.path.join(cwd, new_name), 'w', encoding='utf-8') as f:
        f.write(content)

process_file('lecture-1-slides.html', 'v2-lecture-1-slides.html')
process_file('lecture-2-slides.html', 'v2-lecture-2-slides.html')
print('Done processing lecture 1 and 2')

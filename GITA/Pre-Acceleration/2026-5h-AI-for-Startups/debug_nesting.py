from bs4 import BeautifulSoup
soup = BeautifulSoup(open('day1-slides.html', encoding='utf-8').read(), 'html.parser')
slides = soup.find_all('div', class_='slide')
print(f'Total .slide divs: {len(slides)}')
top_level = 0
nested = 0
for i, s in enumerate(slides):
    chain = []
    p = s.parent
    while p is not None and p.name != 'body':
        cls = p.get('class') or []
        pid = p.get('id', '')
        chain.append(f'{p.name}["{cls}"].{pid}')
        p = p.parent
    sid = s.get('id', '?')
    # find top-level parent that's also a slide
    top_slide = None
    for ancestor in [s.parent, *(s.parents)]:
        if ancestor is None or ancestor.name == 'body':
            break
        if ancestor.name == 'div' and 'slide' in (ancestor.get('class') or []) and ancestor is not s:
            top_slide = ancestor.get('id', '?')
            break
    if top_slide:
        nested += 1
        print(f'  NESTED: {sid} inside {top_slide}')
    else:
        top_level += 1
print(f'\nTop-level: {top_level}, Nested: {nested}')
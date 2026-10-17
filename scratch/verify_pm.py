import re
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    'eu4dialogue/index.html',
    'eu4dialogue/proposal.md',
    'eu4dialogue/peacebuilding/index.html',
    'eu4dialogue/peacebuilding/proposal.md',
    'eu4dialogue/pm/index.html',
    'eu4dialogue/pm/proposal.md',
    'eu4dialogue/pm/day-1-slides.html',
    'eu4dialogue/pm/mock-data/index.html',
    'eu4dialogue/pm/post-training-evaluation.html',
    'eu4dialogue/pm/post-training-evaluation.md'
]

banned_words = ['make.com', 'ebrd', 'caritas', 'oppa', 'mcdonald', 'credo', '30 დღიანი', '12 თვიანი', 'rows.com']
currency_patterns = [r'₾', r'\$\d+', r'\d+\s*\$', r'\d+\s*ლარი']
latex_patterns = [r'\$\\rightarrow\$', r'\$\\times\$', r'\\rightarrow', r'\\times']

all_ok = True

for fpath in files:
    if not os.path.exists(fpath):
        print(f'File not found: {fpath}')
        all_ok = False
        continue
    print(f'=== Checking {fpath} ===')
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check dashes
    em_dashes = len(re.findall(r'—', content))
    en_dashes = len(re.findall(r'–', content))
    if em_dashes or en_dashes:
        print(f'  [WARNING] Found dashes: em-dash={em_dashes}, en-dash={en_dashes}')
        all_ok = False
    else:
        print('  [OK] No em/en dashes found.')

    # Check latex
    latex_found = False
    for lp in latex_patterns:
        m = re.findall(lp, content)
        if m:
            print(f'  [WARNING] Found latex pattern {lp}: {len(m)}')
            latex_found = True
            all_ok = False
    if not latex_found:
        print('  [OK] No LaTeX syntax found.')
    
    # Check banned words
    banned_found = False
    for bw in banned_words:
        m = re.findall(bw, content, re.IGNORECASE)
        if m:
            print(f'  [WARNING] Found banned word "{bw}": {len(m)}')
            banned_found = True
            all_ok = False
    if not banned_found:
        print('  [OK] No banned words found.')

    # Check currency/pricing
    curr_found = False
    for cp in currency_patterns:
        m = re.findall(cp, content, re.IGNORECASE)
        if m:
            print(f'  [WARNING] Found currency/price match "{cp}": {m[:5]}')
            curr_found = True
            all_ok = False
    if not curr_found:
        print('  [OK] No currency/pricing found.')

print('\nOVERALL STATUS:', 'ALL PASSED' if all_ok else 'SOME CHECKS FAILED')

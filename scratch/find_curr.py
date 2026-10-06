import re
import sys

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

for fpath in ['eu4dialogue-pm/proposal.md', 'eu4dialogue-pm/index.html']:
    with open(fpath, 'r', encoding='utf-8') as f:
        for idx, line in enumerate(f, 1):
            if re.search(r'\b(GEL|EUR)\b', line, re.IGNORECASE):
                print(f'{fpath}:{idx}: {line.strip()[:100]}')

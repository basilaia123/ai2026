import sys
import subprocess
import re

sys.stdout.reconfigure(encoding='utf-8')

for fname in ['archi/demo-lecture-plan.md', 'archi/demo-masterclass.html']:
    print(f"\n================ DIFF FOR {fname} ================\n")
    res = subprocess.run(['git', 'diff', '4625597', '--', fname], capture_output=True, text=True, encoding='utf-8')
    lines = res.stdout.splitlines()
    for l in lines:
        if l.startswith('+') and not l.startswith('+++'):
            # Print added lines that contain text
            clean = l[1:].strip()
            if clean:
                print(f"+ {clean[:120]}")

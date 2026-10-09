# -*- coding: utf-8 -*-
import sys
import os
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/build_deck.py', 'w', encoding='utf-8') as f:
    f.write('''# -*- coding: utf-8 -*-
import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# We will read template and inject slides
print("Building slide deck with 10 post-course playbooks...")
''')
print("Helper ready")

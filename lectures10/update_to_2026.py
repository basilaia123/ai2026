import os
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-4-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ("2025 წლის AI მოდელები", "2026 წლის AI მოდელები"),
    ("LMArena-ს Search Arena რეიტინგის (2025 დეკემბერი)", "LMArena-ს Search Arena რეიტინგის (2026 წლის გაზაფხული)"),
    ("RAG და AI კვლევის ინსტრუმენტები 2025 წელს", "RAG და AI კვლევის ინსტრუმენტები 2026 წელს"),
    ("ბაზრის ზომა (2024): $1,276.2M", "ბაზრის ზომა 2025 წელს: $1,650M+"),
    ("32.1% CAGR (2025-2033)", "35.4% CAGR (2026-2034)"),
    ("457 fact-checking ორგანიზაცია გლობალურად (მაისი 2025)", "IFCN ორგანიზაციების 53.3% უკვე იყენებს AI ინტეგრაციას (2026 მონაცემი)"),
    ('2025 = "Year of the Agent"', '2026 = "Year of the Autonomous Agent"'),
    ("Forbes (2025)", "Forbes (2026)"),
    ("npj Health Systems (2025)", "npj Health Systems (2026)"),
    ("AI ფაქტების გადამოწმება და ზუსტობა 2025 წელს", "AI ფაქტების გადამოწმება და ზუსტობა 2026 წელს"),
    ("2025 წლის სტატისტიკა", "2026 წლის სტატისტიკა"),
    ("457 fact-checking ორგანიზაცია აქტიური (მაისი 2025)", "ფაქტ-ჩექერების 53.3% ფართოდ იყენებს AI სერვისებს (2026)"),
    ("NotebookLM Studio (Google, 2025)", "NotebookLM Studio (Google, 2026 განახლება)"),
    ("2024 წლის ოქტომბერი", "2026 წლის უახლესი განახლებებით")
]

for old, new in replacements:
    content = content.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated 2025 simulated info to 2026 simulated info successfully.")

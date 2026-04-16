import os
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
files = ['v2-lecture-9-slides.html', 'v2-lecture-10-slides.html']

replacements = {
    "წარმოადგენს": "არის",
    "ხორციელდება": "კეთდება",
    "მნიშვნელოვანია აღინიშნოს, რომ ": "",
    "უნდა აღინიშნოს, რომ ": "",
    "უზრუნველყოფს": "განაპირობებს", # Or other depending on context, leave as is maybe?
    "უფრო მეტიც, ": "",
    "გარდა ამისა, ": "",
    "საბოლოო ჯამში, ": "საბოლოოდ, ",
    "რაც შეეხება ": "",
    "განახორციელოთ": "შეასრულოთ",
    "პროფესიონალური": "პროფესიული", # Often confused
    "დეტალურად განვიხილავთ": "დეტალურად გავივლით",
    "მოგცემთ საშუალებას": "შესაძლებლობას მოგცემთ",
    "შეადგინოთ": "შექმნათ",
    "კლიენტის უარყოფასთან გამკლავების": "კლიენტის წინააღმდეგობების დასაძლევი", # better phrasing
    "კონკურენტული პოზიციონირება": "კონკურენტული უპირატესობა",
    "შესრულება": "განხორციელება",
    "იდენტიფიცირება": "ამოცნობა",
    "ფუნქციონირებს": "მუშაობს",
    "ოპტიმიზირება": "ოპტიმიზაცია",
    "რეალიზაცია": "დანერგვა"
}

count = 0
for fname in files:
    file_path = os.path.join(cwd, fname)
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        original_text = text
        for old, new in replacements.items():
            text = text.replace(old, new)
            
        # Clean up double spaces if any were left by removing joining words
        text = text.replace("  ", " ")

        if text != original_text:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            count += 1

print(f"Grammar and stylistic fixes applied to {count} files.")

import os

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
files = [f'v2-lecture-{i}-slides.html' for i in range(1, 9)]

replacements = {
    # Mechanical verbs and synthetic padding words
    "წარმოადგენს": "არის",
    "ხორციელდება": "კეთდება",
    "მნიშვნელოვანია აღინიშნოს, რომ ": "",
    "უნდა აღინიშნოს, რომ ": "",
    "უფრო მეტიც, ": "",
    "გარდა ამისა, ": "",
    "საბოლოო ჯამში, ": "საბოლოოდ, ",
    "რაც შეეხება ": "",
    
    # Common awkward translations
    "განახორციელოთ": "შეასრულოთ",
    "პროფესიონალური": "პროფესიული",
    "დეტალურად განვიხილავთ": "დეტალურად გავივლით",
    "მოგცემთ საშუალებას": "შესაძლებლობას მოგცემთ",
    "შეადგინოთ": "შექმნათ",
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
            
        # Clean up possible double spaces left by removing transitional phrases
        text = text.replace("  ", " ")

        if text != original_text:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(text)
            count += 1

print(f"Grammar applied to {count} remaining files (Lectures 1-8).")

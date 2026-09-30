import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

files = [
    r"c:\Users\GBASILAIA\claude\ai2026\openday\interactive-school-game.html",
    r"c:\Users\GBASILAIA\claude\ai2026\openday\teachers-ai-slides.html",
    r"c:\Users\GBASILAIA\claude\ai2026\openday\teachers-ai-lecture.html"
]

# Common mistakes in Georgian:
# 1. თითოეულ + plural noun (თითოეულ მოსწავლეებს -> თითოეულ მოსწავლეს)
# 2. ყოველ + plural noun
# 3. Double letters where shouldn't be, or missing letters:
#    მაგ: "შესაძლებლობა", "მასწავლებელი", "გადაწყვეტილება", "დიფერენცირებული", "ინტერაქციული", "რეკომენდაცია"
# 4. English words transliterated incorrectly or typos
# 5. Georgian punctuation

suspicious_patterns = [
    (re.compile(r'თითოეულ(ი|მა|ს)?\s+([ა-ჰ]+(ები|ებად|ებს|ების|ებით|ებო))\b'), "თითოეულ + მრავლობითი რიცხვი (უნდა იყოს მხოლობითი)"),
    (re.compile(r'ყოველ(ი|მა|ს)?\s+([ა-ჰ]+(ები|ებად|ებს|ების|ებით|ებო))\b'), "ყოველ + მრავლობითი რიცხვი (უნდა იყოს მხოლობითი)"),
    (re.compile(r'რამოდენიმე'), "„რამოდენიმე“ -> „რამდენიმე“"),
    (re.compile(r'არანაირი'), "„არანაირი“ -> „არავითარი / არცერთი“"),
    (re.compile(r'თავის თავზე'), "„თავის თავზე“ -> „თავის თავზე / საკუთარ თავზე“"),
    (re.compile(r'დააინტრიგ'), "„დააინტრიგოს / დასაინტრიგებლად“ -> სასაუბროა, სჯობს: „ინტერესის აღსაძრავად / ინტერესის გასაღვივებლად“"),
    (re.compile(r'პედაგოგების'), "პედაგოგების -> პედაგოგთა / მასწავლებელთა"),
    (re.compile(r'მოსწავლეების'), "მოსწავლეების -> მოსწავლეთა (ნართანიანი მრავლობითი სტილისტურად უკეთესია ნათესაობითში)"),
]

for fpath in files:
    fname = fpath.split('\\')[-1]
    print(f"\n================ Checking {fname} ================")
    with open(fpath, 'r', encoding='utf-8') as f:
        text = f.read()

    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        for pat, desc in suspicious_patterns:
            for m in pat.finditer(line):
                print(f"[{fname}:{i}] {desc} -> ნაპოვნია: '{m.group(0)}'")

import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

files = [
    r"c:\Users\GBASILAIA\claude\ai2026\openday\interactive-school-game.html",
    r"c:\Users\GBASILAIA\claude\ai2026\openday\teachers-ai-slides.html",
    r"c:\Users\GBASILAIA\claude\ai2026\openday\teachers-ai-lecture.html"
]

# Patterns to inspect:
# 1. Number + plural noun (e.g., "3 მოსწავლეები", "5 წუთები")
num_plural_pattern = re.compile(r'\b(\d+|რამდენიმე|ორი|სამი|ოთხი|ხუთი)\s+([ა-ჰ]+(ები|ებად|ებს|ების|ებით|ებო))\b')

# 2. Subordinate conjunctions without preceding comma (e.g., "იმის გამო რომ", "იმისთვის რომ", "იმ დროს როდესაც")
conj_pattern = re.compile(r'([ა-ჰ0-9]+)\s+(რომ|რადგან|რადგანაც|რაკი|რათა|როდესაც|თუკი)\b')

# 3. English double quotes around Georgian words: "სიტყვა"
quote_pattern = re.compile(r'"([ა-ჰ\s]+)"')

# 4. Spaced postpositions: სიტყვა -ში, etc.
postposition_pattern = re.compile(r'([ა-ჰ]+)\s+(-ში|-ზე|-დან|-თან|-თვის|-მდე)\b')

print("=== STARTING AUDIT ===")

for fpath in files:
    fname = fpath.split('\\')[-1]
    print(f"\n--- Checking {fname} ---")
    with open(fpath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    for i, line in enumerate(lines, 1):
        # Skip script/style content if needed, but let's check text
        # 1. Number + plural
        for m in num_plural_pattern.finditer(line):
            # check if it's not false positive
            print(f"[{fname}:{i}] Num+Plural: {m.group(0)}")
            
        # 2. Conjunction without comma
        for m in conj_pattern.finditer(line):
            pre_word = m.group(1)
            conj = m.group(2)
            # check if pre_word ends with punctuation or is a common expression needing comma
            if pre_word in ['გამო', 'იმის', 'იმისთვის', 'იმ', 'იმედით', 'იმით', 'იმისათვის']:
                print(f"[{fname}:{i}] Conjunction comma check: '{pre_word} {conj}' (usually needs comma before {conj} or {pre_word})")
                
        # 3. Quotes
        for m in quote_pattern.finditer(line):
            # If in HTML text, not attribute
            if 'class="' not in line and 'id="' not in line and 'onclick="' not in line and 'href="' not in line:
                print(f"[{fname}:{i}] ASCII Quote: \"{m.group(1)}\" -> should be „{m.group(1)}“")

        # 4. Postposition
        for m in postposition_pattern.finditer(line):
            print(f"[{fname}:{i}] Spaced postposition: {m.group(0)}")

print("\n=== AUDIT COMPLETED ===")

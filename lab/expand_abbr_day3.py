import re

def expand_abbreviations_day3():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-3-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = {
        '20 წთ</strong> — ავტომ.': '20 წთ</strong> — ავტომატიზაცია',
        '30 წთ</strong> — ასისტ.': '30 წთ</strong> — ასისტენტის',
        '30 წთ</strong> — მოდ.': '30 წთ</strong> — მოდელის',
        'სრული ინტ.': 'სრული ინტეგრაცია',
        'ერთ ადგ.': 'ერთ ადგილას',
        'Google კორპ. ანგ.': 'Google კორპორატიული ანგარიში',
        'ინსტრ. ტექსტი მხ.': 'ინსტრუქციის ტექსტი მხოლოდ',
        'Knowledge files — შეზღ.': 'Knowledge files — შეზღუდულია',
        'Actions — გარ. API-ებთან კავშ.': 'Actions — გარე API-ებთან კავშირი',
        'Code Interpreter ჩართ.': 'Code Interpreter ჩართულია',
        'GPT Store — გაზ. შ.შ.': 'GPT Store — გაზიარების შესაძლებლობა',
        'Plus ($20/თვე) საჭ.': 'Plus ($20/თვე) საჭიროა',
        'ყოველდღ. ოპ. — Workspace': 'ყოველდღიური ოპერაციები — Workspace',
        'გრძ. დოკ., JCI ანალ.': 'გრძელი დოკუმენტები, JCI ანალიზი',
        'Governance და დეპ. დანერგვა': 'Governance და დეპარტამენტული დანერგვა',
        'პრ. 2 + დახ.': 'პრაქტიკა 2 + დახურვა',
        '(იხ. ქვემოთ)': '(იხილეთ ქვემოთ)',
        'ძირ. კონც.': 'ძირითადი კონცეფციები',
        'ძირ.': 'ძირითადი',
    }

    # Custom line replacements for safety
    lines = content.split('\\n')
    for i, line in enumerate(lines):
        for old, new in replacements.items():
            if old in line:
                lines[i] = lines[i].replace(old, new)
                
    content = '\\n'.join(lines)

    # Some additional precise replacements
    content = content.replace('კორპ.', 'კორპორატიული')
    
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-3-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Abbreviations expanded in Day 3.")

if __name__ == '__main__':
    expand_abbreviations_day3()
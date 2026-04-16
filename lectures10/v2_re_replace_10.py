import os

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-10-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    # Fix separated lines from last attempt
    "უფრო ძლიერი Reasoning": "უფრო ძლიერი ლოგიკური მსჯელობა (Reasoning)",
    "ტექსტი + ხმა + ვიდეო ერთად": "ტექსტი, ხმა და ვიდეო ერთად",
    "ავტონომიური ამოცანების განხორციელება": "ავტონომიური ამოცანების შესრულება",
    "ადამიანის დონის ინტელექტი": "ადამიანის დონის მოაზროვნე სისტემები",
    "Brain-Computer Interfaces:": "ტვინი-კომპიუტერის ინტერფეისები:",
    "პირდაპირი კავშირი": "პირდაპირი კავშირი კომპიუტერთან",
    "დემო (2 წთ):": "დემონსტრაცია (2 წთ):",
    "მაჩვენეთ შედეგი": "გვაჩვენეთ მიღებული შედეგი",
    "რა პრობლემას წყვეტთ?": "რა პრობლემას აგვარებთ?",
    
    # English -> Georgian translations
    "- Upload image → See full provenance (AI tool, date, edits)": "- სურათის ატვირთვა → სრული ისტორიის ნახვა (AI ხელსაწყო, თარიღი, ცვლილებები)",
    "\"The best way to predict the future is to create it.\"": "\"მომავლის წინასწარმეტყველების საუკეთესო გზა მისი შექმნაა.\"",
    "- Peter Drucker": "- პიტერ დრაკერი (Peter Drucker)"
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Second pass string replacement completed globally.")

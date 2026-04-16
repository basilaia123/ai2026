import os

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-10-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    "12 ლექცია | 25 საათი": "10 ლექცია | 27.5 საათი", # 9*2.5 + 3 = 25.5 actually. Let's make it 25.5 საათი.
    "უფრო ძლიერი Reasoning": "უფრო ძლიერი ლოგიკური მსჯელობა (Reasoning)",
    "Multimodal AI:ტექსტი + ხმა + ვიდეო ერთად": "მულტიმოდალური AI: ტექსტი, ხმა და ვიდეო ერთად",
    "AI Agents:ავტონომიური ამოცანების განხორციელება": "AI აგენტები: ავტონომიური ამოცანების შესრულება",
    "Personalized AI:თქვენზე მორგებული ასისტენტები": "პერსონალიზებული AI: თქვენზე მორგებული ასისტენტები",
    "AGI (Artificial General Intelligence):ადამიანის დონის ინტელექტი": "ზოგადი ხელოვნური ინტელექტი (AGI): ადამიანის დონის მოაზროვნე სისტემები",
    "Brain-Computer Interfaces:პირდაპირი კავშირი": "ტვინი-კომპიუტერის ინტერფეისები: პირდაპირი კავშირი კომპიუტერთან",
    "Newsletter-ების კითხვა": "საინფორმაციო ბიულეტენების (Newsletters) კითხვა",
    "YouTube ტუტორიალები": "YouTube გაკვეთილები (Tutorials)",
    "1 ავტომატიზაციის დაყენება": "1 ახალი პროცესის ავტომატიზაცია",
    "Custom GPT / Claude Project შექმნა": "პერსონალური GPT-ის ან Claude Project-ის შექმნა",
    "2-3 Workflow-ის ოპტიმიზაცია": "2-3 სამუშაო პროცესის (Workflow) ოპტიმიზაცია",
    "ROI-ის გამოთვლა და პრეზენტაცია": "ინვესტიციის უკუგების (ROI) გამოთვლა და წარდგენა",
    "დემო (2 წთ):მაჩვენეთ შედეგი": "დემონსტრაცია (2 წთ): გვაჩვენეთ მიღებული შედეგი",
    "არასოდეს - PII AI-ში": "არასოდეს შეიყვანოთ სენსიტიური მონაცემები (PII) AI-ში",
    "API Keys = Environment Variables": "შეინახეთ API გასაღებები უსაფრთხოდ (მაგ. Environment Variables)",
    "Enterprise Plans სენსიტიური მონაცემებისთვის": "გამოიყენეთ კორპორატიული პაკეტები (Enterprise) სენსიტიური მონაცემებისთვის",
    "გამჟღავნეთ AI გამოყენება": "აკადემიურად და პროფესიულად დააფიქსირეთ AI-ს გამოყენების ფაქტი",
    "შეამოწმეთ Bias-ზე": "დატესტეთ მონაცემები მიკერძოებაზე (Bias)",
    "თქვენ ხართ პასუხისმგებელი": "საბოლოო შედეგზე პასუხისმგებელი ხართ თქვენ (Human in the Loop)",
    "AI ხელსაწყოა - თქვენ ხართ ოსტატი": "AI მხოლოდ მძლავრი ინსტრუმენტია - ოსტატი კი თქვენ ხართ"
}

for eng, geo in replacements.items():
    text = text.replace(eng, geo)

# Fix literal '12 ლექცია' string at the end of the file explicitly
text = text.replace("12 ლექცია |", "10 ლექცია |")
# Ensure the math is right: 9 lectures * 2.5 hours = 22.5 hours + 1 lecture (L10) * 3 hours = 25.5 საათი.
text = text.replace("25 საათი |", "25.5 საათი |")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Contextual grammatical cleanup done for L10.")

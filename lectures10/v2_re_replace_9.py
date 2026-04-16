import os
import re

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-9-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    # Tasks
    "Create ONE custom AI assistant for your most frequent task. Start simple, use it daily, improve based on real usage.": "შექმენით 1 მორგებული AI ასისტენტი თქვენი ყველაზე ხშირი დავალებისთვის. დაიწყეთ მარტივად, გამოიყენეთ ყოველდღიურად და განაახლეთ.",
    "Create 2-3 more assistants for different workflows. Document your setup. Share with team if helpful.": "შექმენით 2-3 დამატებითი ასისტენტი სხვადასხვა პროცესისთვის. შექმენით დოკუმენტაცია და გაუზიარეთ გუნდს.",
    
    # 12 vs 10 Navigation and Titles
    "ლექცია 12: AI Playbook და სამომავლო განვითარება": "ლექცია 10: AI Playbook და სამომავლო განვითარება",
    "ლექცია 12: AI Playbook →": "ლექცია 10: AI Playbook →",
    "← ლექცია 10: No-Code": "← ლექცია 8: No-Code Development",
    
    # Separated fragments
    "სპეციალურად შექმნილი input-ები": "მავნე ინტენციით შექმნილი შეყვანილი მონაცემები (Inputs)",
    "API key პირდაპირ წყაროს კოდში": "API გასაღების პირდაპირ კოდში ჩაწერა (Hardcoding)",
    "API გასაღები საჯარო რეპოზიტორიაში": "API გასაღები საჯარო რეპოზიტორიაში (GitHub-ის რისკი)",
    "API გასაღები JavaScript კოდში": "API გასაღები ღიად კლიენტის JavaScript-ში",
    "API key-ს როტაცია არ ხდება": "API გასაღების განახლების (როტაციის) არარსებობა",
    
    # EU AI ACT
    "Unacceptable Risk": "მიუღებელი რისკი (Unacceptable Risk)",
    "High Risk": "მაღალი რისკი (High Risk)",
    "Limited Risk": "შეზღუდული რისკი (Limited Risk)",
    "Minimal Risk": "მინიმალური რისკი (Minimal Risk)",
    "Social scoring, real-time biometric surveillance": "სოციალური ქულების სისტემა, რეალურ დროში ბიომეტრიული მეთვალყურეობა",
    "Hiring AI, credit scoring, law enforcement": "დაქირავების AI, საკრედიტო შეფასება, სამართალდამცავი სისტემები",
    "Strict testing, documentation, human oversight": "მკაცრი ტესტირება, დოკუმენტაცია, ადამიანური ზედამხედველობა",
    "Chatbots, AI content generators": "ჩატბოტები, AI კონტენტის გენერატორები",
    "Transparency (disclose AI use)": "გამჭვირვალობა (AI გამოყენების გამჟღავნება)",
    "AI games, spam filters": "AI თამაშები, სპამის ფილტრები",
    "No restrictions": "შეზღუდვების გარეშე",
    
    # Separated Compliance policies
    "Content drafting": "ტექსტის დრაფტის შექმნა",
    "Code assistance": "პროგრამირებისას დახმარება",
    "Legal compliance": "იურიდიული შესაბამისობა",

    # GDPR 30 day plan
    "Inventory all AI tools, Check existing DPAs, Review privacy policy": "აღრიცხეთ ყველა AI ინსტრუმენტი, შეამოწმეთ DPA-ები, გადახედეთ კონფიდენციალურობის პოლიტიკას",
    "Data flow mapping, Identify PII in AI workflows, Gap analysis": "მონაცემთა ნაკადის რუკა, იდენტიფიცირეთ PII ინტეგრაციებში, ხარვეზების ანალიზი",
    "Sign missing DPAs, Implement anonymization, Update consent forms": "გააფორმეთ დაკარგული DPA-ები, დანერგეთ ანონიმიზაცია, განაახლეთ თანხმობის ფორმები",
    "Employee training, Establish monitoring, Document everything": "თანამშრომელთა ტრენინგი, მონიტორინგის დაწესება, ყველაფრის დოკუმენტირება"
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Second pass semantic replacements applied to L9.")

import os
import re
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-10-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Dates
text = re.sub(r'2024', '2025', text)
text = re.sub(r'2025', '2026', text)

# Emoji map for L10
emoji_map = {
    "კურსის მოგზაურობა - 12 ლექცია": "🗺️ კურსის მოგზაურობა - 10 ლექცია", # Title update incorporated
    "კურსის მოგზაურობა - 10 ლექცია": "🗺️ კურსის მოგზაურობა - 10 ლექცია",
    "თქვენი პერსონალური AI Playbook": "📖 თქვენი პერსონალური AI Playbook",
    "AI-ის მომავალი ტენდენციები": "🚀 AI-ის მომავალი ტენდენციები",
    "უწყვეტი სწავლის სტრატეგია": "🧠 უწყვეტი სწავლის სტრატეგია",
    "90 დღის სამოქმედო გეგმა": "🗓️ 90 დღის სამოქმედო გეგმა",
    "Capstone პროექტების პრეზენტაცია": "🏆 Capstone პროექტების პრეზენტაცია",
    "პრეზენტაციების რიგი": "📋 პრეზენტაციების რიგი",
    "პრეზენტაციების რიგი (გაგრძელება)": "📋 პრეზენტაციების რიგი (გაგრძელება)",
    "რესურსები და შემდეგი ნაბიჯები": "📚 რესურსები და შემდეგი ნაბიჯები",
    "მთავარი დასკვნები": "🎯 მთავარი დასკვნები",
    "უკუკავშირი და შეკითხვები": "❓ უკუკავშირი და შეკითხვები",
    "გილოცავთ კურსის დასრულებას!": "🎓 გილოცავთ კურსის დასრულებას!"
}

soup = BeautifulSoup(text, 'html.parser')

# 2. Add Emojis
for slide in soup.find_all('div', class_='slide'):
    for t in slide.find_all(['h1', 'h2']):
        t_str = t.get_text(strip=True)
        # Handle the specific 12 -> 10 lecture rename if it occurs without emoji
        if t_str == "კურსის მოგზაურობა - 12 ლექცია" or t_str == "კურსის მოგზაურობა - 10 ლექცია":
            t.string = "🗺️ კურსის მოგზაურობა - 10 ლექცია"
        for raw_t, em in emoji_map.items():
            if t_str == raw_t:
                t.string = em

# 3. Update Slide 2 content entirely
new_curriculum_html = """
  <div class="two-column">
   <div>
    <h3>
     ლექციები 1-5:
    </h3>
    <ul>
     <li><strong>1:</strong> შესავალი + ChatGPT საფუძვლები</li>
     <li><strong>2:</strong> Prompt Engineering</li>
     <li><strong>3:</strong> ტექსტის გენერაცია + პროფესიული მიმოწერა</li>
     <li><strong>4:</strong> ინფორმაციის დამუშავება და კვლევა</li>
     <li><strong>5:</strong> ვიზუალური კონტენტის გენერაცია</li>
    </ul>
   </div>
   <div>
    <h3>
     ლექციები 6-10:
    </h3>
    <ul>
     <li><strong>6:</strong> აუდიო და ვიდეო გენერაცია</li>
     <li><strong>7:</strong> ავტომატიზაცია (Make, Zapier)</li>
     <li><strong>8:</strong> No-Code Development</li>
     <li><strong>9:</strong> AI ასისტენტები და უსაფრთხოება</li>
     <li><strong>10:</strong> დასკვნითი პრეზენტაციები</li>
    </ul>
   </div>
  </div>
"""

slides = soup.find_all('div', class_='slide')
if len(slides) > 1:
    col_div = slides[1].find('div', class_='two-column')
    if col_div:
        new_tag = BeautifulSoup(new_curriculum_html, 'html.parser').div
        col_div.replace_with(new_tag)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print("L10 fixed visually and updated to 10 lectures.")

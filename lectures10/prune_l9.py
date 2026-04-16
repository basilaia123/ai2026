import os
import re
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-9-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update Dates to 2026
text = re.sub(r'2024', '2025', text)
text = re.sub(r'2025', '2026', text)

# Emoji map for AI Security slides
emoji_map = {
    "AI უსაფრთხოების საფუძვლები": "🔒",
    "API უსაფრთხოება და Key Management": "🔑",
    "Prompt Injection და Jailbreaking": "⚠️",
    "Deepfakes და დეზინფორმაცია": "🎭",
    "Content Authenticity და Watermarking": "🛡️",
    "AI ეთიკის პრინციპები": "⚖️",
    "AI Bias და სამართლიანობა": "⚖️",
    "AI რეგულაციები (EU AI Act)": "📜",
    "პრაქტიკული სავარჯიშო: სცენარების ანალიზი": "💪",
    "ორგანიზაციული AI პოლიტიკის შაბლონი": "🏢",
    "GDPR Compliance - 30 დღის გეგმა": "📋",
    "მონაცემთა დაცვის საუკეთესო პრაქტიკები": "✨"
}

soup = BeautifulSoup(text, 'html.parser')
slides = soup.find_all('div', class_='slide')

# 2. Add emojis and handle Slide 17 missing title
for slide in slides:
    title_tags = slide.find_all(['h1', 'h2'])
    if not title_tags:
        # If no title (like Slide 17 maybe), decompose if it is empty formatting
        text_content = slide.get_text(strip=True)
        if not text_content or len(text_content) < 10:
            slide.decompose()
        else:
            # Let's give it a synthetic title
            h1 = soup.new_tag('h1')
            h1.string = "🔒 ნაწილი II: AI უსაფრთხოება და ეთიკა"
            slide.insert(0, h1)
    else:
        for t in title_tags:
            t_str = t.get_text(strip=True)
            for raw_t, em in emoji_map.items():
                if t_str == raw_t:
                    t.string = f"{em} {raw_t}"

# 3. Add Thank you to the last slide
current_slides = soup.find_all('div', class_='slide')
if current_slides:
    last = current_slides[-1]
    p = soup.new_tag('p')
    p['style'] = "font-size: 1.5rem; margin-top: 3rem; color: #666; text-align: center;"
    p.string = "გმადლობთ ყურადღებისთვის! 🙏"
    last.append(p)

# 4. Renumber Slides properly
current_slides = soup.find_all('div', class_='slide')
total = len(current_slides)
for idx, slide in enumerate(current_slides, 1):
    sn = slide.find(class_='slide-number')
    if sn:
        sn.string = f"{idx}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print(f"L9 processed successfully. New slide count: {total}")

import os
from bs4 import BeautifulSoup

cwd = r'c:\Users\GBASILAIA\claude\ai2026\lectures10'
file_path = os.path.join(cwd, 'v2-lecture-3-slides.html')

with open(file_path, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

# 1. Delete Slide 6
slides = soup.find_all('div', class_='slide')
for slide in slides:
    num = slide.find('span', class_='slide-number')
    if num and num.get_text().startswith('6/'):
        slide.decompose()
        print("Deleted Slide 6 (Stats).")
        break

# 2. Merge Practical Exercises
# Find the existing practical exercise in v2-lecture-3-slides.html
target_slide = None
for s in soup.find_all('div', class_='slide'):
    t = s.find(['h1', 'h2'])
    if t and 'პრაქტიკული სავარჯიშო' in t.get_text():
        target_slide = s
        break

if target_slide:
    # Get the existing slide-content
    content_div = target_slide.find('div', class_='slide-content')
    if content_div:
        # Wrap existing content into a two-column layout
        two_col = soup.new_tag('div')
        two_col['class'] = 'two-column'
        
        # Existing exercise (Content Adaptation)
        ex1_box = content_div.find('div', class_='exercise-box')
        if ex1_box:
            ex1_box.extract()
            two_col.append(ex1_box)
            
        # Add new exercise (Ideation Sprint from old L4)
        ex2_html = """
        <div class="exercise-box">
            <h3>🎯 ამოცანა: "იდეების სპრინტი"</h3>
            <div style="margin-top: 1.5rem;">
                <h4>რას ვაკეთებთ:</h4>
                <ol style="margin-left: 1.5rem; margin-top: 0.5rem;">
                    <li><strong>აირჩიეთ სამუშაო პრობლემა</strong> ან გამოიყენეთ: „როგორ გავზარდოთ ცნობადობა ბიუჯეტის გარეშე?“</li>
                    <li style="margin-top: 0.5rem;"><strong>გამოიყენეთ Brainstorm ტექნიკები:</strong>
                        <ul style="margin-top: 0.2rem;">
                            <li>SCAMPER (7 ინოვაციური იდეა)</li>
                            <li>What If (3 რადიკალური იდეა)</li>
                        </ul>
                    </li>
                    <li style="margin-top: 0.5rem;"><strong>აირჩიეთ საუკეთესო:</strong> ყველაზე ინოვაციური და განხორციელებადი.</li>
                </ol>
            </div>
            <div class="demo-box" style="margin-top: 1.5rem; padding: 1rem;">
                <h4>💡 AI შაბლონები:</h4>
                <p style="font-size: 0.9rem;"><strong>SCAMPER:</strong> პრობლემა: [X]. მომეცი თითო იდეა S.C.A.M.P.E.R. ასოებისთვის (7 სულ).</p>
                <p style="font-size: 0.9rem; margin-top: 0.5rem;"><strong>What If:</strong> დააგენერირე 3 რადიკალური "What If" სცენარი ამ პრობლემისთვის.</p>
            </div>
        </div>
        """
        ex2_soup = BeautifulSoup(ex2_html, 'html.parser')
        two_col.append(ex2_soup.div)
        
        # the warning box at the bottom is already there, let's keep it (or update its time)
        warning_box = content_div.find('div', class_='warning-box')
        if warning_box:
            warning_box.extract()
            # Update time to 25 minutes for both
            h = warning_box.find('h4')
            if h:
                h.string = "⏱️ სრული დრო: 25 წუთი (ორივე ამოცანისთვის)"
                
        # clear content_div and append two_col and warning_box
        content_div.clear()
        content_div.append(two_col)
        if warning_box:
            content_div.append(warning_box)
            
        # rename title to 'კომპლექსური პრაქტიკული სავარჯიშო'
        tit = target_slide.find(['h1', 'h2'])
        tit.string = "კომპლექსური პრაქტიკული სავარჯიშო (ტექსტი + იდეაცია)"
        print("Merged exercises successfully.")

# Re-number slides
slides = soup.find_all('div', class_='slide')
total = len(slides)
for i, slide in enumerate(slides, 1):
    span = slide.find(class_='slide-number')
    if span:
        span.string = f"{i}/{total}"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print(f"File updated. New slide count: {total}")

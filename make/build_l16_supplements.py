import os

CSS_STYLE = """
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'FiraGO', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; color: #2c3e50; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); min-height: 100vh; padding: 2rem 1rem; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 3rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; margin-bottom: 2rem; padding-bottom: 1rem; border-bottom: 3px solid #667eea; font-size: 2.5rem; }
        h2 { color: #667eea; margin-top: 2.5rem; margin-bottom: 1.5rem; font-size: 2rem; }
        h3 { color: #2c3e50; margin-top: 2rem; margin-bottom: 1rem; font-size: 1.5rem; }
        h4 { color: #495057; margin-top: 1.5rem; margin-bottom: 0.8rem; font-size: 1.2rem; }
        p { margin-bottom: 1rem; font-size: 1.1rem; line-height: 1.8; }
        ul, ol { margin-bottom: 1.5rem; padding-left: 2rem; }
        li { margin-bottom: 0.8rem; font-size: 1.1rem; }
        .highlight-box { background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3; margin: 1.5rem 0; }
        .warning-box { background: #fff3e0; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #ff9800; margin: 1.5rem 0; }
        .key-points { background: #f1f8e9; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4caf50; margin: 1.5rem 0; }
        .nav-links { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; border-radius: 10px; display: flex; justify-content: center; flex-wrap: wrap; gap: 1rem; margin-bottom: 2rem; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        .nav-link { color: white; text-decoration: none; padding: 0.7rem 1.5rem; border-radius: 8px; background: rgba(255,255,255,0.15); backdrop-filter: blur(10px); transition: all 0.3s; font-weight: 500; border: 2px solid transparent; }
        .nav-link:hover { background: rgba(255,255,255,0.25); transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        .nav-link.current { background: white; color: #667eea; border: 2px solid white; font-weight: 600; }
        table { width: 100%; border-collapse: collapse; margin: 1.5rem 0; background: white; border-radius: 10px; overflow: hidden; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }
        th { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 1rem; text-align: left; font-weight: 600; }
        td { padding: 1rem; border-bottom: 1px solid #e9ecef; }
        tr:hover { background: #f8f9fa; }
        .code-block, code { background: #2b2b2b; color: #f8f8f2; padding: 1rem; border-radius: 8px; font-family: 'Courier New', monospace; display: block; white-space: pre-wrap; margin: 1rem 0; font-size: 0.95rem; }
        p code, li code { display: inline; background: #f8f9fa; color: #e83e8c; padding: 0.2rem 0.5rem; }
        .section-summary { background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1.5rem 0; border-left: 4px solid #667eea; }
        @media (max-width: 768px) { .container { padding: 1.5rem; } h1 { font-size: 2rem; } h2 { font-size: 1.6rem; } .nav-links { flex-direction: column; } .nav-link { width: 100%; text-align: center; } }
"""

def generate_html(title, current_page, content, lecture_num):
    nav_links = {
        "index.html": "🏠 მთავარი",
        f"lecture-{lecture_num}-slides.html": "📊 სლაიდები",
        f"lecture-{lecture_num}-summary.html": "📚 შეჯამება",
        f"lecture-{lecture_num}-quick-ref.html": "📋 სწრაფი ცნობარი",
        f"lecture-{lecture_num}-exercises.html": "💪 სავარჯიშოები",
        f"lecture-{lecture_num}-study-guide.html": "📖 სასწავლო გზამკვლევი"
    }
    
    nav_html = '<nav class="nav-links">\n'
    for link, text in nav_links.items():
        css_class = 'nav-link current' if link == current_page else 'nav-link'
        nav_html += f'        <a href="{link}" class="{css_class}">{text}</a>\n'
    nav_html += '    </nav>'

    return f"""<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet"/>
    <style>{CSS_STYLE}</style>
</head>
<body>
    {nav_html}
    <div class="container">
        {content}
    </div>
</body>
</html>"""

# ==========================================
# LECTURE 1
# ==========================================
l1_summary = """
        <h1>ლექცია 1: შეჯამება (AI ასისტენტების საფუძვლები)</h1>
        
        <div class="highlight-box">
            <h3>📚 ლექციის მიზნები</h3>
            <ul>
                <li>AI ასისტენტების არქიტექტურის გაგება (Stateful vs Stateless).</li>
                <li>Custom GPT და Claude Projects-ის შექმნა კონკრეტული ამოცანებისთვის.</li>
                <li>Make.com-ის პლატფორმაზე პირველი ენთერფრაიზ ავტომატიზაციის აწყობა.</li>
                <li>ლოკალური მოდელების (Llama, DeepSeek) და მულტიმოდალურობის საფუძვლები.</li>
            </ul>
        </div>

        <h2>1️⃣ AI არქიტექტურა და პარადიგმები</h2>
        <div class="section-summary">
            <h3>Stateful vs Stateless ინტერაქცია</h3>
            <p><strong>Stateless (უმისამართო):</strong> სტანდარტული ჩატბოტები, რომლებსაც არ ახსოვთ წინა საუბრები და არ აქვთ სპეციფიკური კონტექსტი. ყოველ ჯერზე ნულიდან გიწევთ ახსნა.</p>
            <p><strong>Stateful (მდგომარეობიანი):</strong> AI ასისტენტები (Custom GPT/Claude Projects), რომლებსაც აქვთ წინასწარ გაწერილი ინსტრუქციები (System Prompt), ინახავენ მეხსიერებას და აქვთ პირდაპირი წვდომა თქვენს ატვირთულ დოკუმენტებზე.</p>
        </div>

        <h2>2️⃣ ლოკალური მოდელები (Local LLMs)</h2>
        <div class="section-summary">
            <h3>რატომ არის ეს 2026 წლის სტანდარტი?</h3>
            <p>ენთერფრაიზ კლიენტები (მაგ. ბანკები) ვერ იყენებენ OpenAI-ს ღრუბლოვან სერვისებს კონფიდენციალურობის გამო. ჩვენ შეგვიძლია იგივე სიმძლავრის მოდელები (როგორიცაა Llama 3 ან Qwen) გავუშვათ <strong>ლოკალურად</strong> (ინტერნეტის გარეშე), რაც უზრუნველყოფს მონაცემთა 100%-იან უსაფრთხოებას.</p>
        </div>

        <h2>3️⃣ პირველი Build ვორქშოპი</h2>
        <div class="section-summary">
            <h3>Make.com-ის პირველი ავტომატიზაცია</h3>
            <p>ჩვენ ავაწყვეთ პირველი სცენარი, რომელიც იწყება <strong>გამომწვევით (Trigger)</strong> (მაგ. ახალი ფორმის შევსება) და სრულდება <strong>მოქმედებებით (Actions)</strong> (მაგ. მონაცემების Google Sheets-ში შეტანა და Gmail-ით შეტყობინების გაგზავნა). ეს არის ავტომატიზაციის უმარტივესი, თუმცა ყველაზე ძლიერი სტრუქტურა.</p>
        </div>
"""

l1_study_guide = """
        <h1>📖 სასწავლო გზამკვლევი: ლექცია 1</h1>

        <h2>1. რა არის Custom GPT / Claude Project?</h2>
        <div class="highlight-box">
            <p>ეს არ არის უბრალოდ ჩატი, ეს არის თქვენი პერსონალური თანამშრომელი, რომელსაც აქვს:</p>
            <ul>
                <li><strong>როლი:</strong> (მაგ. "შენ ხარ Senior HR მენეჯერი")</li>
                <li><strong>ინსტრუქცია:</strong> (მაგ. "პასუხი გასეცი მხოლოდ 2 წინადადებით, ოფიციალური ტონით")</li>
                <li><strong>ცოდნა (Knowledge):</strong> მასში ატვირთული PDF ან Word ფაილები, რომლიდანაც კითხულობს ინფორმაციას.</li>
            </ul>
        </div>

        <h2>2. Make.com სტრუქტურა დამწყებთათვის</h2>
        <p>ავტომატიზაციის აწყობისას ყოველთვის ვსვამთ 2 კითხვას:</p>
        <ol>
            <li><strong>როდის უნდა გაეშვას ეს სცენარი? (Trigger)</strong> - <em>მაგ: როცა ახალი კლიენტი შეავსებს Typeform-ს.</em></li>
            <li><strong>რა უნდა მოხდეს ამის შემდეგ? (Action)</strong> - <em>მაგ: გაიგზავნოს Slack შეტყობინება და დაემატოს CRM-ში.</em></li>
        </ol>

        <h2>3. Local LLMs (ლოკალური მოდელები)</h2>
        <table style="margin-top: 1rem;">
            <tr>
                <th>თვისება</th>
                <th>Cloud (OpenAI / Claude)</th>
                <th>Local (Ollama / LM Studio)</th>
            </tr>
            <tr>
                <td><strong>ინტერნეტი</strong></td>
                <td>აუცილებელია</td>
                <td>არ არის საჭირო (Offline)</td>
            </tr>
            <tr>
                <td><strong>მონაცემთა დაცვა</strong></td>
                <td>მონაცემები იგზავნება სერვერზე</td>
                <td>Zero-Leakage (100% უსაფრთხო)</td>
            </tr>
            <tr>
                <td><strong>ფასი</strong></td>
                <td>ფასიანი (ტოკენების მიხედვით)</td>
                <td>უფასო (Open-Source)</td>
            </tr>
            <tr>
                <td><strong>აპარატურა (Hardware)</strong></td>
                <td>ნებისმიერ ტელეფონზე მუშაობს</td>
                <td>მოითხოვს ძლიერ კომპიუტერს (RAM)</td>
            </tr>
        </table>
"""

l1_quick_ref = """
        <h1>📋 სწრაფი ცნობარი (Cheat Sheet): ლექცია 1</h1>

        <div class="key-points">
            <h3>🤖 Perfect Prompt Formula (Custom GPT-სთვის)</h3>
            <p>საუკეთესო ინსტრუქციის დასაწერად გამოიყენეთ <strong>CREATE</strong> ფორმულა:</p>
            <ul>
                <li><strong>Context (კონტექსტი):</strong> ვინ ხარ შენ? (მაგ. "ხარ გამოცდილი კოპირაიტერი").</li>
                <li><strong>Request (მოთხოვნა):</strong> რა არის დავალება?</li>
                <li><strong>Examples (მაგალითები):</strong> აჩვენეთ 1 ან 2 იდეალური შედეგი.</li>
                <li><strong>Adjustments (შეზღუდვები):</strong> რა არ უნდა გააკეთოს? (მაგ. "არ გამოიყენო სიტყვა `ინოვაციური`").</li>
                <li><strong>Tone (ტონი):</strong> პროფესიონალური, მეგობრული, კრეატიული.</li>
                <li><strong>Extra (ფორმატი):</strong> დააბრუნე ცხრილის ან სიის სახით.</li>
            </ul>
        </div>

        <div class="highlight-box">
            <h3>⚡ Make.com Debugging (შეცდომების ძებნა)</h3>
            <ul>
                <li>თუ სცენარი არ ეშვება: შეამოწმეთ, ჩართულია თუ არა <strong>"ON"</strong> ღილაკი ქვედა მარცხენა კუთხეში.</li>
                <li>თუ მონაცემი არ გადავიდა: შეამოწმეთ <strong>Execution History</strong>, ნახეთ წინა მოდულის გამომავალი (Output) ბუშტუკი.</li>
                <li>თუ წერს "Unauthorized": განაახლეთ კავშირი (Connection), თავიდან გაიარეთ ავტორიზაცია.</li>
            </ul>
        </div>
"""

l1_exercises = """
        <h1>💪 სავარჯიშოები: ლექცია 1</h1>

        <div class="info-box">
            <p><strong>ინსტრუქცია:</strong> ეს დავალებები შექმნილია თქვენი პირველი AI ასისტენტის და ავტომატიზაციის შესაქმნელად.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 1: პერსონალური ასისტენტის (Custom GPT) შექმნა</h3>
            <ol>
                <li>შედით ChatGPT-ში და გახსენით "Explore GPTs" ➔ "Create".</li>
                <li>შექმენით <strong>"Email Responder Pro"</strong>.</li>
                <li>დაუწერეთ ინსტრუქცია: <em>"შენ ხარ ჩემი პირადი მდივანი. როცა მე დაგიკოპირებ შემოსულ ელ.ფოსტას, შენ უნდა შეადგინო პროფესიონალური, ზრდილობიანი და მოკლე (მაქსიმუმ 3 წინადადება) პასუხი ქართულ ენაზე."</em></li>
                <li>დატესტეთ ასისტენტი პრაქტიკაში ნებისმიერი მოგონილი იმეილის ჩაგდებით.</li>
            </ol>
        </div>

        <div class="section-summary">
            <h3>დავალება 2: Make.com-ის პირველი სცენარი</h3>
            <p><strong>მიზანი:</strong> ავტომატური შეტყობინების გაგზავნა Telegram-ში ფორმის შევსებისას.</p>
            <ol>
                <li>შექმენით Google Form 2 კითხვით (სახელი და ტელეფონის ნომერი).</li>
                <li>Make.com-ში შექმენით ახალი სცენარი და დაამატეთ <strong>Google Forms (Watch Responses)</strong> მოდული.</li>
                <li>დააკავშირეთ თქვენი Google-ის ანგარიში და აირჩიეთ შექმნილი ფორმა.</li>
                <li>დაამატეთ მეორე მოდული: <strong>Telegram Bot (Send a Text Message)</strong> (ან Slack/Gmail).</li>
                <li>მესიჯის ტექსტში (Text) ჩასვით (Map) ფორმიდან წამოსული მონაცემები: <em>"ახალი ლიდი: [სახელი], ტელეფონი: [ნომერი]"</em>.</li>
                <li>შეავსეთ ფორმა და შეამოწმეთ, მიიღეთ თუ არა შეტყობინება.</li>
            </ol>
        </div>
"""

# ==========================================
# LECTURE 6
# ==========================================
l6_summary = """
        <h1>ლექცია 6: შეჯამება (Workshop & Trend Analysis)</h1>
        
        <div class="highlight-box">
            <h3>📚 ფინალური ლექციის მიზნები</h3>
            <ul>
                <li>სტუდენტების მიერ შექმნილი ფინალური ენთერფრაიზ ავტომატიზაციების პრეზენტაცია (Pitch).</li>
                <li>მომავლის ტენდენციების (Future Trends) და AGI-ისკენ სვლის ანალიზი.</li>
                <li>AI არქიტექტორების Alumni Network-ის ფორმირება და კარიერული ნაბიჯები.</li>
            </ul>
        </div>

        <h2>1️⃣ Final Project Pitches (პრეზენტაციები)</h2>
        <div class="section-summary">
            <h3>10-წუთიანი პრეზენტაციის სტრუქტურა</h3>
            <p>თითოეულმა მონაწილემ წარადგინა საკუთარი ავტომატიზაცია შემდეგი სტრუქტურით:</p>
            <ol>
                <li><strong>პრობლემა:</strong> რა ტკივილი ჰქონდა ბიზნესს (მაგ. დროის კარგვა ინვოისებზე).</li>
                <li><strong>არქიტექტურა:</strong> Make/n8n + AI მოდელის ლოგიკა.</li>
                <li><strong>Live Demo:</strong> სისტემის მუშაობის რეალურ დროში ჩვენება.</li>
                <li><strong>ROI:</strong> დაზოგილი დრო და ფინანსები.</li>
            </ol>
        </div>

        <h2>2️⃣ Future Trends (მომავლის ტენდენციები 2026+)</h2>
        <div class="section-summary">
            <h3>საით მიდის ინდუსტრია?</h3>
            <p>ჩვენ განვიხილეთ, რომ No-Code ინსტრუმენტები თანდათან ქრება და მათ ანაცვლებს <strong>Voice-to-Code</strong> და <strong>Natural Language Programming</strong>. ანუ, მომავალში ავტომატიზაციას ავაწყობთ უბრალოდ კომპიუტერთან საუბრით. თუმცა, დღეს ნასწავლი <strong>სისტემური აზროვნება</strong> და <strong>არქიტექტურული ხედვა</strong> არის ის უნარი, რომელიც არასოდეს დაძველდება.</p>
        </div>

        <h2>3️⃣ Alumni Network და შემდეგი ნაბიჯები</h2>
        <div class="section-summary">
            <h3>კარიერული პოზიციონირება</h3>
            <p>არასოდეს გაყიდოთ თქვენი თავი როგორც "Prompt Engineer". პოზიციონირდით როგორც <strong>"AI Automation Architect"</strong>. გაყიდეთ არა პროცესი (Make.com-ის აწყობა), არამედ შედეგი (შემცირებული საოპერაციო ხარჯები).</p>
        </div>
"""

l6_study_guide = """
        <h1>📖 სასწავლო გზამკვლევი: ლექცია 6 (Career & Future)</h1>

        <h2>1. როგორ შევინარჩუნოთ ცოდნა?</h2>
        <div class="highlight-box">
            <p>AI ინდუსტრია იცვლება ყოველკვირეულად. აქტუალობის შესანარჩუნებლად:</p>
            <ul>
                <li><strong>გამოიწერეთ:</strong> TLDR Newsletter, The Rundown AI, GitHub Trending.</li>
                <li><strong>პრაქტიკა:</strong> ყოველდღიურად ერთი მცირე ამოცანა მაინც შეასრულებინეთ AI-ს.</li>
                <li><strong>Local Deployment:</strong> მიეჩვიეთ ახალი Open-Source მოდელების (Ollama) ლოკალურად ტესტირებას.</li>
            </ul>
        </div>

        <h2>2. კლიენტებთან კომუნიკაციის (Pricing) მოდელები</h2>
        <p>როგორ უნდა შეაფასოთ თქვენი შრომა, როცა კლიენტს ავტომატიზაციას უწყობთ?</p>
        <table style="margin-top: 1rem;">
            <tr>
                <th>მოდელი</th>
                <th>პრინციპი</th>
                <th>როდის გამოვიყენოთ?</th>
            </tr>
            <tr>
                <td><strong>Hourly Rate</strong></td>
                <td>საათობრივი ანაზღაურება (მაგ. $50/სთ)</td>
                <td>როცა პროექტი ბუნდოვანია და გამუდმებით იცვლება.</td>
            </tr>
            <tr>
                <td><strong>Project Based</strong></td>
                <td>ფიქსირებული თანხა მთლიან პროექტზე</td>
                <td>როცა ამოცანა (Scope) ზუსტად არის გაწერილი.</td>
            </tr>
            <tr>
                <td><strong>Value-Based (ROI)</strong></td>
                <td>თანხის მოთხოვნა დაზოგილი ფულის მიხედვით</td>
                <td>საუკეთესო ვარიანტი! თუ კომპანიას უზოგავთ თვეში $5000-ს, სისტემის აწყობა თავისუფლად შეგიძლიათ გაყიდოთ $10,000-ად.</td>
            </tr>
        </table>

        <h2>3. AGI (Artificial General Intelligence) მოლოდინები</h2>
        <p>კურსის ბოლოს ჩვენ შევეხეთ AGI-ს კონცეფციას (მანქანა, რომელიც ნებისმიერ ინტელექტუალურ ამოცანაში სჯობს ადამიანს). ამ ეპოქაში გადარჩენისთვის საჭიროა ფოკუსირება <strong>Domain Expertise</strong>-ზე (თქვენი ინდუსტრიის ღრმა ცოდნა), რადგან ტექნიკურ შესრულებას AI თავად გააკეთებს.</p>
"""

l6_quick_ref = """
        <h1>📋 სწრაფი ცნობარი: ლექცია 6 (Pitch & Freelance)</h1>

        <div class="key-points">
            <h3>🎤 იდეალური პრეზენტაციის (Pitch) ჩონჩხი</h3>
            <ol>
                <li><strong>Hook (15 წამი):</strong> პრობლემა, რომელიც ყველას სტკივა.</li>
                <li><strong>Solution (30 წამი):</strong> როგორ აგვარებს ამას თქვენი AI აგენტი.</li>
                <li><strong>Demo (3-4 წუთი):</strong> აჩვენეთ სისტემა მოქმედებაში (არ აჩვენოთ მხოლოდ კოდი/ნოდები).</li>
                <li><strong>ROI (30 წამი):</strong> რამდენი ფული/დრო დაიზოგა.</li>
                <li><strong>Q&A:</strong> მზადყოფნა ტექნიკური კითხვებისთვის.</li>
            </ol>
        </div>

        <div class="highlight-box">
            <h3>💼 Freelance სტარტერ-პაკეტი</h3>
            <ul>
                <li><strong>პორტფოლიო:</strong> მინიმუმ 3 რეალური, ვიდეო-ჩაწერილი (Loom) Case Study.</li>
                <li><strong>GitHub/Notion:</strong> სადაც ტექნიკურად გაქვთ აღწერილი თქვენი სისტემების არქიტექტურა.</li>
                <li><strong>LinkedIn:</strong> სათაურში მიუთითეთ "AI Automation Architect", რეგულარულად დაპოსტეთ ავტომატიზაციის შედეგები.</li>
            </ul>
        </div>
"""

l6_exercises = """
        <h1>💪 სავარჯიშოები: ლექცია 6 (Networking & Pitching)</h1>

        <div class="info-box">
            <p><strong>ინსტრუქცია:</strong> ეს არის თქვენი კარიერული განვითარების ფინალური დავალებები კურსის მიღმა.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 1: პორტფოლიოს ვიდეოს ჩაწერა (Loom)</h3>
            <p><strong>მიზანი:</strong> კლიენტებისთვის საჩვენებელი მასალის შექმნა.</p>
            <ol>
                <li>გადმოწერეთ <strong>Loom</strong> (ან ნებისმიერი Screen Recorder).</li>
                <li>ჩაწერეთ მაქსიმუმ 3-წუთიანი ვიდეო, სადაც აჩვენებთ თქვენს ფინალურ პროექტს მოქმედებაში.</li>
                <li>ვიდეოში ისაუბრეთ ბიზნესის ენაზე (ROI, პროდუქტიულობა) და არა ტექნიკური ტერმინებით (JSON, API).</li>
                <li>ატვირთეთ ვიდეო LinkedIn-ზე მოკლე აღწერით და მონიშნეთ Smart Academy.</li>
            </ol>
        </div>

        <div class="section-summary">
            <h3>დავალება 2: პირადი AI Information Pipeline-ის აწყობა</h3>
            <p><strong>მიზანი:</strong> მუდმივად სიახლეების საქმის კურსში ყოფნა დროის ხარჯვის გარეშე.</p>
            <ol>
                <li>ააწყვეთ Make.com სცენარი, რომელიც წამოიღებს RSS Feed-ს ტექნოლოგიური ბლოგებიდან (მაგ. TechCrunch, OpenAI Blog).</li>
                <li>გაატარეთ ეს სიახლეები ChatGPT/Claude მოდულში, რათა გააკეთოს 1-აბზაციანი ქართული შეჯამება თითოეულ სტატიაზე.</li>
                <li>გააგზავნეთ ეს შეჯამებები თქვენს პირად Telegram ჩატში ყოველ დილით 09:00 საათზე.</li>
            </ol>
        </div>
"""

base_path = r"c:\Users\GBASILAIA\claude\make"

files_to_generate = {
    "lecture-1-summary.html": ("ლექცია 1: შეჯამება", l1_summary, 1),
    "lecture-1-study-guide.html": ("ლექცია 1: სასწავლო გზამკვლევი", l1_study_guide, 1),
    "lecture-1-quick-ref.html": ("ლექცია 1: სწრაფი ცნობარი", l1_quick_ref, 1),
    "lecture-1-exercises.html": ("ლექცია 1: სავარჯიშოები", l1_exercises, 1),
    
    "lecture-6-summary.html": ("ლექცია 6: შეჯამება", l6_summary, 6),
    "lecture-6-study-guide.html": ("ლექცია 6: სასწავლო გზამკვლევი", l6_study_guide, 6),
    "lecture-6-quick-ref.html": ("ლექცია 6: სწრაფი ცნობარი", l6_quick_ref, 6),
    "lecture-6-exercises.html": ("ლექცია 6: სავარჯიშოები", l6_exercises, 6)
}

for filename, (title, content, lecture_num) in files_to_generate.items():
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(generate_html(title, filename, content, lecture_num))
    print(f"Generated {filename}")

print("All L1 and L6 supplementary files successfully generated!")

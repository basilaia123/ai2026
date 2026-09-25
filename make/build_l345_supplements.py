import os

CSS_STYLE = """
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'FiraGO', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #2c3e50;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            min-height: 100vh;
            padding: 2rem 1rem;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            padding: 3rem;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }

        h1 {
            color: #2c3e50;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 3px solid #667eea;
            font-size: 2.5rem;
        }

        h2 {
            color: #667eea;
            margin-top: 2.5rem;
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }

        h3 {
            color: #2c3e50;
            margin-top: 2rem;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }

        h4 {
            color: #495057;
            margin-top: 1.5rem;
            margin-bottom: 0.8rem;
            font-size: 1.2rem;
        }

        p {
            margin-bottom: 1rem;
            font-size: 1.1rem;
            line-height: 1.8;
        }

        ul, ol {
            margin-bottom: 1.5rem;
            padding-left: 2rem;
        }

        li {
            margin-bottom: 0.8rem;
            font-size: 1.1rem;
        }

        .highlight-box {
            background: #e3f2fd;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #2196f3;
            margin: 1.5rem 0;
        }

        .warning-box {
            background: #fff3e0;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #ff9800;
            margin: 1.5rem 0;
        }

        .key-points {
            background: #f1f8e9;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #4caf50;
            margin: 1.5rem 0;
        }

        .nav-links {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1rem;
            border-radius: 10px;
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 1rem;
            margin-bottom: 2rem;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        .nav-link {
            color: white;
            text-decoration: none;
            padding: 0.7rem 1.5rem;
            border-radius: 8px;
            background: rgba(255,255,255,0.15);
            backdrop-filter: blur(10px);
            transition: all 0.3s;
            font-weight: 500;
            border: 2px solid transparent;
        }

        .nav-link:hover {
            background: rgba(255,255,255,0.25);
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }

        .nav-link.current {
            background: white;
            color: #667eea;
            border: 2px solid white;
            font-weight: 600;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }

        th {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }

        td {
            padding: 1rem;
            border-bottom: 1px solid #e9ecef;
        }

        tr:hover {
            background: #f8f9fa;
        }

        .code-block, code {
            background: #2b2b2b;
            color: #f8f8f2;
            padding: 1rem;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            display: block;
            white-space: pre-wrap;
            margin: 1rem 0;
            font-size: 0.95rem;
        }
        
        p code, li code {
            display: inline;
            background: #f8f9fa;
            color: #e83e8c;
            padding: 0.2rem 0.5rem;
        }

        .section-summary {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1.5rem 0;
            border-left: 4px solid #667eea;
        }

        @media (max-width: 768px) {
            .container {
                padding: 1.5rem;
            }
            h1 {
                font-size: 2rem;
            }
            h2 {
                font-size: 1.6rem;
            }
            .nav-links {
                flex-direction: column;
            }
            .nav-link {
                width: 100%;
                text-align: center;
            }
        }
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
# LECTURE 3: API & Make.com Advanced
# ==========================================

l3_summary = """
        <h1>ლექცია 3: შეჯამება (API და No-Code ავტომატიზაცია)</h1>
        
        <div class="highlight-box">
            <h3>📚 ლექციის მიზნები</h3>
            <ul>
                <li>API-ს (Application Programming Interface) მუშაობის პრინციპების გაგება.</li>
                <li>Make.com-ში რთული ლოგიკური ოპერაციების (Routers, Iterators, Aggregators) აწყობა.</li>
                <li>მონაცემების რეალურ დროში მიღება (Webhooks).</li>
                <li>AI Coding Assistant-ების (Antigravity) და Advanced Web Scraping-ის გამოყენება.</li>
            </ul>
        </div>

        <h2>1️⃣ Make.com Advanced</h2>
        <div class="section-summary">
            <h3>Iteration და Aggregation</h3>
            <p><strong>მთავარი არსი:</strong> მასივებთან (Arrays) მუშაობა არის No-Code ავტომატიზაციის ყველაზე რთული, მაგრამ აუცილებელი ნაწილი.</p>
            <ul>
                <li><strong>Iterator (იტერატორი):</strong> იღებს ერთ დიდ სიას (მაგ. 5 ელფოსტა) და შლის ცალ-ცალკე მოქმედებებად. შესაბამისად, შემდგომი მოდული 5-ჯერ გაეშვება.</li>
                <li><strong>Aggregator (აგრეგატორი):</strong> შებრუნებული პროცესი. იღებს ბევრ ცალკეულ ინფორმაციას (მაგ. 5 გაანალიზებული ტექსტი) და აერთიანებს ერთ დიდ ტექსტად, რათა 1 ელფოსტით გააგზავნოს.</li>
            </ul>
            
            <h3>Data Routing (მონაცემთა მართვა)</h3>
            <p><strong>Routers (მარშრუტიზატორები)</strong> და <strong>Filters (ფილტრები)</strong> არის IF-THEN პირობითი ლოგიკა. Router ანაწილებს ნაკადს 2 ან მეტ გზაზე, ხოლო ფილტრი ამოწმებს პირობას თითოეულ გზაზე (მაგ. "თუ თანხა მეტია $1000-ზე").</p>
        </div>

        <h2>2️⃣ API და HTTP (ვების ენა)</h2>
        <div class="section-summary">
            <h3>როგორ საუბრობენ პროგრამები</h3>
            <p>API არის ოფიციალური "შემკვეთი", რომელიც იღებს თქვენს მოთხოვნას (მაგ. "რა ღირს ბიტკოინი?"), მიდის სერვერთან და უკან გიბრუნებთ პასუხს JSON ფორმატში.</p>
            <ul>
                <li><strong>GET მოთხოვნა:</strong> გამოიყენება ინფორმაციის წამოსაღებად (წასაკითხად).</li>
                <li><strong>POST მოთხოვნა:</strong> გამოიყენება ინფორმაციის გასაგზავნად (ახლის შესაქმნელად).</li>
                <li><strong>Headers:</strong> დამატებითი ინფორმაცია, სადაც ვათავსებთ ავტორიზაციის კოდებს (API Keys).</li>
            </ul>
            
            <h3>Webhooks (მომენტალური გამომწვევები)</h3>
            <p>თუ სტანდარტული API არის პერიოდული "შეკითხვა" (მაგ. ყოველ 15 წუთში ერთხელ ვამოწმებთ), Webhook არის პასიური მიმღები, რომელიც მუდამ უსმენს. როგორც კი გარე სისტემაში მოხდება რამე (მაგ. ახალი გადახდა), ის <strong>რეალურ დროში</strong> გვიგზავნის მონაცემებს.</p>
        </div>

        <h2>3️⃣ AI Coding & Web Scraping</h2>
        <div class="section-summary">
            <h3>Google Antigravity & Firecrawl</h3>
            <p>ავტომატიზაციაში ხშირად ვაწყდებით რთულ მონაცემებს, რომლის დამუშავებაც No-Code მოდულებით რთულია (მაგ. რთული Regex წესები). ამ დროს ვიყენებთ <strong>Google Antigravity</strong>-ს, რათა მან დაგვიწეროს უნივერსალური კოდი (JavaScript/Python) რთული ინფორმაციის დასამუშავებლად.</p>
            <p>ხოლო ვებ-გვერდებიდან ინფორმაციის ამოსაღებად (Lead Generation) ვიყენებთ <strong>Firecrawl</strong>-ს, რომელიც HTML-ს სუფთა Markdown-ად გარდაქმნის AI მოდელებისთვის.</p>
        </div>
"""

l3_study_guide = """
        <h1>📖 სასწავლო გზამკვლევი: ლექცია 3 (API და Make.com)</h1>

        <h2>1. მონაცემთა სტრუქტურები (Arrays & Objects)</h2>
        <div class="highlight-box">
            <p>იმისათვის რომ ავტომატიზაცია ავაწყოთ, უნდა გვესმოდეს როგორ ინახავს სერვერი მონაცემებს:</p>
            <ul>
                <li><strong>Object (ობიექტი):</strong> ერთი კონკრეტული ნივთის ან ადამიანის აღწერა. მას აქვს თვისებები (Keys) და მნიშვნელობები (Values).</li>
                <li><strong>Array (მასივი):</strong> ობიექტების სია. (მაგ. კალათაში არსებული 5 პროდუქტი).</li>
            </ul>
            <p><strong>რატომ არის ეს მნიშვნელოვანი?</strong> Make.com-ში თუ ამოიღებთ "Array"-ს, მას სჭირდება <strong>Iterator</strong> მოდული, რათა სია დაიშალოს და თითოეულ ობიექტს ცალკე მიხედოთ (მაგ. გაუგზავნოთ 5 ცალკეული მეილი).</p>
        </div>

        <h2>2. API - რესტორნის ანალოგია</h2>
        <p>API-ის გასაგებად, წარმოიდგინეთ რესტორანი:</p>
        <ul>
            <li><strong>მომხმარებელი (თქვენ):</strong> გაქვთ მენიუ და ითხოვთ საჭმელს.</li>
            <li><strong>ოფიციანტი (API):</strong> იღებს თქვენს შეკვეთას და მიაქვს სამზარეულოში. ოფიციანტის გარეშე, სამზარეულოში ვერ შეხვალთ (უსაფრთხოება).</li>
            <li><strong>სამზარეულო (სერვერი/მონაცემთა ბაზა):</strong> ამზადებს მოთხოვნილ ინფორმაციას და ატანს ოფიციანტს.</li>
            <li><strong>შეკვეთა მოვიდა:</strong> ოფიციანტს მოაქვს საჭმელი (ეს არის API Response JSON ფორმატში).</li>
        </ul>

        <h2>3. HTTP სტატუს კოდები - რას ნიშნავს რიცხვები?</h2>
        <p>როცა API-ს უკავშირდებით, ის გაძლევთ სტატუსს (3-ნიშნა რიცხვს). ამ რიცხვების გაგება Debugging-ისთვის კრიტიკულია:</p>
        <ul>
            <li><strong>2xx (წარმატება):</strong> <code>200 OK</code> - ყველაფერი იდეალურადაა.</li>
            <li><strong>4xx (კლიენტის შეცდომა):</strong> შეცდომა თქვენს მხარესაა.
                <ul>
                    <li><code>400 Bad Request</code> - არასწორი პარამეტრები გაგზავნეთ.</li>
                    <li><code>401 Unauthorized</code> - API Key არასწორია ან დაგავიწყდათ Headers-ში ჩასმა.</li>
                    <li><code>404 Not Found</code> - მონაცემი (ან URL) არ არსებობს.</li>
                </ul>
            </li>
            <li><strong>5xx (სერვერის შეცდომა):</strong> შეცდომა სისტემის მხარესაა. <code>500 Internal Server Error</code> - უნდა დაელოდოთ სერვერის გამოსწორებას.</li>
        </ul>

        <h2>4. Advanced Tools: როდის რა გამოვიყენოთ?</h2>
        <table style="margin-top: 1rem;">
            <tr>
                <th>ამოცანა</th>
                <th>იდეალური ინსტრუმენტი</th>
            </tr>
            <tr>
                <td>ვებ-გვერდის URL-დან ტექსტის ამოღება AI-სთვის</td>
                <td><strong>Firecrawl API</strong> (ვებგვერდს Markdown-ად აქცევს)</td>
            </tr>
            <tr>
                <td>ელ.ფოსტის მოსვლაზე მყისიერი რეაგირება</td>
                <td><strong>Webhook</strong> (მყისიერი Trigger)</td>
            </tr>
            <tr>
                <td>ტექსტიდან ურთულესი მონაცემების (მაგ. ID-ების) ძებნა</td>
                <td><strong>AI Coding Assistant (Antigravity)</strong> Regex ლოგიკისთვის</td>
            </tr>
            <tr>
                <td>რამდენიმე პირობის (IF) შემოწმება ერთდროულად</td>
                <td><strong>Make.com Router + Filters</strong></td>
            </tr>
        </table>
"""

l3_quick_ref = """
        <h1>📋 სწრაფი ცნობარი (Cheat Sheet): ლექცია 3</h1>

        <div class="key-points">
            <h3>Make.com-ის მთავარი მოდულები</h3>
            <ul>
                <li><code>Iterators (მწვანე მოდული):</code> Array ➔ ცალკეულ ობიექტებად დაშლა.</li>
                <li><code>Aggregators (მწვანე მოდული):</code> ობიექტები ➔ ერთიან Array-დ შეკვრა.</li>
                <li><code>Routers (მწვანე მოდული):</code> მონაცემთა გზაჯვარედინი. ერთი Flow იყოფა რამდენიმედ.</li>
                <li><code>Text Parser (ლურჯი მოდული):</code> ტექსტის დაყოფა, ან Regular Expressions (Regex) გამოყენება.</li>
                <li><code>HTTP Module (იისფერი მოდული):</code> ნებისმიერი გარე API-ის გამოძახება, რასაც ოფიციალური ინტეგრაცია არ აქვს.</li>
            </ul>
        </div>

        <div class="highlight-box">
            <h3>📝 JSON-ის კითხვა: ობიექტი VS მასივი</h3>
            <div class="code-block">
{
  "user": {  <-- ეს არის Object (ფიგურული ფრჩხილები)
    "name": "David",
    "role": "Admin"
  },
  "orders": [  <-- ეს არის Array (კვადრატული ფრჩხილები)
    { "id": 1, "total": 100 },
    { "id": 2, "total": 250 }
  ]
}
            </div>
            <p><strong>გახსოვდეთ:</strong> თუ ხედავთ <code>[ ]</code>, ესეიგი სიაა, და დაგჭირდებათ <strong>Iterator</strong>!</p>
        </div>

        <div class="warning-box">
            <h3>🔌 API მოთხოვნის აწყობის Checklist (HTTP Module)</h3>
            <ol>
                <li><strong>URL:</strong> სად ვაგზავნით? (მაგ. <code>https://api.openweathermap.org/data/2.5/weather</code>)</li>
                <li><strong>Method:</strong> <code>GET</code> (კითხვა), <code>POST</code> (შექმნა), თუ <code>PUT</code> (განახლება)?</li>
                <li><strong>Headers:</strong> გვაქვს თუ არა ჩასმული <code>Authorization: Bearer [API_KEY]</code>?</li>
                <li><strong>Query String (Parameters):</strong> მივუთითეთ თუ არა დამატებითი ფილტრები? (მაგ. <code>?q=Tbilisi&units=metric</code>)</li>
                <li><strong>Parse response:</strong> ჩართული გვაქვს თუ არა Yes, რათა Make.com-მა JSON წაიკითხოს?</li>
            </ol>
        </div>
"""

l3_exercises = """
        <h1>💪 სავარჯიშოები: ლექცია 3 (API & No-Code)</h1>

        <div class="info-box">
            <p><strong>ინსტრუქცია:</strong> ეს დავალებები შეამოწმებს თქვენს პრაქტიკულ უნარებს API ინტეგრაციებსა და Data Routing-ში.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 1: HTTP მოდული და Public API</h3>
            <p><strong>მიზანი:</strong> შექმენით Workflow, რომელიც ინფორმაციას წამოიღებს გარე სერვერიდან.</p>
            <ol>
                <li>Make.com-ში დაამატეთ <strong>HTTP -> Make a request</strong> მოდული.</li>
                <li>გამოიყენეთ უფასო API: <code>https://api.chucknorris.io/jokes/random</code></li>
                <li>Method აირჩიეთ <strong>GET</strong> და Parse response დააყენეთ <strong>Yes</strong>-ზე.</li>
                <li>გაუშვით მოდული (Run this module only).</li>
                <li>დაამატეთ Telegram ან Slack მოდული და გააგზავნეთ მიღებული ხუმრობის ტექსტი (ველი <code>value</code>) შეტყობინებად.</li>
            </ol>
        </div>

        <div class="section-summary">
            <h3>დავალება 2: Webhook Trigger-ის აწყობა</h3>
            <p><strong>მიზანი:</strong> მიიღეთ მონაცემები რეალურ დროში.</p>
            <ol>
                <li>Make.com-ში დაამატეთ <strong>Webhooks -> Custom webhook</strong> პირველ (Trigger) მოდულად.</li>
                <li>დააკლიკეთ Add-ს და დაარქვით სახელი "My Test Webhook".</li>
                <li>დააკოპირეთ მოცემული URL (დაიწყება <code>https://hook.eu1.make.com/...</code>).</li>
                <li>ბრაუზერის ახალ ფანჯარაში ჩასვით ეს URL, და ბოლოში მიუწერეთ <code>?name=Giorgi&email=test@test.com</code> და დააჭირეთ Enter-ს. (ბრაუზერი დაწერს "Accepted").</li>
                <li>დაბრუნდით Make.com-ში და ნახავთ, რომ მოდულმა წარმატებით დაადგინა სტრუქტურა. ახლა ეს მონაცემები შეგიძლიათ გამოიყენოთ შემდეგ მოდულებში!</li>
            </ol>
        </div>

        <div class="section-summary">
            <h3>დავალება 3: Router და პირობითი ლოგიკა (Filters)</h3>
            <p><strong>მიზანი:</strong> მონაცემების დაყოფა მნიშვნელობის მიხედვით.</p>
            <p>ააწყვეთ ლოგიკა წინა დავალების (Webhook-ის) გაგრძელებად:</p>
            <ol>
                <li>დაამატეთ <strong>Router</strong> მოდული Webhook-ის შემდეგ.</li>
                <li>გააკეთეთ ორი განშტოება (Flow).</li>
                <li><strong>ზედა განშტოების ფილტრი:</strong> დაარქვით "Giorgi" და Condition-ში მიუთითეთ: თუ <code>name</code> (Webhook-დან) უდრის <code>Giorgi</code>. ამ გზაზე დაამატეთ Telegram მოდული ტექსტით "Hello Admin".</li>
                <li><strong>ქვედა განშტოების ფილტრი:</strong> დაარქვით "Other" და Condition-ში მიუთითეთ: თუ <code>name</code> <strong>არ უდრის</strong> <code>Giorgi</code>. ამ გზაზე დაამატეთ ტექსტი "Hello Guest".</li>
                <li>დატესტეთ Webhook-ის ბრაუზერიდან სხვადასხვა სახელის გაგზავნით.</li>
            </ol>
        </div>
"""

# ==========================================
# LECTURE 4: n8n, Deep Research & UI Agents
# ==========================================

l4_summary = """
        <h1>ლექცია 4: შეჯამება (n8n, ლოკალური მოდელები და UI აგენტები)</h1>
        
        <div class="highlight-box">
            <h3>📚 ლექციის მიზნები</h3>
            <ul>
                <li>გადასვლა Cloud პლატფორმიდან (Make.com) Self-Hosted ეკოსისტემაზე (n8n).</li>
                <li>მონაცემთა ნულოვანი გაჟონვის (Zero Data Leakage) კონცეფცია და Ollama-ს ინტეგრაცია.</li>
                <li>Deep Research (ღრმა კვლევის) აგენტური არქიტექტურის გაცნობა.</li>
                <li>Computer Use API და UI აგენტების დანერგვა კომპიუტერული გარემოს სამართავად.</li>
            </ul>
        </div>

        <h2>1️⃣ n8n და ლოკალური AI სისტემები</h2>
        <div class="section-summary">
            <h3>Fair-Code და Self-Hosting</h3>
            <p>ბანკები, სადაზღვევო და ჯანდაცვის კომპანიები ვერ იყენებენ Make.com-ს, რადგან Cloud სერვერებზე კონფიდენციალური მონაცემების ატვირთვა არღვევს უსაფრთხოების რეგულაციებს (Compliance). გამოსავალი არის <strong>n8n</strong> - პლატფორმა, რომელიც შეგიძლიათ დააინსტალიროთ პირდაპირ თქვენს ლოკალურ სერვერზე (Docker-ის მეშვეობით) და მონაცემები არასოდეს ტოვებს თქვენს ინფრასტრუქტურას.</p>
            
            <h3>Zero Data Leakage ლოკალური მოდელებით (Ollama)</h3>
            <p>უსაფრთხოება არ სრულდება მხოლოდ n8n-ით. თუ თქვენი სისტემა ტექსტს აანალიზებს OpenAI-ს (ChatGPT) API-ით, მონაცემები მაინც იგზავნება ინტერნეტში. ამიტომ ვიყენებთ <strong>Ollama</strong>-ს, რომელიც ლოკალურად რთავს ძლიერ მოდელებს (DeepSeek, Llama 3). ამ კომბინაციით (n8n + Ollama), ავტომატიზაცია მუშაობს მაშინაც კი, თუ ინტერნეტს გავთიშავთ (Wi-Fi Off ექსპერიმენტი).</p>
        </div>

        <h2>2️⃣ Deep Research (ღრმა კვლევა)</h2>
        <div class="section-summary">
            <h3>Iterative Searching (ციკლური კვლევა)</h3>
            <p>სტანდარტული Search Tool აკეთებს ერთ ძიებას და აბრუნებს 10 შედეგს. <strong>Deep Research</strong> აგენტი კი არის ციკლური სისტემა (Sub-workflows გამოყენებით n8n-ში), რომელიც:</p>
            <ol>
                <li>ძებნის ინფორმაციას.</li>
                <li>კითხულობს კონტენტს.</li>
                <li>პოულობს ხარვეზებს მიღებულ ცოდნაში.</li>
                <li>აკეთებს მეორე, უფრო სპეციფიკურ ძიებას.</li>
                <li>იმეორებს ამ ციკლს სანამ არ მიიღებს სრულყოფილ სურათს.</li>
            </ol>
        </div>

        <h2>3️⃣ Computer Use და UI აგენტები</h2>
        <div class="section-summary">
            <h3>რას ვაკეთებთ, როცა პროგრამას API არ აქვს?</h3>
            <p>ძალიან ბევრ ძველ Enterprise სისტემას ან ლოკალურ პროგრამას არ აქვს API. აქ შემოდის <strong>Claude Computer Use</strong>. ეს არის AI აგენტი, რომელიც ხედავს და მართავს თქვენს ეკრანს ზუსტად ისე, როგორც ადამიანი.</p>
            <p><strong>პროცესი:</strong> Screenshot ➔ LLM აანალიზებს პიქსელებს ➔ Action (მაუსის გადაადგილება, კლიკი, კლავიატურაზე ბეჭდვა).</p>
            <p><strong>უსაფრთხოება:</strong> ასეთი აგენტების გაშვება უნდა მოხდეს იზოლირებულ გარემოში (Sandboxing - Virtual Machines ან Docker Containers), რათა მათ არ შეცვალონ კრიტიკული სისტემური ფაილები.</p>
        </div>
"""

l4_study_guide = """
        <h1>📖 სასწავლო გზამკვლევი: ლექცია 4 (n8n & UI Agents)</h1>

        <h2>1. არქიტექტურული სხვაობა: Make.com VS n8n</h2>
        <table style="margin-top: 1rem;">
            <tr>
                <th>მახასიათებელი</th>
                <th>Make.com (SaaS)</th>
                <th>n8n (Self-Hosted)</th>
            </tr>
            <tr>
                <td><strong>ჰოსტინგი</strong></td>
                <td>Cloud-ზე (Make-ის სერვერები)</td>
                <td>ლოკალურად (თქვენს სერვერზე/Docker)</td>
            </tr>
            <tr>
                <td><strong>უსაფრთხოება</strong></td>
                <td>სტანდარტული (მონაცემები გარეთ გადის)</td>
                <td>უმაღლესი (Zero Leakage)</td>
            </tr>
            <tr>
                <td><strong>ფინანსები (ფასი)</strong></td>
                <td>ყოველი Operation (Operation-based) ფასიანია</td>
                <td>უფასო (იხდით მხოლოდ თქვენი სერვერის ფულს)</td>
            </tr>
            <tr>
                <td><strong>UI და სინტაქსი</strong></td>
                <td>მარტივი ვიზუალური UI</td>
                <td>ნახევრად პროგრამისტული (JavaScript/JSON)</td>
            </tr>
        </table>

        <h2>2. Privacy Compliance (რეგულაციები)</h2>
        <div class="highlight-box">
            <p>კომპანიებს (განსაკუთრებით ევროკავშირსა და აშშ-ში) აქვთ მკაცრი <strong>GDPR / HIPAA</strong> რეგულაციები. თუ სადაზღვევო კომპანია პაციენტის ჯანმრთელობის ისტორიას აგზავნის OpenAI-ში გასაანალიზებლად, ეს არის დანაშაული. გამოსავალი არის <strong>Local LLMs (Ollama)</strong>.</p>
            <p><strong>Ollama-ს მუშაობის პრინციპი:</strong> ის თქვენს კომპიუტერში/სერვერზე ტვირთავს მოდელების წონებს (Weights), ისევე როგორც პროგრამის ინსტალაციას. გაგზავნილი Prompt თქვენს კომპიუტერს არასოდეს ტოვებს.</p>
        </div>

        <h2>3. n8n Expressions (გამოსახულებები)</h2>
        <p>n8n იყენებს JavaScript-ს (უფრო კონკრეტულად კი <code>{{$json.fieldname}}</code> ფორმატს) მონაცემების გადასატანად ერთ ნოდიდან მეორეში.</p>
        <ul>
            <li>თუ Make-ში მაუსით ვაგდებდით ვარდისფერ "ბუშტუკებს", n8n-ში ვწერთ: <code>{{ $json.email }}</code>, რაც ნიშნავს წინა ნოდის JSON-დან "email" ველის წამოღებას.</li>
        </ul>

        <h2>4. Computer Use - ეთიკა და იზოლაცია</h2>
        <div class="warning-box">
            <h3>Sandboxing (იზოლაცია)</h3>
            <p>UI აგენტი ხედავს და მართავს ეკრანს. შეცდომის (Hallucination) გამო მას შეუძლია წაშალოს მნიშვნელოვანი ფაილები, ან გააგზავნოს არასწორი ელ.ფოსტები. ამიტომ <strong>არასოდეს გაუშვათ UI აგენტი თქვენს პირად/სამუშაო კომპიუტერზე!</strong></p>
            <p>გამოიყენეთ <strong>Docker Container</strong> ან ვირტუალური მანქანა (VM). თუ აგენტი რამეს გააფუჭებს, უბრალოდ წაშლით Container-ს და სისტემა არ დაზიანდება.</p>
        </div>
"""

l4_quick_ref = """
        <h1>📋 სწრაფი ცნობარი (Cheat Sheet): ლექცია 4</h1>

        <div class="key-points">
            <h3>n8n VS Make.com ტერმინოლოგია</h3>
            <table>
                <tr>
                    <th>Make.com</th>
                    <th>n8n</th>
                </tr>
                <tr>
                    <td>Module</td>
                    <td>Node</td>
                </tr>
                <tr>
                    <td>Scenario</td>
                    <td>Workflow</td>
                </tr>
                <tr>
                    <td>Mapping (Variables)</td>
                    <td>Expressions (<code>{{$json.var}}</code>)</td>
                </tr>
                <tr>
                    <td>Router</td>
                    <td>Switch / IF Node</td>
                </tr>
                <tr>
                    <td>Data structure panel</td>
                    <td>JSON Output preview</td>
                </tr>
            </table>
        </div>

        <div class="highlight-box">
            <h3>Deep Research აგენტის ციკლი</h3>
            <div class="code-block">
1. Receive Query: "ანალიზი ბლოკჩეინის რეგულაციებზე EU-ში"
2. Initialize Sub-Workflow:
   [LOOP START]
   3. Search Web (Query 1)
   4. Extract content (Firecrawl)
   5. LLM Analysis: "გვაქვს საკმარისი ინფო?"
      IF YES -> Exit Loop
      IF NO -> Generate Query 2 -> Go to Step 3
   [LOOP END]
6. Aggregate all findings
7. Write Final Report
            </div>
        </div>

        <div class="warning-box">
            <h3>🔒 Zero-Leakage სისტემის Checklist</h3>
            <ol>
                <li><strong>n8n Hosting:</strong> დაყენებულია ლოკალურად Docker-ით (არა n8n Cloud).</li>
                <li><strong>LLM:</strong> გამოიყენება Ollama Node (მოდელი: Llama 3 ან DeepSeek ლოკალურად).</li>
                <li><strong>Network:</strong> სისტემა იზოლირებულია, ან აყენია Firewall, რომელიც კრძალავს გარე მოთხოვნებს (Outbound traffic).</li>
                <li><strong>APIs:</strong> არ გამოიყენება არანაირი გარე 3rd Party API, რომელიც ამუშავებს ტექსტს (მაგ. OpenAI, Anthropic).</li>
            </ol>
        </div>
"""

l4_exercises = """
        <h1>💪 სავარჯიშოები: ლექცია 4 (n8n & Computer Use)</h1>

        <div class="info-box">
            <p><strong>ინსტრუქცია:</strong> ეს არის არქიტექტურული და კონცეპტუალური დავალებები ენთერფრაიზ სისტემებზე.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 1: n8n Expression ლოგიკა</h3>
            <p><strong>მიზანი:</strong> n8n-ის სინტაქსის გაგება.</p>
            <p>ვთქვათ, გაქვთ Webhook Node (სახელით <code>Webhook</code>), რომელმაც მიიღო შემდეგი JSON მონაცემი:</p>
            <div class="code-block">
{
  "body": {
    "company_name": "Smart Academy",
    "budget": 5000
  }
}
            </div>
            <p>დაწერეთ n8n-ის <strong>Expression</strong>, როგორ ამოიღებთ კომპანიის სახელს (company_name) შემდეგ ნოდში.</p>
            <details style="margin-top: 1rem; cursor: pointer;">
                <summary><strong>💡 დააკლიკეთ პასუხის სანახავად</strong></summary>
                <div class="code-block" style="margin-top: 0.5rem;">
{{ $json.body.company_name }}
                </div>
            </details>
        </div>

        <div class="section-summary">
            <h3>დავალება 2: Privacy (Zero-Leakage) Audit</h3>
            <p><strong>მიზანი:</strong> უსაფრთხოების რისკების იდენტიფიცირება.</p>
            <p><strong>სცენარი:</strong> სამედიცინო კლინიკის IT დირექტორი გიჩვენებთ ახალ ავტომატიზაციას: <em>"პაციენტის ისტორია (სიმპტომები, დიაგნოზი) მოდის ჩვენი ლოკალური სერვერიდან (Webhook). ჩვენ ეს შევაერთეთ ChatGPT API-სთან, რომელიც პაციენტს უწერს სამკურნალო რეკომენდაციებს და უგზავნის ელფოსტაზე."</em></p>
            <p><strong>კითხვა:</strong> რატომ არის ეს სისტემა კატასტროფული იურიდიულად და უსაფრთხოების კუთხით? შესთავაზეთ ალტერნატიული არქიტექტურა ჩვენი ლექციის (Ollama) ცოდნის საფუძველზე.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 3: UI აგენტის მოქმედებების დაშლა</h3>
            <p><strong>მიზანი:</strong> გაიგოთ, როგორ ხედავს კომპიუტერს AI.</p>
            <p><strong>დავალება:</strong> თქვენ გინდათ, რომ Claude Computer Use-მა დამოუკიდებლად შეუკვეთოს პიცა ვებგვერდიდან. ჩამოწერეთ ტექსტურად ის მინიმუმ 5 მიკრო-ნაბიჯი (Action), რომლის შესრულებაც მოუწევს UI აგენტს ეკრანზე (Screenshot-ის ნახვის შემდეგ). მაგალითად: <em>1. მაუსის გადატანა Chrome-ის Icon-ზე.</em></p>
        </div>
"""

# ==========================================
# LECTURE 5: B2B Case Studies, ROI & Security
# ==========================================

l5_summary = """
        <h1>ლექცია 5: შეჯამება (B2B Case Studies და ROI)</h1>
        
        <div class="highlight-box">
            <h3>📚 ლექციის მიზნები</h3>
            <ul>
                <li>ენთერფრაიზ ავტომატიზაციის პარადიგმების გაგება (Deterministic VS Reasoning).</li>
                <li>რეალური ბიზნეს-პრობლემების გადაჭრა ულტრა-თანამედროვე მეთოდებით (Support Automation, Vision AI).</li>
                <li>Human-in-the-Loop (HITL) მექანიზმის დანერგვა რისკების დასაზღვევად.</li>
                <li>უსაფრთხოება (PII Masking) და პროექტის ფინანსური შეფასება (ROI გამოთვლა).</li>
            </ul>
        </div>

        <h2>1️⃣ პარადიგმები და ჰიბრიდული მიდგომა</h2>
        <div class="section-summary">
            <h3>მკაცრი ლოგიკა მოაზროვნე აგენტის წინააღმდეგ</h3>
            <p><strong>Deterministic (მკაცრი) ლოგიკა:</strong> ტრადიციული ავტომატიზაციაა (მაგ. თუ A, მაშინ B). 100%-ით სანდოა, მაგრამ არ არის მოქნილი.</p>
            <p><strong>Reasoning (მოაზროვნე) აგენტი:</strong> იღებს დამოუკიდებელ გადაწყვეტილებებს კონტექსტიდან გამომდინარე (LLM). მოქნილია, მაგრამ აქვს ჰალუცინაციის რისკი.</p>
            <p><strong>ჰიბრიდული მიდგომა (Best Practice):</strong> სისტემის ჩონჩხი და მარშრუტები (Routers) არის მკაცრი და დეტერმინისტული (Make.com/n8n), ხოლო კონკრეტული კვანძები, სადაც კრეატივი ან ანალიზია საჭირო, ეთმობა Reasoning აგენტს. ასე ვიღებთ უსაფრთხო, კონტროლირებად და ინტელექტუალურ სისტემას.</p>
        </div>

        <h2>2️⃣ B2B Case Studies</h2>
        <div class="section-summary">
            <h3>Customer Support (ტექსტის ანალიზი)</h3>
            <p>კლიენტების იმეილები მუშავდება AI-ის მიერ, რომელიც ჯერ აკეთებს <strong>Categorization-ს</strong> (რა ტიპის პრობლემაა). სტანდარტულ პრობლემებზე (მაგ. პაროლის აღდგენა) სისტემა პირდაპირ აგზავნის პასუხს. რთულ პრობლემებზე (მაგ. ფინანსური დავა) სისტემა ამზადებს Draft პასუხს და უგზავნის մենეჯერს Slack-ში დასადასტურებლად.</p>
            
            <h3>დოკუმენტების კონვეიერი (Vision AI)</h3>
            <p>კომპანიებს აქვთ ბევრი არა-სტრუქტურირებული დოკუმენტი (დასკანერებული PDF ინვოისები, ხელშეკრულებები). GPT-4o-ს (Vision) გამოყენებით, სისტემა პირდაპირ "კითხულობს" სურათს, იღებს მონაცემებს (კომპანიის სახელი, თანხა) და წერს სუფთა სახით Google Sheets-ში ან ERP ბაზაში.</p>
        </div>

        <h2>3️⃣ უსაფრთხოება და ROI</h2>
        <div class="section-summary">
            <h3>PII (Personal Identifiable Information) Masking</h3>
            <p>როდესაც არ გვაქვს Local LLM-ის ფუფუნება და Cloud (OpenAI) უნდა გამოვიყენოთ, აუცილებელია <strong>მონაცემების დაფარვა (Masking)</strong>. სანამ კლიენტის საჩივარი წავა OpenAI-ში, ლოკალური სკრიპტით ყველა სახელი, ტელეფონის ნომერი და პირადი ნომერი უნდა შეიცვალოს XXXXX-ით.</p>
            
            <h3>ROI (Return on Investment)</h3>
            <p>ROI არის ინვესტიციის უკუგება. ბიზნესს არ აინტერესებს რა ტექნოლოგიას იყენებთ, მას აინტერესებს რამდენ ფულს დაუზოგავთ. ROI ითვლება: <strong>(ადამიანის დროის ფასი - API ტოკენების ხარჯი) / პროექტის დანერგვის ღირებულება</strong>.</p>
        </div>
"""

l5_study_guide = """
        <h1>📖 სასწავლო გზამკვლევი: ლექცია 5 (Enterprise, Security & ROI)</h1>

        <h2>1. Human-in-the-Loop (HITL) არქიტექტურა</h2>
        <div class="highlight-box">
            <p>როდესაც საქმე ეხება ფინანსურ გადარიცხვებს, კონტრაქტებს ან კლიენტებთან სენსიტიურ კომუნიკაციას, AI-ის ბრმად ნდობა კატასტროფაა.</p>
            <ul>
                <li><strong>HITL:</strong> პროცესი ჩერდება კრიტიკულ მომენტში და ელოდება ადამიანის (მენეჯერის) დასტურს.</li>
                <li><strong>როგორ მუშაობს:</strong> Make/n8n აგენერირებს 2 ღილაკს Slack-ში ან მეილში (Approve / Reject). ადამიანი აჭერს ღილაკს, და Trigger-ით (Webhook) ავტომატიზაცია აგრძელებს მუშაობას.</li>
            </ul>
        </div>

        <h2>2. Vision AI - Prompt სტრუქტურა სურათებისთვის</h2>
        <p>PDF დოკუმენტებიდან მონაცემების ამოსაღებად (Invoice OCR-ის ნაცვლად), Prompt-ს უნდა ჰქონდეს მკაცრი სტრუქტურა:</p>
        <div class="code-block">
Role: შენ ხარ მთავარი ბუღალტერი, რომლის საქმეა სურათებიდან ტექსტის ამოღება.
Task: მოწოდებული ინვოისის სურათიდან ამოიღე შემდეგი ველები:
- კომპანიის სახელი
- გადასახდელი ჯამური თანხა
- ინვოისის თარიღი
Format: დააბრუნე მხოლოდ და მხოლოდ ვალიდური JSON. არ დაწერო არანაირი სხვა ტექსტი.
        </div>

        <h2>3. PII (პერსონალური მონაცემების) მართვა</h2>
        <p>GDPR-ის მიხედვით, პერსონალური მონაცემები (PII) მოიცავს:</p>
        <ul>
            <li>სახელი და გვარი</li>
            <li>პირადი ნომერი / სოციალური დაზღვევის ნომერი</li>
            <li>ტელეფონის ნომერი, მისამართი, ელ.ფოსტა</li>
            <li>საბანკო ბარათის დეტალები</li>
        </ul>
        <p><strong>წესი:</strong> LLM მოდელებს არ სჭირდებათ იცოდნენ, რომ კლიენტს ჰქვია "გიორგი". მათ შეუძლიათ ემოცია ან საჩივრის შინაარსი გააანალიზონ PII მონაცემების გარეშეც (Data Masking).</p>

        <h2>4. Production Readiness Checklist</h2>
        <p>სანამ ავტომატიზაციას ბიზნესს ჩააბარებთ, შეამოწმეთ ეს 3 პუნქტი:</p>
        <ol>
            <li><strong>Error Handling:</strong> თუ OpenAI-ის სერვერი გაითიშა, თქვენი Make.com-ის სცენარი ხომ არ წყვეტს მუშაობას? გაქვთ Error Route (Break Node)?</li>
            <li><strong>Logging:</strong> სად ინახება წარმატებული და წარუმატებელი პროცესების ისტორია? (Google Sheets Database).</li>
            <li><strong>Cost Monitoring:</strong> თუ ვინმემ System-ში ჩაყარა 10,000 PDF ფაილი, API-ის ბალანსი ხომ არ ამოიწურება 1 საათში?</li>
        </ol>
"""

l5_quick_ref = """
        <h1>📋 სწრაფი ცნობარი (Cheat Sheet): ლექცია 5</h1>

        <div class="key-points">
            <h3>💰 ROI-ის (Return on Investment) ფორმულა</h3>
            <p>როგორ ავუხსნათ ბიზნესს ავტომატიზაციის სარგებელი რიცხვებში?</p>
            <div class="code-block" style="background: #2b2b2b; color: #a6e22e;">
1. დათვალეთ ადამიანის ხარჯი (Current Cost):
   მაგ: მენეჯერი დღეში ხარჯავს 2 საათს მეილების პასუხზე.
   თვეში: 40 საათი. ମენეჯერის ხელფასი: $15/სთ.
   ძველი ხარჯი: 40 * $15 = $600 თვეში.

2. დათვალეთ AI-ის ხარჯი (New Cost):
   API Tokens + n8n სერვერის ჰოსტინგი.
   ახალი ხარჯი: მაგ. $20 თვეში.

3. ყოველთვიური მოგება (Monthly Savings):
   $600 - $20 = $580 დაზოგილი თვეში.
            </div>
            <p><strong>ბიზნესს ეუბნებით:</strong> <em>"ეს სისტემა თვეში დაგიზოგავთ 40 საათს და $580-ს, რომლითაც მენეჯერი შეძლებს რეალური გაყიდვების კეთებას."</em></p>
        </div>

        <div class="highlight-box">
            <h3>🛡️ PII Masking Workflow</h3>
            <ol>
                <li>მიიღე ელფოსტა (Trigger).</li>
                <li>გაატარე ლოკალურ Regex/Text Parser-ში, რათა იპოვოს +995 ტელეფონის ნომრები ან @ ნიშნები.</li>
                <li>შეცვალე ნაპოვნი მონაცემები `[MASKED]` ტექსტით.</li>
                <li>გაგზავნე `[MASKED]` ტექსტი OpenAI-ში გასაანალიზებლად.</li>
                <li>მიღებულ პასუხს ისევ მიაბი ორიგინალი იდენტიფიკატორი (ID) და გაგზავნე ბაზაში.</li>
            </ol>
        </div>

        <div class="warning-box">
            <h3>⚖️ Deterministic VS Reasoning (მოკლე წესები)</h3>
            <ul>
                <li><strong>გამოიყენეთ Deterministic (Routers/Filters):</strong> გადახდებზე, ბაზაში ჩაწერაზე, მეილის გაგზავნაზე, ნოტიფიკაციებზე. (სადაც შეცდომის ფასი მაღალია).</li>
                <li><strong>გამოიყენეთ Reasoning (LLMs):</strong> ტექსტის გაგებაზე, სურათების ანალიზზე, შინაარსის კატეგორიზაციაზე, შეჯამებაზე.</li>
            </ul>
        </div>
"""

l5_exercises = """
        <h1>💪 სავარჯიშოები: ლექცია 5 (B2B ავტომატიზაცია & ROI)</h1>

        <div class="info-box">
            <p><strong>ინსტრუქცია:</strong> ეს დავალებები აჯამებს თქვენს ბიზნეს-ანალიტიკურ აზროვნებას, რაც აუცილებელია ფინალური პროექტისთვის.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 1: დაითვალეთ ROI</h3>
            <p><strong>მიზანი:</strong> გამოთვალოთ ფინანსური სარგებელი.</p>
            <p><strong>მოცემულობა:</strong> ლოჯისტიკურ კომპანიაში ოპერატორი ყოველდღიურად ბეჭდავს 100 ინვოისს ERP სისტემაში სურათებიდან გადაწერით. ერთ ინვოისს სჭირდება 3 წუთი. ოპერატორის ანაზღაურებაა 10 ₾ საათში. თქვენ სთავაზობთ Vision AI-ის სისტემას. 1 სურათის გაანალიზება API-ით ჯდება 0.05 ₾.</p>
            <p><strong>გამოთვალეთ (ერთ თვეზე - 22 სამუშაო დღე):</strong></p>
            <ol>
                <li>რამდენს ხარჯავდა კომპანია ძველი მეთოდით?</li>
                <li>რა დაუჯდება კომპანიას თქვენი AI სისტემა?</li>
                <li>რამდენია ყოველთვიური დანაზოგი (ROI)?</li>
            </ol>
            <details style="margin-top: 1rem; cursor: pointer;">
                <summary><strong>💡 დააკლიკეთ პასუხის სანახავად</strong></summary>
                <div class="code-block" style="margin-top: 0.5rem;">
1. ძველი ხარჯი:
   100 ინვოისი * 3 წთ = 300 წთ (5 საათი დღეში).
   5 სთ * 10₾ = 50 ₾ დღეში.
   თვეში: 50₾ * 22 = 1,100 ₾.

2. ახალი (API) ხარჯი:
   100 ინვოისი * 0.05₾ = 5 ₾ დღეში.
   თვეში: 5₾ * 22 = 110 ₾.

3. დანაზოგი:
   1,100 - 110 = 990 ₾ დაზოგილი თვეში + ოპერატორის გამოთავისუფლებული 110 საათი!
                </div>
            </details>
        </div>

        <div class="section-summary">
            <h3>დავალება 2: PII მონაცემების იდენტიფიკაცია</h3>
            <p><strong>მიზანი:</strong> ამოიცნოთ კონფიდენციალური მონაცემები ტექსტში.</p>
            <p>წაიკითხეთ კლიენტის მოწერილი ტექსტი:</p>
            <p><em>"გამარჯობა, მე ვარ თამარ კვარაცხელია. ჩემი მანქანა, მერსედესი, ნომრით AA-123-BB მოხვდა ავარიაში რუსთაველის 15 ნომერთან. გთხოვთ დამიკავშირდეთ ნომერზე 599 12 34 56. ჩემი პირადი ნომერია 01012345678."</em></p>
            <p><strong>დავალება:</strong> ხელახლა დაწერეთ ეს ტექსტი, ოღონდ დაფარეთ ყველა PII მონაცემი `[MASKED]` ტეგით, ისე რომ ChatGPT-მ მაინც შეძლოს გაგება, რომ ეს არის ავტო-დაზღვევის სადაზღვევო შემთხვევა.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 3: Human-in-the-Loop სცენარის დაგეგმვა</h3>
            <p><strong>მიზანი:</strong> რისკების მართვის დაგეგმვა.</p>
            <p>თქვენ აწყობთ ავტომატიზაციას, რომელიც კლიენტის მოთხოვნისთანავე ავტომატურად უკეთებს მას თანხის დაბრუნებას (Refund) Stripe-ის ან TBC API-ის გავლით. ეს ძლიერ სარისკოა.</p>
            <p><strong>დავალება:</strong> დახატეთ/ჩამოწერეთ ავტომატიზაციის ნაბიჯები Make.com-ში ისე, რომ თანხის დაბრუნების Action Node არ გაეშვას, სანამ ფინანსური მენეჯერი Slack-ში არ დააჭერს "Approve" ღილაკს.</p>
        </div>
"""

# ==========================================
# FILE GENERATION LOGIC
# ==========================================

base_path = r"c:\Users\GBASILAIA\claude\make"

files_to_generate = {
    # Lecture 3
    "lecture-3-summary.html": ("ლექცია 3: შეჯამება", l3_summary, 3),
    "lecture-3-study-guide.html": ("ლექცია 3: სასწავლო გზამკვლევი", l3_study_guide, 3),
    "lecture-3-quick-ref.html": ("ლექცია 3: სწრაფი ცნობარი", l3_quick_ref, 3),
    "lecture-3-exercises.html": ("ლექცია 3: სავარჯიშოები", l3_exercises, 3),
    
    # Lecture 4
    "lecture-4-summary.html": ("ლექცია 4: შეჯამება", l4_summary, 4),
    "lecture-4-study-guide.html": ("ლექცია 4: სასწავლო გზამკვლევი", l4_study_guide, 4),
    "lecture-4-quick-ref.html": ("ლექცია 4: სწრაფი ცნობარი", l4_quick_ref, 4),
    "lecture-4-exercises.html": ("ლექცია 4: სავარჯიშოები", l4_exercises, 4),
    
    # Lecture 5
    "lecture-5-summary.html": ("ლექცია 5: შეჯამება", l5_summary, 5),
    "lecture-5-study-guide.html": ("ლექცია 5: სასწავლო გზამკვლევი", l5_study_guide, 5),
    "lecture-5-quick-ref.html": ("ლექცია 5: სწრაფი ცნობარი", l5_quick_ref, 5),
    "lecture-5-exercises.html": ("ლექცია 5: სავარჯიშოები", l5_exercises, 5)
}

for filename, (title, content, lecture_num) in files_to_generate.items():
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(generate_html(title, filename, content, lecture_num))
    print(f"Generated {filename}")

print("All 12 supplementary files generated successfully!")

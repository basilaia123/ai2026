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

def generate_html(title, current_page, content):
    nav_links = {
        "index.html": "🏠 მთავარი",
        "lecture-2-slides.html": "📊 სლაიდები",
        "lecture-2-summary.html": "📚 შეჯამება",
        "lecture-2-quick-ref.html": "📋 სწრაფი ცნობარი",
        "lecture-2-exercises.html": "💪 სავარჯიშოები",
        "lecture-2-study-guide.html": "📖 სასწავლო გზამკვლევი"
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

# ---------------------------------------------------------
# 1. SUMMARY
# ---------------------------------------------------------
summary_content = """
        <h1>ლექცია 2: შეჯამება (Custom Assistants & Agents)</h1>
        
        <div class="highlight-box">
            <h3>📚 ლექციის მიზნები</h3>
            <ul>
                <li>Custom GPTs და Claude Projects-ის გამოყენება.</li>
                <li>ცოდნის ბაზების (Knowledge Bases) და RAG სისტემების გაგება.</li>
                <li>ასისტენტებსა და AI აგენტებს შორის განსხვავების დანახვა (ReAct Framework).</li>
                <li>Model Context Protocol (MCP) ტექნოლოგიის საფუძვლების შესწავლა.</li>
            </ul>
        </div>

        <h2>1️⃣ ნაწილი 1: Custom Assistants & Knowledge Bases</h2>
        <div class="section-summary">
            <h3>Custom GPTs & Claude Projects</h3>
            <p><strong>მთავარი არსი:</strong> უბრალო Chat ინტერფეისიდან გადავდივართ მორგებულ ასისტენტებზე. Claude Projects გვაძლევს საშუალებას ერთ სივრცეში მოვაქციოთ კონკრეტული პროექტის კონტექსტი, სისტემური ინსტრუქციები (Style & Tone) და დოკუმენტები (200K ტოკენამდე, რაც დაახლოებით 500 გვერდია).</p>
            
            <h3>RAG და ვექტორული ბაზები</h3>
            <ul>
                <li><strong>RAG (Retrieval-Augmented Generation):</strong> AI-ის მიერ მოძიებული ინფორმაციის საფუძველზე პასუხის გენერაცია. (როგორც ბიბლიოთეკარი, რომელიც ჯერ წიგნს პოულობს და მერე გპასუხობთ).</li>
                <li><strong>Semantic Search (სემანტიკური ძიება):</strong> ინფორმაციის მოძიება შინაარსის და არა მხოლოდ ზუსტი სიტყვების მიხედვით. "ძაღლი" და "dog" აღიქმება ერთნაირად.</li>
                <li><strong>ვექტორული ბაზები (Vector DB):</strong> ტექსტი გარდაიქმნება რიცხვებად (Embeddings) და ინახება ისე, რომ AI-მ სწრაფად იპოვოს მსგავსი კონტექსტი.</li>
            </ul>
        </div>

        <h2>2️⃣ ნაწილი 2: Autonomous Agents და ReAct Framework</h2>
        <div class="section-summary">
            <h3>Assistant VS Agent</h3>
            <p>ასისტენტი ელოდება თქვენს კითხვას, აგენტი კი - დამოუკიდებლად იღებს გადაწყვეტილებებს და იყენებს ინსტრუმენტებს (Tools) მიზნის მისაღწევად.</p>
            
            <h3>ReAct (Reasoning + Action)</h3>
            <p>აგენტის აზროვნების ციკლი შედგება 3 ნაბიჯისგან:</p>
            <ol>
                <li><strong>Reasoning:</strong> აგენტი ფიქრობს რა უნდა გააკეთოს ("მჭირდება ინფორმაცია ამინდზე").</li>
                <li><strong>Action:</strong> იყენებს კონკრეტულ Tool-ს ("ვრთავ API-ს").</li>
                <li><strong>Observation:</strong> იღებს და აანალიზებს შედეგს ("წვიმს"). ამის მერე წყვეტს, დაასრულოს თუ ხელახლა იფიქროს.</li>
            </ol>
        </div>

        <h2>3️⃣ ნაწილი 3: Model Context Protocol (MCP)</h2>
        <div class="section-summary">
            <h3>ახალი სტანდარტი სისტემების დასაკავშირებლად</h3>
            <p>ადრე, API-ების დასაკავშირებლად გვიწევდა რთული კოდის წერა ყოველი ახალი სერვისისთვის. <strong>MCP</strong> არის ახალი ღია სტანდარტი (შექმნილი Anthropic-ის მიერ), რომელიც საშუალებას აძლევს AI-ს პირდაპირ, უსაფრთხოდ დაუკავშირდეს თქვენს ლოკალურ ფაილებს, მონაცემთა ბაზებს და სერვისებს (Google Drive, Github, Slack).</p>
            <p><strong>მთავარი უპირატესობა:</strong> მონაცემები არსად არ იტვირთება (Zero-leakage). AI თავად მოდის მონაცემებთან.</p>
        </div>
"""

# ---------------------------------------------------------
# 2. STUDY GUIDE
# ---------------------------------------------------------
study_guide_content = """
        <h1>📖 სასწავლო გზამკვლევი: ლექცია 2</h1>

        <div class="info-box" style="background: #e8f5e9; border-left: 5px solid #4caf50; padding: 1.5rem; margin-bottom: 2rem;">
            <p><strong>როგორ გამოვიყენოთ ეს გზამკვლევი?</strong> ეს დოკუმენტი დაგეხმარებათ ლექციაზე მიღებული ცოდნის სტრუქტურირებაში და წარმოადგენს მთავარ თეორიულ სახელმძღვანელოს ფინალური პროექტისთვის მოსამზადებლად.</p>
        </div>

        <h2>1. კონცეპტუალური ტრანზიცია (The Paradigm Shift)</h2>
        <p>ჩვენი კურსის მთავარი მიზანია Prompt Engineer-იდან გადავიქცეთ <strong>AI Automation Architect</strong>-ად. ამისთვის მნიშვნელოვანია გვესმოდეს შემდეგი ტერმინები:</p>
        
        <table style="margin-top: 1rem;">
            <tr>
                <th>ტერმინი</th>
                <th>განმარტება</th>
            </tr>
            <tr>
                <td><strong>Knowledge Base (ცოდნის ბაზა)</strong></td>
                <td>თქვენი ბიზნესის სპეციფიკური დოკუმენტები, რომელსაც AI იყენებს სწორი კონტექსტის შესაქმნელად.</td>
            </tr>
            <tr>
                <td><strong>JSON (JavaScript Object Notation)</strong></td>
                <td>მონაცემთა გაცვლის უნივერსალური ფორმატი. სისტემები (მაგ. n8n) ერთმანეთს ესაუბრებიან JSON ენით.</td>
            </tr>
            <tr>
                <td><strong>Embeddings</strong></td>
                <td>ტექსტის, სურათის ან აუდიოს მათემატიკური (რიცხვითი) წარმოდგენა, რომელსაც AI კითხულობს.</td>
            </tr>
            <tr>
                <td><strong>Model Context Protocol (MCP)</strong></td>
                <td>ახალი პროტოკოლი, რომელიც AI აგენტებს აძლევს ლოკალურ სერვერებზე წვდომის საშუალებას ფაილების Cloud-ში ატვირთვის გარეშე.</td>
            </tr>
        </table>

        <h2>2. RAG სისტემის ანატომია</h2>
        <div class="highlight-box">
            <h3>რა ხდება კულისებში, როცა AI-ს თქვენს დოკუმენტზე ეკითხებით?</h3>
            <p>1. თქვენ ატვირთავთ 100 გვერდიან PDF დოკუმენტს.</p>
            <p>2. სისტემა ჭრის მას პატარა ნაწილებად (Chunks).</p>
            <p>3. თითოეულ ნაწილს გარდაქმნის ვექტორად (Embeddings) და ინახავს ვექტორულ ბაზაში.</p>
            <p>4. როცა სვამთ კითხვას, თქვენი კითხვაც გარდაიქმნება ვექტორად.</p>
            <p>5. სისტემა ადარებს რიცხვებს და პოულობს ყველაზე რელევანტურ პასუხს (Semantic Search).</p>
            <p>6. LLM კითხულობს ამ ამოღებულ ტექსტს და აგენერირებს ლამაზ, ადამიანურ პასუხს.</p>
        </div>

        <h2>3. ReAct: როგორ ვაზროვნებინოთ აგენტს?</h2>
        <p>AI აგენტი არ არის უბრალოდ ჩატბოტი. ის არის სისტემა, რომელსაც შეუძლია შეასრულოს დავალება. ReAct (Reasoning + Acting) Framework-ის მიხედვით:</p>
        <ul>
            <li><strong>Reasoning:</strong> მიზნის გააზრება და დაგეგმვა. (<em>"უნდა ვიპოვო კლიენტის ტელეფონის ნომერი"</em>).</li>
            <li><strong>Action:</strong> ხელსაწყოს გამოყენება. (<em>"ვრთავ CRM API-ს"</em>).</li>
            <li><strong>Observation:</strong> შედეგის მიღება. (<em>"CRM-მა დააბრუნა ნომერი"</em>).</li>
        </ul>
        <p>ეს ციკლი გრძელდება მანამ, სანამ აგენტი არ მიაღწევს საბოლოო მიზანს.</p>

        <h2>4. Model Context Protocol (MCP) - ახალი ერა (2026)</h2>
        <p>MCP არის რევოლუციური. თუ ადრე გვიწევდა რთული OAuth და API დაკავშირება ყოველი სერვისისთვის, დღეს Claude Desktop App-ს შეუძლია პირდაპირ დაუკავშირდეს თქვენს კომპიუტერს.</p>
        <ul>
            <li>MCP არ ტვირთავს თქვენს ლოკალურ ფაილებს Cloud-ში.</li>
            <li>ის საშუალებას აძლევს Claude-ს "დაინახოს" თქვენი ლოკალური ფაილური სისტემა, მონაცემთა ბაზები და GitHub რეპოზიტორები.</li>
            <li>ეს ხდის AI აგენტებს 100%-ით უსაფრთხოს Enterprise დონის კომპანიებისთვის (Zero-Leakage Policy).</li>
        </ul>
"""

# ---------------------------------------------------------
# 3. QUICK REF (CHEAT SHEET)
# ---------------------------------------------------------
quick_ref_content = """
        <h1>📋 სწრაფი ცნობარი (Cheat Sheet): ლექცია 2</h1>

        <div class="key-points">
            <h3>Assistant VS Agent (სწრაფი შედარება)</h3>
            <table>
                <tr>
                    <th>თვისება</th>
                    <th>Assistant (ChatGPT/Claude)</th>
                    <th>Agent (AutoGPT/Custom Agent)</th>
                </tr>
                <tr>
                    <td><strong>ინიციატივა</strong></td>
                    <td>რეაქტიული (ელოდება თქვენს ბრძანებას)</td>
                    <td>პროაქტიული (მოქმედებს მიზნისკენ)</td>
                </tr>
                <tr>
                    <td><strong>Tools (ხელსაწყოები)</strong></td>
                    <td>შეზღუდული (მხოლოდ რაც აქვს ჩაშენებული)</td>
                    <td>შეუძლია გარე API-ების და ლოკალური სერვისების ჩართვა</td>
                </tr>
                <tr>
                    <td><strong>Workflows</strong></td>
                    <td>ერთი კითხვა - ერთი პასუხი</td>
                    <td>მრავალეტაპიანი, დამოუკიდებელი დაგეგმვა</td>
                </tr>
            </table>
        </div>

        <div class="highlight-box">
            <h3>📝 JSON ფორმატის შაბლონი (ყველაზე მნიშვნელოვანი სტრუქტურა)</h3>
            <p>JSON (JavaScript Object Notation) არის გასაღები ნებისმიერი ავტომატიზაციის პლატფორმისთვის (Make.com, n8n).</p>
            <div class="code-block">
{
  "client": {
    "first_name": "გიორგი",
    "last_name": "მაისურაძე",
    "email": "giorgi@example.com"
  },
  "request": "მჭირდება ფასდაკლება 20%",
  "status": "pending",
  "priority": 1
}
            </div>
            <p><strong>წესი 1:</strong> Keys (გასაღებები) ყოველთვის ბრჭყალებშია (<code>"email"</code>).</p>
            <p><strong>წესი 2:</strong> ფიგურული ფრჩხილები <code>{}</code> ქმნიან ობიექტს.</p>
        </div>

        <div class="warning-box">
            <h3>🧠 ReAct Loop-ის 3 ოქროს წესი</h3>
            <ol>
                <li>ყოველთვის მიეცით აგენტს მკაფიო <strong>პერსონა და მიზანი</strong>.</li>
                <li>აღუწერეთ ხელსაწყოები (Tools) ძალიან დეტალურად, რათა აგენტმა იცოდეს, <strong>როდის რომელი გამოიყენოს</strong>.</li>
                <li>დაუტოვეთ <strong>Fallback</strong> (ალტერნატიული გზა), თუ რომელიმე Action შეცდომით დასრულდა (Error Handling).</li>
            </ol>
        </div>

        <div class="info-box" style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #2196f3; margin: 1.5rem 0;">
            <h3>🔌 MCP (Model Context Protocol) ლოგიკა</h3>
            <p>MCP კავშირის დასამყარებლად საჭიროა 3 კომპონენტი:</p>
            <ol>
                <li><strong>MCP Host:</strong> მაგალითად Claude Desktop აპლიკაცია, რომელიც ითხოვს ინფორმაციას.</li>
                <li><strong>MCP Client:</strong> პროტოკოლი, რომელიც უზრუნველყოფს უსაფრთხო ლოკალურ კავშირს.</li>
                <li><strong>MCP Server:</strong> ლოკალური პროგრამა (მაგ. ფაილური სისტემის წამკითხველი ან SQL ბაზა), რომელიც გასცემს მონაცემებს.</li>
            </ol>
        </div>
"""

# ---------------------------------------------------------
# 4. EXERCISES
# ---------------------------------------------------------
exercises_content = """
        <h1>💪 სავარჯიშოები: ლექცია 2 (Agents & RAG)</h1>

        <div class="info-box">
            <p><strong>ინსტრუქცია:</strong> ეს სავარჯიშოები შექმნილია იმისთვის, რომ თქვენი თეორიული ცოდნა პრაქტიკულ უნარებად აქციოს. დაასრულეთ სამივე დავალება დამოუკიდებლად.</p>
        </div>

        <div class="section-summary">
            <h3>დავალება 1: Claude Project-ის შექმნა (Knowledge Base-ით)</h3>
            <p><strong>მიზანი:</strong> შექმენით მორგებული ასისტენტი კონკრეტული ბიზნეს-დავალებისთვის.</p>
            <ol>
                <li>შედით Claude.ai-ზე და შექმენით ახალი "Project".</li>
                <li>დაარქვით პროექტს: <em>"HR Policy Assistant"</em>.</li>
                <li>ატვირთეთ ნებისმიერი შიდა წესდების (ან მოგონილი დოკუმენტის) PDF ფაილი Project Knowledge-ში.</li>
                <li><strong>Custom Instructions-ში ჩაწერეთ:</strong> <br>
                <em>"შენ ხარ კომპანიის HR ასისტენტი. შენი მიზანია თანამშრომლებს გასცე პასუხები მხოლოდ ატვირთული დოკუმენტის მიხედვით. თუ კითხვა სცდება დოკუმენტს, მოიბოდიშე და უთხარი, რომ ინფორმაცია არ გაქვს."</em></li>
                <li>დაუსვით ასისტენტს 1 რელევანტური და 1 არარელევანტური (ტრიუკური) კითხვა. დააკვირდით, როგორ იცავს წესებს.</li>
            </ol>
        </div>

        <div class="section-summary">
            <h3>დავალება 2: JSON სტრუქტურის აწყობა</h3>
            <p><strong>მიზანი:</strong> გადაიყვანეთ ადამიანური ტექსტი სისტემურ (JSON) ენაზე.</p>
            <p><strong>მოცემულობა:</strong> კლიენტმა მოგწერათ ელ.ფოსტაზე: <br><em>"გამარჯობა, მე ვარ ნინო ბერიძე. ჩემი შეკვეთის ნომერია #4599. სამწუხაროდ პროდუქტი დაზიანებული ჩამოვიდა და მინდა თანხის დაბრუნება. დამიკავშირდით ნომერზე 555-12-34-56."</em></p>
            <p><strong>თქვენი ამოცანაა:</strong> დაწერეთ ამ ტექსტის შესაბამისი JSON ობიექტი, რომელიც შეიცავს შემდეგ გასაღებებს (Keys): <code>customer_name</code>, <code>order_id</code>, <code>issue_type</code>, <code>phone_number</code>.</p>
            <details style="margin-top: 1rem; cursor: pointer;">
                <summary><strong>💡 დააკლიკეთ პასუხის სანახავად</strong></summary>
                <div class="code-block" style="margin-top: 0.5rem;">
{
  "customer_name": "ნინო ბერიძე",
  "order_id": "#4599",
  "issue_type": "refund_damaged_item",
  "phone_number": "555-12-34-56"
}
                </div>
            </details>
        </div>

        <div class="section-summary">
            <h3>დავალება 3: ReAct (Reasoning + Action) ციკლის სიმულაცია</h3>
            <p><strong>მიზანი:</strong> გაიაზრეთ, როგორ ფიქრობს აგენტი ავტონომიურად.</p>
            <p><strong>სიტუაცია:</strong> თქვენი აგენტი ჩართულია E-commerce პლატფორმაზე და აქვს 2 Tool: <br>
            1) <code>check_inventory(product_name)</code> <br>
            2) <code>send_email(customer, message)</code>.</p>
            <p><strong>კლიენტის კითხვა:</strong> "მაქვს თუ არა შანსი შევიძინო iPhone 15 Pro, თუ ახლავე გამოვიწერ?"</p>
            <p><strong>თქვენი ამოცანაა:</strong> ფურცელზე ან Text ფაილში ჩამოწერეთ ReAct ციკლის ნაბიჯები (Reasoning ➔ Action ➔ Observation ➔ Action), სანამ აგენტი საბოლოო პასუხს არ გასცემს კლიენტს.</p>
        </div>
"""

# Write all files
import os
base_path = r"c:\Users\GBASILAIA\claude\make"

files = {
    "lecture-2-summary.html": ("ლექცია 2: შეჯამება", summary_content),
    "lecture-2-study-guide.html": ("ლექცია 2: სასწავლო გზამკვლევი", study_guide_content),
    "lecture-2-quick-ref.html": ("ლექცია 2: სწრაფი ცნობარი", quick_ref_content),
    "lecture-2-exercises.html": ("ლექცია 2: სავარჯიშოები", exercises_content)
}

for filename, (title, content) in files.items():
    file_path = os.path.join(base_path, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(generate_html(title, filename, content))
    print(f"Generated {filename}")

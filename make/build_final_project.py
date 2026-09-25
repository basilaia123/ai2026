import os

html_content = """<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Final Project: Enterprise AI Automation System</title>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet"/>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'FiraGO', sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
            padding: 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        header {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
            color: white;
            padding: 2.5rem;
            text-align: center;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        header h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .meta-info {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 1rem;
            flex-wrap: wrap;
        }

        .meta-item {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            background: rgba(255,255,255,0.2);
            padding: 0.5rem 1rem;
            border-radius: 20px;
        }

        .points-badge {
            background: #ffd700;
            color: #000;
            padding: 0.7rem 2rem;
            border-radius: 30px;
            font-weight: 700;
            font-size: 1.5rem;
            display: inline-block;
            margin-top: 1rem;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        nav.nav-links {
            background: white;
            padding: 1rem;
            border-radius: 8px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
        }

        nav.nav-links a {
            text-decoration: none;
            color: #ff6b6b;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            transition: all 0.3s;
            font-weight: 500;
        }

        nav.nav-links a:hover {
            background: #ff6b6b;
            color: white;
        }

        .content-box {
            background: white;
            padding: 2rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }

        .content-box h2 {
            color: #2c3e50;
            margin-bottom: 1rem;
            font-size: 1.8rem;
            border-bottom: 3px solid #ff6b6b;
            padding-bottom: 0.5rem;
        }

        .content-box h3 {
            color: #ff6b6b;
            margin: 1.5rem 0 1rem 0;
            font-size: 1.4rem;
        }

        .content-box h4 {
            color: #495057;
            margin: 1rem 0 0.5rem 0;
            font-size: 1.1rem;
        }

        .content-box p {
            margin-bottom: 1rem;
            font-size: 1.05rem;
        }

        .content-box ul, .content-box ol {
            margin: 1rem 0 1rem 2rem;
        }

        .content-box li {
            margin-bottom: 0.5rem;
        }

        .info-box {
            background: #e3f2fd;
            border-left: 4px solid #2196f3;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-radius: 5px;
        }

        .warning-box {
            background: #fff3e0;
            border-left: 4px solid #ff9800;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-radius: 5px;
        }

        .success-box {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 1.5rem;
            margin: 1.5rem 0;
            border-radius: 5px;
        }

        .highlight-box {
            background: linear-gradient(135deg, #fff9e6 0%, #ffe6cc 100%);
            border: 3px solid #ffa500;
            padding: 2rem;
            margin: 2rem 0;
            border-radius: 10px;
        }

        .project-option {
            background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%);
            border: 2px solid #9c27b0;
            padding: 2rem;
            margin: 1.5rem 0;
            border-radius: 10px;
        }

        .project-option h3 {
            color: #6a1b9a;
            margin-top: 0;
        }

        .component-card {
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 1.5rem;
            margin: 1rem 0;
            border-radius: 5px;
        }

        .timeline {
            margin: 2rem 0;
        }

        .timeline-item {
            padding-left: 2rem;
            border-left: 4px solid #ff6b6b;
            margin-bottom: 2rem;
            position: relative;
        }

        .timeline-item::before {
            content: '📅';
            position: absolute;
            left: -1.2rem;
            background: white;
            padding: 0.2rem;
            font-size: 1.5rem;
        }

        .timeline-item h4 {
            color: #ff6b6b;
            margin-bottom: 0.5rem;
        }

        .checklist {
            background: #f8f9fa;
            border: 2px solid #dee2e6;
            padding: 1.5rem;
            border-radius: 8px;
            margin: 1rem 0;
        }

        .checklist li {
            padding: 0.5rem 0;
            border-bottom: 1px solid #e9ecef;
        }

        .checklist li:last-child {
            border-bottom: none;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.5rem 0;
            background: white;
        }

        table th {
            background: #ff6b6b;
            color: white;
            padding: 1rem;
            text-align: left;
            font-weight: 600;
        }

        table td {
            padding: 1rem;
            border-bottom: 1px solid #dee2e6;
        }

        table tr:hover {
            background: #f8f9fa;
        }

        .grading-table th {
            background: #28a745;
        }

        .requirements-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin: 2rem 0;
        }

        .requirement-card {
            background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%);
            border: 2px solid #4caf50;
            padding: 1.5rem;
            border-radius: 8px;
        }

        .requirement-card h4 {
            color: #2e7d32;
            margin-top: 0;
        }

        @media (max-width: 768px) {
            header h1 {
                font-size: 1.8rem;
            }
            .meta-info {
                flex-direction: column;
                gap: 0.5rem;
            }
            .content-box {
                padding: 1.5rem;
            }
            .content-box h2 {
                font-size: 1.5rem;
            }
            .requirements-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <h1>🎓 Final Project: Enterprise AI Automation System</h1>
        <p>Capstone Project - თქვენი პირველი B2B პორტფოლიო</p>
        <div class="meta-info">
            <div class="meta-item">
                <span>📅</span>
                <span>Deadline: ლექცია 6 (ფიზიკური ვორქშოპი)</span>
            </div>
            <div class="meta-item">
                <span>⏱️</span>
                <span>პრეზენტაცია (Pitch): მკაცრი 10 წუთი</span>
            </div>
        </div>
        <div class="points-badge">🏆 სერტიფიკატის მთავარი მოთხოვნა</div>
    </header>

    <nav class="nav-links">
        <a href="index.html">🏠 მთავარი</a>
        <a href="lecture-4-slides.html">📊 ლექცია 4</a>
        <a href="lecture-5-slides.html">📊 ლექცია 5</a>
        <a href="lecture-6-slides.html">🎓 ლექცია 6 (Workshop)</a>
    </nav>

    <div class="content-box">
        <h2>🎯 პროექტის მიზანი</h2>
        <p>ფინალური პროექტი წარმოადგენს 6 კვირიანი ინტენსიური სწავლების შეჯამებას, სადაც თქვენ დაამტკიცებთ, რომ შეგიძლიათ დამოუკიდებლად დაგეგმოთ, ააწყოთ და ბიზნესს მიჰყიდოთ <strong>Production-Ready AI სისტემა</strong>.</p>
        
        <div class="highlight-box">
            <h3 style="color: #e65100; margin-top: 0;">🌟 ეს არის თქვენი Portfolio Piece!</h3>
            <p style="font-size: 1.1rem;">კურსის შემდეგ თქვენ ამ პროექტს გადაიტანთ პირდაპირ LinkedIn-სა და თქვენს პირად პორტფოლიოში. ეს პროექტი აჩვენებს დამსაქმებლებსა და კლიენტებს, რომ თქვენ ხართ <strong>AI Automation Architect</strong>.</p>
        </div>

        <div class="info-box">
            <p><strong>💡 რა უნდა შექმნათ:</strong> End-to-end (მრავალეტაპიანი) ავტომატიზაციის სისტემა Make.com-ზე ან n8n-ზე, რომელიც ჭრის კონკრეტულ <strong>ბიზნეს პრობლემას</strong>, იყენებს მინიმუმ ერთ <strong>AI აგენტს/მოდელს</strong>, იყენებს გარე API ინტეგრაციებს და აქვს დათვლილი <strong>ROI (ფინანსური უკუგება)</strong>.</p>
        </div>
    </div>

    <div class="content-box">
        <h2>✅ სავალდებულო მოთხოვნები (4 Pillars)</h2>
        <div class="requirements-grid">
            <div class="requirement-card">
                <h4>1. ორკესტრაციის პლატფორმა ⚙️</h4>
                <p>სისტემა აწყობილი უნდა იყოს Make.com-ზე ან n8n-ზე. უნდა შეიცავდეს მინიმუმ 1 Router-ს და IF პირობით ლოგიკას, რათა აჩვენოს რთული გადაწყვეტილების მიღება.</p>
            </div>
            <div class="requirement-card">
                <h4>2. AI ინტეგრაცია 🧠</h4>
                <p>ავტომატიზაციაში ჩართული უნდა იყოს მინიმუმ 1 AI მოდელი (OpenAI, Anthropic Claude, ან ლოკალური Llama/Ollama). მოდელმა უნდა შეასრულოს არა მხოლოდ თარგმნა, არამედ ანალიტიკა, მონაცემთა ექსტრაქცია ან მსჯელობა (Reasoning).</p>
            </div>
            <div class="requirement-card">
                <h4>3. გარე სისტემებთან კავშირი 🔌</h4>
                <p>პროცესი უნდა იწყებოდეს (Trigger) ან სრულდებოდეს გარე სისტემაში API-ის ან Webhook-ის გავლით. (მაგ. Google Sheets ბაზა, Telegram/Slack ნოტიფიკაცია, CRM ინტეგრაცია).</p>
            </div>
            <div class="requirement-card">
                <h4>4. ROI-ის დათვლა 💰</h4>
                <p>სავალდებულოა ბოლო სლაიდზე გქონდეთ დათვლილი ფინანსური სარგებელი. რამდენი საათი დაზოგა სისტემამ თვეში? რამდენი დოლარი დაეზოგა კომპანიას ადამიანური რესურსის ხარჯზე?</p>
            </div>
        </div>
    </div>

    <div class="content-box">
        <h2>📋 პროექტის თემები (იდეები ინსპირაციისთვის)</h2>
        <p>შეგიძლიათ აირჩიოთ ერთ-ერთი ქვემოთ ჩამოთვლილი ვარიანტი, ან შემოგვთავაზოთ თქვენი უნიკალური იდეა თქვენი ბიზნეს-საჭიროებიდან გამომდინარე.</p>

        <div class="project-option">
            <h3>Option 1: B2B ტექსტური მხარდაჭერის ავტომატიზაცია (Customer Support) 🎧</h3>
            <p><strong>პრობლემა:</strong> კომპანია დღეში 100-ზე მეტ იდენტურ ელ.ფოსტას/მესიჯს იღებს და პასუხზე იხარჯება 4-5 საათი.</p>
            <p><strong>გამოსავალი:</strong></p>
            <ul>
                <li><strong>Trigger:</strong> შემოსული ელ.ფოსტა ან Telegram მესიჯი.</li>
                <li><strong>Action (Make.com/n8n):</strong> ტექსტის გაგზავნა Claude ან GPT მოდელთან. მოდელი ადგენს, არის თუ არა კითხვა სტანდარტული.</li>
                <li><strong>Router:</strong> თუ სტანდარტულია, AI თავად აგენერირებს პასუხს RAG-ის (კომპანიის ბაზის) გამოყენებით. თუ რთულია, აგზავნის Slack-ში მენეჯერთან (Human-in-the-Loop).</li>
                <li><strong>Database:</strong> ყველა ქეისი ინახება Google Sheets-ში Analytics-თვის.</li>
            </ul>
        </div>

        <div class="project-option">
            <h3>Option 2: დოკუმენტების დანერგვის კონვეიერი (Vision AI) 📄</h3>
            <p><strong>პრობლემა:</strong> ბუღალტერიას დღეში 50-მდე ინვოისის (PDF ან სურათი) ხელით შეყვანა უწევს ERP სისტემაში.</p>
            <p><strong>გამოსავალი:</strong></p>
            <ul>
                <li><strong>Trigger:</strong> ახალი ფაილის ატვირთვა Google Drive-ის კონკრეტულ ფოლდერში.</li>
                <li><strong>Action (Make.com/n8n):</strong> ფაილის გაგზავნა OpenAI Vision ან Claude API-ში, რათა ავტომატურად მოხდეს კომპანიის სახელის, თანხისა და თარიღის ამოღება JSON ფორმატში.</li>
                <li><strong>Database:</strong> ამოღებული მონაცემები სუფთად იწერება ბაზაში.</li>
                <li><strong>Notification:</strong> წარმატებული ინვოისების რეპორტი მოდის Telegram-ში.</li>
            </ul>
        </div>

        <div class="project-option">
            <h3>Option 3: Deep Research / Lead Generation ავტომატიზაცია 🔍</h3>
            <p><strong>პრობლემა:</strong> გაყიდვების გუნდი საათებს კარგავს პოტენციური კლიენტების (Leads) ვებ-გვერდების კითხვასა და ანალიზში.</p>
            <p><strong>გამოსავალი:</strong></p>
            <ul>
                <li><strong>Trigger:</strong> ვებ-გვერდის URL-ის ჩაგდება Google Sheets-ში.</li>
                <li><strong>Action (n8n + Firecrawl):</strong> აგენტი შედის ვებ-გვერდზე, კითხულობს კონტენტს. LLM აანალიზებს, არის თუ არა ეს კომპანია თქვენი პოტენციური კლიენტი.</li>
                <li><strong>Output:</strong> სისტემა თავად წერს პერსონალიზებულ Pitch ელ.ფოსტას და ინახავს Draft ფორმატში გასაგზავნად.</li>
            </ul>
        </div>

        <div class="project-option">
            <h3>Option 4: 100% Zero-Leakage (Local LLM) ბიზნეს ავტომატიზაცია 🔒</h3>
            <p><strong>პრობლემა:</strong> კომპანიას აქვს იურიდიული შეზღუდვები მონაცემთა უსაფრთხოებაზე (GDPR) და ვერ იყენებს OpenAI-ს (Cloud) API-ს კლიენტების მონაცემებზე.</p>
            <p><strong>გამოსავალი:</strong></p>
            <ul>
                <li><strong>Trigger:</strong> ლოკალური ფაილის ატვირთვა.</li>
                <li><strong>Action (n8n + Ollama):</strong> ლოკალურად გაშვებული Llama 3 ან DeepSeek მოდელი ამუშავებს ტექსტს (მაგ. აკეთებს კონტრაქტის ანალიზს) ისე, რომ მონაცემები არ ტოვებს კომპანიის სერვერს.</li>
                <li><strong>Output:</strong> უსაფრთხო რეპორტის გენერაცია.</li>
            </ul>
        </div>
    </div>

    <div class="content-box">
        <h2>🎤 პრეზენტაციის (Pitch) სტრუქტურა - 10 წუთი</h2>
        <div class="warning-box">
            <p><strong>მნიშვნელოვანია:</strong> მე-6 ლექციაზე თქვენ გექნებათ <strong>მკაცრი 10-წუთიანი ფანჯარა</strong>. წარმოიდგინეთ, რომ ეს არის Startup Pitch ინვესტორებთან.</p>
        </div>
        <table class="grading-table">
            <tr>
                <th style="width: 20%;">დრო</th>
                <th>ეტაპი</th>
                <th>რას ვაკეთებთ?</th>
            </tr>
            <tr>
                <td><strong>1 წუთი</strong></td>
                <td>პრობლემის იდენტიფიკაცია</td>
                <td>რა ბიზნეს პრობლემას ჭრით? რატომ იხარჯებოდა აქამდე ზედმეტი დრო?</td>
            </tr>
            <tr>
                <td><strong>2 წუთი</strong></td>
                <td>არქიტექტურა</td>
                <td>აჩვენეთ n8n ან Make.com-ის ეკრანი (ნოდები, მარშრუტები, API კავშირები). ახსენით AI-ის როლი.</td>
            </tr>
            <tr>
                <td><strong>4 წუთი</strong></td>
                <td>⚡ Live Demo</td>
                <td>გაუშვით სისტემა რეალურ დროში და აჩვენეთ აუდიტორიას, როგორ სრულდება დავალება.</td>
            </tr>
            <tr>
                <td><strong>1 წუთი</strong></td>
                <td>ROI-ის პრეზენტაცია</td>
                <td>ფინანსური ნაწილი: რამდენი საათი ან დოლარი დაიზოგება თვეში ამ სისტემით? (Cost vs Benefit).</td>
            </tr>
            <tr>
                <td><strong>2 წუთი</strong></td>
                <td>Q&A</td>
                <td>კითხვები აუდიტორიიდან და ლექტორის ფიდბექი.</td>
            </tr>
        </table>
    </div>

    <div class="content-box">
        <h2>🚀 Next Steps - დაიწყეთ დღესვე!</h2>
        <div class="checklist">
            <ul>
                <li>👉 <strong>ლექცია 4-ის მერე:</strong> მოიფიქრეთ ბიზნეს-პრობლემა და შეარჩიეთ ერთი Option.</li>
                <li>👉 <strong>ლექცია 5-ის მერე:</strong> ააწყვეთ ლოგიკა, დატესტეთ API-ები და დაიანგარიშეთ ROI.</li>
                <li>👉 <strong>ლექცია 6-მდე (1 დღით ადრე):</strong> მოამზადეთ მოკლე პრეზენტაცია და დარწმუნდით, რომ Live Demo უშეცდომოდ მუშაობს.</li>
            </ul>
        </div>
        <div class="success-box" style="text-align: center; margin-top: 3rem;">
            <h2 style="color: #2e7d32; font-size: 2rem;">გელოდებით მე-6 ლექციაზე!</h2>
            <p>ეს არის თქვენი შანსი, დატოვოთ თეორია უკან და აჩვენოთ რეალური, ხელშესახები ღირებულება.</p>
        </div>
    </div>
</div>

</body>
</html>
"""

fpath = r"c:\Users\GBASILAIA\claude\make\final-project.html"
with open(fpath, "w", encoding="utf-8") as f:
    f.write(html_content)

print("final-project.html has been successfully rebuilt with 2026 Enterprise requirements!")

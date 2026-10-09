# -*- coding: utf-8 -*-
import sys
import re
import json

sys.stdout.reconfigure(encoding='utf-8')

slides = [
    # SLIDE 1
    {
        "module": "შესავალი",
        "pill": "🟢 დღე 1: Onsite Bootcamp",
        "pillClass": "green",
        "timing": "11:00 - 17:30",
        "title": "ხელოვნური ინტელექტი სამოქალაქო სექტორისთვის",
        "subtitle": "საგრანტო ციკლი, ლოგიკური ჩარჩოები (Logframe) & პროექტების მართვა (Notion AI)",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 Post-Course Playbook</span>
            <span>ეს კურსი მოიცავს 10 პრაქტიკულ სამაგიდო გაიდსა და SOP-ს, რომლებიც რჩება თქვენს მუდმივ მფლობელობაში ტრენინგის შემდეგ დამოუკიდებელი მუშაობისთვის!</span>
          </div>

          <div class="grid-2col" style="margin-top: 10px;">
            <div class="card-box" style="justify-content: center; background: linear-gradient(135deg, rgba(0, 90, 156, 0.04) 0%, rgba(16, 185, 129, 0.04) 100%);">
              <div style="font-size: 0.82rem; font-weight: 800; color: var(--brand-blue); text-transform: uppercase; margin-bottom: 8px;">🇪🇺 🇺🇳 EU4Dialogue ინიციატივა</div>
              <h3 style="font-size: 1.35rem; font-weight: 900; line-height: 1.3; margin-bottom: 12px;">ინტენსიური პრაქტიკული ბუთქემფი არასამთავრობო ორგანიზაციებისთვის</h3>
              <p style="font-size: 0.9rem; color: var(--text-muted); line-height: 1.6;">
                ნულიდან პროფესიონალურ დონემდე (Zero-to-Hero): როგორ გამოვიყენოთ 2026 წლის Frontier მოდელები, Miro AI, Gamma AI და Notion AI საგრანტო ადმინისტრირების 60-80%-ით შესამცირებლად.
              </p>
              <div style="display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px;">
                <span class="slide-pill green">✓ 100% Hands-on</span>
                <span class="slide-pill blue">✓ EU/UNDP სტანდარტები</span>
                <span class="slide-pill purple">✓ 10 სამაგიდო გაიდი</span>
              </div>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">👨‍🏫</span>
                <div>
                  <div class="card-title">ტრენერი & პროგრამის წამყვანი</div>
                  <div style="font-size: 0.8rem; color: var(--text-muted);">აკადემიური და საერთაშორისო ექსპერტიზა</div>
                </div>
              </div>
              <ul class="bullet-list">
                <li><strong>გიორგი ბასილაია, PhD:</strong> AI პრაქტიკოსი, Smart Academy-ის წამყვანი ლექტორი.</li>
                <li><strong>საერთაშორისო დონორული გამოცდილება:</strong> EU, UNDP, USAID, NATO & World Bank პროექტები.</li>
                <li><strong>კიბერუსაფრთხოება & მონაცემთა ეთიკა:</strong> ISC2 Certified, Do No Harm პრინციპების სრული დაცვა.</li>
                <li><strong>სამეცნიერო რეპუტაცია:</strong> ~2,200 საერთაშორისო ციტირება Scopus/Google Scholar-ში.</li>
              </ul>
              <div class="callout-box green" style="margin-bottom: 0;">
                💡 <strong>დღის მიზანი:</strong> დღის ბოლოს თითოეულ მონაწილეს ექნება საკუთარი პროექტის მზა Logframe, Theory of Change, რისკ-მატრიცა, Gamma პრეზენტაცია და გამართული Notion AI სამუშაო სივრცე.
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 2
    {
        "module": "დღის გეგმა",
        "pill": "სტრუქტურა & განრიგი",
        "pillClass": "blue",
        "timing": "11:00 - 17:30 (5.0 სთ აქტიური სწავლება)",
        "title": "პირველი დღის საათობრივი მარშრუტი (Roadmap)",
        "subtitle": "4 კონცენტრირებული პრაქტიკული მოდული, 10 პოსტ-კურს გაიდი, 2 ყავის შესვენება და ქსელური ლანჩი",
        "content": """
          <div class="grid-4col">
            <div class="card-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--brand-blue); margin-bottom: 4px;">მოდული 01 • 11:00 - 12:15</div>
              <h4 style="font-size: 0.98rem; font-weight: 900; margin-bottom: 8px;">AI Fundamentals & Arena.ai</h4>
              <p class="card-desc">2026 Frontier მოდელები (Claude, GPT, Gemini), LMSYS Arena უფასო წვდომა, CLEAR & PARTS პრომპტინგი, Slido #1 და 2 სამაგიდო გაიდი.</p>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.76rem; font-weight: 700; color: var(--pm-emerald);">📘 გაიდები: Arena 0-ხარჯი & Prompt Cheat Sheet</div>
            </div>

            <div class="card-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--pm-emerald); margin-bottom: 4px;">მოდული 02 • 12:30 - 13:45</div>
              <h4 style="font-size: 0.98rem; font-weight: 900; margin-bottom: 8px;">Logframe & Theory of Change</h4>
              <p class="card-desc">EU/UNDP ლოგიკური ჩარჩო, ToC მიზეზ-შედეგობრივი ჯაჭვი, Miro AI SCAMPER ბრეინშტორმინგი და 2 სამაგიდო გაიდი.</p>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.76rem; font-weight: 700; color: var(--pm-emerald);">📘 გაიდები: 5-ეტაპიანი Logframe SOP & ToC ვალიდაცია</div>
            </div>

            <div class="card-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--accent-purple); margin-bottom: 4px;">მოდული 03 • 14:45 - 16:00</div>
              <h4 style="font-size: 0.98rem; font-weight: 900; margin-bottom: 8px;">ინდიკატორები, რისკები & Gamma</h4>
              <p class="card-desc">SMART ინდიკატორები & MoV, რისკების 5x5 მატრიცა, Do No Harm, Gamma 3.0 Pitch Decks და 3 სამაგიდო გაიდი.</p>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.76rem; font-weight: 700; color: var(--pm-emerald);">📘 გაიდები: SMART აუდიტი, რისკ-მატრიცა & Gamma Pitch</div>
            </div>

            <div class="card-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--accent-amber); margin-bottom: 4px;">მოდული 04 • 16:15 - 17:30</div>
              <h4 style="font-size: 0.98rem; font-weight: 900; margin-bottom: 8px;">Notion AI & Deep Research</h4>
              <p class="card-desc">საგრანტო ბიუროკრატიის შემცირება, Notion Grant Tracker, Perplexity კვლევა, Slido #2 და 30-დღიანი იმპლემენტაციის გეგმა.</p>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.76rem; font-weight: 700; color: var(--pm-emerald);">📘 გაიდები: Notion Weekly Cadence & 30-Day Roadmap</div>
            </div>
          </div>

          <div class="callout-box" style="margin-top: 16px;">
            ☕ <strong>შესვენებები:</strong> ყავის შესვენება 1 (12:15 - 12:30) • ლანჩი და არაფორმალური ქსელი (13:45 - 14:45) • ყავის შესვენება 2 (16:00 - 16:15).
          </div>
        """
    },

    # SLIDE 3
    {
        "module": "მოდული 1",
        "pill": "📊 ინტერაქტიული გამოკითხვა #1",
        "pillClass": "green",
        "timing": "11:05 - 11:15",
        "title": "სტარტის დიაგნოსტიკა (Baseline) & მოლოდინები",
        "subtitle": "ცოცხალი გამოკითხვა Slido.com-ზე: დაასკანერეთ QR კოდი თქვენი სმარტფონით",
        "content": """
          <div class="slido-box">
            <div class="slido-qr-frame">
              <div class="slido-qr-code">
                <div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div>
                <div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div>
                <div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div>
                <div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div>
              </div>
              <div style="font-size: 0.68rem; font-weight: 800; color: #0f172a;">#EU4D-PM1</div>
            </div>

            <div class="slido-content">
              <span class="slido-badge">Live Poll #1 • slido.com</span>
              <div class="slido-question">რა არის თქვენი მთავარი საოპერაციო გამოწვევა საგრანტო პროექტების მართვაში?</div>
              <p style="font-size: 0.84rem; color: var(--text-muted); margin-bottom: 8px;">მონაწილეთა პასუხები ცოცხალ რეჟიმში გამოჩნდება ეკრანზე Word Cloud-ისა და რეიტინგის სახით:</p>
              
              <div class="slido-options">
                <div class="slido-option-item">
                  <span>A. Logframe-ისა და Theory of Change-ის ფორმულირება დონორის მკაცრი სტანდარტებით</span>
                  <strong>42%</strong>
                </div>
                <div class="slido-option-item">
                  <span>B. საგრანტო ბიუროკრატია, გუნდური დავალებების კოორდინაცია & დედლაინების ტრეკინგი</span>
                  <strong>28%</strong>
                </div>
                <div class="slido-option-item">
                  <span>C. ინდიკატორების გაზომვა, M&E კითხვარების ანალიზი და ნარატიული რეპორტინგი</span>
                  <strong>20%</strong>
                </div>
                <div class="slido-option-item">
                  <span>D. დონორული დოკუმენტების სწრაფი, ზუსტი თარგმნა და Do No Harm უსაფრთხოება</span>
                  <strong>10%</strong>
                </div>
              </div>
            </div>
          </div>

          <div class="callout-box green">
            🎯 <strong>დიაგნოსტიკის მიზანი:</strong> ტრენინგის შინაარსის მომენტალური ადაპტაცია დარბაზში მსხდომი არასამთავრობო ორგანიზაციების რეალურ საჭიროებებზე.
          </div>
        """
    },

    # SLIDE 4
    {
        "module": "მოდული 1",
        "pill": "Frontier AI Landscape 2026",
        "pillClass": "blue",
        "timing": "11:15 - 11:35",
        "title": "2026 წლის წამყვანი AI მოდელები: რომელი რისთვის გამოვიყენოთ?",
        "subtitle": "Frontier LLM-ების სპეციალიზაცია, მსჯელობის სიღრმე (Extended Thinking) და კონტექსტის ფანჯარა",
        "content": """
          <div class="grid-3col">
            <div class="card-box" style="border-top: 4px solid #d97706;">
              <div class="card-box-header">
                <span class="card-icon">🧠</span>
                <div>
                  <div class="card-title">Anthropic Claude 5.x / 3.7</div>
                  <div style="font-size: 0.78rem; color: #d97706; font-weight: 800;">Hybrid Reasoning Champion</div>
                </div>
              </div>
              <ul class="bullet-list">
                <li><strong>Extended Thinking:</strong> ხილული მსჯელობის ჯაჭვი რთული ლოგიკური ჩარჩოებისთვის.</li>
                <li><strong>საუკეთესო გამოყენება:</strong> საგრანტო განაცხადები, Logframe/ToC არქიტექტურა, დოკუმენტების თარგმანი და ნარატიული რეპორტები.</li>
                <li><strong>ტონი & სტილი:</strong> აკადემიური, დიპლომატიური, გაწონასწორებული, ჰალუცინაციების მინიმალური რისკი.</li>
              </ul>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.78rem; color: var(--text-muted);">კონტექსტი: 200K - 500K Tokens</div>
            </div>

            <div class="card-box" style="border-top: 4px solid #10b981;">
              <div class="card-box-header">
                <span class="card-icon">⚡</span>
                <div>
                  <div class="card-title">OpenAI GPT-6 / GPT-5.6</div>
                  <div style="font-size: 0.78rem; color: #10b981; font-weight: 800;">Multimodal & Automation</div>
                </div>
              </div>
              <ul class="bullet-list">
                <li><strong>Astra / High-Speed Engine:</strong> მყისიერი სტრუქტურირებული პასუხები, JSON/ცხრილები.</li>
                <li><strong>საუკეთესო გამოყენება:</strong> დავალებების დეკომპოზიცია, რისკების მატრიცა, Notion AI ინტეგრაციები და საველე მონაცემთა ექსტრაქცია.</li>
                <li><strong>ინსტრუმენტების გამოძახება:</strong> მოწინავე Function Calling და ვებ-ძიება.</li>
              </ul>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.78rem; color: var(--text-muted);">კონტექსტი: 128K - 1M Tokens</div>
            </div>

            <div class="card-box" style="border-top: 4px solid #0284c7;">
              <div class="card-box-header">
                <span class="card-icon">📚</span>
                <div>
                  <div class="card-title">Google Gemini 3.8 / 3.1 Pro</div>
                  <div style="font-size: 0.78rem; color: #0284c7; font-weight: 800;">Ultra-Long Context King</div>
                </div>
              </div>
              <ul class="bullet-list">
                <li><strong>1M - 2M Token Window:</strong> მთლიანი წიგნების, 500-გვერდიანი კვლევებისა და ათობით დონორული გაიდლაინის ერთდროული დამუშავება.</li>
                <li><strong>საუკეთესო გამოყენება:</strong> Google NotebookLM ცოდნის ბაზა, საველე აუდიო-ანგარიშების ანალიზი.</li>
                <li><strong>მულტიმოდალობა:</strong> ვიდეო, აუდიო და PDF ფაილების პირდაპირი ანალიზი.</li>
              </ul>
              <div style="margin-top: auto; padding-top: 10px; font-size: 0.78rem; color: var(--text-muted);">კონტექსტი: 1,000,000+ Tokens</div>
            </div>
          </div>

          <div class="callout-box" style="margin-top: 16px;">
            🔑 <strong>ოქროს წესი:</strong> არ არსებობს ერთი "ყველაზე ჭკვიანი" მოდელი - წარმატებული ორგანიზაცია იყენებს თითოეულ ხელსაწყოს თავისი უნიკალური ძლიერი მხარის მიხედვით.
          </div>
        """
    },

    # SLIDE 5
    {
        "module": "მოდული 1",
        "pill": "Zero-Cost ინოვაცია",
        "pillClass": "green",
        "timing": "11:35 - 11:45",
        "title": "LMSYS Chatbot Arena (arena.ai): უფასო წვდომა Frontier AI-ზე",
        "subtitle": "როგორ იმუშაოს არასამთავრობო ორგანიზაციამ 0-დანახარჯით მსოფლიოს საუკეთესო მოდელებთან",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">⚖️</span>
                <div class="card-title">რა არის arena.ai და რატომ არის რევოლუციური?</div>
              </div>
              <p class="card-desc">
                LMSYS Chatbot Arena არის UC Berkeley-ის კვლევითი პლატფორმა, სადაც მსოფლიოს ყველა წამყვანი AI ლაბორატორია (OpenAI, Anthropic, Google, Meta) ტესტავს თავის უახლეს მოდელებს.
              </p>
              <ul class="bullet-list" style="margin-top: 12px;">
                <li><strong>100% უფასო წვდომა:</strong> არ მოითხოვს ფასიან ყოველთვიურ გამოწერას.</li>
                <li><strong>Direct Chat რეჟიმი:</strong> მენიუდან ირჩევთ სასურველ მოდელს (მაგ. Claude 3.7 Sonnet ან GPT-5) და მუშაობთ შეუზღუდავად.</li>
                <li><strong>A/B Blind Battle რეჟიმი:</strong> ერთი და იგივე პრომპტი იგზავნება ორ ანონიმურ მოდელთან; ადარებთ შედეგებს და ირჩევთ საუკეთესო პასუხს.</li>
              </ul>
            </div>

            <div class="card-box" style="background: var(--bg-subtle);">
              <div class="card-box-header">
                <span class="card-icon">💡</span>
                <div class="card-title">Arena-ს სამუშაო სტრატეგია NGO-ებისთვის</div>
              </div>
              <div class="step-pipeline" style="flex-direction: column; gap: 8px;">
                <div style="background: var(--bg-card); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>ნაბიჯი 1:</strong> გახსენით <code style="color: var(--brand-blue);">arena.ai</code> → გადადით Direct Chat ჩანართზე.
                </div>
                <div style="background: var(--bg-card); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>ნაბიჯი 2:</strong> აირჩიეთ Claude ან GPT და ჩასვით თქვენი საგრანტო პრომპტი.
                </div>
                <div style="background: var(--bg-card); padding: 10px 14px; border-radius: 8px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>ნაბიჯი 3:</strong> დახვეწილი ტექსტი პირდაპირ დააკოპირეთ Notion-ში ან Word-ში.
                </div>
              </div>
              <div class="callout-box green" style="margin: 10px 0 0 0; padding: 10px 14px;">
                🛡️ <strong>მონაცემთა დაცვა:</strong> arena.ai-ზე არ შეიყვანოთ ბენეფიციართა პერსონალური მონაცემები (PII). გამოიყენეთ ანონიმიზებული დრაფტები!
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 6 (NEW GUIDE 1)
    {
        "module": "მოდული 1",
        "pill": "📘 სამაგიდო გაიდი #1",
        "pillClass": "green",
        "timing": "11:45 - 11:55",
        "title": "სამაგიდო გაიდი: LMSYS Arena.ai-ს 0-ხარჯიანი საოპერაციო სახელმძღვანელო",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: როგორ იმუშაოს ორგანიზაციამ ყოველთვიური გამოწერების გარეშე",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>ეს გაიდი განკუთვნილია ტრენინგის შემდგომ ორგანიზაციის ყოველდღიურ საქმიანობაში გამოსაყენებლად (Post-Course SOP).</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🛠️</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">ნაბიჯ-ნაბიჯ სამუშაო პროტოკოლი (SOP)</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">1</div>
                <div class="guide-step-body">
                  <strong>სამუშაო რეჟიმის შერჩევა (arena.ai)</strong>
                  რთული საგრანტო ტექსტებისთვის აირჩიეთ <em>Direct Chat</em> → მოდელი: <code>Claude 3.7 Sonnet</code> ან <code>GPT-5.x</code>. როცა არგუმენტაციის სიძლიერეში ეჭვი გეპარებათ, გამოიყენეთ <em>Side-by-Side (A vs B)</em> ბრმა შედარება.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">2</div>
                <div class="guide-step-body">
                  <strong>პარამეტრების ოპტიმიზაცია</strong>
                  დააყენეთ Temperature: <strong>0.2 - 0.3</strong> (ზუსტი, მკაცრი ლოგიკური ჩარჩოებისთვის, რისკ-ანალიზისთვის და დოკუმენტების თარგმანისთვის); <strong>0.7</strong> (იდეების გენერირებისა და ბრეინშტორმინგისთვის).
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">3</div>
                <div class="guide-step-body">
                  <strong>მონაცემთა ანონიმიზაციის ფილტრი (Do No Harm)</strong>
                  სანამ ტექსტს Arena-ში ჩასვამთ, წაშალეთ სახელები, ტელეფონის ნომრები და სენსიტიური ლოკაციები. ჩაანაცვლეთ ფორმატით: <code>[ბენეფიციარი X]</code>, <code>[მუნიციპალიტეტი Y]</code>.
                </div>
              </div>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📌</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">გუნდის ყოველდღიური ჩეკლისტი (Cheat Sheet)</strong>
              </div>
              <div class="checklist-grid" style="grid-template-columns: 1fr;">
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>როცა Arena გადატვირთულია:</strong> გადატვირთეთ გვერდი ან აირჩიეთ ალტერნატიული მოდელი სიიდან (Claude 3.5 Sonnet / Gemini Pro 1.5/3.0).</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>დიალოგის ისტორიის შენახვა:</strong> Arena არ ინახავს ჩატების ისტორიას ხანგრძლივად! მიღებული კარგი პასუხი დაუყოვნებლივ დააკოპირეთ Notion Workspace-ში ან Google Doc-ში.</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>ფინანსური ეკონომია:</strong> ამ მეთოდით 5-კაციანი ორგანიზაცია ყოველწლიურად ზოგავს ათასობით დოლარს კომერციულ ხელმოწერებზე.</div>
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 7
    {
        "module": "მოდული 1",
        "pill": "პრომპტ-ინჟინერია",
        "pillClass": "purple",
        "timing": "11:55 - 12:05",
        "title": "სისტემური პრომპტინგის ჩარჩოები: CLEAR & PARTS",
        "subtitle": "როგორ გადავიდეთ შემთხვევითი კითხვებიდან პროფესიულ, განმეორებად შედეგებზე",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🎯</span>
                <div>
                  <div class="card-title">CLEAR Framework (საოპერაციო ამოცანებისთვის)</div>
                  <div style="font-size: 0.78rem; color: var(--brand-blue); font-weight: 800;">Context • Limitation • Expectation • Action • Review</div>
                </div>
              </div>
              <ul class="bullet-list">
                <li><strong>C - Context (კონტექსტი):</strong> ვინ ხართ, რა პროექტია, ვინ არის დონორი და რა არის სამიზნე თემი.</li>
                <li><strong>L - Limitation (შეზღუდვები):</strong> სიტყვების ლიმიტი, აკრძალული ტერმინები, ბიუჯეტის ჩარჩო.</li>
                <li><strong>E - Expectation (მოლოდინი):</strong> სასურველი ტონი (ოფიციალური, დიპლომატიური, ემპათიური).</li>
                <li><strong>A - Action (კონკრეტული მოქმედება):</strong> "შეადგინე 4-სვეტიანი Logframe", "გამოყავი 3 რისკი".</li>
                <li><strong>R - Review (კრიტიკა & გადამოწმება):</strong> "გადაამოწმე შეესაბამება თუ არა EU გაიდლაინს".</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🧩</span>
                <div>
                  <div class="card-title">PARTS Framework (საგრანტო წერისთვის)</div>
                  <div style="font-size: 0.78rem; color: var(--accent-purple); font-weight: 800;">Persona • Audience • Recipe • Tone • Specifics</div>
                </div>
              </div>
              <ul class="bullet-list">
                <li><strong>P - Persona (როლი):</strong> "იმოქმედე როგორც EU საგრანტო პროგრამების წამყვანი ექსპერტი".</li>
                <li><strong>A - Audience (აუდიტორია):</strong> "ტექსტი განკუთვნილია საგრანტო კომიტეტის შემფასებლებისთვის".</li>
                <li><strong>R - Recipe (სტრუქტურა/რეცეპტი):</strong> სათაური → პრობლემა → გადაწყვეტა → ინდიკატორი.</li>
                <li><strong>T - Tone (ტონი):</strong> ობიექტური, მტკიცებულებებზე დაფუძნებული, Do No Harm.</li>
                <li><strong>S - Specifics (სპეციფიკაციები):</strong> ცხრილის ფორმატი, SMART ფორმულირება.</li>
              </ul>
            </div>
          </div>

          <div class="callout-box purple" style="margin-top: 14px;">
            ⚠️ <strong>მთავარი შეცდომა:</strong> მოკლე 1-წინადადებიანი პრომპტი ("დამიწერე პროექტი") იძლევა ბუნდოვან, უსარგებლო პასუხს. ხარისხიანი პრომპტი შეიცავს მინიმუმ 4-5 პარამეტრს!
          </div>
        """
    },

    # SLIDE 8 (NEW GUIDE 2)
    {
        "module": "მოდული 1",
        "pill": "📘 სამაგიდო გაიდი #2",
        "pillClass": "purple",
        "timing": "12:05 - 12:15",
        "title": "სამაგიდო გაიდი: CLEAR & PARTS პრომპტინგის ჩეკლისტი საგრანტო წერისთვის",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: 10-პუნქტიანი საკონტროლო სია ყოველი საგრანტო განაცხადისთვის",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>შეინახეთ ეს ჩეკლისტი Notion-ში ან დაბეჭდეთ მაგიდაზე: გადაამოწმეთ ყოველი ახალი პრომპტი გაგზავნამდე!</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📋</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">პრომპტის აგების 5 ოქროს ეტაპი</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">1</div>
                <div class="guide-step-body">
                  <strong>როლის განსაზღვრა (System Prompt)</strong>
                  მიანიჭეთ მკაფიო ექსპერტული როლი: "იმოქმედე როგორც EU4Dialogue/UNDP საგრანტო პროექტების მთავარი შემფასებელი."
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">2</div>
                <div class="guide-step-body">
                  <strong>სამიზნე აუდიტორიის დასახელება</strong>
                  დააკონკრეტეთ, ვისთვის იწერება დოკუმენტი (დონორის ტექნიკური კომიტეტი, სათემო ბენეფიციარები თუ ფინანსური აუდიტორი).
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">3</div>
                <div class="guide-step-body">
                  <strong>უარყოფითი შეზღუდვები (Negative Constraints)</strong>
                  უთხარით რა <em>არ</em> გააკეთოს: "არ გამოიყენო ზედმეტად პათეტიკური ენა", "არ გადააჭარბო 300 სიტყვას", "არ ახსენო სახელები".
                </div>
              </div>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">⚡</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">მზა Master Prompt შაბლონი (Copy-Paste)</strong>
              </div>
              <div class="prompt-snippet">
                <div class="prompt-snippet-header">
                  <span>Grant Section Master Prompt</span>
                  <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
                </div>
                <div class="prompt-text">როლი: EU/UNDP საგრანტო პროგრამების წამყვანი ექსპერტი.
კონტექსტი: ჩვენ ვართ რეგიონული NGO, ვახორციელებთ პროექტს [პროექტის თემა] სამიზნე ჯგუფისთვის [ჯგუფი].
ამოცანა: შეადგინე საგრანტო განაცხადის სექცია: [სექციის სახელი, მაგ. Problem Justification].
მოთხოვნები:
1. გამოიყენე ობიექტური, მტკიცებულებებზე დაფუძნებული ტონი.
2. ტექსტის მოცულობა: მაქსიმუმ 250-300 სიტყვა.
3. დაიცავი Do No Harm პრინციპი.
4. ბოლოს შეაფასე ტექსტი დონორის კრიტერიუმებით და მითხარი 1 გაუმჯობესების რეკომენდაცია.</div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 9
    {
        "module": "მოდული 1",
        "pill": "მოწინავე ტექნიკები",
        "pillClass": "blue",
        "timing": "12:15 - 12:25",
        "title": "Multi-Turn Prompting & Few-Shot სწავლება",
        "subtitle": "როგორ ასწავლოთ AI-ს თქვენი ორგანიზაციის უნიკალური ხმა და დონორული ფორმატი",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🔄</span>
                <div class="card-title">Multi-Turn (დიალოგური დახვეწა)</div>
              </div>
              <p class="card-desc">არასდროს მოელოდოთ სრულყოფილ შედეგს ერთ ნაბიჯში. პროფესიული დრაფტინგი არის 3-4 რაუნდიანი დიალოგი:</p>
              <div style="margin-top: 12px; display: flex; flex-direction: column; gap: 8px;">
                <div style="background: var(--bg-subtle); padding: 8px 12px; border-radius: 6px; font-size: 0.82rem;">
                  <strong>რაუნდი 1:</strong> სტრუქტურისა და იდეების გენერირება (Outline).
                </div>
                <div style="background: var(--bg-subtle); padding: 8px 12px; border-radius: 6px; font-size: 0.82rem;">
                  <strong>რაუნდი 2:</strong> შერჩეული სექციის გაშლა და SMART ინდიკატორების მინიჭება.
                </div>
                <div style="background: var(--bg-subtle); padding: 8px 12px; border-radius: 6px; font-size: 0.82rem;">
                  <strong>რაუნდი 3:</strong> კრიტიკოსის როლი: "იპოვე სუსტი წერტილები და შემომთავაზე გაუმჯობესება".
                </div>
              </div>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">📋</span>
                <div class="card-title">Few-Shot Prompting (მაგალითებით სწავლება)</div>
              </div>
              <p class="card-desc">აჩვენეთ AI-ს 1-2 რეალური კარგი მაგალითი წარსულში მოგებული გრანტიდან:</p>
              
              <div class="prompt-snippet" style="margin-top: 10px;">
                <div class="prompt-snippet-header">
                  <span>Few-Shot Prompt შაბლონი</span>
                  <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
                </div>
                <div class="prompt-text">აი მაგალითი იმისა, თუ როგორ ვაყალიბებთ Outcome-ს:
მაგალითი 1: "სამიზნე თემში ახალგაზრდების 60%-ს აქვს გაუმჯობესებული წვდომა ციფრულ სერვისებზე..."
ახლა ანალოგიური სტილითა და სიღრმით ჩამოაყალიბე ჩვენი ახალი პროექტის მე-2 Outcome:
[პროექტის მონაცემები...]</div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 10
    {
        "module": "მოდული 1",
        "pill": "🛠️ Hands-on Workshop #1",
        "pillClass": "green",
        "timing": "12:25 - 12:35 (დავალება)",
        "title": "პრაქტიკული სავარჯიშო: CLEAR პრომპტი Arena.ai-ში",
        "subtitle": "თითოეული მონაწილე ქმნის თავისი ორგანიზაციის პირველ სისტემურ პრომპტს",
        "content": """
          <div class="workshop-card">
            <div class="workshop-header">
              <div class="workshop-title">
                <span>📋 დავალება 1.1: საგრანტო პროექტის კონცეფციის გენერირება & A/B შედარება</span>
              </div>
              <span class="workshop-duration">⏱️ 15 წუთი</span>
            </div>

            <div class="grid-2col">
              <div>
                <h4 style="font-size: 0.95rem; margin-bottom: 8px;">სამუშაო ნაბიჯები:</h4>
                <ol style="padding-left: 20px; font-size: 0.88rem; line-height: 1.6; color: var(--text-main);">
                  <li>გახსენით ბრაუზერში <code>arena.ai</code> (Side-by-Side ან Direct Chat).</li>
                  <li>შეარჩიეთ თქვენი ორგანიზაციის ერთი რეალური სათემო პრობლემა.</li>
                  <li>ააგეთ პრომპტი CLEAR ჩარჩოთი (Context, Limitation, Expectation, Action, Review).</li>
                  <li>შეადარეთ Claude 3.7 Sonnet-ისა და GPT-4o/5-ის პასუხები.</li>
                  <li>დააკოპირეთ საუკეთესო ვერსია თქვენს სამუშაო ფაილში.</li>
                </ol>
              </div>

              <div>
                <h4 style="font-size: 0.95rem; margin-bottom: 8px;">მოსალოდნელი შედეგი (Deliverable):</h4>
                <div class="callout-box green" style="margin-top: 0;">
                  ✓ ჩამოყალიბებული პროექტის სათაური<br>
                  ✓ პრობლემის მოკლე დასაბუთება (Statement of Problem)<br>
                  ✓ პროექტის გრძელვადიანი მიზანი (Overall Objective)<br>
                  ✓ 2 შუალედური შედეგი (Specific Outcomes)
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 11
    {
        "module": "შესვენება",
        "pill": "☕ ყავის შესვენება 1",
        "pillClass": "amber",
        "timing": "12:35 - 12:50 (15 წუთი)",
        "title": "ყავა, ენერგიის განახლება & ქსელური კომუნიკაცია",
        "subtitle": "დრო კითხვა-პასუხისთვის და მონაწილეთა შორის შთაბეჭდილებების გაზიარებისთვის",
        "content": """
          <div class="grid-2col" style="margin-top: 20px;">
            <div class="card-box" style="align-items: center; justify-content: center; text-align: center; background: linear-gradient(135deg, rgba(217, 119, 6, 0.05) 0%, rgba(217, 119, 6, 0.15) 100%);">
              <div style="font-size: 3.5rem; margin-bottom: 10px;">☕ 🥐</div>
              <h3 style="font-size: 1.4rem; font-weight: 900; margin-bottom: 6px;">15-წუთიანი შესვენება</h3>
              <p style="font-size: 0.9rem; color: var(--text-muted);">განაახლეთ ენერგია, გაეცანით კოლეგებს სხვადასხვა არასამთავრობო ორგანიზაციიდან.</p>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🔜</span>
                <div class="card-title">შემდეგ მოდულში (12:50 - 13:45):</div>
              </div>
              <ul class="bullet-list">
                <li><strong>Logical Frameworks (Logframes):</strong> ლოგიკური ჩარჩოს სრული მატრიცა EU & UNDP სტანდარტებით.</li>
                <li><strong>Theory of Change (ToC):</strong> როგორ დავაკავშიროთ აქტივობები რეალურ სისტემურ გავლენასთან.</li>
                <li><strong>Miro AI ბრეინშტორმინგი:</strong> SCAMPER მეთოდოლოგია და De Bono-ს 6 ქუდი სათემო პრობლემების გადასაჭრელად.</li>
              </ul>
            </div>
          </div>
        """
    },

    # SLIDE 12
    {
        "module": "მოდული 2",
        "pill": "საგრანტო არქიტექტურა",
        "pillClass": "green",
        "timing": "12:50 - 13:05",
        "title": "Logical Frameworks (Logframe) AI ეპოქაში",
        "subtitle": "რატომ ითხოვენ დონორები Logframe-ს და როგორ აქცევს AI მას 4-ჯერ უფრო სწრაფ პროცესად",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🏛️</span>
                <div class="card-title">Logframe-ის 4 დონე (EU/UNDP სტანდარტი)</div>
              </div>
              <div class="step-pipeline" style="flex-direction: column; gap: 6px;">
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border-left: 4px solid #005a9c; width: 100%;">
                  <strong>1. Impact (ზეგავლენა):</strong> გრძელვადიანი სოციალური ცვლილება ქვეყნის ან რეგიონის დონეზე.
                </div>
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border-left: 4px solid #10b981; width: 100%;">
                  <strong>2. Outcomes (შედეგები):</strong> ქცევითი, ინსტიტუციური ცვლილებები სამიზნე ჯგუფში პროექტის ბოლოს.
                </div>
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border-left: 4px solid #7c3aed; width: 100%;">
                  <strong>3. Outputs (პროდუქტები):</strong> ხელშესახები მიწოდებული სერვისები, ტრენინგები, პუბლიკაციები.
                </div>
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border-left: 4px solid #d97706; width: 100%;">
                  <strong>4. Activities (აქტივობები):</strong> კონკრეტული ნაბიჯები პროდუქტების შესაქმნელად.
                </div>
              </div>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">⚡</span>
                <div class="card-title">სად ეხმარება AI არასამთავრობო ორგანიზაციას?</div>
              </div>
              <ul class="bullet-list">
                <li><strong>ვერტიკალური ლოგიკის შემოწმება:</strong> მართლა გამოიწვევს თუ არა ეს აქტივობები ამ Outputs-ს და შემდეგ Outcomes-ს?</li>
                <li><strong>დაშვებებისა და რისკების გამოვლენა:</strong> რა გარე ფაქტორებმა შეიძლება ჩაშალოს მიზნის მიღწევა?</li>
                <li><strong>ინდიკატორების ფორმულირება:</strong> SMART სამიზნეების ავტომატური გენერირება.</li>
                <li><strong>განახლება პროექტის მიმდინარეობისას:</strong> Logframe-ის ადაპტაცია შეცვლილ საველე რეალობასთან.</li>
              </ul>
              <div class="callout-box green" style="margin-top: 10px;">
                ⏱️ <strong>ROI ეფექტი:</strong> ტრადიციული 8-12 საათი მცირდება 45-60 წუთამდე.
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 13
    {
        "module": "მოდული 2",
        "pill": "პრაქტიკული შაბლონი",
        "pillClass": "blue",
        "timing": "13:05 - 13:15",
        "title": "Logframe-ის 4x4 მატრიცა: სტრუქტურა და პრომპტი",
        "subtitle": "როგორ ააგოთ სრულყოფილი ლოგიკური ჩარჩო Claude 3.7-სა და GPT-ში",
        "content": """
          <div class="slide-table-wrapper">
            <table class="slide-table">
              <thead>
                <tr>
                  <th>ინტერვენციის ლოგიკა</th>
                  <th>ინდიკატორები (Indicators)</th>
                  <th>გადამოწმების წყაროები (MoV)</th>
                  <th>დაშვებები & რისკები (Assumptions)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Impact:</strong> სოციალური ერთიანობისა და მშვიდობის გაძლიერება სამიზნე თემში</td>
                  <td>თემებს შორის ნდობის ინდექსის 25%-იანი ზრდა 2027 წლამდე</td>
                  <td>დამოუკიდებელი სოციოლოგიური კვლევა, ოფიციალური სტატისტიკა</td>
                  <td>რეგიონული პოლიტიკური სტაბილურობა შენარჩუნებულია</td>
                </tr>
                <tr>
                  <td><strong>Outcome 1:</strong> სამოქალაქო აქტივისტების გაძლიერებული უნარები დიალოგში</td>
                  <td>მონაწილეთა 80% წარმატებით იყენებს დიალოგის მეთოდებს</td>
                  <td>Pre/Post შეფასების კითხვარები, ფოკუს-ჯგუფების ოქმები</td>
                  <td>ადგილობრივი თვითმმართველობა ღიაა თანამშრომლობისთვის</td>
                </tr>
                <tr>
                  <td><strong>Output 1.1:</strong> ჩატარებული 6 მოდულიანი სასწავლო კურსი</td>
                  <td>120 გადამზადებული მონაწილე (მინ. 50% ქალი)</td>
                  <td>დასწრების სიები, გაცემული სერტიფიკატები, ფოტომასალა</td>
                  <td>მონაწილეთა მაღალი ჩართულობა და დასწრება</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="prompt-snippet">
            <div class="prompt-snippet-header">
              <span>EU/UNDP Logframe Generator Prompt</span>
              <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
            </div>
            <div class="prompt-text">იმოქმედე როგორც ევროკავშირის საგრანტო პროგრამების წამყვანი ექსპერტი.
პროექტის იდეა: [ჩასვით პროექტის იდეა და სამიზნე ჯგუფი]
შეადგინე სრული 4x4 Logframe მატრიცა Markdown ცხრილის სახით:
1. Intervention Logic (Impact, Outcomes, Outputs, Activities)
2. Objectively Verifiable Indicators (SMART)
3. Sources / Means of Verification
4. Critical Assumptions & Risks
დაიცავი Do No Harm პრინციპი და საერთაშორისო დონორული სტანდარტები.</div>
          </div>
        """
    },

    # SLIDE 14 (NEW GUIDE 3)
    {
        "module": "მოდული 2",
        "pill": "📘 სამაგიდო გაიდი #3",
        "pillClass": "green",
        "timing": "13:15 - 13:25",
        "title": "სამაგიდო გაიდი: EU/UNDP Logframe-ის 5-ეტაპიანი საოპერაციო პროცედურა (SOP)",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: პრობლემის ხიდან დონორის სრულყოფილ 4x4 ლოგიკურ ჩარჩომდე",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>ეს გაიდი გამოიყენეთ ორგანიზაციაში ყოველი ახალი საგრანტო განაცხადის მომზადებისას (Step-by-Step SOP).</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📐</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">Logframe-ის აგების 5 ეტაპი AI-ით</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">1</div>
                <div class="guide-step-body">
                  <strong>პრობლემის ხიდან მიზნების ხეზე გადასვლა</strong>
                  ჩასვით სათემო პრობლემა Claude-ში: <code>"გარდაქმენი ეს პრობლემის ხე (Causes → Core Problem → Effects) მიზნების ხედ (Outputs → Outcomes → Impact)."</code>
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">2</div>
                <div class="guide-step-body">
                  <strong>ვერტიკალური ლოგიკის შემოწმება (Vertical Logic Test)</strong>
                  შეამოწმეთ ჯაჭვი: <em>თუ აქტივობები შესრულდა → შეიქმნება Outputs? თუ Outputs შეიქმნა → მიიღწევა Outcomes?</em> AI-ს დაავალეთ: <code>"იპოვე ლოგიკური ხარვეზები ამ ჯაჭვში."</code>
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">3</div>
                <div class="guide-step-body">
                  <strong>SMART ინდიკატორებისა და სამიზნეების მიბმა</strong>
                  თითოეულ Output-სა და Outcome-ზე მოითხოვეთ მინიმუმ 1 რაოდენობრივი და 1 თვისებრივი SMART ინდიკატორი.
                </div>
              </div>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🛡️</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">ეტაპი 4-5: MoV და რისკების ვალიდაცია</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">4</div>
                <div class="guide-step-body">
                  <strong>Means of Verification-ის რეალისტურობის ტესტი</strong>
                  დაუსვით AI-ს კითხვა: <code>"შეძლებს თუ არა ჩვენი 3-კაციანი გუნდი ამ MoV-ის შეგროვებას ზედმეტი ხარჯების გარეშე?"</code>
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">5</div>
                <div class="guide-step-body">
                  <strong>კრიტიკული დაშვებების (Assumptions) ფორმულირება</strong>
                  გამოავლინეთ გარე ფაქტორები, რომლებიც აუცილებელია წარმატებისთვის, მაგრამ თქვენს კონტროლს მიღმაა.
                </div>
              </div>
              <div class="callout-box green" style="margin-top: 10px; padding: 10px 14px;">
                💡 <strong>გუნდის წესი:</strong> დონორთან გაგზავნამდე Logframe-ის საბოლოო ვერსია ყოველთვის გადაიკითხოს გუნდის წევრების მიერ!
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 15
    {
        "module": "მოდული 2",
        "pill": "სტრატეგიული ხედვა",
        "pillClass": "purple",
        "timing": "13:25 - 13:35",
        "title": "Theory of Change (ToC): ცვლილების თეორიის არქიტექტურა",
        "subtitle": "როგორ ავუხსნათ დონორს, თუ რატომ მოიტანს ჩვენი აქტივობა გრძელვადიან გავლენას",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🔗</span>
                <div class="card-title">Logframe vs. Theory of Change</div>
              </div>
              <ul class="bullet-list">
                <li><strong>Logframe:</strong> ხაზოვანი, ოპერატიული მართვის ინსტრუმენტი (რა აქტივობას რა Output მოსდევს). დონორისთვის ხელშეკრულების საფუძველია.</li>
                <li><strong>Theory of Change:</strong> სტრატეგიული, სისტემური რუკა (რატომ და როგორ ხდება ცვლილება). მოიცავს მიზეზ-შედეგობრივ კავშირებს და ფარულ დაშვებებს.</li>
                <li><strong>სინერგია:</strong> ToC არის ფილოსოფია და სტრატეგია; Logframe არის მისი აღსრულების გეგმა.</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🪜</span>
                <div class="card-title">ToC-ის მიზეზ-შედეგობრივი ჯაჭვი (Causal Pathway)</div>
              </div>
              <div class="step-pipeline" style="flex-direction: column; gap: 8px;">
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>თუ (If):</strong> ჩავატარებთ AI და პროექტების მართვის პრაქტიკულ ბუთქემფს NGO-ებისთვის...
                </div>
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>მაშინ (Then):</strong> ორგანიზაციები დაზოგავენ დროს ადმინისტრირებაზე და გაზრდიან საგრანტო ხარისხს...
                </div>
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>რადგან (Because):</strong> ციფრული ხელსაწყოები ხსნის ბიუროკრატიულ ბარიერებს და ათავისუფლებს დროს საველე საქმიანობისთვის...
                </div>
                <div style="background: var(--bg-card); padding: 8px 12px; border-radius: 6px; border: 1px solid var(--border-subtle); width: 100%;">
                  <strong>რაც გამოიწვევს (Leading to):</strong> თემების გაძლიერებას და სამოქალაქო სექტორის მდგრადობას.
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 16 (NEW GUIDE 4)
    {
        "module": "მოდული 2",
        "pill": "📘 სამაგიდო გაიდი #4",
        "pillClass": "purple",
        "timing": "13:35 - 13:45",
        "title": "სამაგიდო გაიდი: Theory of Change-ის (ToC) შემუშავებისა და ვალიდაციის გაიდი",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: როგორ დავასაბუთოთ პროექტის სტრატეგიული გავლენა დონორთან",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>გამოიყენეთ ეს გაიდი საგრანტო განაცხადის Narrative Proposal-ის და ToC დიაგრამის მომზადებისას.</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🧠</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">ToC-ის ფორმულირების 4 კრიტიკული კითხვა</strong>
              </div>
              <ul class="bullet-list">
                <li><strong>1. რა არის საბოლოო გრძელვადიანი გავლენა?</strong> (Impact: როგორ შეიცვლება თემის ცხოვრება 3-5 წლის შემდეგ?)</li>
                <li><strong>2. რა წინაპირობებია აუცილებელი?</strong> (Preconditions: რა უნდა მოხდეს მანამდე, რომ ეს შედეგი დადგეს?)</li>
                <li><strong>3. რატომ გვჯერა, რომ ჩვენი მიდგომა იმუშავებს?</strong> (Rationale: რა მტკიცებულებები ან წარსული გამოცდილება გვაქვს?)</li>
                <li><strong>4. რა ფარული რისკები არსებობს?</strong> (Assumptions: რა შეიძლება მოხდეს თემში, რაც შეაფერხებს პროცესს?)</li>
              </ul>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">⚡</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">ToC Validation Prompt (Claude / GPT)</strong>
              </div>
              <div class="prompt-snippet">
                <div class="prompt-snippet-header">
                  <span>ToC Causal Pathway Validator</span>
                  <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
                </div>
                <div class="prompt-text">იმოქმედე როგორც საერთაშორისო დონორის (EU/UNDP) კრიტიკული შემფასებელი (Devil's Advocate).
აი ჩვენი პროექტის ცვლილების თეორია (Theory of Change):
[ჩასვით თქვენი ToC ჯაჭვი]
შეაფასე შემდეგი კრიტერიუმებით:
1. არის თუ არა მიზეზ-შედეგობრივი კავშირები ლოგიკური და დამაჯერებელი?
2. რა ფარული დაშვებები გვაქვს გამოტოვებული?
3. სად შეიძლება გაწყდეს ჯაჭვი რეალურ საველე პირობებში?
4. შემომთავაზე 3 გაუმჯობესებული ფორმულირება.</div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 17
    {
        "module": "მოდული 2",
        "pill": "ინოვაციური ბრეინშტორმინგი",
        "pillClass": "green",
        "timing": "13:45 - 13:55",
        "title": "სათემო იდეების გენერაცია: Miro AI & SCAMPER",
        "subtitle": "ვიზუალური ბრეინშტორმინგი, Sidekicks და იდეების კლასტერიზაცია Miro დაფაზე",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">💡</span>
                <div class="card-title">SCAMPER ჩარჩო სამოქალაქო ინოვაციებისთვის</div>
              </div>
              <ul class="bullet-list" style="font-size: 0.84rem;">
                <li><strong>S - Substitute:</strong> რა შეგვიძლია ჩავანაცვლოთ არსებულ მიდგომაში?</li>
                <li><strong>C - Combine:</strong> რა სხვა ინიციატივებთან შეგვიძლია გავაერთიანოთ?</li>
                <li><strong>A - Adapt:</strong> რა საერთაშორისო პრაქტიკა შეგვიძლია მოვარგოთ ადგილობრივ თემს?</li>
                <li><strong>M - Modify / Magnify:</strong> რომელი კომპონენტის გაძლიერება მოიტანს გარდამტეხ ეფექტს?</li>
                <li><strong>P - Put to another use:</strong> როგორ გამოვიყენოთ არსებული რესურსი ახალი მიზნით?</li>
                <li><strong>E - Eliminate:</strong> რა ზედმეტი ბიუროკრატიული ეტაპი შეგვიძლია ამოვიღოთ?</li>
                <li><strong>R - Reverse:</strong> როგორ წარიმართება პროექტი, თუ პროცესს პირიქით დავიწყებთ?</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🎨</span>
                <div class="card-title">Miro AI (Innovation Workspace) ფუნქციები</div>
              </div>
              <ul class="bullet-list">
                <li><strong>Sticky Notes Auto-Cluster:</strong> ასობით სათემო იდეის ავტომატური დაჯგუფება თემატურ კლასტერებად.</li>
                <li><strong>Mind Map Expansion:</strong> ერთი საწყისი იდეიდან სრული პრობლემის ხის (Problem Tree) აგება.</li>
                <li><strong>Miro Sidekicks:</strong> AI ასისტენტები (მაგ. Devil's Advocate, Facilitator), რომლებიც სვამენ კრიტიკულ შეკითხვებს.</li>
                <li><strong>პირდაპირი ექსპორტი Notion-ში:</strong> ვიზუალური იდეების გადატანა სამუშაო დავალებებში.</li>
              </ul>
            </div>
          </div>
        """
    },

    # SLIDE 18
    {
        "module": "მოდული 2",
        "pill": "🛠️ Hands-on Workshop #2",
        "pillClass": "green",
        "timing": "13:55 - 14:05 (დავალება)",
        "title": "პრაქტიკული სავარჯიშო: Logframe & ToC გენერაცია",
        "subtitle": "თითოეული მონაწილე აწყობს სრულყოფილ ლოგიკურ ჩარჩოს თავისი პროექტისთვის",
        "content": """
          <div class="workshop-card">
            <div class="workshop-header">
              <div class="workshop-title">
                <span>📋 დავალება 2.1: EU/UNDP Logframe-ისა და Theory of Change-ის შექმნა</span>
              </div>
              <span class="workshop-duration">⏱️ 15 წუთი</span>
            </div>

            <div class="grid-2col">
              <div>
                <h4 style="font-size: 0.95rem; margin-bottom: 8px;">სამუშაო ინსტრუქცია:</h4>
                <ol style="padding-left: 20px; font-size: 0.88rem; line-height: 1.6; color: var(--text-main);">
                  <li>აიღეთ 1-ელ ვორქშოფში შექმნილი პროექტის მიზანი და Outcomes.</li>
                  <li>გამოიყენეთ Logframe Generator Prompt-ი Claude-ში ან Arena-ში.</li>
                  <li>დაამატეთ Outputs და Activities თითოეულ Outcome-ზე.</li>
                  <li>ჩამოაყალიბეთ ToC-ის მიზეზ-შედეგობრივი ჯაჭვი (If → Then → Because).</li>
                  <li>შეინახეთ მიღებული მატრიცა შემდგომ მოდულებში Notion-ში გადასატანად.</li>
                </ol>
              </div>

              <div>
                <h4 style="font-size: 0.95rem; margin-bottom: 8px;">მოსალოდნელი შედეგი (Deliverable):</h4>
                <div class="callout-box green" style="margin-top: 0;">
                  ✓ სრული 4x4 Logframe მატრიცა<br>
                  ✓ მინიმუმ 2 Outcome და 4 Output<br>
                  ✓ თითოეულ დონეზე გადამოწმების წყაროები<br>
                  ✓ კრიტიკული დაშვებების (Assumptions) ჩამონათვალი
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 19
    {
        "module": "შესვენება",
        "pill": "🍽️ ლანჩი & ქსელური კომუნიკაცია",
        "pillClass": "amber",
        "timing": "14:05 - 15:05 (1 საათი)",
        "title": "სადილი & არაფორმალური დისკუსია",
        "subtitle": "გამოცდილების გაზიარება კოლეგებთან, იდეების განხილვა და დასვენება",
        "content": """
          <div class="grid-2col" style="margin-top: 20px;">
            <div class="card-box" style="align-items: center; justify-content: center; text-align: center; background: linear-gradient(135deg, rgba(5, 150, 105, 0.05) 0%, rgba(5, 150, 105, 0.15) 100%);">
              <div style="font-size: 3.5rem; margin-bottom: 10px;">🍽️ 🥗 🤝</div>
              <h3 style="font-size: 1.4rem; font-weight: 900; margin-bottom: 6px;">1-საათიანი ლანჩი</h3>
              <p style="font-size: 0.9rem; color: var(--text-muted);">გემრიელი სადილი, არაფორმალური საუბრები და საპარტნიორო იდეების გაცვლა.</p>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🔜</span>
                <div class="card-title">მეორე ნახევრის გეგმა (15:05 - 17:30):</div>
              </div>
              <ul class="bullet-list">
                <li><strong>მოდული 3 (15:05 - 16:15):</strong> SMART ინდიკატორების დახვეწა, რისკების მატრიცა (5x5) და საპროექტო პრეზენტაციები Gamma AI-ში.</li>
                <li><strong>მოდული 4 (16:30 - 17:30):</strong> საგრანტო ბიუროკრატიის შემცირება Notion AI-ით (Grant Tracker), Perplexity კვლევა და 30-დღიანი პოსტ-კურს გეგმა.</li>
              </ul>
            </div>
          </div>
        """
    },

    # SLIDE 20
    {
        "module": "მოდული 3",
        "pill": "M&E ინდიკატორები",
        "pillClass": "purple",
        "timing": "15:05 - 15:20",
        "title": "Developing and Refining Indicators: SMART ინდიკატორები",
        "subtitle": "როგორ შევქმნათ ინდიკატორები, რომლებიც რეალურ ცვლილებას ზომავს და დონორს აკმაყოფილებს",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🎯</span>
                <div class="card-title">SMART ინდიკატორის 5 კრიტერიუმი</div>
              </div>
              <ul class="bullet-list">
                <li><strong>S - Specific (კონკრეტული):</strong> ზუსტად განსაზღვრული შედეგი და სამიზნე ჯგუფი.</li>
                <li><strong>M - Measurable (გაზომვადი):</strong> რიცხვი, პროცენტი ან მკაფიო თვისებრივი მაჩვენებელი.</li>
                <li><strong>A - Achievable (მიღწევადი):</strong> რეალისტური არსებული ბიუჯეტისა და დროის ფარგლებში.</li>
                <li><strong>R - Relevant (რელევანტური):</strong> პირდაპირ უკავშირდება პროექტის მიზანს.</li>
                <li><strong>T - Time-bound (დროში გაწერილი):</strong> მკაფიო დედლაინი (მაგ. "მე-6 თვის ბოლოს").</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">⚖️</span>
                <div class="card-title">სუსტი vs. SMART ინდიკატორი (შედარება)</div>
              </div>
              <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 8px;">
                <div style="background: rgba(239, 68, 68, 0.08); border-left: 4px solid #ef4444; padding: 10px 14px; border-radius: 6px; font-size: 0.84rem;">
                  ❌ <strong>სუსტი:</strong> "ახალგაზრდების ცნობიერების ამაღლება დიალოგის საკითხებზე." <em>(არ აქვს რიცხვი, დრო, გაზომვის მეთოდი).</em>
                </div>
                <div style="background: rgba(16, 185, 129, 0.08); border-left: 4px solid #10b981; padding: 10px 14px; border-radius: 6px; font-size: 0.84rem;">
                  ✓ <strong>SMART:</strong> "სამიზნე მუნიციპალიტეტში 18-29 წლის 120 ახალგაზრდის (მინ. 50% ქალი) 75%-მა გამოავლინა დიალოგის უნარების მინიმუმ 30%-იანი გაუმჯობესება Post-Assessment ტესტში პროექტის მე-8 თვისთვის."
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 21
    {
        "module": "მოდული 3",
        "pill": "აუდიტი & ვერიფიკაცია",
        "pillClass": "blue",
        "timing": "15:20 - 15:30",
        "title": "Means of Verification (MoV) & მონაცემთა სანდოობა",
        "subtitle": "როგორ ავიცილოთ თავიდან აუხდენელი ინდიკატორები, რომლებიც აუდიტში პრობლემებს ქმნის",
        "content": """
          <div class="grid-3col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">📑</span>
                <div class="card-title">ადმინისტრაციული MoV</div>
              </div>
              <ul class="bullet-list">
                <li>რეგისტრაციისა და დასწრების სიები (ხელმოწერებით/ონლაინ).</li>
                <li>გაცემული სერტიფიკატების რეესტრი.</li>
                <li>ფოტო და ვიდეო დოკუმენტაცია (მონაწილეთა თანხმობით).</li>
                <li>შეხვედრების ოქმები და დღის წესრიგი.</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">📊</span>
                <div class="card-title">თვისებრივი/კვლევითი MoV</div>
              </div>
              <ul class="bullet-list">
                <li>Pre- და Post-Assessment კითხვარების შედეგები.</li>
                <li>ფოკუს-ჯგუფების ტრანსკრიპტები (Whisper).</li>
                <li>ბენეფიციართა ინდივიდუალური ინტერვიუები.</li>
                <li>დამოუკიდებელი ექსპერტის შეფასების ანგარიში.</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🌐</span>
                <div class="card-title">გარე/საჯარო MoV</div>
              </div>
              <ul class="bullet-list">
                <li>მედია-მონიტორინგი და საჯარო პუბლიკაციები.</li>
                <li>თვითმმართველობის ოფიციალური დოკუმენტები/აქტები.</li>
                <li>ვებსაიტის ანალიტიკა და ჩამოტვირთვების რაოდენობა.</li>
                <li>სოციალური ქსელების ჩართულობის მეტრიკები.</li>
              </ul>
            </div>
          </div>

          <div class="callout-box" style="margin-top: 14px;">
            💡 <strong>AI შემოწმების პრომპტი:</strong> "გააანალიზე ეს 5 ინდიკატორი და მითხარი, რა რესურსი და ბიუჯეტი დასჭირდება თითოეულის გადამოწმებას? არის თუ არა რომელიმე ზედმეტად ძვირი ან არარეალისტური მცირე გუნდისთვის?"
          </div>
        """
    },

    # SLIDE 22 (NEW GUIDE 5)
    {
        "module": "მოდული 3",
        "pill": "📘 სამაგიდო გაიდი #5",
        "pillClass": "purple",
        "timing": "15:30 - 15:40",
        "title": "სამაგიდო გაიდი: SMART ინდიკატორებისა და MoV-ის აუდიტის გაიდი",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: ინდიკატორების ხარისხის შემოწმების 6-პუნქტიანი ფილტრი",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>გამოიყენეთ ეს სამაგიდო გაიდი M&E გეგმის შედგენისას და დონორთან შუალედური ანგარიშგების დროს.</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🔍</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">ინდიკატორის აუდიტის 6-პუნქტიანი ფილტრი</strong>
              </div>
              <div class="checklist-grid" style="grid-template-columns: 1fr;">
                <div class="checklist-item">
                  <span class="check-icon">1.</span>
                  <div><strong>Baseline (საწყისი წერტილი):</strong> ვიცით თუ არა საწყისი მდგომარეობა? (თუ არა, ჩანიშნეთ Baseline Survey პროექტის 1-ელ თვეში).</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">2.</span>
                  <div><strong>Target (მიზნობრივი მაჩვენებელი):</strong> არის თუ არა ციფრი ზუსტი (მაგ. 60%, 120 მონაწილე) და არა ბუნდოვანი ("გაიზარდა")?</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">3.</span>
                  <div><strong>Disaggregation (დაყოფა):</strong> არის თუ არა გათვალისწინებული გენდერული და ასაკობრივი დაყოფა (Gender & Age Breakdown)?</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">4.</span>
                  <div><strong>MoV ხელმისაწვდომობა:</strong> არსებობს თუ არა დოკუმენტი, რომელსაც აუდიტორი ამოწმებს 3 წლის შემდეგაც?</div>
                </div>
              </div>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">⚡</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">Indicator Refiner Prompt (Claude / GPT)</strong>
              </div>
              <div class="prompt-snippet">
                <div class="prompt-snippet-header">
                  <span>SMART Indicator Quality Refiner</span>
                  <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
                </div>
                <div class="prompt-text">იმოქმედე როგორც გაეროს (UNDP) M&E უფროსი ოფიცერი.
აი ჩვენი პროექტის სამუშაო ინდიკატორები:
[ჩასვით თქვენი ინდიკატორები]
თითოეულზე გააკეთე შემდეგი:
1. შეაფასე SMART კრიტერიუმებით (1-5 ქულა).
2. გამოავლინე სისუსტეები და ბუნდოვანი სიტყვები.
3. გადაწერე სრულყოფილ SMART ფორმატში (Baseline, Target, Timeline, სამიზნე ჯგუფი).
4. მიუთითე 2 კონკრეტული, იაფი და რეალისტური Means of Verification (MoV).</div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 23
    {
        "module": "მოდული 3",
        "pill": "რისკების შეფასება",
        "pillClass": "amber",
        "timing": "15:40 - 15:50",
        "title": "Risk Matrix Development: რისკების 5x5 მატრიცა",
        "subtitle": "EU & UNDP სტანდარტის რისკების შეფასება, კატეგორიზაცია და სიმძიმის განსაზღვრა",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">⚠️</span>
                <div class="card-title">რისკების 4 ძირითადი კატეგორია NGO პროექტებში</div>
              </div>
              <ul class="bullet-list">
                <li><strong>1. საოპერაციო რისკები (Operational):</strong> გუნდის გადატვირთვა, საკადრო ცვლილებები, ტექნიკური შეფერხებები.</li>
                <li><strong>2. სოციალურ-პოლიტიკური რისკები (Contextual/Political):</strong> პოლარიზაცია, დეზინფორმაცია, ადგილობრივი წინააღმდეგობა.</li>
                <li><strong>3. ფინანსური რისკები (Financial):</strong> ინფლაცია, ბიუჯეტის გადახრები, ვალუტის კურსის რყევა.</li>
                <li><strong>4. უსაფრთხოების რისკები (Safety & Do No Harm):</strong> ბენეფიციართა პერსონალური მონაცემების გაჟონვა, რეპუტაციული ზიანი.</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🧮</span>
                <div class="card-title">5x5 ალბათობა vs. გავლენა (Likelihood vs. Impact)</div>
              </div>
              <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-top: 10px;">
                <div style="background: rgba(16, 185, 129, 0.15); border: 1px solid #10b981; padding: 12px; border-radius: 8px; text-align: center;">
                  <strong style="color: #059669; font-size: 0.85rem;">დაბალი რისკი (Low)</strong>
                  <p style="font-size: 0.74rem; color: var(--text-muted); margin-top: 4px;">მონიტორინგი სტანდარტულ რეჟიმში</p>
                </div>
                <div style="background: rgba(217, 119, 6, 0.15); border: 1px solid #d97706; padding: 12px; border-radius: 8px; text-align: center;">
                  <strong style="color: #d97706; font-size: 0.85rem;">საშუალო (Medium)</strong>
                  <p style="font-size: 0.74rem; color: var(--text-muted); margin-top: 4px;">შემარბილებელი გეგმის მომზადება</p>
                </div>
                <div style="background: rgba(239, 68, 68, 0.15); border: 1px solid #ef4444; padding: 12px; border-radius: 8px; text-align: center;">
                  <strong style="color: #ef4444; font-size: 0.85rem;">მაღალი (Critical)</strong>
                  <p style="font-size: 0.74rem; color: var(--text-muted); margin-top: 4px;">დაუყოვნებელი პრევენციული ზომები</p>
                </div>
              </div>
              <div class="callout-box amber" style="margin-top: 12px; font-size: 0.84rem;">
                📌 <strong>დონორის მოლოდინი:</strong> კარგი განაცხადი არ ამბობს "ჩვენთან რისკები არ არის". კარგი განაცხადი აჩვენებს, რომ ყველა რისკი იდენტიფიცირებულია და არსებობს მათი მართვის გეგმა!
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 24
    {
        "module": "მოდული 3",
        "pill": "შემარბილებელი ზომები",
        "pillClass": "purple",
        "timing": "15:50 - 16:00",
        "title": "Risk Mitigation: შემარბილებელი ღონისძიებები & Do No Harm",
        "subtitle": "როგორ შევადგინოთ პრევენციული და საპასუხო ზომები AI-ს დახმარებით",
        "content": """
          <div class="slide-table-wrapper">
            <table class="slide-table">
              <thead>
                <tr>
                  <th>რისკის აღწერა</th>
                  <th>კატეგორია</th>
                  <th>დონე</th>
                  <th>შემარბილებელი ღონისძიება (Mitigation Measure)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>ბენეფიციართა უნდობლობა ან შიში:</strong> სენსიტიურ თემებზე საუბრისგან თავის შეკავება</td>
                  <td>სოციალური</td>
                  <td><span style="color: #d97706; font-weight: 800;">საშუალო</span></td>
                  <td>Do No Harm პროტოკოლი, ანონიმური გამოკითხვები (Slido), ადგილობრივი სანდო ლიდერების ჩართვა.</td>
                </tr>
                <tr>
                  <td><strong>დეზინფორმაცია პროექტის შესახებ:</strong> მცდარი ნარატივები სოც. მედიაში</td>
                  <td>პოლიტიკური</td>
                  <td><span style="color: #ef4444; font-weight: 800;">მაღალი</span></td>
                  <td>პროაქტიული გამჭვირვალე კომუნიკაცია, საინფორმაციო ბროშურები (Gamma) და თემთან ღია შეხვედრები.</td>
                </tr>
                <tr>
                  <td><strong>მონაცემთა გაჟონვა:</strong> ბენეფიციართა PII მონაცემების შემთხვევითი გასაჯაროება</td>
                  <td>უსაფრთხოება</td>
                  <td><span style="color: #ef4444; font-weight: 800;">კრიტიკული</span></td>
                  <td>PII დე-იდენტიფიკაციის მკაცრი პროტოკოლი, ჩაკეტილი NotebookLM ცოდნის ბაზა, ISC2 სტანდარტები.</td>
                </tr>
              </tbody>
            </table>
          </div>

          <div class="prompt-snippet">
            <div class="prompt-snippet-header">
              <span>Risk Assessment Generator Prompt</span>
              <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
            </div>
            <div class="prompt-text">იმოქმედე როგორც საერთაშორისო საგრანტო რისკ-მენეჯერი.
ჩვენი პროექტის მოკლე აღწერა: [ჩასვით პროექტის შინაარსი და სამიზნე რეგიონი]
შეადგინე რისკების სრული მატრიცა:
1. გამოავლინე ტოპ 5 რისკი (საოპერაციო, პოლიტიკური, ფინანსური, Do No Harm).
2. შეაფასე თითოეული Likelihood (1-5) და Impact (1-5) შკალით.
3. ჩამოაყალიბე კონკრეტული, რეალისტური Mitigation Actions თითოეულზე.</div>
          </div>
        """
    },

    # SLIDE 25 (NEW GUIDE 6)
    {
        "module": "მოდული 3",
        "pill": "📘 სამაგიდო გაიდი #6",
        "pillClass": "amber",
        "timing": "16:00 - 16:10",
        "title": "სამაგიდო გაიდი: რისკების მატრიცისა და Do No Harm პრევენციის გაიდი",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: რისკების ყოველკვარტალური მონიტორინგის სახელმძღვანელო",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>ეს გაიდი გამოიყენეთ პროექტის განხორციელებისას ყოველ კვარტალში რისკ-რეესტრის განახლებისთვის.</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🛡️</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">Do No Harm 4-პუნქტიანი ეთიკური ჩეკლისტი</strong>
              </div>
              <ul class="bullet-list">
                <li><strong>1. უსაფრთხოების აუდიტი (Security Impact):</strong> ზრდის თუ არა ჩვენი აქტივობა ბენეფიციარების ან აქტივისტების რისკს ადგილზე?</li>
                <li><strong>2. სტიგმატიზაციის პრევენცია:</strong> უსვამს თუ არა ხაზს ჩვენი კომუნიკაცია მოწყვლადობას? (გამოიყენეთ პოზიტიური, გაძლიერებაზე ორიენტირებული ენა).</li>
                <li><strong>3. მონაცემთა ლოკალური შენახვა:</strong> სად ინახება ჩანაწერები? (არ ატვირთოთ ღია ჩატბოტებში გაუფილტრავი საველე ინტერვიუები!).</li>
                <li><strong>4. კონფლიქტისადმი მგრძნობელობა:</strong> ხომ არ იწვევს პროექტი დაძაბულობას სხვადასხვა სათემო ჯგუფებს შორის?</li>
              </ul>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🔄</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">რისკების კვარტალური განახლების რუტინა</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">1</div>
                <div class="guide-step-body">
                  <strong>რისკების გადაფასება:</strong> ყოველ 3 თვეში გუნდი გადის რისკ-რეესტრს Notion-ში და ამოწმებს, ხომ არ შეიცვალა Likelihood ან Impact.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">2</div>
                <div class="guide-step-body">
                  <strong>ახალი რისკების დამატება:</strong> თუ საველე რეალობა შეიცვალა, რისკ-რეესტრში შედის ახალი ჩანაწერი შესაბამისი Mitigation გეგმით.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">3</div>
                <div class="guide-step-body">
                  <strong>დონორის ინფორმირება:</strong> კრიტიკული რისკების გამოვლენისთანავე იგზავნება მოკლე ბრიფინგი დონორის Project Officer-თან.
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 26
    {
        "module": "მოდული 3",
        "pill": "ვიზუალიზაცია & Pitch Decks",
        "pillClass": "green",
        "timing": "16:10 - 16:20",
        "title": "Creating Presentations with Gamma AI (Gamma.app 3.0)",
        "subtitle": "საპროექტო წინადადებების, Impact Pitch Decks-ისა და სათემო ბროშურების მყისიერი გენერაცია",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🎨</span>
                <div class="card-title">რატომ Gamma.app და არა ჩვეულებრივი PowerPoint?</div>
              </div>
              <ul class="bullet-list">
                <li><strong>ტექსტიდან სრულ პრეზენტაციამდე:</strong> საგრანტო დრაფტის ან Logframe-ის ჩასმით 60 წამში იქმნება 8-10 სლაიდიანი ვიზუალური პრეზენტაცია.</li>
                <li><strong>Smart Diagrams & ბარათები:</strong> კომპლექსური ცხრილები ავტომატურად გარდაიქმნება პროფესიულ ინფოგრაფიკებად.</li>
                <li><strong>3 ფორმატი ერთში:</strong> Presentation (სლაიდშოუ), Document (One-Pager / Concept Note) და Webpage (ინტერაქტიული საიტი).</li>
                <li><strong>მარტივი ექსპორტი:</strong> PDF ან PowerPoint (.pptx) ფორმატში დონორთან გასაგზავნად.</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🚀</span>
                <div class="card-title">NGO Pitch Deck-ის 8 ოქროს სლაიდი Gamma-ში</div>
              </div>
              <ol style="padding-left: 20px; font-size: 0.85rem; line-height: 1.6; color: var(--text-main);">
                <li><strong>სლაიდი 1:</strong> პროექტის სათაური, დონორი და შემსრულებელი NGO.</li>
                <li><strong>სლაიდი 2:</strong> სათემო პრობლემა & გადაუდებელი საჭიროება.</li>
                <li><strong>სლაიდი 3:</strong> შემოთავაზებული ინოვაციური გადაწყვეტა.</li>
                <li><strong>სლაიდი 4:</strong> Theory of Change & ლოგიკური ჩარჩო.</li>
                <li><strong>სლაიდი 5:</strong> საკვანძო SMART ინდიკატორები & სამიზნეები.</li>
                <li><strong>სლაიდი 6:</strong> რისკების მატრიცა & Do No Harm პრინციპი.</li>
                <li><strong>სლაიდი 7:</strong> გუნდის გამოცდილება & პარტნიორები.</li>
                <li><strong>სლაიდი 8:</strong> ბიუჯეტის ლოგიკა & მოსალოდნელი გრძელვადიანი გავლენა.</li>
              </ol>
            </div>
          </div>
        """
    },

    # SLIDE 27 (NEW GUIDE 7)
    {
        "module": "მოდული 3",
        "pill": "📘 სამაგიდო გაიდი #7",
        "pillClass": "green",
        "timing": "16:20 - 16:30",
        "title": "სამაგიდო გაიდი: Gamma AI 10-წუთიანი საგრანტო Pitch Deck-ის შექმნის გაიდი",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: Concept Note-დან დონორის პრეზენტაციამდე 5 მარტივ ნაბიჯში",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>ეს გაიდი გამოიყენეთ დონორთან შეხვედრის, საბჭოს ბრიფინგისა და სათემო პრეზენტაციების წინ.</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">⚡</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">5-ნაბიჯიანი სამუშაო პროტოკოლი (SOP)</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">1</div>
                <div class="guide-step-body">
                  <strong>სტრუქტურის გამზადება:</strong> შეაგროვეთ პროექტის მოკლე აღწერა, Logframe-ის ძირითადი ხაზები და რისკები ერთ ტექსტურ ფაილში.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">2</div>
                <div class="guide-step-body">
                  <strong>Gamma AI-ში იმპორტი:</strong> აირჩიეთ <code>Generate → From Text</code>, ჩასვით მონახაზი და მიუთითეთ 8-სლაიდიანი სტრუქტურა.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">3</div>
                <div class="guide-step-body">
                  <strong>თემის & ვიზუალების მორგება:</strong> შეარჩიეთ სადა, პროფესიული თემა (მაგ. 'Oasis' ან 'Slate'), გამოიყენეთ Smart Diagrams ცხრილების ნაცვლად.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">4</div>
                <div class="guide-step-body">
                  <strong>Do No Harm ვიზუალური ფილტრი:</strong> არ გამოიყენოთ სენსიტიური ბენეფიციარების არაავტორიზებული ფოტოები; გამოიყენეთ აბსტრაქტული ინფოგრაფიკები ან სიმბოლოები.
                </div>
              </div>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📋</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">ექსპორტისა & გაზიარების წესები</strong>
              </div>
              <div class="checklist-grid" style="grid-template-columns: 1fr;">
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>PDF ექსპორტი:</strong> ოფიციალური დონორული მიმოწერისთვის ყოველთვის გაგზავნეთ ექსპორტირებული PDF დოკუმენტი.</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>Live Web Link:</strong> ონლაინ შეხვედრისას გააზიარეთ Gamma-ს ინტერაქტიული ლინკი, რომელიც იდეალურად იკითხება მობილურზეც.</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>Edit Mode:</strong> ნებისმიერი ციფრის ან ინდიკატორის შეცვლა ხდება წამებში პირდაპირ სლაიდზე დაკლიკებით.</div>
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 28
    {
        "module": "მოდული 3",
        "pill": "🛠️ Hands-on Workshop #3",
        "pillClass": "green",
        "timing": "16:30 - 16:40 (დავალება)",
        "title": "პრაქტიკული სავარჯიშო: Gamma Pitch Deck & რისკ-მატრიცა",
        "subtitle": "თითოეული მონაწილე აგენერირებს 8-სლაიდიან საპროექტო პრეზენტაციას Gamma.app-ში",
        "content": """
          <div class="workshop-card">
            <div class="workshop-header">
              <div class="workshop-title">
                <span>📋 დავალება 3.1: პროექტის Pitch Deck-ის შექმნა Gamma AI-ში</span>
              </div>
              <span class="workshop-duration">⏱️ 15 წუთი</span>
            </div>

            <div class="grid-2col">
              <div>
                <h4 style="font-size: 0.95rem; margin-bottom: 8px;">სამუშაო ნაბიჯები:</h4>
                <ol style="padding-left: 20px; font-size: 0.88rem; line-height: 1.6; color: var(--text-main);">
                  <li>შედით <code>gamma.app</code>-ზე (უფასო რეგისტრაცია 400 კრედიტით).</li>
                  <li>აირჩიეთ <strong>Generate → Presentation</strong>.</li>
                  <li>ჩასვით თქვენი Logframe-ისა და პროექტის მოკლე მონახაზი.</li>
                  <li>მიუთითეთ 8 სლაიდის სტრუქტურა და აირჩიეთ პროფესიული თემა.</li>
                  <li>შეცვალეთ ტექსტები, დაამატეთ რისკ-მატრიცა და დააექსპორტეთ PDF.</li>
                </ol>
              </div>

              <div>
                <h4 style="font-size: 0.95rem; margin-bottom: 8px;">მოსალოდნელი შედეგი (Deliverable):</h4>
                <div class="callout-box green" style="margin-top: 0;">
                  ✓ მზა 8-სლაიდიანი ვიზუალური Pitch Deck<br>
                  ✓ ინტეგრირებული Logframe & ToC სქემები<br>
                  ✓ რისკ-მატრიცის ვიზუალიზაცია<br>
                  ✓ ექსპორტირებული PDF დონორთან წარსადგენად
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 29
    {
        "module": "შესვენება",
        "pill": "☕ ყავის შესვენება 2",
        "pillClass": "amber",
        "timing": "16:40 - 16:55 (15 წუთი)",
        "title": "ყავა & მზადება ფინალური მოდულისთვის",
        "subtitle": "15 წუთი დასვენებისთვის ბოლო, უმნიშვნელოვანესი მოდულის დაწყებამდე",
        "content": """
          <div class="grid-2col" style="margin-top: 20px;">
            <div class="card-box" style="align-items: center; justify-content: center; text-align: center; background: linear-gradient(135deg, rgba(124, 58, 237, 0.05) 0%, rgba(124, 58, 237, 0.15) 100%);">
              <div style="font-size: 3.5rem; margin-bottom: 10px;">☕ 🍪</div>
              <h3 style="font-size: 1.4rem; font-weight: 900; margin-bottom: 6px;">ყავის შესვენება</h3>
              <p style="font-size: 0.9rem; color: var(--text-muted);">მოემზადეთ დღის ფინალური, საოპერაციო ბლოკისთვის: Notion AI & Perplexity.</p>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🔜</span>
                <div class="card-title">ფინალურ მოდულში (16:55 - 17:30):</div>
              </div>
              <ul class="bullet-list">
                <li><strong>Notion AI Workspace:</strong> Grant Tracker, მონაცემთა ბაზები, Kanban დაფები და Gantt Timeline.</li>
                <li><strong>საგრანტო ბიუროკრატიის შემცირება:</strong> როგორ დავზოგოთ კვირაში 10+ საათი გუნდურ კოორდინაციაზე.</li>
                <li><strong>Perplexity Deep Research:</strong> საერთაშორისო გრანტების კვლევა წყაროების ციტირებით.</li>
                <li><strong>Slido #2 Exit Ticket:</strong> დღის შეჯამება და უკუკავშირი.</li>
              </ul>
            </div>
          </div>
        """
    },

    # SLIDE 30
    {
        "module": "მოდული 4",
        "pill": "საოპერაციო ეფექტიანობა",
        "pillClass": "green",
        "timing": "16:55 - 17:05",
        "title": "Reducing Grant Administration & Bureaucracy through AI",
        "subtitle": "სად იკარგება არასამთავრობო ორგანიზაციების დრო და როგორ ვანაცვლებთ მას ჭკვიანი სისტემებით",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">⏳</span>
                <div class="card-title">სად იკარგება NGO-ების დრო დღეს?</div>
              </div>
              <ul class="bullet-list">
                <li><strong>ფრაგმენტული კომუნიკაცია:</strong> დავალებები იკარგება WhatsApp-ში, Messenger-სა და პირად მეილებში.</li>
                <li><strong>ვერსიების ქაოსი:</strong> <code>Project_Proposal_Final_v3_revised_FINAL.docx</code>.</li>
                <li><strong>გამოტოვებული დონორული დედლაინები:</strong> ანგარიშგების თარიღების ხელით ტრეკინგი სხვადასხვა ცხრილებში.</li>
                <li><strong>ხელით წერა:</strong> ყოველთვიური ანგარიშების ნულიდან აწყობა დაფანტული ჩანაწერებიდან.</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🚀</span>
                <div class="card-title">AI-ზე დაფუძნებული საოპერაციო მოდელი</div>
              </div>
              <ul class="bullet-list">
                <li><strong>ერთიანი სამუშაო სივრცე (Single Source of Truth):</strong> Notion AI-ში თავმოყრილი ყველა პროექტი, დავალება და დოკუმენტი.</li>
                <li><strong>ავტომატური სტატუს-რეპორტინგი:</strong> AI ერთი კლიკით აჯამებს, რა გაკეთდა ამ კვირაში და რა რჩება გასაკეთებელი.</li>
                <li><strong>გუნდური გამჭვირვალობა:</strong> თითოეულმა თანამშრომელმა იცის თავისი დავალება, დედლაინი და მიბმული დოკუმენტი.</li>
                <li><strong>60-80%-ით შემცირებული ბიუროკრატია:</strong> მეტი დრო რჩება საველე მუშაობისა და თემის გაძლიერებისთვის!</li>
              </ul>
            </div>
          </div>
        """
    },

    # SLIDE 31
    {
        "module": "მოდული 4",
        "pill": "Notion AI არქიტექტურა",
        "pillClass": "blue",
        "timing": "17:05 - 17:15",
        "title": "Notion AI Grant Tracker: სისტემური არქიტექტურა",
        "subtitle": "როგორ ავაწყოთ პროექტების, დავალებებისა და M&E ინდიკატორების ერთიანი ბაზა",
        "content": """
          <div class="grid-3col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🗂️</span>
                <div class="card-title">1. Projects Database</div>
              </div>
              <p class="card-desc">მთავარი პროექტების რეესტრი:</p>
              <ul class="bullet-list" style="font-size: 0.82rem;">
                <li>პროექტის სახელი & დონორი (EU, UNDP...)</li>
                <li>სტატუსი (Pipeline, Active, Completed)</li>
                <li>დაწყება & დასრულების თარიღები</li>
                <li>პასუხისმგებელი Project Manager</li>
                <li>მიბმული Logframe & ბიუჯეტის ლინკი</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">📋</span>
                <div class="card-title">2. Tasks & Activities</div>
              </div>
              <p class="card-desc">ყოველდღიური ოპერაციები:</p>
              <ul class="bullet-list" style="font-size: 0.82rem;">
                <li>დავალება & მიბმული Output-ი</li>
                <li>Assignee (პასუხისმგებელი პირი)</li>
                <li>Due Date (დედლაინი)</li>
                <li>Priority (Urgent, High, Normal)</li>
                <li>Kanban View & Timeline (Gantt) View</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">📅</span>
                <div class="card-title">3. Donor Deadlines & M&E</div>
              </div>
              <p class="card-desc">ანგარიშგებისა და მონიტორინგის ბაზა:</p>
              <ul class="bullet-list" style="font-size: 0.82rem;">
                <li>Interim / Final Report დედლაინები</li>
                <li>M&E ინდიკატორების მიმდინარე პროგრესი</li>
                <li>Means of Verification დოკუმენტების ბაზა</li>
                <li>Calendar View ავტომატური შეხსენებებით</li>
                <li>Notion AI Auto-Summary გენერატორი</li>
              </ul>
            </div>
          </div>

          <div class="callout-box green" style="margin-top: 14px;">
            🎁 <strong>მონაწილეთა საჩუქარი:</strong> თითოეული მონაწილე იღებს წინასწარ გამართულ Notion AI Grant Tracker & M&E Workspace-ის მზა შაბლონს (Template), რომლის დუბლირებაც შესაძლებელია საკუთარ ანგარიშში 1 კლიკით!
          </div>
        """
    },

    # SLIDE 32 (NEW GUIDE 8)
    {
        "module": "მოდული 4",
        "pill": "📘 სამაგიდო გაიდი #8",
        "pillClass": "blue",
        "timing": "17:15 - 17:25",
        "title": "სამაგიდო გაიდი: Notion AI-ის ყოველკვირეული საოპერაციო რუტინა (Weekly Team Cadence)",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: როგორ მართოს გუნდმა საგრანტო პროექტები შეუფერხებლად",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>ეს გაიდი გამოიყენეთ გუნდში ყოველკვირეული სამუშაო რუტინის დასანერგად (Team Operating Cadence).</span>
          </div>

          <div class="grid-3col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📅</span>
                <strong style="font-size: 0.92rem; color: var(--text-main);">ორშაბათი: კვირის დაგეგმვა</strong>
              </div>
              <ul class="bullet-list" style="font-size: 0.82rem;">
                <li>15-წუთიანი გუნდური შეხვედრა Notion Kanban დაფასთან.</li>
                <li>კვირის პრიორიტეტული Tasks-ების გადანაწილება თანამშრომლებზე.</li>
                <li>მომავალი 14 დღის დონორული დედლაინების შემოწმება.</li>
                <li>ბლოკერებისა და რისკების გამოვლენა.</li>
              </ul>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">⚡</span>
                <strong style="font-size: 0.92rem; color: var(--text-main);">ოთხშაბათი: Mid-Week პულსი</strong>
              </div>
              <ul class="bullet-list" style="font-size: 0.82rem;">
                <li>საველე აქტივობების პროგრესის შემოწმება.</li>
                <li>Means of Verification ფაილების ატვირთვა პირდაპირ Notion Task-ში.</li>
                <li>თუ დავალება ყოვნდება, სტატუსის შეცვლა: <code>Needs Support</code>.</li>
                <li>არანაირი ზედმეტი შეხვედრა - ყველაფერი ჩანს დაფაზე!</li>
              </ul>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📊</span>
                <strong style="font-size: 0.92rem; color: var(--text-main);">პარასკევი: AI Auto-Summary</strong>
              </div>
              <ul class="bullet-list" style="font-size: 0.82rem;">
                <li>Notion AI-ს გააქტიურება პროექტის გვერდზე.</li>
                <li>პრომპტი: <code>"შეაჯამე ამ კვირაში დასრულებული Tasks და შეადგინე 1-გვერდიანი სტატუს-რეპორტი."</code></li>
                <li>ავტომატური რეპორტის გაგზავნა მენეჯმენტთან ან დონორთან.</li>
                <li>გუნდი კვირას ასრულებს სრული სიმშვიდით!</li>
              </ul>
            </div>
          </div>
        """
    },

    # SLIDE 33
    {
        "module": "მოდული 4",
        "pill": "დონორთა ძიება & კვლევა",
        "pillClass": "purple",
        "timing": "17:25 - 17:35",
        "title": "Perplexity Pro & Deep Research: საგრანტო შესაძლებლობების კვლევა",
        "subtitle": "რეალურ დროში ვებ-ძიება, დონორული პრიორიტეტები და სტატისტიკის მოძიება პირდაპირი ციტირებით",
        "content": """
          <div class="grid-2col">
            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">🔎</span>
                <div class="card-title">რატომ Perplexity და არა ჩვეულებრივი Google?</div>
              </div>
              <ul class="bullet-list">
                <li><strong>პირდაპირი პასუხი წყაროებით:</strong> ლინკების სიის ნაცვლად გაძლევთ სინთეზირებულ პასუხს, სადაც ყოველი ფაქტი დამოწმებულია კონკრეტული წყაროთი.</li>
                <li><strong>Deep Research რეჟიმი:</strong> აგენტი ახორციელებს 20-30 ვებ-გვერდის სიღრმისეულ კვლევას, ადარებს მონაცემებს და ადგენს სრულ კვლევით ანგარიშს.</li>
                <li><strong>საგრანტო კონკურსების მონიტორინგი:</strong> "იპოვე 2026 წლის შემოდგომის ღია საგრანტო კონკურსები სამხრეთ კავკასიის რეგიონში სამოქალაქო აქტივიზმისთვის".</li>
              </ul>
            </div>

            <div class="card-box">
              <div class="card-box-header">
                <span class="card-icon">📊</span>
                <div class="card-title">საგრანტო კვლევის პრომპტი Perplexity-ში</div>
              </div>
              <div class="prompt-snippet" style="margin-top: 10px;">
                <div class="prompt-snippet-header">
                  <span>Donor Intelligence Prompt</span>
                  <button class="prompt-copy-btn" onclick="copyPromptSnippet(this)">კოპირება</button>
                </div>
                <div class="prompt-text">მოიძიე და გამიანალიზე ევროკავშირის (EU) და გაეროს (UNDP) მიმდინარე სტრატეგიული პრიორიტეტები სამოქალაქო ჩართულობისა და ახალგაზრდების გაძლიერების მიმართულებით.
მომაწოდე:
1. საკვანძო პრიორიტეტული თემები და დაფინანსების მიმართულებები.
2. უახლესი სტატისტიკური მონაცემები და კვლევები წყაროების პირდაპირი ციტირებით.
3. რეკომენდაცია: რა აქცენტები გავაკეთოთ ჩვენს საგრანტო განაცხადში შესაბამისობის ასამაღლებლად?</div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 34 (NEW GUIDE 9)
    {
        "module": "მოდული 4",
        "pill": "📘 სამაგიდო გაიდი #9",
        "pillClass": "purple",
        "timing": "17:35 - 17:45",
        "title": "სამაგიდო გაიდი: Perplexity Deep Research-ით დონორთა ძიებისა და კვლევის გაიდი",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: საგრანტო ფონდების მოძიება და მტკიცებულებების შეგროვება",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>გამოიყენეთ ეს გაიდი ახალი საგრანტო შესაძლებლობების კვლევისა და Needs Assessment-ის მომზადებისას.</span>
          </div>

          <div class="grid-2col">
            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">🔎</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">დონორთა ძიების 4-საფეხურიანი ალგორითმი</strong>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">1</div>
                <div class="guide-step-body">
                  <strong>Call for Proposals ძიება:</strong> გამოიყენეთ Perplexity Pro და მიუთითეთ ზუსტი გეოგრაფია, სამიზნე თემა და ვადები: <code>"აქტიური საგრანტო კონკურსები სამოქალაქო საზოგადოებისთვის საქართველოში 2026"</code>.
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">2</div>
                <div class="guide-step-body">
                  <strong>Guidelines & Eligibility ანალიზი:</strong> ატვირთეთ დონორის Call Guidelines PDF ფაილი Perplexity-ში ან NotebookLM-ში: <code>"გამომიყავი განმცხადებლის კრიტერიუმები, ბიუჯეტის ლიმიტები და აკრძალული ხარჯები."</code>
                </div>
              </div>
              <div class="guide-step-row">
                <div class="guide-step-num">3</div>
                <div class="guide-step-body">
                  <strong>სტატისტიკის ექსტრაქცია ციტირებით:</strong> Problem Statement-ის გასამყარებლად მოითხოვეთ ოფიციალური ციფრები: <code>"მომიძიე უახლესი კვლევები წყაროებით თემაზე..."</code>
                </div>
              </div>
            </div>

            <div class="guide-box">
              <div class="guide-box-header">
                <span class="card-icon">📌</span>
                <strong style="font-size: 0.95rem; color: var(--text-main);">დონორის პრიორიტეტებთან შესაბამისობის გაიდი</strong>
              </div>
              <div class="checklist-grid" style="grid-template-columns: 1fr;">
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>Cross-Cutting Themes:</strong> შეამოწმეთ მოიცავს თუ არა თქვენი პროექტი დონორის სავალდებულო ჰორიზონტალურ თემებს (Gender Equality, Green Transition, Digital Inclusion).</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>ტექნიკური ლექსიკონი:</strong> გამოიყენეთ დონორის ზუსტი ტერმინოლოგია, რომელიც ამოღებულია Call Guidelines-იდან.</div>
                </div>
                <div class="checklist-item">
                  <span class="check-icon">✓</span>
                  <div><strong>ციტირების გადამოწმება:</strong> განაცხადში ჩასმამდე ყოველთვის გადაამოწმეთ Perplexity-ის მიერ მოწოდებული პირველადი წყაროს ბმული.</div>
                </div>
              </div>
            </div>
          </div>
        """
    },

    # SLIDE 35
    {
        "module": "მოდული 4",
        "pill": "📊 ინტერაქტიული გამოკითხვა #2",
        "pillClass": "green",
        "timing": "17:45 - 17:55",
        "title": "დღე 1-ის შეჯამება (Pulse-Check) & Exit Ticket",
        "subtitle": "ცოცხალი გამოკითხვა Slido.com-ზე: ცოდნის პროგრესი და პირველი დღის შედეგები",
        "content": """
          <div class="slido-box">
            <div class="slido-qr-frame">
              <div class="slido-qr-code">
                <div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div>
                <div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div>
                <div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div>
                <div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div><div class="slido-qr-dot"></div><div class="slido-qr-dot accent"></div>
              </div>
              <div style="font-size: 0.68rem; font-weight: 800; color: #0f172a;">#EU4D-PM2</div>
            </div>

            <div class="slido-content">
              <span class="slido-badge">Live Poll #2 • slido.com</span>
              <div class="slido-question">რომელი ინსტრუმენტი იყო დღეს თქვენთვის ყველაზე სასარგებლო აღმოჩენა?</div>
              <p style="font-size: 0.84rem; color: var(--text-muted); margin-bottom: 8px;">მონაწილეთა უკუკავშირი და მზაობის შეფასება პირველი დღის ბოლოს:</p>
              
              <div class="slido-options">
                <div class="slido-option-item">
                  <span>A. LMSYS Arena (arena.ai) - Frontier მოდელებზე უფასო წვდომა გამოწერის გარეშე</span>
                  <strong>38%</strong>
                </div>
                <div class="slido-option-item">
                  <span>B. EU/UNDP Logframe & Theory of Change გენერატორი Claude 3.7-ში</span>
                  <strong>32%</strong>
                </div>
                <div class="slido-option-item">
                  <span>C. Notion AI Grant Tracker - პროექტების, დავალებებისა და M&E-ს ერთიანი ბაზა</span>
                  <strong>18%</strong>
                </div>
                <div class="slido-option-item">
                  <span>D. Gamma AI 3.0 - 8-სლაიდიანი საგრანტო Pitch Deck-ის მყისიერი შექმნა</span>
                  <strong>12%</strong>
                </div>
              </div>
            </div>
          </div>

          <div class="callout-box green">
            🌟 <strong>დღის შედეგი:</strong> მონაწილეთა 95%-მა აღნიშნა, რომ მიღებული ცოდნა უშუალოდ გამოიყენება მათ ორგანიზაციულ საქმიანობაში უკვე ხვალიდან!
          </div>
        """
    },

    # SLIDE 36 (NEW GUIDE 10)
    {
        "module": "შეჯამება",
        "pill": "📘 სამაგიდო გაიდი #10",
        "pillClass": "green",
        "timing": "17:55 - 18:05",
        "title": "სამაგიდო გაიდი: 30-დღიანი პოსტ-კურს იმპლემენტაციის საგზაო რუკა (Adoption Roadmap)",
        "subtitle": "შეინახეთ და გამოიყენეთ კურსის შემდგომ: 4-კვირიანი სამოქმედო გეგმა ორგანიზაციაში AI-ის დასანერგად",
        "content": """
          <div class="guide-banner">
            <span class="guide-tag">📘 პოსტ-კურს გაიდი</span>
            <span>ეს არის თქვენი ორგანიზაციის პრაქტიკული გზამკვლევი ტრენინგის დასრულებიდან მომდევნო 1 თვის განმავლობაში.</span>
          </div>

          <div class="grid-4col">
            <div class="guide-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--brand-blue); margin-bottom: 4px;">კვირა 1: ონბორდინგი</div>
              <h4 style="font-size: 0.96rem; font-weight: 900; margin-bottom: 8px;">Workspace & Arena</h4>
              <ul class="bullet-list" style="font-size: 0.78rem;">
                <li>Notion Grant Tracker შაბლონის დუბლირება გუნდისთვის.</li>
                <li>LMSYS Arena-ს ბმულებისა და CLEAR პრომპტ-შაბლონების გაზიარება თანამშრომლებთან.</li>
                <li>Do No Harm მონაცემთა დაცვის წესების გაცნობა.</li>
              </ul>
            </div>

            <div class="guide-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--pm-emerald); margin-bottom: 4px;">კვირა 2: საგრანტო აუდიტი</div>
              <h4 style="font-size: 0.96rem; font-weight: 900; margin-bottom: 8px;">Logframe & რისკები</h4>
              <ul class="bullet-list" style="font-size: 0.78rem;">
                <li>მიმდინარე პროექტის ლოგიკური ჩარჩოს გადამოწმება Claude-ით.</li>
                <li>SMART ინდიკატორებისა და MoV-ის ხარისხის აუდიტი.</li>
                <li>რისკ-მატრიცის განახლება 5x5 მეთოდით.</li>
              </ul>
            </div>

            <div class="guide-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--accent-purple); margin-bottom: 4px;">კვირა 3: ვიზუალიზაცია</div>
              <h4 style="font-size: 0.96rem; font-weight: 900; margin-bottom: 8px;">Gamma AI Pitch Deck</h4>
              <ul class="bullet-list" style="font-size: 0.78rem;">
                <li>პროექტის პირველი 8-სლაიდიანი პრეზენტაციის აწყობა Gamma-ში.</li>
                <li>დონორისთვის წარსადგენი Concept Note-ის ვიზუალიზაცია.</li>
                <li>გუნდური უკუკავშირი და დახვეწა.</li>
              </ul>
            </div>

            <div class="guide-box">
              <div style="font-size: 0.76rem; font-weight: 800; color: var(--accent-amber); margin-bottom: 4px;">კვირა 4: შედეგები & ROI</div>
              <h4 style="font-size: 0.96rem; font-weight: 900; margin-bottom: 8px;">ავტო-რეპორტინგი</h4>
              <ul class="bullet-list" style="font-size: 0.78rem;">
                <li>Notion AI-ით პირველი ყოველთვიური სტატუს-რეპორტის სინთეზი.</li>
                <li>დაზოგილი საათების აღრიცხვა (დროის ეკონომიის ROI შეფასება).</li>
                <li>პროცესების ოპტიმიზაციის შემდეგი ეტაპის დაგეგმვა.</li>
              </ul>
            </div>
          </div>

          <div class="callout-box green" style="margin-top: 14px;">
            🎯 <strong>შედეგი 30 დღეში:</strong> ორგანიზაცია სრულად გადადის ქაოსური ცხრილებიდან ერთიან, გამჭვირვალე და ავტომატიზებულ სამუშაო მოდელზე!
          </div>
        """
    },

    # SLIDE 37
    {
        "module": "შეჯამება",
        "pill": "დღე 1-ის ფინიში",
        "pillClass": "green",
        "timing": "18:05 - 18:15",
        "title": "დღე 1-ის შეჯამება & ხვალინდელი დღის (დღე 2) ანონსი",
        "subtitle": "რა შევქმენით დღეს და რას ვისწავლით ხვალ ბუთქემფის მე-2 დღეს",
        "content": """
          <div class="grid-2col">
            <div class="card-box" style="background: linear-gradient(135deg, rgba(16, 185, 129, 0.04) 0%, rgba(0, 90, 156, 0.04) 100%);">
              <div class="card-box-header">
                <span class="card-icon">✅</span>
                <div class="card-title">დღეს შექმნილი აქტივები & 10 სამაგიდო გაიდი:</div>
              </div>
              <ul class="bullet-list">
                <li><strong>Frontier AI & Arena.ai:</strong> მოდელების შედარებითი ტესტირებისა და CLEAR პრომპტინგის გაიდები.</li>
                <li><strong>EU/UNDP Logframe & ToC:</strong> 4x4 ლოგიკური ჩარჩოს 5-ეტაპიანი საოპერაციო SOP.</li>
                <li><strong>SMART ინდიკატორები & MoV:</strong> ინდიკატორების ხარისხის აუდიტის 6-პუნქტიანი ფილტრი.</li>
                <li><strong>რისკების მატრიცა:</strong> 5x5 მატრიცა და Do No Harm კვარტალური მონიტორინგის გაიდი.</li>
                <li><strong>Gamma Pitch Deck:</strong> დონორული პრეზენტაციის 10-წუთიანი შექმნის გაიდი.</li>
                <li><strong>Notion AI Grant Tracker:</strong> ყოველკვირეული გუნდური საოპერაციო რუტინა.</li>
                <li><strong>Perplexity Deep Research:</strong> დონორთა ძიების 4-საფეხურიანი ალგორითმი.</li>
                <li><strong>30-Day Roadmap:</strong> ორგანიზაციული იმპლემენტაციის 4-კვირიანი გეგმა.</li>
              </ul>
            </div>

            <div class="card-box" style="border-top: 4px solid var(--pm-emerald);">
              <div class="card-box-header">
                <span class="card-icon">🚀</span>
                <div class="card-title">ხვალ: დღე 2-ის ძირითადი თემები (11:00 - 17:30)</div>
              </div>
              <ul class="bullet-list">
                <li><strong>Julius AI:</strong> M&E მონაცემთა ანალიტიკა, ბიუჯეტების გადახრების აუდიტი და Pre/Post კითხვარები.</li>
                <li><strong>დოკუმენტების AI თარგმანი:</strong> Reflection Translation Multi-Pass მოდელი, EU/UNDP გლოსარიუმები და ფორმატირების დაცვა.</li>
                <li><strong>Google NotebookLM & Granola:</strong> ჩაკეტილი ორგანიზაციული ცოდნის ბაზა და შეხვედრების ბოტ-თავისუფალი ჩაწერა.</li>
                <li><strong>Do No Harm & Cybersecurity:</strong> ბენეფიციართა PII მონაცემების დე-იდენტიფიკაცია და უსაფრთხოება.</li>
                <li><strong>Gender-Responsive AI:</strong> გენდერული მიკერძოების აუდიტი და ინკლუზიური ენა.</li>
              </ul>
            </div>
          </div>

          <div class="callout-box" style="text-align: center; margin-top: 16px;">
            👏 <strong>მადლობა ნაყოფიერი მუშაობისთვის!</strong> ყველა გაიდი და მასალა რჩება თქვენს მუდმივ მფლობელობაში. ხვალ შევხვდებით 11:00 საათზე მეორე ინტენსიურ სამუშაო დღეს!
          </div>
        """
    }
]

# Read template and inject slidesData
from generate_day1_slides import html_content

js_code = f"""
    const slidesData = {json.dumps(slides, ensure_ascii=False, indent=6)};

    let currentSlide = 0;

    function renderSlide(index) {{
      if (index < 0 || index >= slidesData.length) return;
      currentSlide = index;

      const slide = slidesData[index];
      const viewport = document.getElementById('slideViewport');

      // Update Header & Progress
      document.getElementById('slideCounter').textContent = `სლაიდი ${{index + 1}} / ${{slidesData.length}}`;
      document.getElementById('headerModuleTag').textContent = slide.module;
      const progressPercent = ((index + 1) / slidesData.length) * 100;
      document.getElementById('progressBar').style.width = `${{progressPercent}}%`;

      // Update Nav Buttons
      document.getElementById('prevBtn').disabled = (index === 0);
      document.getElementById('nextBtn').disabled = (index === slidesData.length - 1);
      document.getElementById('nextBtn').textContent = (index === slidesData.length - 1) ? 'დასრულება ✓' : 'შემდეგი →';

      // Render HTML into viewport
      viewport.innerHTML = `
        <div class="slide-header">
          <div>
            <div class="slide-meta-row">
              <span class="slide-pill ${{slide.pillClass}}">${{slide.pill}}</span>
              <span class="slide-timing">⏱️ ${{slide.timing}}</span>
            </div>
            <h1 class="slide-title">${{slide.title}}</h1>
            <p class="slide-subtitle">${{slide.subtitle}}</p>
          </div>
          <div class="slide-badge-num">${{String(index + 1).padStart(2, '0')}}</div>
        </div>
        <div class="slide-body">
          ${{slide.content}}
        </div>
      `;

      // Update Overview active state if drawer is open
      updateOverviewSelection();
    }}

    function nextSlide() {{
      if (currentSlide < slidesData.length - 1) {{
        renderSlide(currentSlide + 1);
      }}
    }}

    function prevSlide() {{
      if (currentSlide > 0) {{
        renderSlide(currentSlide - 1);
      }}
    }}

    function goToSlide(index) {{
      renderSlide(index);
      toggleOverview(false);
    }}

    // Keyboard Navigation
    document.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') {{
        e.preventDefault();
        nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        prevSlide();
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        renderSlide(0);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        renderSlide(slidesData.length - 1);
      }} else if (e.key === 'o' || e.key === 'O') {{
        toggleOverview();
      }} else if (e.key === 'f' || e.key === 'F') {{
        toggleFullscreen();
      }} else if (e.key === 'Escape') {{
        toggleOverview(false);
      }}
    }});

    // Touch swipe support for mobile
    let touchStartX = 0;
    let touchEndX = 0;
    document.addEventListener('touchstart', (e) => {{
      touchStartX = e.changedTouches[0].screenX;
    }}, {{ passive: true }});
    document.addEventListener('touchend', (e) => {{
      touchEndX = e.changedTouches[0].screenX;
      handleSwipe();
    }}, {{ passive: true }});

    function handleSwipe() {{
      const diff = touchEndX - touchStartX;
      if (diff < -50) {{
        nextSlide();
      }} else if (diff > 50) {{
        prevSlide();
      }}
    }}

    // Theme Toggle
    function toggleTheme() {{
      document.body.classList.toggle('night-mode');
      const isNight = document.body.classList.contains('night-mode');
      localStorage.setItem('eu4d-deck-theme', isNight ? 'night' : 'day');
    }}

    (function() {{
      const saved = localStorage.getItem('eu4d-deck-theme');
      if (saved === 'night') {{
        document.body.classList.add('night-mode');
      }}
    }})();

    // Fullscreen Toggle
    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(() => {{}});
      }} else {{
        if (document.exitFullscreen) {{
          document.exitFullscreen();
        }}
      }}
    }}

    // Overview Drawer
    function toggleOverview(forceState) {{
      const drawer = document.getElementById('overviewDrawer');
      const isOpen = drawer.classList.contains('active');
      const shouldOpen = (forceState !== undefined) ? forceState : !isOpen;

      if (shouldOpen) {{
        buildOverviewGrid();
        drawer.classList.add('active');
      }} else {{
        drawer.classList.remove('active');
      }}
    }}

    function buildOverviewGrid() {{
      const grid = document.getElementById('overviewGrid');
      grid.innerHTML = '';
      slidesData.forEach((s, idx) => {{
        const item = document.createElement('div');
        item.className = `overview-item ${{idx === currentSlide ? 'current' : ''}}`;
        item.onclick = () => goToSlide(idx);
        item.innerHTML = `
          <div>
            <div class="overview-item-num">სლაიდი ${{idx + 1}} • ${{s.timing}}</div>
            <div class="overview-item-title">${{s.title}}</div>
          </div>
          <div class="overview-item-mod">${{s.module}}</div>
        `;
        grid.appendChild(item);
      }});
    }}

    function updateOverviewSelection() {{
      const items = document.querySelectorAll('.overview-item');
      items.forEach((it, idx) => {{
        if (idx === currentSlide) {{
          it.classList.add('current');
        }} else {{
          it.classList.remove('current');
        }}
      }});
    }}

    // Prompt Copy Helper
    function copyPromptSnippet(btn) {{
      const snippet = btn.closest('.prompt-snippet').querySelector('.prompt-text');
      if (!snippet) return;
      navigator.clipboard.writeText(snippet.innerText.trim()).then(() => {{
        const orig = btn.innerText;
        btn.innerText = '✓ კოპირებულია';
        btn.style.background = '#10b981';
        setTimeout(() => {{
          btn.innerText = orig;
          btn.style.background = '';
        }}, 2000);
      }});
    }}

    // Initialize slide deck on load
    document.addEventListener('DOMContentLoaded', () => {{
      renderSlide(0);
    }});
  </script>
</body>
</html>
"""

full_html = html_content + js_code

with open('eu4dialogue/pm/day-1-slides.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated eu4dialogue/pm/day-1-slides.html successfully with", len(slides), "slides!")

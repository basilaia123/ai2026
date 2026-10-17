# -*- coding: utf-8 -*-
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read all mock data files to embed preview text
base_dir = "eu4dialogue/pm/mock-data"

files = [
    ("mock_01_pre_post_survey_responses.csv", "M&E Pre/Post კითხვარის მონაცემები (ChatGPT Data Analysis & Claude)", "მოდული 5 (დღე 2)", "CSV მონაცემთა ბაზა (64 რესპონდენტი)", "Pre/Post შეფასების სტატისტიკური ანალიზი, Paired t-test, ქულების დინამიკა (1-დან 5-მდე), მუნიციპალური ჭრილი და Net Promoter Score (NPS). მზად არის ChatGPT Data Analysis-სა და Claude-ში ჩასატვირთად (Julius AI ალტერნატივით)."),
    ("mock_02_grant_budget_variance.csv", "საგრანტო ბიუჯეტის გადახრების აუდიტი (Budget Variance)", "მოდული 5 (დღე 2)", "CSV ბიუჯეტის ცხრილი (13 მუხლი)", "დაგეგმილი vs ფაქტობრივი ხარჯები ერთეულებში, პროცენტული გადახრა და დონორის თანხმობის საჭიროების ალგორითმი. ChatGPT Data Analysis-ითა და Claude-ით გადახრების ვიზუალიზაცია (Julius AI ალტერნატივით)."),
    ("mock_03_field_interviews_raw.txt", "საველე ინტერვიუების ნედლი ტრანსკრიფცია (Whisper Audio)", "მოდული 6 (დღე 2)", "ტექსტური ფაილი (3 ინტერვიუ)", "სათემო ახალგაზრდული ლიდერის, უხუცესი ფერმერისა და მეწარმე ქალის ციტატები კონფლიქტისპირა რეგიონიდან. დონორული რეპორტის ნარატივის სინთეზისთვის."),
    ("mock_04_donor_guidelines_excerpt.txt", "EU/UNDP საგრანტო გაიდლაინის ამონარიდი (ინგლისურად)", "მოდული 6 (დღე 2)", "ტექსტური დოკუმენტი (Official Guidelines)", "Do No Harm, GESI ინკლუზია, მონაცემთა დაცვა (PII) და ანგარიშგების წესები. გამოიყენება Google NotebookLM-ის ცოდნის ბაზისთვის და Reflection Translation-ისთვის."),
    ("mock_05_sensitive_field_report_raw.txt", "სენსიტიური საველე ანგარიში (PII ანონიმიზაციის სიმულაცია)", "მოდული 7 (დღე 2)", "საველე ქეისები მოგონილი PII-ით", "მოგონილი სახელები, პირადი ნომრები, ტელეფონები, მისამართები და სენსიტიური დეტალები. დავალება: AI-ით სრული დე-იდენტიფიკაცია და Do No Harm დაცვა."),
    ("mock_06_biased_project_narrative.txt", "მიკერძოებული საპროექტო ნარატივი (Gender & Inclusion Audit)", "მოდული 8 (დღე 2)", "საპროექტო განაცხადი ხარვეზებით", "გამიზნულად დაშვებული გენდერული სტერეოტიპები, ასაკობრივი მიკერძოება და არაინკლუზიური გარემო. დავალება: AI Bias Detection და ინკლუზიური გადაწერა."),
    ("mock_07_notion_grant_tasks.csv", "Notion AI საგრანტო ამოცანების ბაზა (Grant Tracker CSV)", "მოდული 4 (დღე 1)", "CSV იმპორტის ფაილი (10 ეტაპი)", "საპროექტო ფაზები, როლები, ვადები და პრიორიტეტები. პირდაპირი იმპორტი Notion-ში ცოცხალი საგრანტო დაფისა და Gantt ხედის მყისიერად ასაგებად."),
    ("mock_08_iptt_indicator_tracking_table.csv", "Indicator Performance Tracking Table (IPTT)", "მოდული 5 (დღე 2)", "CSV ინდიკატორების მატრიცა (12 ინდიკატორი)", "EU/UNDP სტანდარტის სრული IPTT ცხრილი: Baseline, Q1-Q3 Targets vs Actuals, RAG (Red/Amber/Green) სტატუსი, MoV ვერიფიკაციის წყაროები და ჩამორჩენების ადრეული გაფრთხილების სისტემა."),
    ("mock_09_qualitative_msc_interviews.txt", "თვისებრივი M&E: Most Significant Change (MSC) ქეისები", "მოდული 6 (დღე 2)", "თვისებრივი მონაცემები (4 საველე ისტორია)", "Most Significant Change მეთოდოლოგიით შეგროვებული საველე ისტორიები: AI თემატური კოდირება (Thematic Coding), განწყობის ანალიზი (Sentiment Shift) და დონორისთვის Human Interest Story-ს მომზადება.")
]

cards_html = []

for fname, title, mod, badge, desc in files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Escape for HTML attribute / display
    import html
    escaped_content = html.escape(content)
    preview_lines = "\n".join(content.strip().split("\n")[:8])
    escaped_preview = html.escape(preview_lines)
    
    card = f"""
      <div class="mock-card" id="{fname}">
        <div class="mock-card-header">
          <div class="mock-card-meta">
            <span class="mock-tag module">{mod}</span>
            <span class="mock-tag type">{badge}</span>
          </div>
          <h3 class="mock-card-title">{title}</h3>
          <p class="mock-card-desc">{desc}</p>
        </div>
        
        <div class="mock-code-box">
          <div class="mock-code-header">
            <span class="mock-code-filename">📄 {fname}</span>
            <div class="mock-actions">
              <button class="mock-btn copy-btn" onclick="copyMockData('{fname}')" title="მთლიანი ტექსტის კოპირება">
                📋 კოპირება
              </button>
              <a href="{fname}" download="{fname}" class="mock-btn download-btn" title="ფაილის ჩამოტვირთვა">
                ⬇️ ჩამოტვირთვა
              </a>
            </div>
          </div>
          <pre class="mock-code-pre"><code>{escaped_preview}
... (სრული მონაცემები ხელმისაწვდომია კოპირებით ან ჩამოტვირთვით)</code></pre>
          <textarea id="data-{fname}" style="display:none;">{escaped_content}</textarea>
        </div>
      </div>
    """
    cards_html.append(card)

full_cards = "\n".join(cards_html)

html_template = f"""<!DOCTYPE html>
<html lang="ka">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mock მონაცემთა პაკეტი | EU4Dialogue Project Management AI</title>
  <style>
    :root {{
      --brand-primary: #1e3a8a;
      --brand-secondary: #0d9488;
      --pm-emerald: #059669;
      --pm-emerald-light: rgba(16, 185, 129, 0.12);
      --accent-gold: #d97706;
      --bg-primary: #f8fafc;
      --bg-surface: #ffffff;
      --text-main: #0f172a;
      --text-muted: #475569;
      --border-color: #e2e8f0;
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 16px;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.08);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);
      --transition: all 0.2s ease-in-out;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      word-break: break-word;
      overflow-wrap: anywhere;
    }}

    body {{
      font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
      background: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      padding: 0;
      margin: 0;
      -webkit-font-smoothing: antialiased;
    }}

    .top-nav {{
      background: var(--brand-primary);
      color: #ffffff;
      padding: 14px 20px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: var(--shadow-md);
    }}

    .nav-brand {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 800;
      font-size: 1.05rem;
      letter-spacing: -0.01em;
    }}

    .nav-links {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}

    .nav-btn {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.15);
      color: #ffffff;
      text-decoration: none;
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 700;
      transition: var(--transition);
      border: 1px solid rgba(255, 255, 255, 0.25);
    }}

    .nav-btn:hover {{
      background: rgba(255, 255, 255, 0.3);
      transform: translateY(-1px);
    }}

    .container {{
      max-width: 1080px;
      margin: 0 auto;
      padding: 24px 16px 60px 16px;
    }}

    .hero-banner {{
      background: linear-gradient(135deg, #1e3a8a 0%, #0d9488 100%);
      color: #ffffff;
      padding: 32px 24px;
      border-radius: var(--radius-lg);
      margin-bottom: 30px;
      box-shadow: var(--shadow-md);
    }}

    .hero-badge {{
      display: inline-block;
      background: rgba(255, 255, 255, 0.2);
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .hero-title {{
      font-size: 1.7rem;
      font-weight: 800;
      line-height: 1.3;
      margin-bottom: 10px;
    }}

    .hero-subtitle {{
      font-size: 0.95rem;
      opacity: 0.92;
      max-width: 780px;
      line-height: 1.5;
    }}

    .info-callout {{
      background: #eff6ff;
      border-left: 4px solid #3b82f6;
      padding: 16px 20px;
      border-radius: var(--radius-sm);
      margin-bottom: 28px;
      font-size: 0.9rem;
      color: #1e40af;
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }}

    .mock-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 24px;
    }}

    .mock-card {{
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      box-shadow: var(--shadow-sm);
      overflow: hidden;
      transition: var(--transition);
    }}

    .mock-card:hover {{
      border-color: #cbd5e1;
      box-shadow: var(--shadow-md);
    }}

    .mock-card-header {{
      padding: 20px 20px 14px 20px;
    }}

    .mock-card-meta {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
      margin-bottom: 10px;
    }}

    .mock-tag {{
      font-size: 0.75rem;
      font-weight: 700;
      padding: 3px 10px;
      border-radius: 14px;
    }}

    .mock-tag.module {{
      background: var(--pm-emerald-light);
      color: var(--pm-emerald);
      border: 1px solid rgba(16, 185, 129, 0.25);
    }}

    .mock-tag.type {{
      background: #f1f5f9;
      color: var(--text-muted);
      border: 1px solid #e2e8f0;
    }}

    .mock-card-title {{
      font-size: 1.15rem;
      font-weight: 800;
      color: var(--brand-primary);
      margin-bottom: 6px;
      line-height: 1.4;
    }}

    .mock-card-desc {{
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    .mock-code-box {{
      background: #0f172a;
      border-top: 1px solid #1e293b;
      padding: 12px 16px 16px 16px;
    }}

    .mock-code-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
      padding-bottom: 8px;
      border-bottom: 1px solid #1e293b;
    }}

    .mock-code-filename {{
      font-family: monospace;
      font-size: 0.8rem;
      color: #94a3b8;
      font-weight: 600;
    }}

    .mock-actions {{
      display: flex;
      align-items: center;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .mock-btn {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 0.78rem;
      font-weight: 700;
      cursor: pointer;
      text-decoration: none;
      transition: var(--transition);
      border: none;
    }}

    .copy-btn {{
      background: #334155;
      color: #f8fafc;
    }}

    .copy-btn:hover {{
      background: #475569;
      color: #ffffff;
    }}

    .download-btn {{
      background: var(--brand-secondary);
      color: #ffffff;
    }}

    .download-btn:hover {{
      background: #0f766e;
    }}

    .mock-code-pre {{
      font-family: 'Consolas', 'Courier New', monospace;
      font-size: 0.8rem;
      line-height: 1.5;
      color: #e2e8f0;
      white-space: pre-wrap;
      word-break: break-all;
      background: #020617;
      padding: 12px;
      border-radius: 6px;
      border: 1px solid #1e293b;
      max-height: 220px;
      overflow-y: auto;
    }}

    .toast-msg {{
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #10b981;
      color: #ffffff;
      padding: 12px 20px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.9rem;
      box-shadow: 0 10px 15px -3px rgba(0,0,0,0.2);
      transform: translateY(100px);
      opacity: 0;
      transition: all 0.3s ease;
      z-index: 999;
    }}

    .toast-msg.show {{
      transform: translateY(0);
      opacity: 1;
    }}

    @media (max-width: 600px) {{
      .hero-title {{
        font-size: 1.35rem;
      }}
      .top-nav {{
        padding: 10px 14px;
      }}
      .mock-code-header {{
        flex-direction: column;
        align-items: flex-start;
      }}
      .mock-actions {{
        width: 100%;
        justify-content: flex-start;
      }}
    }}
  </style>
</head>
<body>

  <nav class="top-nav">
    <div class="nav-brand">
      <span>🛡️ EU4Dialogue</span>
      <span style="opacity: 0.6;">|</span>
      <span>Mock Data Hub</span>
    </div>
    <div class="nav-links">
      <a href="../index.html" class="nav-btn">← PM პროგრამა</a>
      <a href="../day-1-slides.html" class="nav-btn">🖥️ დღე 1-ის სლაიდები</a>
    </div>
  </nav>

  <div class="container">
    
    <div class="hero-banner">
      <div class="hero-badge">Zero-Privacy-Risk Training Suite</div>
      <h1 class="hero-title">სიმულაციური Mock მონაცემთა პაკეტი</h1>
      <p class="hero-subtitle">
        ეს გვერდი უზრუნველყოფს ტრენინგის 100%-ით ავტონომიურ ჩატარებას. მონაწილეებს არ უწევთ საკუთარი ორგანიზაციის კონფიდენციალური ფაილების გაზიარება: ყველა დავალებისთვის მომზადებულია რეალისტური, სინთეზური მონაცემები.
      </p>
    </div>

    <div class="info-callout">
      <div style="font-size: 1.4rem;">💡</div>
      <div>
        <strong>ინსტრუქცია ტრენერისა და მონაწილეებისთვის:</strong><br>
        თითოეული დავალების შესრულებისას გამოიყენეთ ქვემოთ მოცემული მზა ფაილები. შეგიძლიათ დააკოპიროთ ტექსტი 1 კლიკით (📋 კოპირება) ან ჩამოტვირთოთ ფაილი (⬇️ ჩამოტვირთვა) ChatGPT Data Analysis-ში, Claude-ში, Julius AI-ში, Google NotebookLM-სა და Notion-ში ასატვირთად.
      </div>
    </div>

    <div class="mock-grid">
      {full_cards}
    </div>

  </div>

  <div id="toast" class="toast-msg">ტექსტი წარმატებით დაკოპირდა ბუფერში!</div>

  <script>
    function copyMockData(fname) {{
      const textarea = document.getElementById('data-' + fname);
      if (!textarea) return;
      
      navigator.clipboard.writeText(textarea.value).then(() => {{
        showToast('ტექსტი (' + fname + ') დაკოპირდა ბუფერში!');
      }}).catch(err => {{
        textarea.style.display = 'block';
        textarea.select();
        document.execCommand('copy');
        textarea.style.display = 'none';
        showToast('ტექსტი დაკოპირდა!');
      }});
    }}

    function showToast(msg) {{
      const toast = document.getElementById('toast');
      toast.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {{
        toast.classList.remove('show');
      }}, 2500);
    }}
  </script>
</body>
</html>
"""

output_path = os.path.join(base_dir, "index.html")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_template.strip() + "\n")

print(f"Generated {output_path} successfully!")

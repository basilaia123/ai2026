# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

html_content = """<!DOCTYPE html>
<html lang="ka">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>პოსტ-ტრენინგ შეფასების კითხვარი | EU4Dialogue Civic AI & PM</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
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
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08);
      --transition: all 0.2s ease-in-out;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      word-break: break-word;
      overflow-wrap: anywhere;
    }

    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      line-height: 1.6;
      padding-bottom: 80px;
    }

    .top-bar {
      background: #0f172a;
      color: #94a3b8;
      padding: 12px 0;
      border-bottom: 1px solid rgba(255,255,255,0.1);
      font-size: 0.82rem;
    }

    .container {
      width: 100%;
      max-width: 900px;
      margin: 0 auto;
      padding: 0 20px;
    }

    .top-bar-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 10px;
    }

    .top-bar a {
      color: #38bdf8;
      text-decoration: none;
      font-weight: 600;
    }

    .hero-section {
      background: linear-gradient(135deg, #1e3a8a 0%, #065f46 100%);
      color: #ffffff;
      padding: 40px 0;
      border-bottom: 3px solid var(--accent-gold);
    }

    .hero-badge {
      display: inline-block;
      background: rgba(255,255,255,0.15);
      border: 1px solid rgba(255,255,255,0.3);
      padding: 4px 14px;
      border-radius: 20px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      margin-bottom: 14px;
      text-transform: uppercase;
    }

    .hero-title {
      font-size: 1.85rem;
      font-weight: 800;
      line-height: 1.25;
      margin-bottom: 12px;
    }

    .hero-desc {
      font-size: 0.95rem;
      color: #e2e8f0;
      max-width: 750px;
      line-height: 1.5;
    }

    .eval-meta-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 12px;
      margin-top: 24px;
    }

    .eval-meta-item {
      background: rgba(255,255,255,0.1);
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid rgba(255,255,255,0.15);
      font-size: 0.82rem;
    }

    .eval-meta-item strong {
      color: #fde68a;
      display: block;
      margin-bottom: 2px;
    }

    .section-card {
      background: var(--bg-surface);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 24px;
      margin-top: 24px;
      box-shadow: var(--shadow-sm);
    }

    .section-header {
      border-bottom: 2px solid #f1f5f9;
      padding-bottom: 14px;
      margin-bottom: 20px;
    }

    .section-num {
      display: inline-block;
      background: var(--pm-emerald-light);
      color: var(--pm-emerald);
      font-size: 0.75rem;
      font-weight: 800;
      padding: 2px 10px;
      border-radius: 12px;
      margin-bottom: 6px;
    }

    .section-title {
      font-size: 1.25rem;
      font-weight: 800;
      color: var(--text-main);
    }

    .section-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 4px;
    }

    .form-group {
      margin-bottom: 20px;
    }

    .form-label {
      display: block;
      font-weight: 700;
      font-size: 0.9rem;
      margin-bottom: 8px;
      color: #1e293b;
    }

    .form-control {
      width: 100%;
      padding: 10px 14px;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      background: #ffffff;
      color: var(--text-main);
      font-family: inherit;
    }

    .form-control:focus {
      outline: none;
      border-color: var(--brand-secondary);
      box-shadow: 0 0 0 3px rgba(13,148,136,0.15);
    }

    .radio-grid, .checkbox-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
      gap: 10px;
    }

    .option-label {
      display: flex;
      align-items: center;
      gap: 10px;
      background: #f8fafc;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      font-size: 0.86rem;
      font-weight: 500;
      cursor: pointer;
      transition: var(--transition);
    }

    .option-label:hover {
      background: #f1f5f9;
      border-color: #cbd5e1;
    }

    .option-label input {
      accent-color: var(--pm-emerald);
      width: 16px;
      height: 16px;
    }

    /* LIKERT MATRIX */
    .likert-table-wrap {
      width: 100%;
      overflow-x: auto;
      margin-top: 10px;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
    }

    .likert-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.85rem;
      min-width: 550px;
    }

    .likert-table th, .likert-table td {
      padding: 12px 14px;
      text-align: center;
      border-bottom: 1px solid var(--border-color);
    }

    .likert-table th {
      background: #f8fafc;
      font-weight: 700;
      color: #334155;
    }

    .likert-table th:first-child, .likert-table td:first-child {
      text-align: left;
      font-weight: 600;
      width: 50%;
    }

    .likert-table tr:hover td {
      background: #fafafa;
    }

    .likert-table input[type="radio"] {
      accent-color: var(--pm-emerald);
      width: 18px;
      height: 18px;
      cursor: pointer;
    }

    /* PRE VS POST CARDS */
    .comp-card {
      background: #f8fafc;
      border: 1px solid var(--border-color);
      border-radius: var(--radius-sm);
      padding: 16px;
      margin-bottom: 14px;
    }

    .comp-title {
      font-weight: 700;
      font-size: 0.92rem;
      color: #0f172a;
      margin-bottom: 4px;
    }

    .comp-desc {
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 12px;
    }

    .comp-scores {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 16px;
    }

    @media (max-width: 600px) {
      .comp-scores {
        grid-template-columns: 1fr;
        gap: 12px;
      }
    }

    .score-block {
      background: #ffffff;
      padding: 10px 14px;
      border-radius: var(--radius-sm);
      border: 1px solid #e2e8f0;
    }

    .score-block-title {
      font-size: 0.76rem;
      font-weight: 800;
      text-transform: uppercase;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
    }

    .score-block-title.pre {
      color: #64748b;
    }

    .score-block-title.post {
      color: var(--pm-emerald);
    }

    .scale-row {
      display: flex;
      justify-content: space-between;
      gap: 4px;
    }

    .scale-btn {
      flex: 1;
      text-align: center;
      padding: 6px 2px;
      border: 1px solid #cbd5e1;
      border-radius: 4px;
      font-size: 0.8rem;
      font-weight: 700;
      cursor: pointer;
      background: #ffffff;
      transition: var(--transition);
    }

    .scale-btn:hover {
      background: #f1f5f9;
    }

    .scale-btn.active-pre {
      background: #475569;
      color: #ffffff;
      border-color: #475569;
    }

    .scale-btn.active-post {
      background: var(--pm-emerald);
      color: #ffffff;
      border-color: var(--pm-emerald);
    }

    /* NPS SELECTOR */
    .nps-box {
      text-align: center;
      padding: 20px;
      background: #f8fafc;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
    }

    .nps-row {
      display: flex;
      justify-content: center;
      flex-wrap: wrap;
      gap: 6px;
      margin: 16px 0;
    }

    .nps-btn {
      width: 44px;
      height: 44px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.95rem;
      font-weight: 800;
      border-radius: 8px;
      border: 1px solid #cbd5e1;
      background: #ffffff;
      cursor: pointer;
      transition: var(--transition);
    }

    .nps-btn:hover {
      border-color: #0f172a;
    }

    .nps-btn.detractor.selected {
      background: #ef4444;
      color: #ffffff;
      border-color: #ef4444;
    }

    .nps-btn.passive.selected {
      background: #f59e0b;
      color: #ffffff;
      border-color: #f59e0b;
    }

    .nps-btn.promoter.selected {
      background: #10b981;
      color: #ffffff;
      border-color: #10b981;
    }

    .nps-legend {
      display: flex;
      justify-content: space-between;
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 600;
    }

    .action-bar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-top: 30px;
      padding-top: 20px;
      border-top: 1px solid var(--border-color);
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 12px 24px;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      font-weight: 700;
      text-decoration: none;
      cursor: pointer;
      border: none;
      transition: var(--transition);
    }

    .btn-primary {
      background: var(--pm-emerald);
      color: #ffffff;
    }

    .btn-primary:hover {
      background: #047857;
    }

    .btn-secondary {
      background: #e2e8f0;
      color: #334155;
    }

    .btn-secondary:hover {
      background: #cbd5e1;
    }

    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      color: #ffffff;
      padding: 14px 22px;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      font-weight: 600;
      box-shadow: var(--shadow-md);
      display: none;
      z-index: 1000;
    }
  </style>
</head>
<body>

  <!-- TOP BAR -->
  <div class="top-bar">
    <div class="container top-bar-inner">
      <div>
        <span>🇪🇺 EU4Dialogue | Civic AI & Project Management Bootcamp</span>
      </div>
      <div>
        <a href="index.html">← დაბრუნება კურსის მთავარ გვერდზე</a>
      </div>
    </div>
  </div>

  <!-- HERO -->
  <section class="hero-section">
    <div class="container">
      <span class="hero-badge">M&E Formal Evaluation Tool</span>
      <h1 class="hero-title">პოსტ-ტრენინგ შეფასების კითხვარი</h1>
      <p class="hero-desc">
        გთხოვთ, შეაფასოთ გავლილი 2-დღიანი ბუთქემფი. თქვენი უკუკავშირი გამოიყენება ტრენინგის შედეგების სტატისტიკური ანალიზისთვის (Learning Gain, t-test, NPS) და შემაჯამებელი დონორული რეპორტისთვის.
      </p>

      <div class="eval-meta-grid">
        <div class="eval-meta-item">
          <strong>მეთოდოლოგიური ჩარჩო:</strong>
          Kirkpatrick 4-Level Evaluation
        </div>
        <div class="eval-meta-item">
          <strong>ინდიკატორის კოდი:</strong>
          IND-OUT-02 (Learning Gain)
        </div>
        <div class="eval-meta-item">
          <strong>სავარაუდო დრო:</strong>
          7-10 წუთი (ანონიმური)
        </div>
      </div>
    </div>
  </section>

  <!-- FORM CONTAINER -->
  <main class="container">
    <form id="evalForm">

      <!-- SECTION 1 -->
      <div class="section-card">
        <div class="section-header">
          <span class="section-num">ნაწილი 1</span>
          <h2 class="section-title">ზოგადი ინფორმაცია და დისაგრეგაცია</h2>
          <p class="section-desc">მონაცემები გამოიყენება ანონიმური დისაგრეგაციისთვის (სქესი, ასაკი, რეგიონი, როლი)</p>
        </div>

        <div class="form-group">
          <label class="form-label" for="roleSelect">1.1. თქვენი როლი ორგანიზაციაში:</label>
          <select class="form-control" id="roleSelect" required>
            <option value="" disabled selected>აირჩიეთ პოზიცია...</option>
            <option value="Executive">ორგანიზაციის ხელმძღვანელი / დირექტორი</option>
            <option value="PM">პროექტის მენეჯერი / კოორდინატორი</option>
            <option value="ME">მონიტორინგისა და შეფასების (M&E) ოფიცერი</option>
            <option value="Finance">ფინანსური მენეჯერი / ბუღალტერი</option>
            <option value="GrantWriter">საგრანტო განაცხადების მწერალი</option>
            <option value="Field">სათემო მობილიზატორი / საველე ოფიცერი</option>
            <option value="Other">სხვა პოზიცია</option>
          </select>
        </div>

        <div class="form-group">
          <label class="form-label">1.2. რეგიონი / მუნიციპალიტეტი, სადაც საქმიანობთ:</label>
          <div class="radio-grid">
            <label class="option-label"><input type="radio" name="region" value="ShidaKartli" required> შიდა ქართლი</label>
            <label class="option-label"><input type="radio" name="region" value="Samegrelo"> სამეგრელო - ზემო სვანეთი</label>
            <label class="option-label"><input type="radio" name="region" value="BorderZone"> გამყოფი ხაზის მიმდებარე თემები</label>
            <label class="option-label"><input type="radio" name="region" value="KvemoKartli"> ქვემო ქართლი</label>
            <label class="option-label"><input type="radio" name="region" value="SamtskheJavakheti"> სამცხე-ჯავახეთი</label>
            <label class="option-label"><input type="radio" name="region" value="Tbilisi"> თბილისი</label>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">1.3. ასაკობრივი კატეგორია:</label>
          <div class="radio-grid">
            <label class="option-label"><input type="radio" name="age" value="18-24" required> 18 - 24 წელი</label>
            <label class="option-label"><input type="radio" name="age" value="25-34"> 25 - 34 წელი</label>
            <label class="option-label"><input type="radio" name="age" value="35-49"> 35 - 49 წელი</label>
            <label class="option-label"><input type="radio" name="age" value="50+"> 50+ წელი</label>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">1.4. გენდერი:</label>
          <div class="radio-grid">
            <label class="option-label"><input type="radio" name="gender" value="Female" required> ქალი</label>
            <label class="option-label"><input type="radio" name="gender" value="Male"> კაცი</label>
            <label class="option-label"><input type="radio" name="gender" value="Undisclosed"> სხვა / არ მსურს გამჟღავნება</label>
          </div>
        </div>
      </div>

      <!-- SECTION 2 -->
      <div class="section-card">
        <div class="section-header">
          <span class="section-num">ნაწილი 2</span>
          <h2 class="section-title">ტრენინგის ხარისხი და მიწოდება (Kirkpatrick Level 1)</h2>
          <p class="section-desc">შეაფასეთ თითოეული პარამეტრი 1-დან 5-მდე სკალით (1 = ძალიან დაბალი, 5 = შესანიშნავი)</p>
        </div>

        <div class="likert-table-wrap">
          <table class="likert-table">
            <thead>
              <tr>
                <th>შეფასების კრიტერიუმი</th>
                <th>1</th>
                <th>2</th>
                <th>3</th>
                <th>4</th>
                <th>5</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>2.1. შინაარსის შესაბამისობა ჩემი ორგანიზაციის რეალურ საჭიროებებთან</td>
                <td><input type="radio" name="sat_1" value="1" required></td>
                <td><input type="radio" name="sat_1" value="2"></td>
                <td><input type="radio" name="sat_1" value="3"></td>
                <td><input type="radio" name="sat_1" value="4"></td>
                <td><input type="radio" name="sat_1" value="5"></td>
              </tr>
              <tr>
                <td>2.2. თეორიისა და პრაქტიკული ეკრანთან სავარჯიშოების ბალანსი</td>
                <td><input type="radio" name="sat_2" value="1" required></td>
                <td><input type="radio" name="sat_2" value="2"></td>
                <td><input type="radio" name="sat_2" value="3"></td>
                <td><input type="radio" name="sat_2" value="4"></td>
                <td><input type="radio" name="sat_2" value="5"></td>
              </tr>
              <tr>
                <td>2.3. ტრენერის კომპეტენცია და დარბაზში ინდივიდუალური მენტორინგი</td>
                <td><input type="radio" name="sat_3" value="1" required></td>
                <td><input type="radio" name="sat_3" value="2"></td>
                <td><input type="radio" name="sat_3" value="3"></td>
                <td><input type="radio" name="sat_3" value="4"></td>
                <td><input type="radio" name="sat_3" value="5"></td>
              </tr>
              <tr>
                <td>2.4. სასწავლო ტემპი და დროის განაწილება 2 დღის განმავლობაში</td>
                <td><input type="radio" name="sat_4" value="1" required></td>
                <td><input type="radio" name="sat_4" value="2"></td>
                <td><input type="radio" name="sat_4" value="3"></td>
                <td><input type="radio" name="sat_4" value="4"></td>
                <td><input type="radio" name="sat_4" value="5"></td>
              </tr>
              <tr>
                <td>2.5. Mock მონაცემთა პაკეტის რეალისტურობა და პრაქტიკული სარგებელი</td>
                <td><input type="radio" name="sat_5" value="1" required></td>
                <td><input type="radio" name="sat_5" value="2"></td>
                <td><input type="radio" name="sat_5" value="3"></td>
                <td><input type="radio" name="sat_5" value="4"></td>
                <td><input type="radio" name="sat_5" value="5"></td>
              </tr>
              <tr>
                <td>2.6. სამაგიდო გაიდების, შაბლონებისა და პრომპტების სარგებლიანობა</td>
                <td><input type="radio" name="sat_6" value="1" required></td>
                <td><input type="radio" name="sat_6" value="2"></td>
                <td><input type="radio" name="sat_6" value="3"></td>
                <td><input type="radio" name="sat_6" value="4"></td>
                <td><input type="radio" name="sat_6" value="5"></td>
              </tr>
              <tr>
                <td>2.7. სამუშაო გარემო, დარბაზი, კვება და ტექნიკური მხარდაჭერა</td>
                <td><input type="radio" name="sat_7" value="1" required></td>
                <td><input type="radio" name="sat_7" value="2"></td>
                <td><input type="radio" name="sat_7" value="3"></td>
                <td><input type="radio" name="sat_7" value="4"></td>
                <td><input type="radio" name="sat_7" value="5"></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- SECTION 3 -->
      <div class="section-card">
        <div class="section-header">
          <span class="section-num">ნაწილი 3</span>
          <h2 class="section-title">სწავლა და კომპეტენციების შეძენა (Kirkpatrick Level 2)</h2>
          <p class="section-desc">შეაფასეთ თქვენი ცოდნა ტრენინგამდე (Pre) და ტრენინგის შემდეგ (Post) 1-დან 5-მდე სკალით</p>
        </div>

        <!-- Comp 1 -->
        <div class="comp-card">
          <div class="comp-title">3.1. Frontier AI მოდელები და CLEAR პრომპტინგი</div>
          <div class="comp-desc">Claude, GPT, Gemini-ს შედარება, LMSYS Arena და სისტემური პრომპტინგი</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c1_pre">-</span></div>
              <div class="scale-row" data-field="c1_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c1_post">-</span></div>
              <div class="scale-row" data-field="c1_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c1_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 2 -->
        <div class="comp-card">
          <div class="comp-title">3.2. საგრანტო განაცხადები, Logframe და ცვლილების თეორია (ToC)</div>
          <div class="comp-desc">EU/UNDP სტანდარტის 4x4 ლოგიკური ჩარჩოები და ცვლილების თეორიის არქიტექტურა</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c2_pre">-</span></div>
              <div class="scale-row" data-field="c2_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c2_post">-</span></div>
              <div class="scale-row" data-field="c2_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c2_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 3 -->
        <div class="comp-card">
          <div class="comp-title">3.3. SMART ინდიკატორები, რისკების მატრიცა და Gamma 5</div>
          <div class="comp-desc">5x5 რისკების შეფასება, შემარბილებელი ზომები და დონორული პრეზენტაციები</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c3_pre">-</span></div>
              <div class="scale-row" data-field="c3_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c3_post">-</span></div>
              <div class="scale-row" data-field="c3_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c3_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 4 -->
        <div class="comp-card">
          <div class="comp-title">3.4. საგრანტო პროექტების მართვა (Notion AI, Granola & Perplexity)</div>
          <div class="comp-desc">Grant Tracker, Kanban/Timeline ხედები და შეხვედრების ოქმების ავტო-სინთეზი</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c4_pre">-</span></div>
              <div class="scale-row" data-field="c4_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c4_post">-</span></div>
              <div class="scale-row" data-field="c4_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c4_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 5 -->
        <div class="comp-card">
          <div class="comp-title">3.5. რაოდენობრივი M&E ანალიტიკა და IPTT ტრეკერი</div>
          <div class="comp-desc">IPTT მატრიცა, RAG სტატუსები, Paired t-test და ბიუჯეტის გადახრების აუდიტი</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c5_pre">-</span></div>
              <div class="scale-row" data-field="c5_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c5_post">-</span></div>
              <div class="scale-row" data-field="c5_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c5_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 6 -->
        <div class="comp-card">
          <div class="comp-title">3.6. თვისებრივი M&E (MSC), თარგმანი & NotebookLM</div>
          <div class="comp-desc">საველე ინტერვიუების AI თემატური კოდირება, Reflection Translation და ცოდნის ბაზა</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c6_pre">-</span></div>
              <div class="scale-row" data-field="c6_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c6_post">-</span></div>
              <div class="scale-row" data-field="c6_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c6_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 7 -->
        <div class="comp-card">
          <div class="comp-title">3.7. Do No Harm, PII ანონიმიზაცია და კიბერუსაფრთხოება</div>
          <div class="comp-desc">ბენეფიციართა მონაცემების დე-იდენტიფიკაცია და Zero Data Retention</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c7_pre">-</span></div>
              <div class="scale-row" data-field="c7_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c7_post">-</span></div>
              <div class="scale-row" data-field="c7_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c7_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Comp 8 -->
        <div class="comp-card">
          <div class="comp-title">3.8. Gender-Responsive AI & Institutional Governance</div>
          <div class="comp-desc">ალგორითმული მიკერძოების (Bias) აღმოჩენა და ორგანიზაციული AI პოლიტიკა</div>
          <div class="comp-scores">
            <div class="score-block">
              <div class="score-block-title pre"><span>ტრენინგამდე (Pre)</span><span id="lbl_c8_pre">-</span></div>
              <div class="scale-row" data-field="c8_pre">
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_pre',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_pre',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_pre',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_pre',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_pre',5)">5</button>
              </div>
            </div>
            <div class="score-block">
              <div class="score-block-title post"><span>ტრენინგის შემდეგ (Post)</span><span id="lbl_c8_post">-</span></div>
              <div class="scale-row" data-field="c8_post">
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_post',1)">1</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_post',2)">2</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_post',3)">3</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_post',4)">4</button>
                <button type="button" class="scale-btn" onclick="setScore(this,'c8_post',5)">5</button>
              </div>
            </div>
          </div>
        </div>

      </div>

      <!-- SECTION 4 -->
      <div class="section-card">
        <div class="section-header">
          <span class="section-num">ნაწილი 4</span>
          <h2 class="section-title">პრაქტიკული დანერგვა და სამომავლო გეგმები (Kirkpatrick Level 3)</h2>
          <p class="section-desc">როგორ გამოიყენებთ მიღებულ ცოდნას თქვენს ორგანიზაციაში მომდევნო 30 დღის განმავლობაში</p>
        </div>

        <div class="form-group">
          <label class="form-label">4.1. რომელ 3 ხელსაწყოს ან მიდგომას დანერგავთ პირველ რიგში? (აირჩიეთ მაქსიმუმ 3)</label>
          <div class="checkbox-grid">
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="LLMPrompts"> Frontier LLMs & CLEAR პრომპტინგი</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="LogframeToC"> Logframe & Theory of Change შაბლონები</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="NotionGrantTracker"> Notion AI Grant Tracker სამუშაო დაფა</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="MEDataAnalysis"> ChatGPT Data Analysis & Google Sheets (IPTT)</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="NotebookLM"> Google NotebookLM ცოდნის ბაზა</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="GranolaAI"> Granola AI შეხვედრების ოქმების სინთეზი</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="ReflectionTranslation"> Multi-Pass Reflection Translation</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="PIIAnonymization"> Do No Harm & PII ანონიმიზაცია</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="Gamma5"> Gamma 5 საპროექტო პრეზენტაციები</label>
            <label class="option-label"><input type="checkbox" name="adopt_tools" value="AIGovernance"> Institutional AI Governance პოლიტიკა</label>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label">4.2. რა იქნება მთავარი გამოწვევა თქვენს ორგანიზაციაში AI-ის დანერგვისას?</label>
          <div class="radio-grid">
            <label class="option-label"><input type="radio" name="barrier" value="Skills" required> გუნდის სხვა წევრების ტექნიკური მზაობა</label>
            <label class="option-label"><input type="radio" name="barrier" value="Time"> დროის დეფიციტი ახალი რუტინების დასანერგად</label>
            <label class="option-label"><input type="radio" name="barrier" value="Security"> მონაცემთა უსაფრთხოებისა და კონფიდენციალურობის შიში</label>
            <label class="option-label"><input type="radio" name="barrier" value="Donors"> დონორის მხრიდან მკაფიო გაიდლაინის არარსებობა</label>
            <label class="option-label"><input type="radio" name="barrier" value="None"> არანაირი ბარიერი: მზად ვართ დაუყოვნებლივ დასანერგად</label>
          </div>
        </div>
      </div>

      <!-- SECTION 5 -->
      <div class="section-card">
        <div class="section-header">
          <span class="section-num">ნაწილი 5</span>
          <h2 class="section-title">Net Promoter Score (NPS) და შემაჯამებელი უკუკავშირი</h2>
          <p class="section-desc">თქვენი რეკომენდაცია და ციტატა დონორის პროგრეს-ანგარიშისთვის</p>
        </div>

        <div class="form-group">
          <label class="form-label">5.1. რამდენად გაუწევდით რეკომენდაციას ამ ტრენინგს კოლეგას ან პარტნიორ ორგანიზაციას?</label>
          <div class="nps-box">
            <div class="nps-row" id="npsRow">
              <button type="button" class="nps-btn detractor" onclick="selectNPS(0)">0</button>
              <button type="button" class="nps-btn detractor" onclick="selectNPS(1)">1</button>
              <button type="button" class="nps-btn detractor" onclick="selectNPS(2)">2</button>
              <button type="button" class="nps-btn detractor" onclick="selectNPS(3)">3</button>
              <button type="button" class="nps-btn detractor" onclick="selectNPS(4)">4</button>
              <button type="button" class="nps-btn detractor" onclick="selectNPS(5)">5</button>
              <button type="button" class="nps-btn detractor" onclick="selectNPS(6)">6</button>
              <button type="button" class="nps-btn passive" onclick="selectNPS(7)">7</button>
              <button type="button" class="nps-btn passive" onclick="selectNPS(8)">8</button>
              <button type="button" class="nps-btn promoter" onclick="selectNPS(9)">9</button>
              <button type="button" class="nps-btn promoter" onclick="selectNPS(10)">10</button>
            </div>
            <div class="nps-legend">
              <span>0 = საერთოდ არ გავუწევდი</span>
              <span id="npsCategoryText" style="font-weight: 800; color: #1e3a8a;">აირჩიეთ ქულა</span>
              <span>10 = უმაღლეს რეკომენდაციას გავუწევდი</span>
            </div>
          </div>
          <input type="hidden" id="npsValue" name="nps" value="">
        </div>

        <div class="form-group">
          <label class="form-label" for="txtValue">5.2. რა იყო თქვენთვის ამ ტრენინგის ყველაზე ღირებული შედეგი? (ანონიმური ციტატა დონორისთვის)</label>
          <textarea class="form-control" id="txtValue" rows="3" placeholder="გთხოვთ გაგვიზიაროთ თქვენი აზრი..."></textarea>
        </div>

        <div class="form-group">
          <label class="form-label" for="txtFeedback">5.3. რა შეიძლებოდა ყოფილიყო უკეთესი ან რა თემას დაუთმობდით მეტ დროს მომავალში?</label>
          <textarea class="form-control" id="txtFeedback" rows="2" placeholder="თქვენი რეკომენდაცია ორგანიზატორებს..."></textarea>
        </div>

        <div class="action-bar">
          <button type="button" class="btn btn-secondary" onclick="window.print()">🖨️ ბეჭდვა / PDF შენახვა</button>
          <button type="button" class="btn btn-primary" onclick="submitAssessment()">✓ შეფასების გაგზავნა</button>
        </div>

      </div>

    </form>
  </main>

  <div id="toast" class="toast">შეფასება წარმატებით დაფიქსირდა! მადლობა მონაწილეობისთვის.</div>

  <script>
    const scores = {};

    function setScore(btn, field, val) {
      scores[field] = val;
      const parent = btn.parentElement;
      parent.querySelectorAll('.scale-btn').forEach(b => {
        b.classList.remove('active-pre', 'active-post');
      });
      const cls = field.endsWith('_pre') ? 'active-pre' : 'active-post';
      btn.classList.add(cls);
      const lbl = document.getElementById('lbl_' + field);
      if (lbl) lbl.textContent = val + ' / 5';
    }

    function selectNPS(val) {
      document.getElementById('npsValue').value = val;
      const buttons = document.querySelectorAll('.nps-btn');
      buttons.forEach(b => b.classList.remove('selected'));
      buttons[val].classList.add('selected');

      const txt = document.getElementById('npsCategoryText');
      if (val <= 6) {
        txt.textContent = `ქულა: ${val} (Detractor)`;
        txt.style.color = '#ef4444';
      } else if (val <= 8) {
        txt.textContent = `ქულა: ${val} (Passive)`;
        txt.style.color = '#f59e0b';
      } else {
        txt.textContent = `ქულა: ${val} (Promoter)`;
        txt.style.color = '#10b981';
      }
    }

    function submitAssessment() {
      const toast = document.getElementById('toast');
      toast.style.display = 'block';
      setTimeout(() => {
        toast.style.display = 'none';
      }, 4000);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  </script>
</body>
</html>
"""

with open("eu4dialogue/pm/post-training-evaluation.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Generated eu4dialogue/pm/post-training-evaluation.html successfully!")

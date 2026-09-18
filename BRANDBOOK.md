# Basilaia AI Network - Official Brandbook & Design System

> **სრული ოფიციალური სახელმძღვანელო (Brand Guidelines, Visual Identity & UI Architecture)**
> ავტორი და მფლობელი: **გიორგი ბასილაია (Giorgi Basilaia)**
> ვერსია: 2.0 (2026) | სტატუსი: Active

---

## 1. ბრენდის არსი და არქიტექტურა (Brand Architecture)

### 1.1 მისია და ხედვა
**Basilaia AI Network** არის წამყვანი ქართული საგანმანათლებლო, ტექნოლოგიური და ეგზეკუტიური AI ეკოსისტემა, რომლის მიზანია ხელოვნური ინტელექტის, ავტომატიზაციისა და No-Code ტექნოლოგიების ინტეგრაცია პროფესიულ და კორპორატიულ საქმიანობაში.

### 1.2 ბრენდის იერარქია (Masterbrand & 6 Pillars)
ეკოსისტემა ეფუძნება **ქოლგა მასტერ-ბრენდს (Masterbrand)** და **6 სპეციალიზებულ პილარ-დომენს**:

```
                              [ basilaia.com ]
                        Masterbrand & Central Hub
                                    │
    ┌──────────────┬──────────────┼──────────────┬──────────────┬──────────────┐
    ▼              ▼              ▼              ▼              ▼              ▼
chatgpt.ge      make.ge     elevenlabs.ge  perplexity.ge   lovable.ge    gipa / teens
GenAI კურსები  No-Code Auto     Voice AI       AI Search      AI Web Apps   პროგრამები
& B2B ტრენინგი & AI Agents    & ხმის კლონი   & Deep Research & Vibe Coding  & აკადემია
```

---

## 2. 6 პილარის ბრენდ-მატრიცა და როლები

| პილარი | დომენი | ძირითადი მისია | პირველადი ფერი | აქცენტის ფერი | აიკონი |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Masterbrand** | `basilaia.com` | აკადემიური ავტორიტეტი, ეგზეკუტიური AI საკონსულტაციო | Royal Magenta (`#ec4899`) | Indigo (`#6366f1`) | 🏛️ Crest / "GB" |
| **GenAI Courses** | `chatgpt.ge` | ფლაგმანი პრაქტიკული AI კურსი და კორპორატიული B2B ტრენინგი | Electric Indigo (`#6366f1`) | Pink Accent (`#ec4899`) | 🎓 AI Sparkle |
| **Automation** | `make.ge` | No-Code ავტომატიზაცია, n8n, AI აგენტები, MCP & Local LLMs | Cyber Sky (`#38bdf8`) | Neon Lime (`#a6ff96`) | ⚡ Bolt |
| **Voice AI** | `elevenlabs.ge` | Voice AI, ქართული Text-to-Speech, ხმის კლონირება & აუდიო | Warm Amber (`#f59e0b`) | Sun Gold (`#fbbf24`) | 🎙️ Sound Wave |
| **AI Search** | `perplexity.ge` | AI საძიებო სისტემა, Deep Research, ფაქტების შემოწმება & AEO | Emerald Green (`#10b981`) | Fresh Mint (`#34d399`) | 🔍 Compass |
| **AI Apps** | `lovable.ge` | Full-Stack AI ვებ-აპლიკაციები & Vibe Coding (React, Supabase) | Vivid Coral (`#ff4b72`) | Rose Purple (`#8b5cf6`)| 💜 Code Heart |

---

## 3. ფერთა სისტემა და დიზაინ-ტოკენები (Color Systems)

### 3.1 ოქროს წესი: Day Theme (Default)
მომხმარებლის მკაცრი მოთხოვნის შესაბამისად, **ყველა ვებ-გვერდი ნაგულისხმევად იხსნება Day Theme-ში (ნათელი, სუფთა დღის რეჟიმი)**. ღამის რეჟიმი (Night Mode) ხელმისაწვდომია გადამრთველით და ინახება მომხმარებლის ლოკალურ მეხსიერებაში (`localStorage`).

### 3.2 საერთო გლობალური პალიტრა (Day Mode - Default)
```css
:root {
  /* Surfaces & Backgrounds */
  --bg-main: #f8fafc;            /* სუფთა ნათელი ფონი (Slate-50) */
  --bg-surface: #ffffff;         /* თეთრი ქარდები და პანელები */
  --bg-surface-elevated: #ffffff;
  --border-subtle: rgba(0, 0, 0, 0.08);
  --border-card: rgba(0, 0, 0, 0.12);

  /* Typography */
  --text-primary: #090d16;       /* მკაფიო მუქი მთავარი ტექსტი */
  --text-secondary: #475569;     /* Slate-600 მეორადი ტექსტი */
  --text-muted: #64748b;         /* Slate-500 დამხმარე ტექსტი */

  /* Shadows for Depth on Light Background */
  --shadow-sm: 0 2px 8px rgba(15, 23, 42, 0.04);
  --shadow-md: 0 8px 24px rgba(15, 23, 42, 0.06);
  --shadow-lg: 0 16px 40px rgba(15, 23, 42, 0.08);

  /* Universal Network Bar (Light) */
  --net-bg: rgba(255, 255, 255, 0.95);
  --net-border: rgba(0, 0, 0, 0.08);
  --net-text: #334155;
}
```

### 3.3 საერთო გლობალური პალიტრა (Night Mode - Optional Toggle)
```css
body.night-mode {
  --bg-main: #090d16;            /* ღრმა მუქი კოსმოსური ფონი */
  --bg-surface: #0f172a;         /* Slate-900 ქარდის ზედაპირი */
  --bg-surface-elevated: #1e293b;
  --border-subtle: rgba(255, 255, 255, 0.08);
  --border-card: rgba(255, 255, 255, 0.12);

  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;

  --shadow-md: 0 10px 30px rgba(0, 0, 0, 0.5);

  --net-bg: rgba(8, 12, 22, 0.94);
  --net-border: rgba(255, 255, 255, 0.08);
  --net-text: #cbd5e1;
}
```

### 3.4 6 პილარის ინდივიდუალური ფერადი კოდები
- **Masterbrand (`basilaia.com`):** Hex `#ec4899` | RGB `(236, 72, 153)` | Dot Glow: `rgba(236, 72, 153, 0.6)`
- **ChatGPT.ge:** Hex `#6366f1` | RGB `(99, 102, 241)` | Dot Glow: `rgba(99, 102, 241, 0.6)`
- **Make.ge:** Hex `#38bdf8` | RGB `(56, 189, 248)` | Dot Glow: `rgba(56, 189, 248, 0.6)`
- **ElevenLabs.ge:** Hex `#f59e0b` | RGB `(245, 158, 11)` | Dot Glow: `rgba(245, 158, 11, 0.6)`
- **Perplexity.ge:** Hex `#10b981` | RGB `(16, 185, 129)` | Dot Glow: `rgba(16, 185, 129, 0.6)`
- **Lovable.ge:** Hex `#ff4b72` | RGB `(255, 75, 114)` | Dot Glow: `rgba(255, 75, 114, 0.6)`

---

## 4. ტიპოგრაფიული წესები (Typography Guidelines)

### 4.1 ძირითადი შრიფტები
1. **პირველადი შრიფტი (Primary Brand Font):** `FiraGO`
   - გამოყენება: ყველა სათაური (Headings), ძირითადი ტექსტი (Body), ნავიგაცია და ღილაკები.
   - ხელმისაწვდომი წონები: Light (300), Regular (400), Medium (500), SemiBold (600), Bold (700), ExtraBold (800).
   - წყარო: `https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css`
2. **დამხმარე ტექნიკური შრიფტი (Code & Monospace):** `JetBrains Mono`
   - გამოყენება: კოდის ბლოკები, ტექნიკური მონაცემები, სესიების ნომრები, API პარამეტრები.

### 4.2 ტიპოგრაფიული მასშტაბი (Type Scale)
- **Display 1 (Hero Title):** `clamp(2.4rem, 5vw, 3.8rem)` | Weight: 800/900 | Line-height: 1.15
- **Heading 1 (H1):** `2.2rem - 2.8rem` | Weight: 800 | Line-height: 1.2
- **Heading 2 (H2):** `1.8rem - 2.2rem` | Weight: 700 | Line-height: 1.25
- **Heading 3 (H3):** `1.3rem - 1.5rem` | Weight: 700 | Line-height: 1.3
- **Lead Paragraph:** `1.15rem - 1.25rem` | Weight: 400/500 | Line-height: 1.6
- **Body Text:** `1rem` (16px) | Weight: 400 | Line-height: 1.65
- **Small / Badges:** `0.75rem - 0.85rem` | Weight: 600/700 | Letter-spacing: 0.04em

### 4.3 კრიტიკული გრამატიკული და სტილისტური წესები
1. **მკაცრად აკრძალულია გრძელი ტირე `—` (Em-dash):**
   - მთელ პროექტში, სათაურებში, აღწერებსა და კოდში გამოიყენება **მხოლოდ სტანდარტული დეფისი `-` (Hyphen)**.
   - არასწორი: `AI — ხელოვნური ინტელექტი — კურსი`
   - სწორი: `AI - ხელოვნური ინტელექტი - კურსი`
2. **ქართული ბრჭყალები:**
   - გამოიყენება ქართული ტრადიციული ბრჭყალები: `„...“`
3. **ტექნიკური ტერმინოლოგიის შენარჩუნება:**
   - ტექნიკური აბრევიატურები და საერთაშორისო ტერმინები იწერება ინგლისურად: `API`, `ROI`, `Prompt`, `MCP`, `LLM`, `RAG`, `Zero Data Leakage`, `Vibe Coding`.

---

## 5. ლოგო და აიკონოგრაფია (Logo & Iconography System)

### 5.1 მასტერბრენდის ლოგო (`Basilaia AI Network` / `GB Crest`)
- **სიმბოლო:** ელეგანტური გეომეტრიული კვადრატი 6px რადიუსით, "GB" მონოგრამით და გრადიენტით:
  `background: linear-gradient(135deg, #ec4899, #6366f1);`
- **სატექსტო ნაწილი:** `GIORGI BASILAIA` ან `BASILAIA AI NETWORK`
- **ბეიჯი:** `AI NETWORK` (White on Gradient)

### 5.2 უსაფრთხო ველი (Clearspace Rule)
- ლოგოს გარშემო დაცული უნდა იყოს მინიმუმ **1X Clearspace**, სადაც X უდრის "G"-ს ან აიკონის სიგანის 50%-ს.
- არანაირი ტექსტი ან გრაფიკული ელემენტი არ უნდა შედიოდეს უსაფრთხო ველში.

### 5.3 ლოგოს არასწორი გამოყენება (Misuse Rules)
- ❌ არ შეცვალოთ ლოგოს პროპორციები (დაჭიმვა, შევიწროება).
- ❌ არ გამოიყენოთ არაავტორიზებული ფერები (მაგ. მწვანე chatgpt.ge-სთვის).
- ❌ არ მოათავსოთ ლოგო დაბალი კონტრასტის მქონე ფერად ფონზე ჩარჩოს გარეშე.
- ❌ არ შეცვალოთ FiraGO შრიფტი სხვა შრიფტით.

---

## 6. Universal Network Bar სტანდარტი

**Universal Network Bar** არის ეკოსისტემის დამაკავშირებელი მთავარი ელემენტი, რომელიც განთავსებულია ყველა 6 საიტის ზედა ნაწილში (`position: fixed` ან `sticky`).

### 6.1 სტრუქტურა:
```html
<header id="basilaia-network-bar" role="navigation" aria-label="Basilaia AI Network">
  <div class="bnb-inner">
    <a href="https://basilaia.com" class="bnb-brand" title="Giorgi Basilaia AI Ecosystem">
      <span class="bnb-brand-badge">AI NETWORK</span>
      <span class="bnb-brand-title">გიორგი ბასილაია</span>
    </a>
    <nav class="bnb-links">
      <a href="https://chatgpt.ge" class="bnb-item bnb-chatgpt" title="...">
        <span class="bnb-dot"></span>
        <span class="bnb-name">chatgpt.ge</span>
        <span class="bnb-desc">· AI კურსები & B2B</span>
      </a>
      <a href="https://make.ge" class="bnb-item bnb-make" title="...">
        <span class="bnb-dot"></span>
        <span class="bnb-name">make.ge</span>
        <span class="bnb-desc">· ავტომატიზაცია</span>
      </a>
      <a href="https://elevenlabs.ge" class="bnb-item bnb-elevenlabs" title="...">
        <span class="bnb-dot"></span>
        <span class="bnb-name">elevenlabs.ge</span>
        <span class="bnb-desc">· Voice AI & მედია</span>
      </a>
      <a href="https://perplexity.ge" class="bnb-item bnb-perplexity" title="...">
        <span class="bnb-dot"></span>
        <span class="bnb-name">perplexity.ge</span>
        <span class="bnb-desc">· ჭკვიანი ძიება</span>
      </a>
      <a href="https://lovable.ge" class="bnb-item bnb-lovable" title="...">
        <span class="bnb-dot"></span>
        <span class="bnb-name">lovable.ge</span>
        <span class="bnb-desc">· AI აპლიკაციები</span>
      </a>
      <a href="https://basilaia.com" class="bnb-item bnb-basilaia" title="...">
        <span class="bnb-dot"></span>
        <span class="bnb-name">basilaia.com</span>
        <span class="bnb-desc">· პროფილი</span>
      </a>
    </nav>
  </div>
</header>
```

---

## 7. საკომუნიკაციო სტილი და ტონი (Tone of Voice)

### 7.1 ტონის 3 საყრდენი
1. **ავტორიტეტული & მეცნიერულად დადასტურებული (Authoritative & Rigorous):**
   - გიორგი ბასილაიას 25+ წლიანი გამოცდილება, თავისუფალი უნივერსიტეტის ასოცირებული პროფესორის სტატუსი, 3388+ საერთაშორისო ციტირება Google Scholar-ზე.
2. **პრაქტიკული & ROI-ზე ორიენტირებული (Practical & Business-focused):**
   - აქცენტი კეთდება არა მშრალ თეორიაზე, არამედ რეალურ სამუშაო ნაკადებზე (+40% პროდუქტიულობა, 60% დროის ეკონომია).
3. **თანამედროვე & მინიმალისტური (Modern & Zero Bullshit):**
   - მარტივი, გასაგები ქართული ენა, გადატვირთული ბიუროკრატიის გარეშე.

### 7.2 ოფიციალური აკადემიური გალინკვა
როდესაც საიტზე ან მასალებში ნახსენებია **თბილისის თავისუფალი უნივერსიტეტი**, ის აუცილებლად უნდა გაილინკოს ოფიციალურ პროფილზე:
`https://freeuni.edu.ge/ge/details/?person=giorgi-basilaia`

---

## 8. სოციალური მედია და Open Graph (1200x630px)

ყველა საიტს გააჩნია 1200x630px ზომის ოფიციალური პრემიუმ საზიარო სურათი (`og-preview.png`):
- **ფორმატი:** PNG (1200 x 630 px)
- **მარჟინები:** 16px გარე საზღვარი, 4px ფერადი აქცენტის ხაზი თავში.
- **შინაარსი:**
  - ზედა ბეიჯი: კაპიტალიზებული კატეგორია (`AI IN PRACTICE * GIORGI BASILAIA`)
  - ცენტრალური სათაური: 46px Bold
  - ქვესათაური: 26px Regular
  - მეტა-ხაზი: 20px Bold (საათები, სესიები, დომენი)
  - მარჯვენა ქვედა კუთხეში: ბრენდის ლოგო და "GB" მონოგრამა.

---

## 9. ანალიტიკა და Cross-Domain Tracking სტანდარტი

ყველა 6 დომენზე გამოყენებულია ერთიანი Google Analytics 4 გაზომვის ID (`G-YZQP4H949Q`) ავტომატური linker-ით:
```javascript
gtag('config', 'G-YZQP4H949Q', {
  'cookie_domain': 'auto',
  'linker': {
    'domains': ['chatgpt.ge', 'make.ge', 'elevenlabs.ge', 'perplexity.ge', 'lovable.ge', 'basilaia.com']
  }
});
```

---

*დოკუმენტი შექმნილია და დამტკიცებულია Basilaia AI Network-ის მიერ. ყველა უფლება დაცულია (2026).*

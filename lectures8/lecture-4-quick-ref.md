# ლექცია 4: ვიზუალური კონტენტი და AI პრეზენტაციები — სწრაფი ცნობარი (Quick Reference)

---

## 🎨 1. 2026 წლის AI სურათების გენერატორების შედარება

| მოდელი | მთავარი ძალა | სუსტი მხარე | საუკეთესო გამოყენება |
|---|---|---|---|
| **Midjourney V8.2** | კინემატოგრაფიული ესთეტიკა, არტ-დირექცია, `--sref` & Edit Model | არ აქვს ჩატის ფორმატი, მოითხოვს გამოწერას | ბრენდინგი, სარეკლამო კამპანიები, კონცეპტ-არტი |
| **Flux 1.1 Pro** | ჰიპერ-ფოტორეალიზმი, ადამიანის ანატომია, პრომპტის ზუსტი შესრულება | რთული ლოკალური გაშვება მძლავრი GPU-ს გარეშე | რეალისტური პორტრეტები, პროდუქტის ფოტოგრაფია |
| **Nano Banana Pro (Gemini)** | ტექსტის უზადო რენდერინგი, დიაგრამები და ინფოგრაფიკა | შედარებით ნაკლები მხატვრული დრამატიზმი | ეტიკეტები, შეფუთვები, პოსტერები, ინფოგრაფიკა |
| **GPT Image 2.5 (ChatGPT)** | დიალოგური რედაქტირება, არსებული სურათის მოდიფიკაცია (Sunburst/Flare) | ხშირად ზედმეტად "გლუვი" / ხელოვნური იერი | სწრაფი იტერაციები, ლოკალური ცვლილებები |
| **Recraft v4.1** | სუფთა ვექტორული გრაფიკა (SVG), იკონოგრაფია, ლოგოები | არ არის გათვლილი რთულ ფოტორეალიზმზე | ვებ-გრაფიკა, იკონები, UI ელემენტები |

---

## 🏗️ 2. უნივერსალური პრომპტის ფორმულა (Prompt Anatomy)

```text
[Subject] + [Action] + [Environment] + [Lighting] + [Camera / Lens] + [Style & Mood] + [Parameters]
```

### 🧩 კომპონენტების ლექსიკონი:
- **Lighting:** `volumetric morning light`, `golden hour`, `dramatic chiaroscuro`, `soft diffused studio softbox`, `neon rim lighting`, `cinematic moody shadows`
- **Camera & Lens:** `shot on Sony A7 IV 85mm f/1.4 lens`, `35mm street photography`, `macro photography 100mm`, `wide angle 24mm architectural shot`, `drone aerial view`
- **Style & Texture:** `hyperrealistic editorial photography`, `natural skin pores and texture`, `matte ceramic texture`, `vintage Kodachrome 64 color grading`, `cinematic film grain`
- **Quality Negatives:** არ გამოიყენოთ "ugly, bad", არამედ გამოიყენეთ `--no blur, plastic skin, deformed hands`

---

## ⚙️ 3. Midjourney პარამეტრების სრული Cheat Sheet

| პარამეტრი | დანიშნულება | მაგალითი |
|---|---|---|
| `--ar [X:Y]` | Aspect Ratio (გვერდების თანაფარდობა) | `--ar 16:9` (ჰორიზონტალური), `--ar 9:16` (Reels/Stories), `--ar 4:5` (Instagram), `--ar 1:1` |
| `--sref [URL]` | Style Reference — სტილისა და ფერთა პალიტრის გადატანა | `--sref https://example.com/style.jpg` |
| `--sw [0-1000]` | Style Weight — სტილის ზეგავლენის ძალა (ნაგულისხმევი: 100) | `--sw 250` (ძლიერი სტილიზაცია) |
| `--cref [URL]` | Character Reference — პერსონაჟის სახისა და იდენტობის შენარჩუნება | `--cref https://example.com/face.jpg` |
| `--cw [0-100]` | Character Weight — ტანსაცმლისა და ვარცხნილობის შენარჩუნება | `--cw 100` (სახე+ტანსაცმელი), `--cw 0` (მხოლოდ სახე) |
| `--v [6/7/8]` | მოდელის ვერსია | `--v 8.1` |
| `--stylize [0-1000]` | Midjourney-ის საკუთარი მხატვრული თავისუფლება | `--s 50` (მკაცრი პრომპტი), `--s 750` (მაღალი არტი) |
| `--chaos [0-100]` | 4 გენერირებული ვარიანტის მრავალფეროვნება | `--c 20` |
| `--no [ელემენტები]` | ნეგატიური პრომპტი (რისი გამორიცხვა გვინდა) | `--no text, watermark, frame, blurry` |

---

## 🔄 4. ვიზუალური კონსისტენტურობა (Consistency Blueprint)

### ერთი და იგივე პერსონაჟის მართვა:
1. **ნაბიჯი 1:** შექმენით პერსონაჟის საწყისი, ნეიტრალური პორტრეტი (`studio lighting, neutral white background, front view --ar 1:1`);
2. **ნაბიჯი 2:** აიღეთ სურათის პირდაპირი ბმული;
3. **ნაბიჯი 3:** ახალ პრომპტში დაამატეთ:
   ```text
   The same character [ახალი მოქმედება და გარემო] --cref [URL] --cw 20 --ar 16:9
   ```

### ბრენდის ერთიანი სტილის მართვა:
1. შეარჩიეთ 1-3 სურათი, რომელიც ზუსტად გამოხატავს თქვენი ბრენდის ფერებს;
2. ახალ პროდუქტზე მუშაობისას გამოიყენეთ:
   ```text
   [ახალი პროდუქტი] --sref [URL1] [URL2] --sw 150
   ```

---

## 📊 5. Gamma AI & Canva Magic Studio გზამკვლევი

### 🚀 Gamma AI 2-წუთიანი Workflow:
1. **Outline Prompt (Claude/ChatGPT-ში):**
   ```text
   "შექმენი 6-ბარათიანი Pitch Deck outline თემაზე: [თემა]. 
   თითოეული ბარათისთვის: სათაური, 3 ბულეტი, ვიზუალური აღწერა.
   მოარგე Gamma.app-ის 'Paste text' ფორმატს."
   ```
2. **Gamma-ში ჩასმა:** გახსენით `gamma.app` → *New with AI* → *Paste in text* → აირჩიეთ ბარათების რაოდენობა;
3. **სურათების ჩანაცვლება:** Gamma-ს სურათების ნაცვლად ატვირთეთ თქვენი AI ვიზუალები;
4. **ექსპორტი:** გააზიარეთ ცოცხალი ბმულით ან დააექსპორტეთ PDF/PowerPoint-ში.

### 🎨 Canva Magic Studio & ქართული ტიპოგრაფია:
- **წესი #1:** არასდროს სთხოვოთ Midjourney-ს ქართული ტექსტის ჩაწერა გამოსახულებაში (მიიღებთ დამახინჯებულ სიმბოლოებს);
- **წესი #2 (ჰიბრიდული მეთოდი):** დააგენერირეთ სუფთა ვიზუალი ცარიელი სივრცით (Negative Space) → გადაიტანეთ Canva-ში → დააწერეთ ტექსტი ქართული ფონტებით (**FiraGO**, **Noto Sans Georgian**);
- **Magic Switch:** 1 კლიკით გადააკეთეთ პრეზენტაცია Instagram პოსტად ან ბროშურად.

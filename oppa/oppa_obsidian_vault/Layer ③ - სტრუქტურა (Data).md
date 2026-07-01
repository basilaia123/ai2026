# Layer ③ - სტრუქტურა (Data & Vision)

> **ფენა ③ ხდის მონაცემებს ხელშესახებს.** Multimodal Vision, Coda HR, Advanced Data Analysis, KPI Dashboard და AML Screening - ყველაფერი, რაც საშუალებას გვაძლევს უსაფრთხო გარემოში რთული ფინანსური მონაცემები და PayBox-ის ეკრანები ვიზუალურად დავამუშაოთ.

- **ფენის ნომერი:** ③ (3)
- **ფენის ტიპი:** სტრუქტურა / Structure
- **მასშტაბი:** 1 სესია (3 საათი)

## 🔗 კავშირები

### 📅 სესიები ამ ფენაში
- [[Session 4 - Multimodal & Coda]]

### 🧠 კონცეფციები
- [[Concept - PII Compliance & Security]] (წინა ფენიდან)
- [[Concept - Data Warehousing & Analytics]]
- [[Concept - Knowledge Base & RAG]]

### 🛠 ხელსაწყოები
- [[Tool - Claude Anthropic]]
- [[Tool - ChatGPT OpenAI]]
- [[Tool - ChatGPT Advanced Data Analysis]] ★
- [[Tool - Gemini Google]]
- [[Tool - Claude Code CLI]] ★
- [[Tool - Coda.io]] ★
- [[Tool - Claude for Excel Add-in]]
- [[Tool - Napkin.ai]]
- [[Tool - Stripe]]

### 📦 Deliverables
- [[Deliverable - PayBox UI Diagnostic]]
- (Coda HR Database, KPI Dashboard, AML Pipeline - S4 outputs)

## 📚 ფენის შინაარსი

### S4 - Data · Vision · Coda

**ხუთი ძირითადი ბლოკი:**

1. **Multimodal Vision** - სურათიდან დიაგნოზამდე (PayBox-ის ეკრანი → ანალიზი)
2. **Advanced Data Analysis** - Excel/CSV-ის სტრუქტურული დამუშავება
3. **Coda.io HR & Docs** - კანდიდატების სკრინინგი + მონაცემთა ბაზა
4. **KPI Dashboard** - OPPA-ს 8+ მეტრიკა (transactions, success rate, etc.)
5. **AML Screening Pipeline** - ტრანზაქციების ფლაგირება
6. **Reconciliation** - ფინანსური შეჯამების ავტომატიზაცია
7. **Claude Code Live Demo** - SQL/Legacy კოდთან პირველი შეხება

## 📊 PayBox Vision Workflow

```
ფოტო/სქრინი → Claude Vision → XML Tags + CoT → 
Diagnosis + Action → Slack Notification
```

## 📤 რა გადაეცემა შემდეგ ფენებს

- **→ ④ ძრავა (S5):** მონაცემთა ბაზა და Vision ლოგიკა Make.com ფლოუების საფუძველია
- **→ ⑤ პროდუქტი (S6):** SQL Index Optimization, Dashboard-ის ლოგიკა Lovable UI-ში

## ⚠️ მეტა-შენიშვნა

> „მონაცემები ფილტრზეა აშენებული: S4-ის Vision ანალიზი არ იქნებოდა უსაფრთხო S3-ის Sanitizer-ის გარეშე - PayBox-ის ეკრანზე PII-ის გაშვება Vision-ზე რისკია. **ფილტრი → მონაცემები → ძრავა.**"
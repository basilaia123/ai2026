# Deliverable: OPPA Sanitizer

- **Type:** Course Deliverable
- **Concept Origin:** [[Concept - PII Compliance & Security]]
- **Sessions:** [[Session 0 - Training Landscape]] (⚠️ ოქროს წესი) → [[Session 3 - Compliance & Sanitizer]] (★ ფორმალიზაცია) → [[Session 5 - Make.com Automation]] (ჩაშენება) → [[Session 6 - Lovable & Prod]] (Production Bot)
- **Primary Tool:** [[Tool - Claude Code CLI]]
- **Concept:** [[Concept - PII Compliance & Security]]

## 📝 აღწერა / Description
პერსონალური მონაცემების (PII) ფილტრაციისა და გასუფთავების სკრიპტი, რომელიც მორგებულია საქართველოს ეროვნული ბანკის კომპლიანსის მოთხოვნებზე.
A security script that filters and cleans client Personal Identifiable Information (PII) before routing data to AI models, compliant with National Bank of Georgia regulations.

## 📜 ევოლუცია / Evolution

### 🌱 S0 - ოქროს წესის დაბადება (21 აპრილი, 2026)
S0-ში პირველად ჩამოყალიბდა **PII-ის ოქროს წესი**:
> „არასოდეს გაუგზავნოთ ხელოვნურ ინტელექტს კლიენტის ID, IBAN ან პერსონალური მონაცემები. ყოველთვის გამოიყენეთ ანონიმიზაცია (მაგალითად: 'კლიენტი X')."

ეს იყო კონცეფცია, არა პროდუქტი - მაგრამ ეს იყო **OPPA Sanitizer-ის გერმი**.

### 🔧 S3 - ფორმალიზაცია
S3-ში ოქროს წესი გადაიქცა **4-ნაბიჯიან Sanitizer-ად**:
1. წინასწარი ფილტრაცია
2. ანონიმიზაცია (კლიენტი X, თანხა Y, თარიღი Z)
3. მოდელის შეტყობინება
4. პოსტ-ვალიდაცია

### ⚙️ S5 - ჩაშენება
S5-ში Sanitizer ჩაიშენა Make.com-ის ყველა ნაკადში (Support Triage, KYC, Fraud Detection).

### 🚀 S6 - Production
S6-ში Sanitizer-ის წესები გახდა Production Slack Bot-ის ნაწილი, Claude Code-ით დაწერილი.

## 🔗 კავშირები / Links

### 📅 Sessions
- [[Session 0 - Training Landscape]] (წარმოშობა)
- [[Session 3 - Compliance & Sanitizer]] (ფორმალიზაცია)
- [[Session 5 - Make.com Automation]] (ჩაშენება)
- [[Session 6 - Lovable & Prod]] (Production)

### 🧱 Knowledge Layers
- [[Layer ⓪ - შესავალი (AI ანატომია)]]
- [[Layer ② - ფილტრი (Compliance)]]
- [[Layer ④ - ძრავა (Automation)]]
- [[Layer ⑤ - პროდუქტი (Production)]]

### 🧠 Concepts
- [[Concept - PII Compliance & Security]] ⭐
- [[Concept - Prompt Formula & Self-Critique]] (Self-Critique → Hallucination Validation)
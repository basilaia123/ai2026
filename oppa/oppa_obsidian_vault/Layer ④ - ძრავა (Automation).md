# Layer ④ - ძრავა (Automation)

> **ფენა ④ აკავშირებს ყველაფერს ერთ ნაკადად.** S1-ის პრომპტები, S3-ის უსაფრთხოება და S4-ის მონაცემთა ლოგიკა Make.com-ში ერთიანდება ავტომატურ KYC, Support Triage და ბილინგის სორტირების ნაკადებად.

- **ფენის ნომერი:** ④ (4)
- **ფენის ტიპი:** ძრავა / Engine
- **მასშტაბი:** 1 სესია (3 საათი)

## 🔗 კავშირები

### 📅 სესიები ამ ფენაში
- [[Session 5 - Make.com Automation]]

### 🧠 კონცეფციები
- [[Concept - Event-Driven Alerts]] ⭐ ცენტრალური
- [[Concept - PII Compliance & Security]] (Sanitizer ჩაშენებული)
- [[Concept - Prompt Formula & Self-Critique]] (Triage Classifier)

### 🛠 ხელსაწყოები
- [[Tool - Claude Anthropic]]
- [[Tool - Make.com]] ★ (S5-ში სრულად დაინერგა)
- [[Tool - n8n]]
- [[Tool - Slack]]
- [[Tool - Telegram]]
- [[Tool - Google Sheets =AI  =GEMINI]]
- [[Tool - Postman]]
- [[Tool - SMS Office]]
- [[Tool - Gmail]]
- [[Tool - Google Forms]]

### 📦 Deliverables
- [[Deliverable - Support Triage]] ⭐ (8,000+ ტერმინალის სორტირება)
- (KYC Onboarding Flow, 5+5 სცენარი, Error Handling Framework)

## 📚 ფენის შინაარსი

### S5 - Make.com · Triage · KYC · 10+ სცენარი

**ძირითადი ბლოკები:**

1. **Make.com Variables & Webhooks** - ფუნდამენტი
2. **5 მარტივი სცენარი** - Webhook → Router → Action
3. **Triage Classifier** - Prompt-based კლასიფიკაცია 8,000+ ბილეთზე
4. **Loops & Batch Processing** - მასიური ოპერაციები
5. **KYC Onboarding Flow** - 3-5 დღე → 15 წუთი
6. **5 რთული სცენარი** - Fraud, AML, Voice Integration
7. **Error Handling Framework** - Retry, Router, Fallback

## ⚙️ მთავარი სცენარი: Support Triage

```
PayBox Terminal → Support Ticket → 
Webhook → Make.com → Sanitizer (S3) → 
Triage Classifier (S1 Prompt) → 
Router → Tech Support / Finance / KYC → 
Slack #channel → Human Review
```

## 📤 რა გადაეცემა შემდეგ ფენას

- **→ ⑤ პროდუქტი (S6):** Make.com Webhook-ები საფუძველია Lovable UI-ისა და Production Slack Bot-ისთვის

## ⚠️ მეტა-შენიშვნა

> „ავტომატიზაცია ყველაფერს აკავშირებს: S5-ის Make.com ფაქტობრივად „წერს" S1-ის პრომპტებს, S3-ის Sanitizer-ს, S4-ის მონაცემთა ბაზას ერთ ნაკადად. **ეს არის integration ფენა, სადაც ხდება ⓪→⑤-ის კონვერგენცია.**"
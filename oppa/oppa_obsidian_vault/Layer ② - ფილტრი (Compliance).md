# Layer ② - ფილტრი (Compliance)

> **ფენა ② ქმნის დამცავ კედელს.** სანამ მონაცემებს ავტომატიზაციას მივცემთ, ვაყალიბებთ PII Sanitization-ს, Jailbreak დაცვას, Hallucination Validation-ს და Brand Voice-ს - NBG-ის რეგულაციების შესაბამისად.

- **ფენის ნომერი:** ② (2)
- **ფენის ტიპი:** ფილტრი / Filter
- **მასშტაბი:** 1 სესია (3 საათი)

## 🔗 კავშირები

### 📅 სესიები ამ ფენაში
- [[Session 3 - Compliance & Sanitizer]]

### 🧠 კონცეფციები
- [[Concept - PII Compliance & Security]] ⭐ ცენტრალური
- [[Concept - Prompt Formula & Self-Critique]] (Self-Critique → Hallucination Validation)

### 🛠 ხელსაწყოები
- [[Tool - Claude Anthropic]]
- [[Tool - Notion AI]]
- [[Tool - Claude Artifacts]]
- [[Tool - Google AI Studio]]

### 📦 Deliverables
- [[Deliverable - OPPA Sanitizer]] ⭐ მთავარი აქტივი

## 📚 ფენის შინაარსი

### S3 - PII · Compliance · Sanitizer

**ოთხი ძირითადი ბლოკი:**

1. **NBG-ის რეგულაციები** - რა შეიძლება და რა არა AI-სთვის ფინტექ-კომპანიაში
2. **PII Anonymization** - 4-ნაბიჯიანი ანონიმიზაცია (სახელი, ID, IBAN, მისამართი)
3. **Prompt Injection / Jailbreak Defense** - მოდელის მანიპულაციისგან დაცვა
4. **Hallucination Validation** - ფაქტების შემოწმების პროტოკოლი
5. **Brand Voice Converter** - ტონის შენარჩუნება 5 სცენარში
6. **Compliance Checklist** - ჩეკლისტი ყოველ ავტომატიზაციამდე

## 🛡 OPPA Sanitizer-ის 4 ნაბიჯი

1. **წინასწარი ფილტრაცია** - კლიენტის პერსონალური მონაცემების მონიშვნა
2. **ანონიმიზაცია** - „კლიენტი X", „თანხა Y", „თარიღი Z"
3. **მოდელის შეტყობინება** - სისტემური პრომპტი: „მონაცემები ანონიმურია"
4. **პოსტ-ვალიდაცია** - გამოსვლის შემოწმება PII-ზე

## 📤 რა გადაეცემა შემდეგ ფენებს

- **→ ③ სტრუქტურა (S4):** PII ფილტრი Vision ანალიზის წინ
- **→ ④ ძრავა (S5):** Sanitizer Make.com ფლოუებში ჩაშენებული
- **→ ⑤ პროდუქტი (S6):** Bot-ში Sanitizer-ის წესები

## ⚠️ მეტა-შენიშვნა

> „ფილტრი ფუნდამენტზე ადრე უნდა ჩამოყალიბდეს: ჯერ უნდა დაინახონ პრომპტის ძალა, მერე - მისი საფრთხე. **OPPA-ს PII ოქროს წესი დაიწყო სესია 0-ში, ფორმალიზდა სესია 3-ში.**"
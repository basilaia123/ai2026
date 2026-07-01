# Concept: Prompt Formula & Self-Critique

- **Type:** Cross-Cutting Concept
- **Origin Session:** [[Session 0 - Training Landscape]]
- **Georgian Description:** პრომპტის უნივერსალური ფორმულა (Role + Context + Task) და „თვითკრიტიკის" ტექნიკა - ხელოვნურ ინტელექტს სთხოვს საკუთარი პასუხის გადამოწმება. ორივე ტექნიკა დაიწყო სესია 0-ში და გამოიყენება ყველა მომდევნო ფენაში.
- **English Description:** Universal prompt formula (Role + Context + Task) and Self-Critique technique that asks AI to verify its own answer. Both originated in Session 0 and are used across all subsequent layers.

## 🔗 კავშირები

### 📅 სესიები, სადაც გამოიყენება
- [[Session 0 - Training Landscape]] ⭐ პირველად
- [[Session 1 - Prompting & Projects]] (Role/CoT/Few-Shot-ის საფუძველი)
- [[Session 3 - Compliance & Sanitizer]] (Self-Critique → Hallucination Validation)
- [[Session 5 - Make.com Automation]] (Triage Classifier Prompt)

### 🧱 Knowledge Layers
- [[Layer ⓪ - შესავალი (AI ანატომია)]]
- [[Layer ① - საფუძველი (Prompting)]]
- [[Layer ② - ფილტრი (Compliance)]]
- [[Layer ④ - ძრავა (Automation)]]

## 📐 პრომპტის უნივერსალური ფორმულა

```
[ROLE]       - ვინ არის AI ამ კონტექსტში
[CONTEXT]    - რა იცის / რა უნდა გაითვალისწინოს
[TASK]       - რა უნდა გააკეთოს კონკრეტულად
[FORMAT]     - როგორ დააფორმატოს პასუხი
[CRITIQUE]   - გადაამოწმე შენი პასუხი შეცდომებზე
```

### მაგალითი (S0-დან, OPPA-სთვის):
```
[ROLE]      შენ ხარ ფინტექ HR სპეციალისტი
[CONTEXT]   OPPA.GE არის წამყვანი ფინტექი საქართველოში
[TASK]      შექმენი 3 კამპანია Gen Z-ის ჩასართავად
[FORMAT]    bullet points, ბუნებრივი ქართულით
[CRITIQUE]  შეამოწმე შენი პასუხი: რისკები და მოლოდინები მითითებულია?
```

## 🔄 Self-Critique Pattern

> „სანამ დააბრუნებ პასუხს, გადაამოწმე:
> 1. ფაქტების სიზუსტე
> 2. ლოგიკური თანმიმდევრობა
> 3. ბრძანების ყველა ნაწილის შესრულება
> 4. შესაძლო ჰალუცინაციები"

**S0-ში აღმოჩენილი:** Self-Critique ტექნიკა მნიშვნელოვნად ამცირებს ჰალუცინაციებს და აძლიერებს პასუხის ხარისხს.

## 📈 ევოლუცია სესიებში

| სესია | გამოყენება |
|---|---|
| S0 | Role+Context+Task ფორმულა პირველად |
| S1 | CoT, Few-Shot, Structured Output |
| S3 | Self-Critique → Hallucination Validation |
| S5 | Triage Classifier Prompt-ში |

## 💡 მეტა-შენიშვნა

> „ეს კონცეფცია არის **ხიდი** ფენა ⓪-სა და ფენა ⑤-ს შორის. პრომპტის ფორმულა, რომელიც სესია 0-ში 3-საათიანი დემოთი დაიწყო, ფინალურად გამოიყენება S6-ის SQL Refactor Prompt-ში და S5-ის Production Classifier-ში."
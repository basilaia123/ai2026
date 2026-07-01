# Tool: ChatGPT Custom GPT

- **Category:** LLM & Custom AI Assistant 📁
- **Tag:** No-Code AI Agent
- **Vendor:** OpenAI
- **Georgian Description:** ChatGPT Plus-ის ფარგლებში შექმნილი პერსონალური AI ასისტენტი, სადაც Instructions-ში ინახება სისტემური პრომპტი, Knowledge-ში - ფაილები, Actions-ში - API კავშირები. OPPA-სთვის S0-ში შეიქმნა პროტოტიპი.
- **English Description:** Custom GPT is a personalized AI assistant inside ChatGPT Plus where you store system prompts (Instructions), upload files (Knowledge), and connect APIs (Actions). For OPPA, a prototype was created in Session 0 as the foundation for later Hermes Skills.

## 🔗 კავშირები

### 📅 Sessions where used
- [[Session 0 - Training Landscape]] ⭐ შემოვიდა

### 🧠 Related Concepts
- [[Concept - Prompt Formula & Self-Critique]] (Instructions = Role+Context+Task)
- [[Concept - Low-Code UI Prototyping]] (No-Code პრინციპი)

### 🛠 Related Tools
- [[Tool - ChatGPT OpenAI]] (მშობელი პლატფორმა)
- [[Tool - Claude Projects]] (მსგავსი, Claude-ის ვერსია - S1)
- [[Tool - Hermes Agent Nous Research]] (ევოლუცია S6-ში)

### 🧱 Knowledge Layers
- [[Layer ⓪ - შესავალი (AI ანატომია)]]
- [[Layer ⑤ - პროდუქტი (Production)]]

## 🔧 როგორ შეიქმნა OPPA-სთვის (S0)

### 4 ნაბიჯი:

1. **ChatGPT → მარცხენა მენიუ → "Explore GPTs" → Create**
2. **Configure Tab:**
   - **Name:** „OPPA.GE Assistant"
   - **Description:** „ფინტეკ AI ასისტენტი"
3. **Instructions-ში** ჩაისვა სისტემური პრომპტი (Role+Context+Task ფორმულით)
4. **Conversation Starters:**
   - „დამეხმარე KYC დოკუმენტის შეჯამებაში"
   - „შემომთავაზე Gen Z-ის მარკეტინგული კამპანია"

## 📐 OPPA-ს Custom GPT-ის Instructions (ნიმუში)

```
შენ ხარ OPPA.GE-ს AI ასისტენტი - წამყვანი ფინტეკი საქართველოში.

შენი როლი:
- დაეხმარე გუნდს ყოველდღიური ამოცანების გადაჭრაში
- დაიცავი PII-ს კონფიდენციალურობას - არასოდეს მოითხოვო კლიენტის ID
- შეინარჩუნე OPPA-ს ბრენდის ტონი - პროფესიონალური, თბილი, ქართული

ფორმატი:
- პასუხები ბუნებრივ ქართულ ენაზე
- საჭიროებისას გამოიყენე bullet points
- რთული თემებისთვის გამოიყენე მაგალითები

თვითკრიტიკა:
სანამ პასუხს დააბრუნებ, შეამოწმე შენი ლოგიკა და ფაქტების სიზუსტე.
```

## 🎯 Custom GPT-ის როლი OPPA-ს ეკოსისტემაში

| Custom GPT (S0) | Claude Projects (S1) | Hermes Skill (S6) |
|---|---|---|
| OpenAI პლატფორმა | Anthropic პლატფორმა | Autonomous Agent |
| მომხმარებლის ინტერფეისი | Persistent Context | სრული autonomy |
| Plus $20/თვეში | Teams/Enterprise | Custom setup |

**ევოლუციური ხაზი:** Custom GPT → Claude Projects → Hermes Skill

## 💰 ღირებულება

- **ChatGPT Plus:** $20/თვე
- **ChatGPT Team:** $25/მომხმარებელი/თვე
- **ChatGPT Enterprise:** Custom pricing

## 🔗 სხვა რესურსები

- [OpenAI Custom GPT Docs](https://help.openai.com/en/articles/8554407)
- [GPT Store](https://chatgpt.com/gpts)

## 💡 მეტა-შენიშვნა

> „Custom GPT არის **ხიდი** მომხმარებლისთვის მოსახერხებელი AI და production-grade AI Agent-ს შორის. OPPA-ს S0-ში შექმნილი პროტოტიპი გახდა საფუძველი იმისა, რომ S6-ში Hermes Skill-ები შეიქმნა - უფრო მძლავრი, autonomous და domain-specific."
---
name: course-proposal-generator
description: >-
  Generates comprehensive, high-converting AI course proposals and corporate training offers in both
  Markdown (proposal.md) and interactive HTML (index.html) formats. Uses established templates and
  patterns from benchmark projects (Elplus, MedPharma, Avita, Heidelberg, Silk Development,
  Eurodrug, Orbi Group, McDonald's, Geo Hospitals). Activates whenever the user asks to create,
  structure, price, or adapt a course offer, syllabus, or corporate AI proposal for any client or industry.
---

# Course Proposal Generator Skill

ეს Skill გამოიყენება ახალი კურსებისა და კორპორატიული AI ტრენინგების სრულყოფილი შეთავაზებების შესაქმნელად.
Skill ავტომატურად აგენერირებს **ორთავე დელივერაბლს (Both Deliverables)**:
1. **`proposal.md`**: სრული, დეტალური, მაღალი დონის აღმასრულებელი წინადადება (სილაბუსი, ბიუჯეტი, ROI, მეთოდოლოგია).
2. **`index.html`**: ინტერაქტიული, კლიენტის ბრენდის ფერებზე მორგებული ვებ-პრეზენტაცია (Day Theme default, FiraGO, Sidebar/Top nav, ფასების გადამრთველი, პრომპტების კოპირება).

---

## 🏛️ 9 საორიენტაციო პროექტი (Benchmark Reference Base)

შეთავაზების სტრუქტურა და ტონი მკაცრად ეფუძნება რეპოზიტორიის 9 წარმატებულ პროექტს:
* დეტალური ანალიზისთვის იხილეთ [references/benchmark-projects.md](./references/benchmark-projects.md)

1. **„ელპლუსი“ (`elplus/`)**: საინჟინრო პროექტირება, MEP, სახანძრო უსაფრთხოება, ადგილობრივი წარმოება, ტენდერები (SPA/NAT), BoQ ექსტრაქცია.
2. **„მედფარმა +“ (`medpharma/`)**: ფარმაცევტული დისტრიბუცია, სამედიცინო აპარატურა, Executive მიკრო-ჯგუფი (4 პირი), Zero-to-Hero ადაპტაცია, NotebookLM, 2,000 ₾/სესია.
3. **„ავიტა“ (`avita/`)**: ფარმა-მარკეტინგი, სამედიცინო წარმომადგენლები (MedReps), ობიექციების დაძლევა, Audio Briefs, Notion CRM.
4. **„ჰანიველი / ჰაიდელბერგცემენტი“ (`heidelberg/`)**: სამრეწველო IT, კომპიუტერული ქსელები, Kurose-Ross 9th Ed, Wireshark ლაბორატორიები, Cisco Packet Tracer.
5. **„Silk Development“ (`silk/`)**: დეველოპმენტი, ჰოსპიტალითი, 2-ეტაპიანი მოდელი (კომპანიის ბაზა + 5 დეპარტამენტი: გაყიდვები, პროექტები, იურისტები, ფინანსები, PR), Claude Enterprise.
6. **„Eurodrug Laboratories“ (`eurodrug/`)**: საერთაშორისო ფარმაცევტული წარმომადგენლობა, PARTS & CREATE ჩარჩოები, Lovable დოზირების კალკულატორი.
7. **„ORBI Group“ (`orbi/`)**: მასშტაბური მშენებლობა (Central Park Towers), Claude Cowork დესკტოპ აგენტები, სატენდერო Bid Leveling (Togal/ConWize მეთოდი), Make.com ინვოისების ნაკადები, 7,000 ₾ პაკეტი.
8. **„მაკდონალდს საქართველო“ (`mcdonalds/`)**: QSR საოპერაციო მენეჯმენტი, თვითნასწავლი AI მომხმარებლები, Gemini Gems (Bolt/Wolt შეფასებები), Taylor მანქანის ვიზუალური დიაგნოსტიკა, Julius.ai ანალიტიკა.
9. **„ჯეო ჰოსპიტალსი“ (`gh/`)**: სამედიცინო და საავადმყოფოების ქსელი, კლინიკური დოკუმენტაცია, პაციენტებთან კომუნიკაცია, Day Theme ინტერაქტიული ვებ-პორტალი.

---

## 🔄 ნაბიჯ-ნაბიჯ სამუშაო პროცესი (Execution Workflow)

როდესაც მომხმარებელი ითხოვს ახალი კურსის ან ტრენინგის შეთავაზების მომზადებას:

### ნაბიჯი 1: კლიენტისა და ამოცანის იდენტიფიცირება
დაადგინეთ შემდეგი საკვანძო პარამეტრები:
- **დამკვეთი კომპანია და ინდუსტრია:** (მაგ. ფარმა, რითეილი, სამშენებლო, ფინანსები, წარმოება, სერვისი).
- **🤝 პარტნიორობა / ორგანიზატორი (სავალდებულო გადამოწმება):**
  > [!IMPORTANT]
  > **თუ მომხმარებლის მიერ პირდაპირ არ არის მითითებული, ვისთან პარტნიორობით კეთდება კურსი, აუცილებლად ჰკითხეთ მომხმარებელს შეთავაზების შექმნამდე!**
  > 
  > პარტნიორობის 3 ძირითადი ვარიანტი:
  > 1. **არავისთან (პირდაპირ გიორგი ბასილაია / დამოუკიდებელი საავტორო პროგრამა):**
  >    - სტატუსი: გიორგი ბასილაია — AI პრაქტიკოსი & კორპორატიული ტრანსფორმაციის კონსულტანტი (`basilaia.com`).
  >    - სერტიფიკატები: გიორგი ბასილაიას ოფიციალური საავტორო სერტიფიკატები.
  >    - ტექსტში არ გამოიყენება „Smart Academy-ს პარტნიორობით“ ან სხვა აკადემიის ხსენება.
  > 2. **Smart Academy (სმარტ აკადემია):**
  >    - სტატუსი: საგანმანათლებლო პარტნიორი — Smart Academy ([smartacademy.ge](https://smartacademy.ge)), კორპორატიული ტრენინგების დეპარტამენტი.
  >    - ტრენერი: Smart Academy-ს AI მიმართულების წამყვანი ლექტორი („AI — გენერაციული ინტელექტი პრაქტიკაში“).
  >    - სერტიფიკატები: Smart Academy-ს ოფიციალური ორენოვანი სერტიფიკატები (როგორც `medpharma`, `elplus`, `avita`, `heidelberg`).
  > 3. **სხვა ორგანიზაცია / საკონსულტაციო კომპანია (მაგ. Walnut, GIPA, GITA და სხვ.):**
  >    - სტატუსი: ორგანიზატორი — მაგალითად Walnut ([wtm.ge](https://www.wtm.ge/about-us/) როგორც `silk`-ში), GIPA, GITA ან კონკრეტული საკონსულტაციო ფირმა.
  >    - სერტიფიკატები: პარტნიორი ორგანიზაციისა და გიორგი ბასილაიას ერთობლივი სერტიფიკატები.
- **გუნდის ზომა და დონე:**
  - *Zero-to-Hero (ნულოვანი ბაზა):* საჭიროებს უსტრესო დაწყებას, ანგარიშების გამართვას (`medpharma`, `avita`).
  - *Advanced / თვითნასწავლი:* პირდაპირ გადადის კომპლექსურ Workflows-ზე (`mcdonalds`).
  - *მიკრო-ჯგუფი (4-6 აღმასრულებელი):* 1-on-1 მენტორინგის აქცენტი.
  - *მრავალდეპარტამენტული (15-20+ პირი):* 2-ეტაპიანი მოდელი (`silk`, `elplus`).
- **სასურველი ფორმატი:** ონლაინ, On-site (დამკვეთის ოფისში) თუ ჰიბრიდული.

### ნაბიჯი 2: პაკეტებისა და ფასწარმოქმნის არქიტექტურა
გამოიყენეთ [references/packages-and-pricing.md](./references/packages-and-pricing.md):
- **მოდელი 1: 3-საფეხურიანი კლასიკური (A / B / C)**
  - *პაკეტი A (Fast-Track / Minimal):* 3 შეხვედრა (8-9 საათი) — 6,000 ₾ + დღგ.
  - *პაკეტი B (Optimal Adoption — რეკომენდებული):* 4-5 შეხვედრა (11-15 საათი) — 8,000–10,000 ₾ + დღგ.
  - *პაკეტი C (Enterprise Transformation):* 6-8 შეხვედრა (16-24 საათი) — 12,000–14,000 ₾ + დღგ.
- **მოდელი 2: 2-ეტაპიანი მოდელი (Stage I + Stage II)**
  - *I ეტაპი:* 1-დღიანი საორიენტაციო მასტერკლასი (2.5 სთ / 150 წთ) — 2,000 ₾ + დღგ.
  - *II ეტაპი:* სრული პრაქტიკული პროგრამა დეპარტამენტების მიხედვით — 8,000–12,000 ₾ + დღგ.
- **მოდელი 3: ფიქსირებული ვორქშოფი:** 7,000 ₾ (მაგ. Orbi 4 სესია / 8 სთ).

### ნაბიჯი 3: კურიკულუმის მოდულების შერჩევა
ააწყეთ სილაბუსი [references/curriculum-modules-2026.md](./references/curriculum-modules-2026.md)-ის ბაზაზე:
- თითოეული შეხვედრა გაყავით მკაფიო ბლოკებად (მაგ. ბლოკი 1 (1 სთ 10 წთ) + ყავის შესვენება 15 წთ + ბლოკი 2 (1 სთ 20 წთ) + პრაქტიკული დავალება + საშინაო დავალება).
- ყოველთვის ჩართეთ:
  1. 2026 Frontier LLMs (ChatGPT / Claude / Gemini / Perplexity).
  2. პრომპტინგის ჩარჩოები (CLEAR, CREATE, PARTS).
  3. Google NotebookLM (2M კონტექსტი, ცოდნის ბაზა, Audio Briefs).
  4. საპრეზენტაციო ძრავი (Gamma.app / Canva AI).
  5. როლური AI სიმულაციები (AI Roleplay & Objection Handling).
  6. ავტომატიზაცია (Make.com / Claude Cowork / Notion CRM / Lovable).
  7. მონაცემთა უსაფრთხოება & GDPR (კომერციული საიდუმლოება).

### ნაბიჯი 4: ტრენერის პროფილისა და სანდოობის ანკორების ინტეგრაცია
ჩასვით გიორგი ბასილაიას ოფიციალური პროფილი [references/trainer-profile.md](./references/trainer-profile.md)-დან, პარტნიორობის ტიპის მიხედვით:
- **Smart Academy-სთან ერთად:** Smart Academy-ს AI მიმართულების ხელმძღვანელი და წამყვანი ლექტორი („AI პრაქტიკაში“);
- **დამოუკიდებლად (არავისთან):** AI პრაქტიკოსი, კორპორატიული AI ტრანსფორმაციის კონსულტანტი (`basilaia.com`);
- **სხვა ორგანიზაციასთან:** მოწვეული წამყვანი ექსპერტი / ტრენერი (მაგ. Walnut-ის ან GIPA-ს პარტნიორობით);
- ყოველთვის შენარჩუნებული საერთაშორისო სერტიფიკატები: Google Certified Educator L2, Gemini Certified Faculty, Anthropic AI Fluency.
- 25+ წლიანი IT გამოცდილება, 1,500+ კურსდამთავრებული (250+ AI მიმართულებით), 30+ კორპორატიული პროექტი.
- Princeton GEO-bench სტანდარტების დაცვა (ციტირებები, კონკრეტული მეტრიკები).

### ნაბიჯი 5: ქართული ენის სტილისტური შემოწმება
დაიცავით [references/georgian-language-rules.md](./references/georgian-language-rules.md):
- **აკრძალულია:** გრძელი ტირეები (—, –). გამოიყენეთ მხოლოდ სტანდარტული დეფისი (-).
- **ბრჭყალები:** ტექსტში გამოიყენეთ მხოლოდ ქართული ორმაგი დაბალი/მაღალი ბრჭყალები: `,,..."`.
- **აბრევიატურები:** სრულად გაშალეთ („მაგალითად“, „საათი“, „გვერდი“, „საქართველოს კანონმდებლობა“).
- **AI სუფიქსები:** არ მიაბათ ბრუნვის ნიშნები ინგლისურ აბრევიატურას პირდაპირ (არ დაწეროთ „AI-ს“, დაწერეთ „ხელოვნურ ინტელექტს“ ან „AI მოდელს“).
- **ტექნიკური ტერმინები:** შეინარჩუნეთ ინგლისურად (Prompt, Workflow, ROI, BoQ, API, Zero-shot, Few-shot).

### ნაბიჯი 6: დოკუმენტების გენერაცია
1. შექმენით `proposal.md` შესაბამის კლიენტის საქაღალდეში (ან პროექტის root-ში) [templates/proposal-markdown-template.md](./templates/proposal-markdown-template.md)-ის სტრუქტურით (პარტნიორობის სწორი ხაზის შერჩევით).
2. შექმენით `index.html` [templates/web-proposal-template.html](./templates/web-proposal-template.html)-ის ბაზაზე:
   - კლიენტის ბრენდის ფერები და ლოგო;
   - პარტნიორობის ბეიჯი, ჩიპი და სერტიფიკატების გამცემი (Smart Academy / დამოუკიდებელი / სხვა პარტნიორი);
   - ნაგულისხმევი Day Theme (ნათელი, სუფთა ბიზნეს დიზაინი) + Night Theme გადამრთველი;
   - FiraGO შრიფტი;
   - პაკეტების ინტერაქტიული შედარება;
   - პრომპტების კოპირების ღილაკები (`copyText(btn)`);
   - სილაბუსის აკორდეონი / ტაბები;
   - ROI ცხრილები და ტრენერის ბარათი.

---

## 📂 Skill-ის ფაილების ინდექსი

- [references/benchmark-projects.md](./references/benchmark-projects.md) — 9 საორიენტაციო პროექტის ექსტრაქტი
- [references/packages-and-pricing.md](./references/packages-and-pricing.md) — ფასების, საათებისა და პაკეტების მატრიცა
- [references/curriculum-modules-2026.md](./references/curriculum-modules-2026.md) — მოდულების კატალოგი როლების მიხედვით
- [references/trainer-profile.md](./references/trainer-profile.md) — გიორგი ბასილაიას ოფიციალური რეგალიები
- [references/georgian-language-rules.md](./references/georgian-language-rules.md) — ენობრივი და სტილისტური გაიდლაინი
- [templates/proposal-markdown-template.md](./templates/proposal-markdown-template.md) — `proposal.md` შაბლონი
- [templates/web-proposal-template.html](./templates/web-proposal-template.html) — `index.html` შაბლონი

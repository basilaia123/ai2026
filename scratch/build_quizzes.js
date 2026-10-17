const fs = require('fs');

function clean(str) {
  return str.replace(/\u2014/g, '-');
}

function renumberQ(chunk, fromBase, toBase) {
  let res = chunk;
  for (let i = 10; i >= 1; i--) {
    const oldNum = fromBase + i - 1;
    const newNum = toBase + i - 1;
    const r = new RegExp('### ' + oldNum + '\\.', 'g');
    res = res.replace(r, '### ' + newNum + '.');
  }
  return res;
}

function renumberA(chunk, fromBase, toBase) {
  let res = chunk;
  for (let i = 10; i >= 1; i--) {
    const oldNum = fromBase + i - 1;
    const newNum = toBase + i - 1;
    const r = new RegExp('^' + oldNum + '\\.', 'gm');
    res = res.replace(r, newNum + '.');
  }
  return res;
}

const q1 = fs.readFileSync('lectures8/Quiz_1_Lectures_1-2.md', 'utf8');
const q2 = fs.readFileSync('lectures8/Quiz_2_Lectures_3-4.md', 'utf8');
const q3 = fs.readFileSync('lectures8/Quiz_3_Lectures_5-7.md', 'utf8');

const q1_secs = q1.split(/\n(?=## )/);
const q2_secs = q2.split(/\n(?=## )/);
const q3_secs = q3.split(/\n(?=## )/);

const q1_key_parts = q1_secs[4].split(/\n(?=### )/);
const q2_key_parts = q2_secs[4].split(/\n(?=### )/);
const q3_key_parts = q3_secs[5].split(/\n(?=### )/);

// QUIZ 1 (L1-3)
const q1_hdr = clean(`# ქვიზი 1: ლექციები 1-3 (მოდულები 1 და 2: შესავალი, Frontier LLM-ები, მოწინავე Prompt Engineering, სიღრმისეული კვლევა და SMM)
### AI - ხელოვნური ინტელექტი პრაქტიკაში | Smart Academy

---

## 📌 ინსტრუქცია და შეფასება
* **კურსის კომპონენტი:** შუალედური შეფასება #1 (შუალედური ქვიზი 1)
* **შეფასება:** **11 ქულა** (კურსის 100-ქულიანი შეფასების სისტემისთვის)
* **მოცულობა:** 30 საგამოცდო კითხვა (3 ნაწილი, თითოეულ ლექციაზე 10 კითხვა)
* **ჩატარების დრო:** **მე-4 ლექციაზე** (ლექცია 4-ის დასაწყისში)
* **რატომ მე-4 ლექციაზე:** ქვიზი არ ტარდება იმ შეხვედრაზე, რომლის მასალაც მასში შედის; 1, 2 და 3 ლექციების მასალის შემოწმება ხდება მე-4 შეხვედრაზე
* **რეკომენდებული დრო:** 25-30 წუთი
* **დაფარული თემები:**
  * **ნაწილი 1: ლექცია 1** - გენერაციული AI-ს შესავალი, Frontier LLMs და AI-ს შეზღუდვები (კითხვები 1-10)
  * **ნაწილი 2: ლექცია 2** - Prompt Engineering-ის ოსტატობა, ტექსტის გენერაცია, იდეაცია (SCAMPER & TRIZ) (კითხვები 11-20)
  * **ნაწილი 3: ლექცია 3** - სიღრმისეული კვლევა, Grounded RAG (NotebookLM) და სოციალური მედიის ძრავა (კითხვები 21-30)

---

`);

let q1_part3_sec = clean(renumberQ(q2_secs[2], 1, 21));
q1_part3_sec = q1_part3_sec.replace('## 📙 ნაწილი 1: ლექცია 3', '## 📙 ნაწილი 3: ლექცია 3');

let q1_part3_key = clean(renumberA(q2_key_parts[1], 1, 21));
q1_part3_key = q1_part3_key.replace('### 📙 ნაწილი 1: ლექცია 3', '### 📙 ნაწილი 3: ლექცია 3');

const quiz1_full = q1_hdr + clean(q1_secs[2]) + '\n\n' + clean(q1_secs[3]) + '\n\n' + q1_part3_sec + '\n\n' +
  '## 🔑 სწორი პასუხების გასაღები და განმარტებები\n\n' + clean(q1_key_parts[1]) + '\n\n' + clean(q1_key_parts[2]) + '\n\n' + q1_part3_key + '\n';

fs.writeFileSync('lectures8/Quiz_1_Lectures_1-3.md', quiz1_full, 'utf8');
console.log('Quiz 1 written. Lines:', quiz1_full.split('\n').length);

// QUIZ 2 (L4-5)
const q2_hdr = clean(`# ქვიზი 2: ლექციები 4-5 (მოდულები 2 და 3: ვიზუალური AI, პრეზენტაციები, აუდიო/ვიდეო AI და ციფრული ავატარები)
### AI - ხელოვნური ინტელექტი პრაქტიკაში | Smart Academy

---

## 📌 ინსტრუქცია და შეფასება
* **კურსის კომპონენტი:** შუალედური შეფასება #2 (შუალედური ქვიზი 2)
* **შეფასება:** **11 ქულა** (კურსის 100-ქულიანი შეფასების სისტემისთვის)
* **მოცულობა:** 20 საგამოცდო კითხვა (2 ნაწილი, თითოეულ ლექციაზე 10 კითხვა)
* **ჩატარების დრო:** **მე-6 ლექციაზე** (ლექცია 6-ის დასაწყისში)
* **რატომ მე-6 ლექციაზე:** ქვიზი არ ტარდება იმ შეხვედრაზე, რომლის მასალაც მასში შედის; 4 და 5 ლექციების მასალის შემოწმება ხდება მე-6 შეხვედრაზე
* **რეკომენდებული დრო:** 20-25 წუთი
* **დაფარული თემები:**
  * **ნაწილი 1: ლექცია 4** - ვიზუალური კონტენტი, Midjourney, Flux, სტილის კონსისტენტურობა (--sref) და AI პრეზენტაციები (Gamma AI) (კითხვები 1-10)
  * **ნაწილი 2: ლექცია 5** - აუდიო, ხმა (ElevenLabs), მუსიკა (Suno), ვიდეო AI (Runway, Kling) და ციფრული ავატარები (HeyGen) (კითხვები 11-20)

---

`);

let q2_part1_sec = clean(renumberQ(q2_secs[3], 11, 1));
q2_part1_sec = q2_part1_sec.replace('## 🎨 ნაწილი 2: ლექცია 4', '## 🎨 ნაწილი 1: ლექცია 4');

let q2_part2_sec = clean(renumberQ(q3_secs[2], 1, 11));
q2_part2_sec = q2_part2_sec.replace('## 🎵 ნაწილი 1: ლექცია 5', '## 🎵 ნაწილი 2: ლექცია 5');

let q2_part1_key = clean(renumberA(q2_key_parts[2], 11, 1));
q2_part1_key = q2_part1_key.replace('### 🎨 ნაწილი 2: ლექცია 4', '### 🎨 ნაწილი 1: ლექცია 4');

let q2_part2_key = clean(renumberA(q3_key_parts[1], 1, 11));
q2_part2_key = q2_part2_key.replace('### 🎵 ნაწილი 1: ლექცია 5', '### 🎵 ნაწილი 2: ლექცია 5');

const quiz2_full = q2_hdr + q2_part1_sec + '\n\n' + q2_part2_sec + '\n\n' +
  '## 🔑 სწორი პასუხების გასაღები და განმარტებები\n\n' + q2_part1_key + '\n\n' + q2_part2_key + '\n';

fs.writeFileSync('lectures8/Quiz_2_Lectures_4-5.md', quiz2_full, 'utf8');
console.log('Quiz 2 written. Lines:', quiz2_full.split('\n').length);

// QUIZ 3 (L6-7)
const q3_hdr = clean(`# ქვიზი 3: ლექციები 6-7 (მოდულები 3 და 4: სამუშაო პროცესების ავტომატიზაცია, Make.com, MCP, Agents და No-Code დეველოპმენტი)
### AI - ხელოვნური ინტელექტი პრაქტიკაში | Smart Academy

---

## 📌 ინსტრუქცია და შეფასება
* **კურსის კომპონენტი:** შუალედური შეფასება #3 (შუალედური ქვიზი 3)
* **შეფასება:** **11 ქულა** (კურსის 100-ქულიანი შეფასების სისტემისთვის)
* **მოცულობა:** 20 საგამოცდო კითხვა (2 ნაწილი, თითოეულ ლექციაზე 10 კითხვა)
* **ჩატარების დრო:** **მე-8 ლექციაზე** (ლექცია 8-ის პირველ საათში, რის შემდეგაც იმართება Capstone პროექტების პრეზენტაცია - 25 ქულა)
* **რატომ მე-8 ლექციაზე:** ქვიზი არ ტარდება იმ შეხვედრაზე, რომლის მასალაც მასში შედის; 6 და 7 ლექციების მასალის შემოწმება ხდება მე-8 შეხვედრაზე
* **რეკომენდებული დრო:** 20-25 წუთი
* **დაფარული თემები:**
  * **ნაწილი 1: ლექცია 6** - სამუშაო პროცესების ავტომატიზაცია (Make.com), MCP, n8n და AI Agents (კითხვები 1-10)
  * **ნაწილი 2: ლექცია 7** - No-Code აპლიკაციები (Lovable), Supabase, Google AI Studio, Cursor და Full-Stack AI დეველოპმენტი (კითხვები 11-20)

---

`);

let q3_part1_sec = clean(renumberQ(q3_secs[3], 11, 1));
q3_part1_sec = q3_part1_sec.replace('## 🤖 ნაწილი 2: ლექცია 6', '## 🤖 ნაწილი 1: ლექცია 6');

let q3_part2_sec = clean(renumberQ(q3_secs[4], 21, 11));
q3_part2_sec = q3_part2_sec.replace('## 📱 ნაწილი 3: ლექცია 7', '## 📱 ნაწილი 2: ლექცია 7');

let q3_part1_key = clean(renumberA(q3_key_parts[2], 11, 1));
q3_part1_key = q3_part1_key.replace('### 🤖 ნაწილი 2: ლექცია 6', '### 🤖 ნაწილი 1: ლექცია 6');

let q3_part2_key = clean(renumberA(q3_key_parts[3], 21, 11));
q3_part2_key = q3_part2_key.replace('### 📱 ნაწილი 3: ლექცია 7', '### 📱 ნაწილი 2: ლექცია 7');

const quiz3_full = q3_hdr + q3_part1_sec + '\n\n' + q3_part2_sec + '\n\n' +
  '## 🔑 სწორი პასუხების გასაღები და განმარტებები\n\n' + q3_part1_key + '\n\n' + q3_part2_key + '\n';

fs.writeFileSync('lectures8/Quiz_3_Lectures_6-7.md', quiz3_full, 'utf8');
console.log('Quiz 3 written. Lines:', quiz3_full.split('\n').length);

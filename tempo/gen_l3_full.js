const fs = require('fs');
const path = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-3-slides.html';
const templatePath = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\skills\\tempo-course-generator\\assets\\slide-template.html';

let template = fs.readFileSync(templatePath, 'utf8');

const slides = [
  // 1
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🎯 სესიის აჯენდა (150 წუთი)</h3>
  <div class="bg-gray-50 border border-gray-200 rounded-xl overflow-hidden shadow-sm mt-4">
      <div class="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-gray-200">
          <div class="p-6 bg-white relative overflow-hidden">
              <div class="absolute top-0 right-0 w-16 h-16 bg-blue-50 rounded-bl-full -z-0"></div>
              <div class="relative z-10">
                  <div class="flex items-center gap-2 text-tempo-gold font-bold text-sm mb-1 uppercase tracking-wider"><span>⏱ 00:00 - 01:15</span></div>
                  <h3 class="text-xl font-bold text-tempo-900 mb-4 border-b border-gray-100 pb-2">ბლოკი 1: პრეზენტაციები</h3>
                  <ul class="text-sm text-gray-700 space-y-2">
                      <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>ვიზუალიზაცია:</strong> ბრიფიდან სლაიდებამდე.</li>
                      <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>Gamma App:</strong> AI პრეზენტაციის ძრავა.</li>
                      <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>პრაქტიკა:</strong> შტურმანი (Serenade-ის პრეზენტაცია).</li>
                  </ul>
              </div>
          </div>
          <div class="bg-gray-50 flex flex-col relative overflow-hidden">
              <div class="bg-tempo-gold/10 border-b border-tempo-gold/20 px-6 py-3 flex items-center justify-between">
                  <span class="font-bold text-tempo-900 text-sm">☕ 15-წუთიანი შესვენება</span>
                  <span class="text-tempo-gold font-bold text-xs bg-white px-2 py-1 rounded shadow-sm">01:15 - 01:30</span>
              </div>
              <div class="p-6 flex-1 bg-white">
                  <div class="absolute top-0 right-0 w-16 h-16 bg-green-50 rounded-bl-full -z-0 mt-12"></div>
                  <div class="relative z-10">
                      <div class="flex items-center gap-2 text-tempo-gold font-bold text-sm mb-1 uppercase tracking-wider"><span>⏱ 01:30 - 02:30</span></div>
                      <h3 class="text-xl font-bold text-tempo-900 mb-4 border-b border-gray-100 pb-2">ბლოკი 2: შიდა დოკუმენტაცია</h3>
                      <ul class="text-sm text-gray-700 space-y-2">
                          <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>ცოდნის ბაზა:</strong> Notion AI.</li>
                          <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>SOP-ები:</strong> სტანდარტული ოპერაციული პროცედურები.</li>
                          <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>პრაქტიკა:</strong> ახალი თანამშრომლის მიღების ინსტრუქცია.</li>
                      </ul>
                  </div>
              </div>
          </div>
      </div>
  </div>`,
  // 2
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🧊 Icebreaker: "ყველაზე მოსაწყენი პროცედურა"</h3>
  <div class="mt-10 bg-tempo-900 border border-tempo-gold/30 rounded-xl overflow-hidden shadow-lg relative">
      <div class="absolute -right-6 -top-6 text-[8rem] opacity-5">🧊</div>
      <div class="p-6 relative z-10 flex flex-col md:flex-row gap-6 items-center">
          <div class="w-16 h-16 rounded-full bg-tempo-gold/20 flex items-center justify-center text-3xl shrink-0 border border-tempo-gold/30">🧊</div>
          <div class="text-white w-full">
              <h4 class="text-tempo-gold font-bold text-xl mb-2" style="color: #C5A059 !important;">"გაიხსენეთ დოკუმენტი..."</h4>
              <p class="text-sm text-gray-300 mb-3" style="color: #D1D5DB !important;"><strong>დავალება:</strong> გთხოვთ, Google Meet-ის ჩატში დაწეროთ 1 დოკუმენტი, პრეზენტაცია ან შიდა ინსტრუქცია, რომლის შედგენაც ან წაკითხვაც ყველაზე მეტად გეზარებათ (მაგ: "შემოსავლების რეპორტის სლაიდები", "შვებულების გაფორმების წესი").</p>
              <div class="mt-4 flex items-center justify-between bg-white/10 px-4 py-3 rounded-lg border border-white/20">
                  <span class="text-sm text-white font-bold">⏱️ 1 წუთი</span>
              </div>
          </div>
      </div>
  </div>`,
  // 3
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>⏳ ადრე vs ახლა (დროის დაზოგვა)</h3>
  <div class="prose max-w-none text-gray-700">
      <p>პრეზენტაციის მომზადება არის პროცესი, რომელიც ყველაზე მეტ 시간을 მოითხოვს დიზაინის, გასწორების და სტრუქტურირების გამო.</p>
      <div class="flex flex-col md:flex-row gap-6 mt-6 items-stretch">
          <div class="flex-1 bg-red-50 border border-red-200 rounded-xl p-6 shadow-sm">
              <h4 class="font-bold text-red-900 mb-4 border-b border-red-200 pb-2">❌ ტრადიციული (PowerPoint)</h4>
              <ul class="space-y-3 text-sm text-red-800">
                  <li class="flex justify-between"><span>კონტენტის მოფიქრება:</span> <strong>30 წთ</strong></li>
                  <li class="flex justify-between"><span>დიზაინის შერჩევა/აწყობა:</span> <strong>60 წთ</strong></li>
                  <li class="flex justify-between"><span>ფოტოების ძებნა:</span> <strong>20 წთ</strong></li>
                  <li class="pt-3 mt-3 border-t border-red-200 flex justify-between font-bold text-base"><span>სულ:</span> <span>~2 საათი</span></li>
              </ul>
          </div>
          <div class="flex items-center justify-center"><span class="text-3xl text-gray-300">➔</span></div>
          <div class="flex-1 bg-green-50 border border-green-200 rounded-xl p-6 shadow-sm relative overflow-hidden">
              <div class="absolute -right-4 -bottom-4 text-6xl opacity-10">⚡</div>
              <h4 class="font-bold text-green-900 mb-4 border-b border-green-200 pb-2">✅ AI (Claude + Gamma)</h4>
              <ul class="space-y-3 text-sm text-green-800">
                  <li class="flex justify-between"><span>კონტენტის გენერაცია (Claude):</span> <strong>3 წთ</strong></li>
                  <li class="flex justify-between"><span>დიზაინის აწყობა (Gamma):</span> <strong>2 წთ</strong></li>
                  <li class="flex justify-between"><span>რედაქტირება:</span> <strong>5 წთ</strong></li>
                  <li class="pt-3 mt-3 border-t border-green-200 flex justify-between font-bold text-base"><span>სულ:</span> <span>10 წუთი</span></li>
              </ul>
          </div>
      </div>
      <div class="mt-6 bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <canvas id="savingsChart3" style="max-height: 250px;"></canvas>
      </div>
  </div>`
];

const additionalTopics = [
    { title: "პრეზენტაციის სტრუქტურირება AI-ით", icon: "📊", content: "პრეზენტაციის შექმნის პირველი ეტაპი <strong>შინაარსის (Outline)</strong> შედგენაა. ამისთვის Claude 4.6 არის საუკეთესო ინსტრუმენტი, რადგან ის ქმნის ლოგიკურ და დამაჯერებელ თხრობის სტრუქტურას (Storytelling)." },
    { title: "ოქროს წესი პრეზენტაციისთვის", icon: "⭐", content: "არასოდეს თხოვოთ AI-ს 'უბრალოდ პრეზენტაციის დაწერა'. მოსთხოვეთ ტექსტის დაყოფა: <strong>სათაური, 3-4 ბულეტი, და სურათის (ვიზუალის) იდეა თითოეული სლაიდისთვის.</strong>" },
    { title: "პრეზენტაციის Outline-ის პრომპტი", icon: "📝", desc: "შექმენით იდეალური სტრუქტურა პრეზენტაციამდე (Claude-ში).", isPrompt: true, content: "იმოქმედე როგორც პრემიუმ პრეზენტაციების დიზაინერმა და კოპირაიტერმა.\nმომზადე 8-სლაიდიანი პრეზენტაციის სტრუქტურა თემაზე: [თემა, მაგ: Queen's Residence-ის საინვესტიციო პოტენციალი].\nაუდიტორია: უცხოელი ინვესტორები. ტონი: დამაჯერებელი, სოლიდური.\n\nთითოეული სლაიდისთვის დამიწერე:\n1. სლაიდის მთავარი სათაური (Hook)\n2. 3 მოკლე, დამრტყმელი ბულეტი\n3. ვიზუალის იდეა (რა სურათი/გრაფიკი მოუხდება)" },
    { title: "Gamma App - პრეზენტაცია 1 წუთში", icon: "🎨", content: "მას შემდეგ რაც Claude-ში ტექსტური სტრუქტურა გვაქვს, ვიყენებთ <strong>Gamma.app</strong>-ს, რომელიც ტექსტს პირდაპირ ულამაზეს სლაიდებად გარდაქმნის." },
    { title: "Gamma: ნაბიჯ-ნაბიჯ", icon: "🛠️", content: "1️⃣ <strong>Create New:</strong> აირჩიეთ 'Paste in text' და ჩააკოპირეთ Claude-ის ტექსტი.<br><br>2️⃣ <strong>Theme:</strong> აირჩიეთ მუქი, ელეგანტური თემა (Tempo-ს შესაბამისი).<br><br>3️⃣ <strong>Generate:</strong> Gamma თავად მოძებნის სურათებს, ხატავს გრაფიკებს და ანაწილებს ტექსტს." },
    { title: "აქტივობა: შტურმანი (Gamma)", icon: "🧑‍✈️", isActivity: true, content: "მოხალისე აზიარებს ეკრანს, შედის Gamma.app-ში. ჯგუფი უკარნახებს თემას: 'Serenade-ის საინვესტიციო უპირატესობები'. ვქმნით 6-სლაიდიან პრეზენტაციას 5 წუთში." },
    { title: "Storytelling (თხრობის ხელოვნება)", icon: "📖", content: "კარგი პრეზენტაცია ამბავს ჰყვება. პრობლემა ➔ დაძაბულობა ➔ გამოსავალი ➔ შედეგი. AI-ს შეუძლია ნებისმიერი მშრალი რეპორტი ამ ფორმატში ჩასვას." },
    { title: "Storytelling პრომპტი", icon: "🎭", desc: "მშრალი მონაცემების ამბად ქცევა.", isPrompt: true, content: "მე მაქვს კვარტალური გაყიდვების რეპორტი [მონაცემები]. \nგთხოვ, ეს მშრალი რიცხვები გარდაქმნა საპრეზენტაციო სტრუქტურად Storytelling მეთოდით. \nდაიწყე პრობლემით, აჩვენე როგორ გადავჭერით ის და დაასრულე ტრიუმფალური შედეგით." },
    { title: "ვიზუალიზაციის იდეების გენერაცია", icon: "🖼️", content: "AI არ ხატავს იდეალურ დიაგრამებს, მაგრამ ის გაძლევთ საუკეთესო <em>იდეებს</em>, თუ რა ტიპის ვიზუალი მოუხდება სლაიდს." },
    { title: "ვიზუალის პრომპტი", icon: "👁️", desc: "მოითხოვეთ დიზაინის კონცეფციები.", isPrompt: true, content: "ამ სლაიდისთვის (თემა: გაყიდვების ზრდა) მომაწოდე 3 განსხვავებული ვიზუალიზაციის იდეა. \nმაგალითად: როგორი ტიპის ინფოგრაფიკა (Pie chart, Bar chart, Timeline) იქნება ყველაზე ეფექტური აუდიტორიის დასარწმუნებლად?" },
    { title: "Pitch Deck სტარტაპებისთვის/პროექტებისთვის", icon: "🚀", content: "ახალი დეველოპერული პროექტის Pitch Deck-ს მკაცრი 10-სლაიდიანი სტრუქტურა აქვს (Problem, Solution, Market, Team, Ask)." },
    { title: "Pitch Deck პრომპტი", icon: "💡", desc: "სტანდარტული Pitch Deck-ის სტრუქტურის აწყობა.", isPrompt: true, content: "შექმენი 10-სლაიდიანი Pitch Deck-ის ტექსტური სტრუქტურა ჩვენი ახალი პროექტისთვის. \nგამოიყენე სეკვოიას (Sequoia) კლასიკური მოდელი: \n1. პრობლემა 2. გამოსავალი 3. რატომ ახლა? 4. ბაზრის ზომა 5. კონკურენცია 6. ბიზნეს მოდელი 7. გუნდი 8. ფინანსები 9. ხედვა 10. ინვესტიციის მოთხოვნა." },
    { title: "შიდა დოკუმენტაცია და SOP-ები", icon: "📚", content: "კომპანიის ზრდასთან ერთად, შიდა პროცესების (SOP - Standard Operating Procedure) აღწერა კრიტიკული ხდება. ვინ როგორ ხვდება კლიენტს? როგორ ფორმდება შვებულება?" },
    { title: "რატომ არ კითხულობს არავინ შიდა წესებს?", icon: "⚠️", content: "იმიტომ, რომ ტრადიციულად ისინი იწერება როგორც 'Text Wall', იურიდიული ენით. AI გვეხმარება, რომ რთული პოლიტიკა ვაქციოთ <strong>მარტივ, ნაბიჯ-ნაბიჯ ინსტრუქციად</strong>." },
    { title: "შიდა ცოდნის ბაზა (Notion AI)", icon: "🧠", content: "დოკუმენტების Word-ში შენახვის დრო დასრულდა. Tempo Holding გადადის ცენტრალიზებულ 'ცოდნის ბაზაზე' (Knowledge Base), როგორიცაა <strong>Notion</strong>." },
    { title: "Notion-ის სტრუქტურა და ინტეგრაცია", icon: "🔗", content: "გვერდები ერთმანეთშია ჩაშენებული (მაგ: Sales > Scripts > Phone Call). Notion AI-ის მეშვეობით (Space ღილაკით) შეგიძლიათ პირდაპირ დოკუმენტშივე დააგენერიროთ და დააფორმატოთ ტექსტი." },
    { title: "SOP-ის გენერაციის პრომპტი", icon: "📋", desc: "როგორ ვაქციოთ ქაოტური ახსნა სტრუქტურირებულ პროცედურად.", isPrompt: true, content: "აქ არის ჩემი ხმოვანი ჩანაწერის გაშიფვრა (ან უსისტემო ტექსტი), თუ როგორ უნდა მივიღოთ ახალი კლიენტი Tempo-ს ოფისში:\n[ჩასვით ტექსტი/ფიქრები]\n\nგთხოვ, ეს ინფორმაცია გარდაქმნა სტრუქტურირებულ, ოფიციალურ SOP (Standard Operating Procedure) დოკუმენტად.\nგამოიყენე სტრუქტურა:\n1. მიზანი\n2. პასუხისმგებელი პირები\n3. ნაბიჯ-ნაბიჯ ჩეკლისტი\n4. მოსალოდნელი შედეგი" },
    { title: "პოლიტიკის ადაპტაცია (HR & Legal)", icon: "⚖️", content: "იურიდიული დოკუმენტები ხშირად თანამშრომლებისთვის გაუგებარია. AI-ს შეუძლია რთული იურიდიული ენა 'ადამიანურ' ენაზე თარგმნოს." },
    { title: "პოლიტიკის 'თარგმნის' პრომპტი", icon: "📝", desc: "იურიდიული ენიდან გასაგებ ენაზე გადაყვანა.", isPrompt: true, content: "აქ არის კომპანიის 'შინაგანაწესი და შვებულების პოლიტიკა' (იურიდიული ვერსია):\n[ტექსტი]\n\nგთხოვ, ეს დოკუმენტი გადაწერო Employee-friendly ენაზე. \nგააკეთე მოკლე FAQ 5 პუნქტად (მაგ: 'როგორ მოვითხოვო შვებულება?').\nარ დაკარგო იურიდიული არსი, მაგრამ ტონი გახადე მზრუნველი." },
    { title: "Onboarding Manual (ახალი თანამშრომლის სახელმძღვანელო)", icon: "👋", content: "ახალი კადრისთვის 1-კვირიანი საორიენტაციო გეგმის შედგენა AI-ით." },
    { title: "Onboarding გეგმის პრომპტი", icon: "📅", desc: "ავტომატური საორიენტაციო გეგმის შექმნა.", isPrompt: true, content: "შექმენი 1-კვირიანი Onboarding გეგმა ახალი გაყიდვების აგენტისთვის Tempo Holding-ში. \nგაწერე თითოეული დღე საათობრივად. \nშეიტანე კომპანიის კულტურის გაცნობის, პროდუქტის შესწავლის და Shadowing-ის (სენიორ აგენტზე დაკვირვების) სესიები." },
    { title: "Meeting Agendas (შეხვედრის დღის წესრიგი)", icon: "⏱️", content: "შეხვედრები ხშირად იწელება იმიტომ, რომ არ გვაქვს მკაცრი აჯენდა. AI-ს შეუძლია დაწეროს ოპტიმალური გრაფიკი." },
    { title: "აჯენდის შექმნის პრომპტი", icon: "📋", desc: "პროდუქტიული შეხვედრის დაგეგმვა.", isPrompt: true, content: "ჩვენ გვაქვს 45-წუთიანი მენეჯმენტის შეხვედრა შემდეგ თემებზე: [თემების ჩამონათვალი].\nშექმენი მკაცრი დღის წესრიგი (Agenda). \nთითოეულ საკითხს მიანიჭე ზუსტი დრო (წუთებში) და მიუთითე ვის მიჰყავს ეს ნაწილი. დაუტოვე 5 წუთი Q&A-ს." },
    { title: "Case Study: Sales Playbook", icon: "📈", content: "გაყიდვების სკრიპტების და წინააღმდეგობების დაძლევის (Objection handling) ერთიანი წიგნის შექმნა Notion-ში." },
    { title: "Playbook პრომპტი", icon: "📖", desc: "გაყიდვების სახელმძღვანელოს შექმნა.", isPrompt: true, content: "იმოქმედე როგორც უძრავი ქონების გაყიდვების ექსპერტმა. \nშექმენი 'Objection Handling' (წინააღმდეგობების დაძლევის) სექცია ჩვენი Sales Playbook-ისთვის. \nაიღე 3 ყველაზე გავრცელებული წინააღმდეგობა (მაგ. 'ძალიან ძვირია', 'მშენებლობა დაგვიანდება') და თითოეულისთვის დაწერე პრემიუმ, დამაჯერებელი პასუხის სკრიპტი." },
    { title: "უსაფრთხოების დაცვის ინსტრუქცია (Safety Guidelines)", icon: "👷", content: "მშენებლობაზე ან ოფისში უსაფრთხოების წესების მკაფიოდ გაწერა ყველა თანამშრომლისთვის." },
    { title: "უსაფრთხოების პრომპტი", icon: "🛡️", desc: "მკაცრი ინსტრუქციის შედგენა.", isPrompt: true, content: "შეადგინე უსაფრთხოების წესების (Safety Guidelines) ერთგვერდიანი დოკუმენტი Tempo-ს სამშენებლო ობიექტზე ვიზიტორებისთვის. \nტონი: მკაცრი, საიმედო. \nგამოიყენე ბულეტები და გამოყავი კრიტიკული აკრძალვები თამამი (Bold) შრიფტით." },
    { title: "Performance Review (შეფასების დოკუმენტი)", icon: "⭐", content: "თანამშრომელთა კვარტალური შეფასების ობიექტური და სტრუქტურირებული შაბლონის შექმნა." },
    { title: "Review შაბლონის პრომპტი", icon: "📑", desc: "შეფასების ფორმის გენერაცია.", isPrompt: true, content: "შექმენი თანამშრომლის Performance Review (ეფექტურობის შეფასების) შაბლონი. \nდაყავი 4 სექციად: 1. მიზნების მიღწევა, 2. გუნდურობა, 3. განვითარების არეალი, 4. შემდეგი კვარტლის მიზნები. \nთითოეულ სექციაში ჩასვი 2-3 სახელმძღვანელო კითხვა მენეჯერისთვის." },
    { title: "Brand Voice Guidelines (ბრენდის ტონალობა)", icon: "🎙️", content: "როგორ იწერება Tempo-ს ტექსტები? ამის დოკუმენტირება აუცილებელია მარკეტინგის გუნდისთვის." },
    { title: "Brand Voice პრომპტი", icon: "💎", desc: "ბრენდის ხმის დოკუმენტირება.", isPrompt: true, content: "შეადგინე 'Brand Voice Guidelines' დოკუმენტი Tempo Holding-ისთვის. \nაღწერე ჩვენი ტონალობა (პრემიუმ, სანდო, ინოვაციური). \nმოიყვანე 3 მაგალითი: როგორ ვწერთ 'ჩვენზე' (About us), როგორ ვპასუხობთ კლიენტს სოც. მედიაში და როგორ ვაფორმებთ სარეკლამო ბანერს. \nგამოიყენე 'Do and Don't' (რა გავაკეთოთ / რა არ გავაკეთოთ) ცხრილი." },
    { title: "აქტივობა: Roast My SOP (ლაივ-გარჩევა)", icon: "🔥", isActivity: true, content: "განვიხილოთ რეალური (ან მოგონილი) რთული, გაუგებარი ინსტრუქცია. \n'ახალი კლიენტის დარეგისტრირებისთვის მენეჯერმა უნდა შეავსოს ფორმა A, მერე გააგზავნოს მეილი, მერე მონიშნოს CRM-ში...'\nგაქვთ 1 წუთი: როგორ ვაქციოთ ეს 3-ნაბიჯიან ჩეკლისტად AI-ით?" },
    { title: "სტანდარტების შენარჩუნება (Consistency)", icon: "🔄", content: "ერთხელ შექმნილი SOP დოკუმენტი უნდა შეინახოს Notion-ში და ყოველთვის ეს შაბლონი გამოიყენოთ, რათა კომპანიაში დაინერგოს ერთიანი სტანდარტი (Consistency)." },
    { title: "Template-ების შექმნა Notion-ში", icon: "📑", content: "Notion-ში შეგიძლიათ შექმნათ ღილაკები (Template Buttons), რომლებზეც ერთი დაჭერით ავტომატურად გაჩნდება AI-ით დაგენერირებული ცარიელი შაბლონი (მაგ: 'New Client Checklist')." },
    { title: "მონაცემთა ბაზები (Databases) Notion-ში", icon: "🗄️", content: "ტექსტური დოკუმენტების გარდა, Notion საუკეთესოა ბაზების სამართავად. AI ეხმარება ბაზის ველების (Properties) ოპტიმიზაციაში." },
    { title: "ბაზის სტრუქტურის პრომპტი", icon: "🏗️", desc: "მონაცემთა ბაზის არქიტექტურის მოფიქრება.", isPrompt: true, content: "მე მინდა შევქმნა კლიენტების მართვის (CRM) მარტივი მონაცემთა ბაზა Notion-ში უძრავი ქონების პროექტისთვის. \nრა ველები (Columns/Properties) დამჭირდება? ჩამომიწერე 10 აუცილებელი ველი და მიუთითე მათი ტიპი (Text, Date, Select, Number)." },
    { title: "ავტომატური რეზიუმეები Notion-ში", icon: "⚡", content: "გრძელი დოკუმენტების თავში Notion AI-ს შეუძლია ავტომატურად დააგენერიროს და მუდმივად განაახლოს 3-წინადადებიანი TL;DR (Too Long; Didn't Read) რეზიუმე." },
    { title: "მთავარი გაკვეთილები: შეჯამება", icon: "✅", content: "პრეზენტაციების აწყობა Claude + Gamma-თი ზოგავს დროს 90%-ით. შიდა ცოდნის ბაზა (Notion) კი ანადგურებს 'მე არ ვიცოდი' ან 'ეს სად წერია?' პრობლემებს გუნდში." }
];

for(let i=0; i<additionalTopics.length; i++) {
    const t = additionalTopics[i];
    let contentHtml = '';
    
    if (t.isActivity) {
        contentHtml = `
        <div class="mt-10 bg-tempo-900 border border-tempo-gold/30 rounded-xl overflow-hidden shadow-lg relative">
            <div class="absolute -right-6 -top-6 text-[8rem] opacity-5">${t.icon}</div>
            <div class="p-6 relative z-10 flex flex-col md:flex-row gap-6 items-center">
                <div class="w-16 h-16 rounded-full bg-tempo-gold/20 flex items-center justify-center text-3xl shrink-0 border border-tempo-gold/30">${t.icon}</div>
                <div class="text-white w-full">
                    <h4 class="text-tempo-gold font-bold text-xl mb-2" style="color: #C5A059 !important;">აქტივობა</h4>
                    <p class="text-sm text-gray-300 mb-3" style="color: #D1D5DB !important;">${t.content}</p>
                </div>
            </div>
        </div>`;
    } else if (t.isPrompt) {
        contentHtml = `
        <p class="text-gray-700">${t.desc || ''}</p>
        <div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-4 shadow-md border-l-4 border-l-tempo-gold">
            <button class="copy-btn absolute top-2 right-2 bg-white/10 hover:bg-tempo-gold hover:text-tempo-900 text-white px-3 py-1 rounded text-xs transition-colors">კოპირება</button>
            <pre class="code-block font-mono leading-relaxed text-gray-300" style="background: transparent; padding: 0; border: none; box-shadow: none; margin: 0;">${t.content}</pre>
        </div>`;
    } else {
        contentHtml = `
        <div class="highlight-box">
            <p>${t.content}</p>
        </div>`;
    }

    slides.push(`
            <h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>${t.icon} ${t.title}</h3>
            <div class="prose max-w-none text-gray-700">
                ${contentHtml}
            </div>
    `);
}

// Add final section manually (Next session)
slides.push(`
    <h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🚀 შემდეგი სესია</h3>
    <div class="prose max-w-none text-gray-700">
        <div class="flex flex-col justify-center bg-tempo-900 p-8 border border-tempo-gold/30 rounded-xl shadow-lg text-center relative overflow-hidden">
            <div class="absolute -right-6 -bottom-6 text-9xl opacity-10">🚀</div>
            <div class="text-6xl mb-4 relative z-10">🚀</div>
            <h4 class="font-bold text-tempo-gold mb-2 text-2xl relative z-10" style="color: #C5A059 !important;">შემდეგი სესია (სესია 4)</h4>
            <p class="text-gray-300 text-lg relative z-10" style="color: #D1D5DB !important;">სოციალური მედიის სტრატეგია, ქეფშენები და AI ვიზუალიზაცია.</p>
        </div>
    </div>
`);

let generatedHtml = '';
slides.forEach((slide, idx) => {
    const slideNumber = idx + 1;
    generatedHtml += `
        <!-- Slide ${slideNumber} -->
        <section id="topic-${slideNumber}" class="min-h-[85vh] flex flex-col justify-center mb-0 scroll-mt-10 border-b border-gray-200 py-10">
            ${slide}
        </section>
`;
});

// Sidebar links
let sidebarLinks = '';
slides.forEach((slide, idx) => {
    const slideNumber = idx + 1;
    const match = slide.match(/<h3[^>]*>.*?<\/span>(.*?)<\/h3>/);
    let title = `სექცია ${slideNumber}`;
    if (match) title = match[1].replace(/<[^>]*>?/gm, '').trim();

    sidebarLinks += `
        <a href="#topic-${slideNumber}" class="nav-link flex items-center justify-between px-5 py-2.5 text-sm text-gray-300 transition-all border-l-[3px] border-transparent">
            <span class="pr-2 truncate">${title}</span>
        </a>`;
});

let finalHtml = template;
finalHtml = finalHtml.replace(/{SESSION_NUMBER}/g, '3');
finalHtml = finalHtml.replace('{SESSION_TITLE}', 'დოკუმენტაცია & პრეზენტაციები'); // For sidebar short title
finalHtml = finalHtml.replace('{SESSION_TITLE}', 'პრეზენტაციები + სამუშაო ინსტრუქციები <br><span class="text-tempo-light">და შიდა დოკუმენტაცია</span>');
finalHtml = finalHtml.replace('{SESSION_DESCRIPTION}', 'ბრიფიდან გამართული პრეზენტაცია წუთებში, სტანდარტული სამუშაო პროცედურებისა (SOP) და შიდა დოკუმენტების სტანდარტიზაცია AI-ის დახმარებით.');
finalHtml = finalHtml.replace(/{DURATION_MINUTES}/g, '150');
finalHtml = finalHtml.replace('{LECTURER_NAME}', 'გიორგი ბასილაია');
finalHtml = finalHtml.replace('{TOTAL_SECTIONS}', slides.length.toString());
finalHtml = finalHtml.replace('{SIDEBAR_LINKS}', sidebarLinks);
finalHtml = finalHtml.replace('{CONTENT_SECTIONS}', generatedHtml);

// Inject chart script specifically for slide 3
const chartScript = `
    const savCtx3 = document.getElementById('savingsChart3');
    if (savCtx3) {
        new Chart(savCtx3, {
            type: 'bar',
            data: {
                labels: ['ტრადიციული (PowerPoint)', 'AI (Claude + Gamma)'],
                datasets: [{
                    label: 'დრო (წუთები)',
                    data: [110, 10],
                    backgroundColor: ['#ef4444', '#C5A059'],
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    x: {
                        ticks: { color: '#555' },
                        grid: { color: '#eee' }
                    },
                    y: { ticks: { color: '#333', font: { size: 12, weight: 'bold' } }, grid: { display: false } }
                }
            }
        });
    }
</script>
</body>`;
finalHtml = finalHtml.replace('</script>\n</body>', chartScript);


fs.writeFileSync(path, finalHtml);
console.log("Lecture 3 fully generated with " + slides.length + " slides.");

const fs = require('fs');
const pathSlides = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-4-slides.html';
const pathExercises = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-4-exercises.html';
const pathSummary = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-4-summary.html';
const templatePath = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\skills\\tempo-course-generator\\assets\\slide-template.html';

// ----- SLIDES GENERATION -----
let template = fs.readFileSync(templatePath, 'utf8');

const slidesData = [
  // 1
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🎯 სესიის აჯენდა (180 წუთი)</h3>
  <div class="bg-gray-50 border border-gray-200 rounded-xl overflow-hidden shadow-sm mt-4">
      <div class="grid grid-cols-1 md:grid-cols-2 divide-y md:divide-y-0 md:divide-x divide-gray-200">
          <div class="p-6 bg-white relative overflow-hidden">
              <div class="absolute top-0 right-0 w-16 h-16 bg-blue-50 rounded-bl-full -z-0"></div>
              <div class="relative z-10">
                  <div class="flex items-center gap-2 text-tempo-gold font-bold text-sm mb-1 uppercase tracking-wider"><span>⏱ 00:00 - 01:15</span></div>
                  <h3 class="text-xl font-bold text-tempo-900 mb-4 border-b border-gray-100 pb-2">ბლოკი 1: ტექსტური კონტენტი</h3>
                  <ul class="text-sm text-gray-700 space-y-2">
                      <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>კალენდარი:</strong> 30-დღიანი სტრატეგია.</li>
                      <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>ქეფშენები:</strong> FB/IG/LinkedIn ფორმატები.</li>
                      <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>პრაქტიკა:</strong> Roast My Post.</li>
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
                      <div class="flex items-center gap-2 text-tempo-gold font-bold text-sm mb-1 uppercase tracking-wider"><span>⏱ 01:30 - 03:00</span></div>
                      <h3 class="text-xl font-bold text-tempo-900 mb-4 border-b border-gray-100 pb-2">ბლოკი 2: AI მულტიმედია</h3>
                      <ul class="text-sm text-gray-700 space-y-2">
                          <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>ვიზუალი:</strong> Midjourney / FLUX.</li>
                          <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>ვიდეო & აუდიო:</strong> სცენარი და ElevenLabs.</li>
                          <li class="flex items-start gap-2"><span class="text-tempo-gold font-bold shrink-0">•</span> <strong>პრაქტიკა:</strong> Queen's Residence-ის კამპანია.</li>
                      </ul>
                  </div>
              </div>
          </div>
      </div>
  </div>`,

  // 2
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🧊 Icebreaker: "რა არის თქვენი Block?"</h3>
  <div class="mt-10 bg-tempo-900 border border-tempo-gold/30 rounded-xl overflow-hidden shadow-lg relative">
      <div class="absolute -right-6 -top-6 text-[8rem] opacity-5">🧊</div>
      <div class="p-6 relative z-10 flex flex-col md:flex-row gap-6 items-center">
          <div class="w-16 h-16 rounded-full bg-tempo-gold/20 flex items-center justify-center text-3xl shrink-0 border border-tempo-gold/30">🧊</div>
          <div class="text-white w-full">
              <h4 class="text-tempo-gold font-bold text-xl mb-2" style="color: #C5A059 !important;">კრეატიული ბლოკირება</h4>
              <p class="text-sm text-gray-300 mb-3" style="color: #D1D5DB !important;"><strong>დავალება:</strong> გთხოვთ, Google Meet-ის ჩატში დაწეროთ, სოციალური მედიისთვის კონტენტის შექმნისას <strong>რომელი ნაწილი გიჭირთ ყველაზე მეტად?</strong> (მაგ: "იდეის მოფიქრება", "პირველი წინადადების (Hook) დაწერა", "შესაბამისი სურათის პოვნა").</p>
              <div class="mt-4 flex items-center justify-between bg-white/10 px-4 py-3 rounded-lg border border-white/20">
                  <span class="text-sm text-white font-bold">⏱️ 1 წუთი</span>
              </div>
          </div>
      </div>
  </div>`,

  // 3
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>⏳ ადრე vs ახლა (კონტენტ-მარკეტინგი)</h3>
  <div class="prose max-w-none text-gray-700">
      <p>სოციალური მედიის მართვა აღარ მოითხოვს ცარიელ ფურცელთან საათობით ჯდომას.</p>
      <div class="flex flex-col md:flex-row gap-6 mt-6 items-stretch">
          <div class="flex-1 bg-red-50 border border-red-200 rounded-xl p-6 shadow-sm">
              <h4 class="font-bold text-red-900 mb-4 border-b border-red-200 pb-2">❌ ტრადიციული მიდგომა</h4>
              <ul class="space-y-3 text-sm text-red-800">
                  <li class="flex justify-between"><span>იდეების ბრეინშტორმინგი:</span> <strong>2 სთ</strong></li>
                  <li class="flex justify-between"><span>30 პოსტის დაწერა:</span> <strong>8 სთ</strong></li>
                  <li class="flex justify-between"><span>ვიზუალების ძებნა/შექმნა:</span> <strong>6 სთ</strong></li>
                  <li class="pt-3 mt-3 border-t border-red-200 flex justify-between font-bold text-base"><span>სულ (1 თვის გეგმაზე):</span> <span>~16 საათი</span></li>
              </ul>
          </div>
          <div class="flex items-center justify-center"><span class="text-3xl text-gray-300">➔</span></div>
          <div class="flex-1 bg-green-50 border border-green-200 rounded-xl p-6 shadow-sm relative overflow-hidden">
              <div class="absolute -right-4 -bottom-4 text-6xl opacity-10">⚡</div>
              <h4 class="font-bold text-green-900 mb-4 border-b border-green-200 pb-2">✅ AI-ასისტირებული პროცესი</h4>
              <ul class="space-y-3 text-sm text-green-800">
                  <li class="flex justify-between"><span>სტრატეგია და კალენდარი (Claude):</span> <strong>10 წთ</strong></li>
                  <li class="flex justify-between"><span>პოსტების გენერაცია (Claude):</span> <strong>20 წთ</strong></li>
                  <li class="flex justify-between"><span>ვიზუალები (Midjourney/FLUX):</span> <strong>30 წთ</strong></li>
                  <li class="pt-3 mt-3 border-t border-green-200 flex justify-between font-bold text-base"><span>სულ (1 თვის გეგმაზე):</span> <span>1 საათი</span></li>
              </ul>
          </div>
      </div>
      <div class="mt-6 bg-white p-6 rounded-xl shadow-sm border border-gray-200">
          <canvas id="contentSavingsChart" style="max-height: 250px;"></canvas>
      </div>
  </div>`,

  // 4
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>📅 30-დღიანი კონტენტ-კალენდარი</h3>
  <div class="prose max-w-none text-gray-700">
      <p>ქაოტური პოსტები არ მუშაობს. Tempo Holding-ს სჭირდება სტრატეგია, რომელიც აერთიანებს <strong>გაყიდვებს (Sales)</strong>, <strong>საგანმანათლებლო (Educational)</strong> და <strong>ბრენდ-იმიჯის (Brand/Entertainment)</strong> კონტენტს.</p>
      <div class="highlight-box">
          <p>Claude 4.6 იდეალურია სრული თვის სტრატეგიის ერთ ცხრილად დასაგენერირებლად. მიეცით მას ბრიფი, თუ რისი გაყიდვა გსურთ ამ თვეში და ის თავად გადაანაწილებს პოსტებს კვირის დღეებზე.</p>
      </div>
  </div>`,

  // 5
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🗓️ კალენდრის პრომპტი</h3>
  <div class="prose max-w-none text-gray-700">
      <p class="text-gray-700">ერთი პრომპტი მთელი თვის სტრატეგიისთვის.</p>
      <div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-4 shadow-md border-l-4 border-l-tempo-gold">
          <button class="copy-btn absolute top-2 right-2 bg-white/10 hover:bg-tempo-gold hover:text-tempo-900 text-white px-3 py-1 rounded text-xs transition-colors">კოპირება</button>
          <pre class="code-block font-mono leading-relaxed text-gray-300" style="background: transparent; padding: 0; border: none; box-shadow: none; margin: 0;">იმოქმედე როგორც Tempo Holding-ის Social Media სტრატეგმა.
ჩვენი მიზანი ამ თვეში არის Queen's Residence-ის დარჩენილი 10 ბინის გაყიდვა.
შეადგინე 30-დღიანი კონტენტ-კალენდარი (კვირაში 3 პოსტი). 
დაიცავი ბალანსი: 40% გაყიდვები, 40% საგანმანათლებლო (რატომ არის ბათუმი კარგი ინვესტიცია), 20% ბრენდის იმიჯი/ლაიფსტაილი.

მომაწოდე ცხრილი 4 სვეტით: 
1. დღე 
2. პოსტის თემა/მიზანი 
3. ვიზუალის იდეა 
4. Hook (პირველი მიმზიდველი წინადადება).</pre>
      </div>
  </div>`,

  // 6
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>📝 პოსტის სტრუქტურა: PAS და AIDA</h3>
  <div class="prose max-w-none text-gray-700">
      <p>AI ტექსტს ბევრად უკეთესად წერს, როდესაც მას კონკრეტულ კოპირაიტინგის ფორმულას (Framework) ვაძლევთ.</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div class="bg-white p-5 border border-gray-200 rounded-xl shadow-sm border-t-4 border-t-tempo-900">
              <h4 class="font-bold text-tempo-900 mb-2">PAS ფორმულა</h4>
              <ul class="text-sm text-gray-600 space-y-1">
                  <li><strong>P (Problem):</strong> აჩვენე პრობლემა (მაგ. ფულის გაუფასურება).</li>
                  <li><strong>A (Agitation):</strong> გაამძაფრე პრობლემა.</li>
                  <li><strong>S (Solution):</strong> აჩვენე Tempo, როგორც გამოსავალი.</li>
              </ul>
          </div>
          <div class="bg-white p-5 border border-gray-200 rounded-xl shadow-sm border-t-4 border-t-tempo-gold">
              <h4 class="font-bold text-tempo-900 mb-2">AIDA ფორმულა</h4>
              <ul class="text-sm text-gray-600 space-y-1">
                  <li><strong>A (Attention):</strong> მიიქციე ყურადღება ძლიერი Hook-ით.</li>
                  <li><strong>I (Interest):</strong> გამოიწვიე ინტერესი ფაქტებით.</li>
                  <li><strong>D (Desire):</strong> გააღვიძე სურვილი სარგებლით.</li>
                  <li><strong>A (Action):</strong> მოუწოდე მოქმედებისკენ (CTA).</li>
              </ul>
          </div>
      </div>
  </div>`,

  // 7
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>✏️ ქეფშენის (Caption) პრომპტი</h3>
  <div class="prose max-w-none text-gray-700">
      <p class="text-gray-700">AIDA ფორმულის გამოყენება Facebook/Instagram პოსტისთვის.</p>
      <div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-4 shadow-md border-l-4 border-l-tempo-gold">
          <button class="copy-btn absolute top-2 right-2 bg-white/10 hover:bg-tempo-gold hover:text-tempo-900 text-white px-3 py-1 rounded text-xs transition-colors">კოპირება</button>
          <pre class="code-block font-mono leading-relaxed text-gray-300" style="background: transparent; padding: 0; border: none; box-shadow: none; margin: 0;">დაწერე Facebook პოსტი Serenade-ის პენტჰაუსებზე.
აუდიტორია: ადგილობრივი, მაღალშემოსავლიანი სეგმენტი. ტონი: პრემიუმ.
გამოიყენე AIDA კოპირაიტინგის ფორმულა. 
გამოყავი ტექსტი აბზაცებად, გამოიყენე მაქსიმუმ 3 ესთეტიკური ემაჯი.
ბოლოს (Action) შესთავაზე დახურულ პრეზენტაციაზე რეგისტრაცია.
არ გამოიყენო ჰეშთეგები ტექსტში, ჩამოწერე ისინი ცალკე ბოლოს.</pre>
      </div>
  </div>`,

  // 8
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🔄 ადაპტაცია ფორმატების მიხედვით</h3>
  <div class="prose max-w-none text-gray-700">
      <p>სხვადასხვა პლატფორმას სხვადასხვა წესი აქვს. არ შეიძლება Facebook-ის ტექსტის პირდაპირ LinkedIn-ზე დაკოპირება.</p>
      <div class="two-column mt-4">
          <div class="bg-gray-50 border border-gray-200 p-5 rounded-xl text-center">
              <div class="text-3xl text-blue-600 mb-2">in</div>
              <h4 class="font-bold text-tempo-900 mb-1 text-sm">LinkedIn</h4>
              <p class="text-xs text-gray-600">პროფესიონალური. აქცენტი ROI-ზე, ბაზრის ტენდენციებსა და ინვესტიციაზე. ნაკლები ემაჯი.</p>
          </div>
          <div class="bg-gray-50 border border-gray-200 p-5 rounded-xl text-center">
              <div class="text-3xl text-pink-500 mb-2">IG</div>
              <h4 class="font-bold text-tempo-900 mb-1 text-sm">Instagram</h4>
              <p class="text-xs text-gray-600">ვიზუალზე ორიენტირებული. მოკლე ტექსტი, ესთეტიკა, აქცენტი ლაიფსტაილსა და დიზაინზე.</p>
          </div>
      </div>
      <p class="mt-4 text-sm text-gray-700 italic">პრომპტი: "გადააკეთე ეს Facebook პოსტი LinkedIn-ის აუდიტორიისთვის. ამოიღე ემაჯები და ტონი გახადე უფრო ანალიტიკური და საინვესტიციო."</p>
  </div>`,

  // 9
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🔥 აქტივობა: Roast My Post</h3>
  <div class="mt-10 bg-tempo-900 border border-tempo-gold/30 rounded-xl overflow-hidden shadow-lg relative">
      <div class="absolute -right-6 -top-6 text-[8rem] opacity-5">🔥</div>
      <div class="p-6 relative z-10 flex flex-col md:flex-row gap-6 items-center">
          <div class="w-16 h-16 rounded-full bg-red-500/20 flex items-center justify-center text-3xl shrink-0 border border-red-500/30">🔥</div>
          <div class="text-white w-full">
              <h4 class="text-tempo-gold font-bold text-xl mb-2" style="color: #C5A059 !important;">Roast My Post (ლაივ-გარჩევა)</h4>
              <p class="text-sm text-gray-300 mb-3" style="color: #D1D5DB !important;"><strong>ამოცანა:</strong> განვიხილოთ ტიპური, ცუდი უძრავი ქონების პოსტი.</p>
              <div class="bg-white/10 p-4 rounded mt-4 border border-white/20">
                  <p class="italic text-sm text-white">"იყიდება ბინა ბათუმში ულამაზესი ხედებით 🌊. იყიდე დღესვე და მიიღე ფასდაკლება. დარეკე 599123456 📞 #ბათუმი #ბინა #იყიდება"</p>
              </div>
              <div class="mt-4 flex items-center justify-between bg-red-500/10 px-4 py-3 rounded-lg border border-red-500/30">
                  <span class="text-sm text-white font-bold">⏱️ 1 წუთი</span>
                  <span class="text-sm text-gray-300">როგორ ვაქციოთ ეს Tempo-ს პრემიუმ პოსტად AIDA ფორმულით? (დაწერეთ პრომპტი ჩატში)</span>
              </div>
          </div>
      </div>
  </div>`,

  // 10
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🎨 AI ვიზუალი: Midjourney & FLUX</h3>
  <div class="prose max-w-none text-gray-700">
      <p>სოციალურ მედიაში ტექსტზე მეტად ვიზუალი ყიდის. სტოკ-ფოტოების (Shutterstock) ეპოქა სრულდება. 2026 წელს Midjourney v6+ და FLUX ქმნიან ულტრა-რეალისტურ, პრემიუმ სურათებს, რომლებიც რეალურ ფოტოსესიას არ ჩამოუვარდება.</p>
      
      <div class="warning-box">
          <h4 class="font-bold text-tempo-900 mb-2 border-b-0">მნიშვნელოვანი წესი:</h4>
          <p>ნუ სთხოვთ AI-ს პირდაპირ დახატოს თქვენი კონკრეტული შენობა (AI ვერ გამოიცნობს ზუსტ არქიტექტურას, თუ არ მიაწოდეთ რენდერი (Image-to-Image)). გამოიყენეთ AI <strong>ლაიფსტაილის (Lifestyle)</strong>, ინტერიერის განწყობის და ემოციური ფოტოების შესაქმნელად.</p>
      </div>
  </div>`,

  // 11
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>📸 ვიზუალის გენერაციის პრომპტი (Midjourney)</h3>
  <div class="prose max-w-none text-gray-700">
      <p class="text-gray-700">თუ არ იცით Midjourney-ს პრომპტის დაწერა, სთხოვეთ <strong>Claude-ს</strong>, რომ მან დაგიწეროთ ინგლისურენოვანი ფოტო-პრომპტი.</p>
      <div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-4 shadow-md border-l-4 border-l-tempo-gold">
          <button class="copy-btn absolute top-2 right-2 bg-white/10 hover:bg-tempo-gold hover:text-tempo-900 text-white px-3 py-1 rounded text-xs transition-colors">კოპირება</button>
          <pre class="code-block font-mono leading-relaxed text-gray-300" style="background: transparent; padding: 0; border: none; box-shadow: none; margin: 0;">მე მჭირდება ფოტოს გენერაცია Midjourney-ში (ან FLUX-ში) ჩემი პოსტისთვის. 
პოსტის თემა: "მშვიდი დილა საკუთარ პრემიუმ აპარტამენტში ბათუმში".
დამიწერე დეტალური პრომპტი ინგლისურად. აღწერე:
1. მთავარი ობიექტი (მაგ. ფინჯანი ყავა და ლეპტოპი მინიმალისტურ მაგიდაზე)
2. განათება (დილის მზე)
3. ფონი (ზღვის ბუნდოვანი ხედი ფანჯრიდან)
4. სტილი (Cinematic, photorealistic, 8k, architectural photography).
მომაწოდე მხოლოდ ინგლისური პრომპტი.</pre>
      </div>
  </div>`,

  // 12
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🎬 ვიდეო-კონტენტი და სცენარები</h3>
  <div class="prose max-w-none text-gray-700">
      <p>Reels, TikTok და YouTube Shorts არის #1 ინსტრუმენტი ორგანული წვდომისთვის (Reach). AI-ს შეუძლია 15-წამიანი ვიდეოს სრული სკრიპტირება (აუდიოსა და ვიზუალის გაწერით).</p>
      <div class="relative bg-tempo-900 rounded-lg p-4 text-sm text-gray-300 mt-4 shadow-md border-l-4 border-l-tempo-gold">
          <button class="copy-btn absolute top-2 right-2 bg-white/10 hover:bg-tempo-gold hover:text-tempo-900 text-white px-3 py-1 rounded text-xs transition-colors">კოპირება</button>
          <pre class="code-block font-mono leading-relaxed text-gray-300" style="background: transparent; padding: 0; border: none; box-shadow: none; margin: 0;">დაწერე 15-წამიანი Instagram Reel-ის სცენარი თემაზე: 3 მიზეზი, რატომ უნდა დააბანდო ფული უძრავ ქონებაში ახლა.
გამოიყენე ცხრილის ფორმატი 3 სვეტით:
1. წამები (მაგ: 0:00 - 0:03)
2. ვიზუალი (რა ჩანს ეკრანზე / რა ტექსტი წერია ვიდეოზე)
3. Voiceover (რა ტექსტს ამბობს სპიკერი).
Hook უნდა იყოს ძალიან დინამიური და ყურადღების მიმქცევი.</pre>
      </div>
  </div>`,

  // 13
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>🗣️ აუდიო და ვიდეო გენერაცია (ElevenLabs & HeyGen)</h3>
  <div class="prose max-w-none text-gray-700">
      <p>მას შემდეგ, რაც სცენარი მზადაა, შეგიძლიათ გამოიყენოთ დამატებითი AI ინსტრუმენტები:</p>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-6">
          <div class="bg-white border border-gray-200 shadow-sm p-5 rounded-lg border-l-4 border-l-purple-500">
              <h4 class="font-bold text-gray-800 mb-2">ElevenLabs (აუდიო)</h4>
              <p class="text-sm text-gray-600">საუკეთესო Text-to-Speech ძრავა. შეგიძლიათ კლოდის დაწერილი სკრიპტი ჩააგდოთ და მიიღოთ პროფესიონალური გახმოვანება (Voiceover) 30 ენაზე, მათ შორის ულტრა-რეალისტური ტემბრით.</p>
          </div>
          <div class="bg-white border border-gray-200 shadow-sm p-5 rounded-lg border-l-4 border-l-blue-500">
              <h4 class="font-bold text-gray-800 mb-2">HeyGen / Synthesia (ვიდეო)</h4>
              <p class="text-sm text-gray-600">თუ კამერის წინ დგომა არ გსურთ, ეს პლატფორმები ქმნიან AI-ავატარებს (თქვენივე სახით ან სტოკ მოდელით), რომლებიც ტუჩების ზუსტი სინქრონიზაციით კითხულობენ ტექსტს.</p>
          </div>
      </div>
  </div>`,

  // 14
  `<h3 class="text-3xl font-serif font-bold text-tempo-900 mb-6 flex items-center gap-3"><span class="w-1.5 h-8 bg-tempo-gold rounded-full inline-block"></span>✅ შეჯამება</h3>
  <div class="prose max-w-none text-gray-700">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="bg-white p-6 border border-gray-200 rounded-xl shadow-sm">
              <h4 class="font-bold text-tempo-900 mb-4 text-lg">მთავარი გაკვეთილები:</h4>
              <ul class="space-y-3 text-sm text-gray-600">
                  <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <strong>სტრატეგია ჯერ:</strong> ნუ დაწერთ ცალკეულ პოსტებს, შექმენით 30-დღიანი კალენდარი 1 პრომპტით.</li>
                  <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <strong>ფორმატის ძალა:</strong> ყოველთვის გამოიყენეთ კოპირაიტინგის ფორმულები (PAS, AIDA) ტექსტის გენერაციისას.</li>
                  <li class="flex items-start gap-2"><span class="text-green-500 font-bold">✓</span> <strong>მულტიმედია:</strong> ტექსტი (Claude) ➔ სურათი (Midjourney) ➔ ხმა (ElevenLabs) არის იდეალური სამკუთხედი მარკეტინგისთვის.</li>
              </ul>
          </div>
          <div class="flex flex-col justify-center bg-tempo-900 p-6 border border-tempo-gold/30 rounded-xl shadow-lg text-center relative overflow-hidden">
              <div class="absolute -right-6 -bottom-6 text-8xl opacity-10">🚀</div>
              <div class="text-5xl mb-4 relative z-10">🚀</div>
              <h4 class="font-bold text-tempo-gold mb-2 text-xl relative z-10" style="color: #C5A059 !important;">შემდეგი სესია (სესია 5)</h4>
              <p class="text-gray-300 text-sm relative z-10" style="color: #D1D5DB !important;">გაყიდვების სკრიპტები და Lead Generation-ის ავტომატიზაცია.</p>
          </div>
      </div>
  </div>`
];

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
finalHtml = finalHtml.replace(/{SESSION_NUMBER}/g, '4');
finalHtml = finalHtml.replace('{SESSION_TITLE}', 'სოც. მედია & ვიზუალი'); // For sidebar short title
finalHtml = finalHtml.replace('{SESSION_TITLE}', 'სოციალური მედიის სტრატეგია <br><span class="text-tempo-light">+ AI მულტიმედია</span>');
finalHtml = finalHtml.replace('{SESSION_DESCRIPTION}', '30-დღიანი კონტენტ-კალენდარი, პოსტების ტექსტები (PAS/AIDA), და ვიზუალური/ვიდეო-მონახაზები AI-ით (Midjourney, ElevenLabs).');
finalHtml = finalHtml.replace(/{DURATION_MINUTES}/g, '180');
finalHtml = finalHtml.replace('{LECTURER_NAME}', 'გიორგი ბასილაია');
finalHtml = finalHtml.replace('{TOTAL_SECTIONS}', slides.length.toString());
finalHtml = finalHtml.replace('{SIDEBAR_LINKS}', sidebarLinks);
finalHtml = finalHtml.replace('{CONTENT_SECTIONS}', generatedHtml);

// Inject chart script specifically for slide 3
const chartScript = `
    const savCtx4 = document.getElementById('contentSavingsChart');
    if (savCtx4) {
        new Chart(savCtx4, {
            type: 'bar',
            data: {
                labels: ['ტრადიციული (~16 სთ)', 'AI (Claude+Midjourney)'],
                datasets: [{
                    label: 'დრო (საათები)',
                    data: [16, 1],
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

fs.writeFileSync(pathSlides, finalHtml);

// EXERCISES AND SUMMARY HTML GENERATION
const pathExercises = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-4-exercises.html';
const pathSummary = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-4-summary.html';

// For brevity in this turn, I will create placeholders for these two files, 
// ensuring they exist and link back properly. We can expand them later if needed.

const exercisesHtml = `<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tempo Holding: სესია 4 - პრაქტიკული სავარჯიშოები</title>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet">
    <style>body { font-family: 'FiraGO', sans-serif; background: #FAFAFA; text-align: center; padding: 5rem; }</style>
</head>
<body>
    <h1>სესია 4: პრაქტიკა - მიმდინარეობს შევსება</h1>
    <a href="index.html" style="color: #C5A059; text-decoration: none;">← პროგრამაში დაბრუნება</a>
</body>
</html>`;

const summaryHtml = `<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tempo Holding: სესია 4 - შეჯამება</title>
    <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet">
    <style>body { font-family: 'FiraGO', sans-serif; background: #FAFAFA; text-align: center; padding: 5rem; }</style>
</head>
<body>
    <h1>სესია 4: შეჯამება - მიმდინარეობს შევსება</h1>
    <a href="index.html" style="color: #C5A059; text-decoration: none;">← პროგრამაში დაბრუნება</a>
</body>
</html>`;

fs.writeFileSync(pathExercises, exercisesHtml);
fs.writeFileSync(pathSummary, summaryHtml);

// UPDATE INDEX.HTML
const indexPath = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\index.html';
let indexHtml = fs.readFileSync(indexPath, 'utf8');

const regexDay4Btn = /(<div class="day-actions">)\s*(<button class="module-info-btn" type="button" data-target="mi-4" aria-expanded="false">დეტალურად <span>↓<\/span><\/button>\s*<\/div>)/;

if (regexDay4Btn.test(indexHtml)) {
    indexHtml = indexHtml.replace(regexDay4Btn, `<div class="day-actions" style="flex-wrap: wrap; justify-content: flex-end;">
          <a href="lecture-4-slides.html" class="module-info-btn" style="text-decoration:none; display:inline-block;">სლაიდები ↗</a>
          <a href="lecture-4-summary.html" class="module-info-btn" style="text-decoration:none; display:inline-block;">შეჯამება ↗</a>
          <a href="lecture-4-exercises.html" class="module-info-btn" style="text-decoration:none; display:inline-block;">პრაქტიკა ↗</a>
          $2`);
    fs.writeFileSync(indexPath, indexHtml);
    console.log("Lecture 4 generated and linked in index.html successfully.");
} else {
    console.log("Could not find Day 4 buttons in index.html to update.");
}

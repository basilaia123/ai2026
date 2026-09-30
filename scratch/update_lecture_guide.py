import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"c:\Users\GBASILAIA\claude\ai2026\openday\teachers-ai-lecture.html"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Sidebar
sidebar_old = '''    <a href="#seg-demo2" class="nav-link flex items-center justify-between px-5 py-2.5 text-sm text-gold-400 transition-all duration-200 border-l-[3px] border-transparent" data-topic="seg-demo2">
      <span class="leading-snug pr-2">3. DEMO 2: ინტერაქტიული სლაიდები</span>
      <span class="shrink-0 text-[10px] bg-gold-500/20 text-gold-400 px-1.5 py-0.5 rounded">20 წთ</span>
    </a>'''

sidebar_new = '''    <a href="#seg-demo2" class="nav-link flex items-center justify-between px-5 py-2.5 text-sm text-gold-400 transition-all duration-200 border-l-[3px] border-transparent" data-topic="seg-demo2">
      <span class="leading-snug pr-2">3. DEMO 2: ინტერაქტიული სლაიდები</span>
      <span class="shrink-0 text-[10px] bg-gold-500/20 text-gold-400 px-1.5 py-0.5 rounded">20 წთ</span>
    </a>
    <a href="#seg-demo2-visual" class="nav-link flex items-center justify-between px-5 py-2 pl-8 text-xs text-purple-300 transition-all duration-200 border-l-[3px] border-transparent" data-topic="seg-demo2-visual">
      <span class="leading-snug pr-2">↳ 🎨 ვიზუალური გენერაცია (5 პრომპტი)</span>
    </a>'''

if sidebar_old in content:
    content = content.replace(sidebar_old, sidebar_new)
    print("Sidebar updated")
else:
    print("Sidebar not matched")

# 2. Header
header_old = 'მოსწავლეების ჩართვის თამაში'
header_new = 'მოსწავლეთა ჩართულობის თამაში'
if header_old in content:
    content = content.replace(header_old, header_new)
    print("Header updated")

# 3. History and Biology cards
hist_bio_old = '''        <div id="seg-demo1-history" class="scroll-mt-24 border-t-4 border-cyan-500 rounded-lg p-4 bg-gray-50">
          <p class="font-bold text-ink-950 text-sm mb-1">🏛️ ისტორია</p>
          <p class="text-xs text-cyan-600 mb-2">მაგ: საქართველოს ისტორია, 8 კლასი</p>
          <ul class="text-xs text-gray-600 space-y-1">
            <li>• როლური სასამართლო - ისტორიული ფიგურის „განსჯა"</li>
            <li>• დებატი: „რა მოხდებოდა, თუ..." ალტერნატიული სცენარი</li>
            <li>• დროის ხაზის ჯგუფური აწყობა კლასში</li>
          </ul>
        </div>
        <div id="seg-demo1-biology" class="scroll-mt-24 border-t-4 border-gold-500 rounded-lg p-4 bg-gray-50">
          <p class="font-bold text-ink-950 text-sm mb-1">🧬 ბიოლოგია</p>
          <p class="text-xs text-gold-600 mb-2">მაგ: უჯრედის აგებულება, 8 კლასი</p>
          <ul class="text-xs text-gray-600 space-y-1">
            <li>• "ააშენე უჯრედი" - ჯგუფური კონსტრუქტორის ამოცანა</li>
            <li>• სიმულაცია: მოსწავლეები = ორგანელები, თამაშობენ ფუნქციებს</li>
            <li>• გამოძიება: "რომელი ორგანელა დააშავა საქმე?"</li>
          </ul>
        </div>'''

hist_bio_new = '''        <div id="seg-demo1-history" class="scroll-mt-24 border-t-4 border-cyan-500 rounded-lg p-4 bg-gray-50">
          <p class="font-bold text-ink-950 text-sm mb-1">🏛️ ისტორია</p>
          <p class="text-xs text-cyan-600 mb-2">მაგ: საქართველოს ისტორია, VIII კლასი</p>
          <ul class="text-xs text-gray-600 space-y-1">
            <li>• როლური სასამართლო - ისტორიული ფიგურის „განსჯა“</li>
            <li>• დებატი: „რა მოხდებოდა, თუ...“ ალტერნატიული სცენარი</li>
            <li>• დროის ხაზის ჯგუფური აწყობა კლასში</li>
          </ul>
        </div>
        <div id="seg-demo1-biology" class="scroll-mt-24 border-t-4 border-gold-500 rounded-lg p-4 bg-gray-50">
          <p class="font-bold text-ink-950 text-sm mb-1">🧬 ბიოლოგია</p>
          <p class="text-xs text-gold-600 mb-2">მაგ: უჯრედის აგებულება, VIII კლასი</p>
          <ul class="text-xs text-gray-600 space-y-1">
            <li>• „ააშენე უჯრედი“ - ჯგუფური კონსტრუქტორის ამოცანა</li>
            <li>• სიმულაცია: მოსწავლეები = ორგანელები, ასრულებენ შესაბამის ფუნქციებს</li>
            <li>• გამოძიება: „რომელმა ორგანელამ გააფუჭა საქმე?“</li>
          </ul>
        </div>'''

if hist_bio_old in content:
    content = content.replace(hist_bio_old, hist_bio_new)
    print("History and biology updated")
else:
    print("History and biology not matched")

# 4. Insert 5 visual generation prompts section
visual_section = '''  <!-- ═══ SUB-SEGMENT: VISUAL GENERATION FOR CLASSROOM (5 DETAILED PROMPTS) ═══ -->
  <section id="seg-demo2-visual" class="scroll-mt-20 mb-12">
    <div class="topic-card bg-white rounded-xl shadow-sm p-6" style="border-left-color:#8b5cf6;">
      <div class="flex items-start gap-4 mb-4">
        <div class="shrink-0 w-10 h-10 rounded-full bg-purple-600 text-white flex items-center justify-center font-bold text-base">🎨</div>
        <div class="flex-1">
          <span class="text-xs font-semibold uppercase tracking-wider text-purple-600">მოდული 3 · პრაქტიკული ბანკი</span>
          <h2 class="text-xl font-bold text-ink-950">ვიზუალური გენერაცია საკლასო ოთახისთვის — 5 სრული პრომპტი</h2>
          <p class="text-gray-500 text-sm mt-1">მზა, გამოცდილი პრომპტები საუკეთესო AI გენერატორებისთვის (Midjourney, Recraft, DALL-E 3, Ideogram, Canva). თითოეულ პრომპტს ახლავს სასკოლო დანიშნულება, ქართული განმარტება და პედაგოგიური მეთოდი.</p>
        </div>
      </div>

      <!-- 5 Prompts Cards -->
      <div class="space-y-6">

        <!-- Prompt 1: Literature / Storybook -->
        <div class="border border-purple-100 rounded-xl p-5 bg-purple-50/30">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <span class="font-bold text-ink-950 text-sm flex items-center gap-1.5">
              <span>📖</span> 1. ქართული ენა და ლიტერატურა — მოთხრობის ილუსტრაცია & კომიქსი
            </span>
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] bg-purple-100 text-purple-700 px-2 py-0.5 rounded font-semibold">III-VI კლასი</span>
              <span class="text-[11px] bg-sky-100 text-sky-700 px-2 py-0.5 rounded font-semibold">Midjourney / Recraft / DALL-E 3</span>
            </div>
          </div>
          <p class="text-xs text-gray-600 mb-3 leading-relaxed">
            <strong>სასკოლო მიზანი:</strong> ტექსტის გააზრება, პერსონაჟთა ემოციების ამოცნობა და დეტალების ანალიზი (აკაკი წერეთლის მოთხრობა „გიმნაზიაში“).
          </p>
          <div class="prompt-box mb-3">
            <button class="copy-btn" onclick="copyPrompt(this)">კოპირება</button>
            <pre>A detailed, heartwarming children's book watercolor illustration depicting a scene from 19th-century Georgian gymnasium classroom. In the foreground, a 10-year-old Georgian schoolboy in traditional dark wool choxa is sitting at a vintage wooden school desk, secretly keeping a warm, freshly baked round cornbread (mchadi) wrapped in clean linen inside his pocket, smiling nervously. In the background, a dignified Georgian schoolmaster with kind eyes and a classic moustache stands beside a chalkboard written with Georgian alphabet chalk inscriptions. Soft warm morning sunlight streaming through high arched windows, nostalgic vintage color palette, rich textures, storybook style, no distorted limbs, highly expressive facial emotions, ultra-high resolution --ar 16:9 --style raw</pre>
          </div>
          <div class="text-xs text-gray-600 space-y-1 bg-white p-3 rounded-lg border border-purple-100">
            <p><strong>🇬🇪 ქართული შინაარსი:</strong> XIX საუკუნის ქართული გიმნაზიის საკლასო ოთახი. 10 წლის მოსწავლე ჩოხაში, რომელსაც ჯიბეში დედის გამომცხვარი ცხელი მჭადი აქვს დამალული და ნერვიულად იღიმის; ფონზე კეთილი ულვაშიანი მასწავლებელი დაფასთან ქართული ანბანის წარწერებით; დილის თბილი მზე თაღოვანი ფანჯრებიდან.</p>
            <p><strong>🎯 საკლასო აქტივობა:</strong> „ვიზუალური დეტექტივი“ — მოსწავლეები აკვირდებიან ნახატს და პასუხობენ: „რა დეტალებია ნახატზე ისეთი, რაც ტექსტში პირდაპირ არ წერია, მაგრამ ეპოქას გადმოგვცემს?“ (ჩოხა, მელნის საწერი, მერხის ფორმა).</p>
          </div>
        </div>

        <!-- Prompt 2: Biology / 3D Cross-Section -->
        <div class="border border-emerald-100 rounded-xl p-5 bg-emerald-50/30">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <span class="font-bold text-ink-950 text-sm flex items-center gap-1.5">
              <span>🧬</span> 2. ბიოლოგია & ბუნებისმეტყველება — 3D ანატომიური ჭრილი & ინფოგრაფიკა
            </span>
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] bg-emerald-100 text-emerald-700 px-2 py-0.5 rounded font-semibold">VII-VIII კლასი</span>
              <span class="text-[11px] bg-sky-100 text-sky-700 px-2 py-0.5 rounded font-semibold">Recraft (3D) / Midjourney / DALL-E 3</span>
            </div>
          </div>
          <p class="text-xs text-gray-600 mb-3 leading-relaxed">
            <strong>სასკოლო მიზანი:</strong> მცენარეული უჯრედის ორგანელების სივრცითი განლაგებისა და ფუნქციების შესწავლა; მზადდება ცარიელი მანიშნებლებით (Blank Callouts) სამუშაო ფურცლისთვის.
          </p>
          <div class="prompt-box mb-3">
            <button class="copy-btn" onclick="copyPrompt(this)">კოპირება</button>
            <pre>Educational isometric 3D cross-section diagram of a eukaryotic plant cell, scientific textbook illustration style. High-detail cutaway view revealing nucleus with nucleolus, chloroplasts with green thylakoids, mitochondria, large central vacuole with light blue cell sap, Golgi apparatus, and thick rigid cell wall. Vibrant distinct contrasting colors for each organelle, clean studio lighting, isolated on solid pure white background, crisp smooth textures, educational science poster quality, no blurry text, schematic scientific accuracy --ar 4:3 --stylize 200</pre>
          </div>
          <div class="text-xs text-gray-600 space-y-1 bg-white p-3 rounded-lg border border-emerald-100">
            <p><strong>🇬🇪 ქართული შინაარსი:</strong> ევკარიოტული მცენარეული უჯრედის იზომეტრიული 3D ჭრილი. მკაფიოდ ჩანს ბირთვი, ქლოროპლასტები, მიტოქონდრიები, დიდი ვაკუოლი და უჯრედის კედელი კონტრასტულ ფერებში, სუფთა თეთრ ფონზე.</p>
            <p><strong>🎯 საკლასო აქტივობა:</strong> „ორგანელების რუკა“ — დაბეჭდილ ფურცელზე მოსწავლეები ისრებით თავად აწერენ ორგანელების სახელებს და წყვილებში ხსნიან: „რა მოხდება, თუ ეს კონკრეტული ორგანელა გაითიშება?“</p>
          </div>
        </div>

        <!-- Prompt 3: History / Epoch Reconstruction -->
        <div class="border border-amber-100 rounded-xl p-5 bg-amber-50/30">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <span class="font-bold text-ink-950 text-sm flex items-center gap-1.5">
              <span>🏛️</span> 3. ისტორია & სამოქალაქო განათლება — ეპოქალური ისტორიული რეკონსტრუქცია
            </span>
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] bg-amber-100 text-amber-700 px-2 py-0.5 rounded font-semibold">VIII-XI კლასი</span>
              <span class="text-[11px] bg-sky-100 text-sky-700 px-2 py-0.5 rounded font-semibold">Midjourney v6 / Ideogram / Flux</span>
            </div>
          </div>
          <p class="text-xs text-gray-600 mb-3 leading-relaxed">
            <strong>სასკოლო მიზანი:</strong> ისტორიული ეპოქის ყოფის, სამშენებლო ხელოვნებისა და პოლიტიკური კონტექსტის გაცოცხლება (დავით IV აღმაშენებელი და გელათის მშენებლობა).
          </p>
          <div class="prompt-box mb-3">
            <button class="copy-btn" onclick="copyPrompt(this)">კოპირება</button>
            <pre>Cinematic historical reconstruction of medieval Georgia in the early 12th century. King David the Builder, tall and noble, dressed in royal Byzantine-Georgian ceremonial robes with silver embroidery, reviewing architectural blueprints on parchment table outdoors overlooking the construction of Gelati Monastery in Kutaisi. In the background, stonemasons carving tuff stones, wooden scaffolding on cathedral arches, verdant Imereti mountain hills in misty golden hour lighting. Authentic medieval historical details, photorealistic textures, atmospheric depth, cinematic lighting, National Geographic documentary photography style --ar 16:9 --v 6.0</pre>
          </div>
          <div class="text-xs text-gray-600 space-y-1 bg-white p-3 rounded-lg border border-amber-100">
            <p><strong>🇬🇪 ქართული შინაარსი:</strong> XII საუკუნის დასაწყისის საქართველოს ისტორიული რეკონსტრუქცია. მეფე დავით აღმაშენებელი საზეიმო სამოსში განიხილავს გელათის სამშენებლო ნახაზებს; ფონზე ქვისმთლელები, ხის ხარაჩოები და იმერეთის მთები მზის ჩასვლის შუქზე.</p>
            <p><strong>🎯 საკლასო აქტივობა:</strong> „ისტორიული ინტერვიუ და როლური დებატი“ — მოსწავლეები ნახატზე დაყრდნობით წერენ მეფის დღიურის ჩანაწერს: რატომ ჩადო სახელმწიფომ უდიდესი რესურსი არა მხოლოდ ციხესიმაგრეებში, არამედ აკადემიასა და განათლებაში?</p>
          </div>
        </div>

        <!-- Prompt 4: Mathematics / Everyday Geometry -->
        <div class="border border-sky-100 rounded-xl p-5 bg-sky-50/30">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <span class="font-bold text-ink-950 text-sm flex items-center gap-1.5">
              <span>📐</span> 4. მათემატიკა & გეომეტრია — ცნების ვიზუალიზაცია რეალურ სამყაროში
            </span>
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] bg-sky-100 text-sky-700 px-2 py-0.5 rounded font-semibold">IV-VII კლასი</span>
              <span class="text-[11px] bg-sky-100 text-sky-700 px-2 py-0.5 rounded font-semibold">Recraft (Clay/3D) / Midjourney / DALL-E 3</span>
            </div>
          </div>
          <p class="text-xs text-gray-600 mb-3 leading-relaxed">
            <strong>სასკოლო მიზანი:</strong> წილადებისა და სივრცითი გეომეტრიული ფიგურების გაგება ყოველდღიური ცხოვრების მაგალითზე; მათემატიკის შიშის დაძლევა სახალისო ვიზუალით.
          </p>
          <div class="prompt-box mb-3">
            <button class="copy-btn" onclick="copyPrompt(this)">კოპირება</button>
            <pre>Charming 3D animated educational scene demonstrating fractions and geometry in a playful kid-friendly bakery town. A friendly cartoon baker character slicing a large round artisanal pizza into exact fractions: 1/2, 1/4, and 1/8 pieces, alongside colorful hexagonal honeycakes, triangular pies, and cylindrical bread loaves. Vibrant pastel lighting, isometric perspective, Pixar 3D render style, claymation aesthetic, joyful and welcoming math learning environment, clear geometric shapes, high detail, clean rendering, 8k resolution --ar 16:9</pre>
          </div>
          <div class="text-xs text-gray-600 space-y-1 bg-white p-3 rounded-lg border border-sky-100">
            <p><strong>🇬🇪 ქართული შინაარსი:</strong> Pixar-ის 3D ანიმაციური სტილის საცხობი, სადაც მხიარული მცხობელი მრგვალ პიცას ჭრის ზუსტ წილადებად (1/2, 1/4, 1/8); ირგვლივ ექვსკუთხა, სამკუთხა და ცილინდრული ნამცხვრებია მკაფიო გეომეტრიული ფორმებით.</p>
            <p><strong>🎯 საკლასო აქტივობა:</strong> „საცხობის ამოცანა“ — მოსწავლეები ითვლიან: თუ კლასმა შეუკვეთა 2 მთელი პიცა და თითოეულმა მოსწავლემ მიიღო 1/8 ნაჭერი, რამდენ მოსწავლეს ეყოფა პიცა?</p>
          </div>
        </div>

        <!-- Prompt 5: Classroom Culture / Growth Mindset Poster -->
        <div class="border border-rose-100 rounded-xl p-5 bg-rose-50/30">
          <div class="flex flex-wrap items-center justify-between gap-2 mb-2">
            <span class="font-bold text-ink-950 text-sm flex items-center gap-1.5">
              <span>🌟</span> 5. საკლასო კულტურა & მოტივაცია — საგანმანათლებლო პოსტერი (A3/A4)
            </span>
            <div class="flex items-center gap-1.5">
              <span class="text-[11px] bg-rose-100 text-rose-700 px-2 py-0.5 rounded font-semibold">I-XII კლასი (უნივერსალური)</span>
              <span class="text-[11px] bg-sky-100 text-sky-700 px-2 py-0.5 rounded font-semibold">Ideogram (ტექსტით) / Recraft / Canva</span>
            </div>
          </div>
          <p class="text-xs text-gray-600 mb-3 leading-relaxed">
            <strong>სასკოლო მიზანი:</strong> პოზიტიური საკლასო გარემოსა და ზრდის აზროვნების (Growth Mindset) ჩამოყალიბება; მზა პოსტერი საკლასო ოთახის კედლისთვის.
          </p>
          <div class="prompt-box mb-3">
            <button class="copy-btn" onclick="copyPrompt(this)">კოპირება</button>
            <pre>Modern minimalist educational wall poster for elementary and middle school classroom decor, flat vector art style. Diverse group of cheerful school children working together to build a towering creative rocket made of books, pencils, gears, and glowing lightbulbs. Inspiring, warm, welcoming color palette of soft navy, mustard yellow, sage green, and coral. Clean graphic design composition, central typography space, Scandinavian children's book illustration aesthetic, ready for high-resolution A3 print --ar 3:4</pre>
          </div>
          <div class="text-xs text-gray-600 space-y-1 bg-white p-3 rounded-lg border border-rose-100">
            <p><strong>🇬🇪 ქართული შინაარსი:</strong> მინიმალისტური ვექტორული პოსტერი სკოლისთვის. მოსწავლეები ერთად აწყობენ წიგნებისგან, ფანქრებისგან და ნათურებისგან შექმნილ რაკეტას; თბილი ფერები (მდოგვისფერი, მარჯნისფერი, სალბისფერი მწვანე), სკანდინავიური საბავშვო ილუსტრაციის სტილი.</p>
            <p><strong>🎯 საკლასო აქტივობა:</strong> „კლასის კონსტიტუცია“ — მასწავლებელი პოსტერს ბეჭდავს Canva-ში, ცენტრში ამატებს კლასის 5 ოქროს წესს ქართულ ენაზე, და სასწავლო წლის დასაწყისში ყველა მოსწავლე ხელს აწერს მასზე.</p>
          </div>
        </div>

      </div>

      <!-- Pro-Tip Box -->
      <div class="tip-box p-4 text-xs text-gray-700 mt-6 leading-relaxed">
        <strong>💡 მასწავლებლის ოქროს წესები AI ილუსტრაციების გენერირებისას:</strong>
        <ul class="mt-2 space-y-1.5 list-disc pl-4">
          <li><strong>ტექსტის პრობლემა:</strong> AI-ს ხშირად უჭირს სურათში ქართული ტექსტის უშეცდომოდ ჩაწერა. <em>გამოსავალი:</em> დააგენერირეთ სურათი სუფთად ტექსტის გარეშე, შემდეგ კი გახსენით უფასო <strong>Canva</strong>-ში და დაადეთ ქართული წარწერები (Sylfaen, FiraGO, Arial GEO).</li>
          <li><strong>ასპექტის თანაფარდობა:</strong> პროექტორისთვის და ეკრანისთვის მიუთითეთ <code>--ar 16:9</code>, ხოლო დასაბეჭდი ფურცლებისთვის და პოსტერებისთვის <code>--ar 3:4</code> ან <code>--ar 1:1</code>.</li>
          <li><strong>უფასო ინსტრუმენტები:</strong> <strong>Recraft.ai</strong> იძლევა საუკეთესო ვექტორულ და 3D ხარისხს უფასო ლიმიტებით; <strong>Canva for Education</strong> კი პედაგოგებისთვის სრულიად უფასოა და შეიცავს Magic Studio-ს გენერატორს.</li>
        </ul>
      </div>
    </div>
  </section>

  <!-- ═══ SEGMENT 4: DEMO 3 GAMES ═══ -->'''

before_demo3 = '  <!-- ═══ SEGMENT 4: DEMO 3 GAMES ═══ -->'
if before_demo3 in content:
    content = content.replace(before_demo3, visual_section)
    print("Visual section added")
else:
    print("Demo 3 marker not matched")

# 5. Game prompts
game_old = '''          <pre>შექმენი "აირჩიე შენი გზა" ტიპის სცენარული თამაში თემაზე: [ჩასვით თემა], კლასი: [მიუთითეთ].
სტრუქტურა:
1. საწყისი სიტუაცია (3-4 წინადადება, ქართული სახელები და რეალური კონტექსტი)
2. 3 გადაწყვეტილების წერტილი, თითოეულზე 2-3 არჩევანი
3. თითო არჩევანს მოჰყვება რეალისტური შედეგი (2-3 წინადადება)
4. ბოლოს 2-3 შესაძლო დასასრული, დამოკიდებული არჩევანებზე
5. საკლასო განხილვის 3 კითხვა თამაშის შემდეგ'''

game_new = '''          <pre>შექმენი „აირჩიე შენი გზა“ ტიპის სცენარული თამაში თემაზე: [ჩასვით თემა], კლასი: [მიუთითეთ].
სტრუქტურა:
1. საწყისი სიტუაცია (3-4 წინადადება, ქართული სახელები და რეალური კონტექსტი)
2. 3 საკვანძო გადაწყვეტილება (არჩევანის წერტილი), თითოეულზე 2-3 არჩევანი
3. თითოეულ არჩევანს მოჰყვება რეალისტური შედეგი (2-3 წინადადება)
4. ბოლოს 2-3 შესაძლო დასასრული, დამოკიდებული არჩევანებზე
5. საკლასო განხილვის 3 კითხვა თამაშის შემდეგ'''

if game_old in content:
    content = content.replace(game_old, game_new)
    print("Game prompts updated")
else:
    print("Game prompts not matched")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("File updated successfully!")

import re

def build_day3_exercises():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-exercises.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Nav
    nav_old = '''        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — კრეატივი და SOP</div>
        <a href="#ex1" class="nav-link">🧠 სავ. 1 · შებრუნებული აზროვნება</a>
        <a href="#ex2" class="nav-link">📝 სავ. 2 · Few-Shot პრომპტინგი</a>
        <a href="#ex3" class="nav-link">📑 სავ. 3 · Notion AI სტრუქტურა</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი II — ანალიზი და კვლევა</div>
        <a href="#ex4" class="nav-link">🔍 სავ. 4 · Perplexity კვლევა</a>
        <a href="#ex5" class="nav-link">📚 სავ. 5 · NotebookLM დოკუმენტები</a>
        <a href="#ex6" class="nav-link">📊 სავ. 6 · მონაცემთა ანალიზი</a>'''

    nav_new = '''        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — ასისტენტები</div>
        <a href="#ex1" class="nav-link">🤖 სავ. 1 · Custom GPT / Gem ინსტრუქცია</a>
        <a href="#ex2" class="nav-link">⚙️ სავ. 2 · რუტინის ავტომატიზაცია</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი II — სტრატეგია და უსაფრთხოება</div>
        <a href="#ex3" class="nav-link">🛡️ სავ. 3 · Shadow AI პოლიტიკა</a>
        <a href="#ex4" class="nav-link">🚀 სავ. 4 · 3 Quick Wins</a>'''

    html = html.replace(nav_old, nav_new)
    
    # Headers
    html = html.replace('დღე 2: ოპერაციები და ანალიზი', 'დღე 3: დანერგვა და მართვა')
    html = html.replace('დღე 2: სავარჯიშოები', 'დღე 3: სავარჯიშოები')
    html = html.replace('დღე 2: სტრატეგიული ოპერაციები, ფინანსები, იურიდიული და PR ანალიზი', 'დღე 3: დანერგვა, კორპორატიული მართვა და Governance')
    html = html.replace('6 ინტენსიური პრაქტიკული დავალება', '4 სტრატეგიული პრაქტიკული დავალება')
    html = html.replace('6 დავალება · ტოპ-მენეჯმენტი', '4 დავალება · ტოპ-მენეჯმენტი')
    html = html.replace('day-2-slides.html', 'day-3-slides.html')
    html = html.replace('6 სავარჯიშო', '4 სავარჯიშო')

    # Content replacement
    content_start = html.find('<!-- ═══════════════════════════════════════════════════\n     OVERVIEW')
    content_end = html.find('<!-- Back to Top -->')

    new_content = '''<!-- ═══════════════════════════════════════════════════
     OVERVIEW
═══════════════════════════════════════════════════ -->
<section id="ex-overview" class="min-h-[70vh] flex flex-col justify-center py-12 border-b border-gray-200 topic-card">
    <span class="badge badge-ex">📋 მიმოხილვა</span>
    <h2 class="text-3xl font-bold mb-6">სავარჯიშოების რუქა და ქულები</h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-0 rounded-xl overflow-hidden shadow-lg mb-8">
        <div class="p-6" style="background:#0f1f2e;">
            <h3 class="text-lg font-bold text-white mb-3 border-b border-white/10 pb-2">ბლოკი I: ასისტენტები (50 ქულა)</h3>
            <ul class="text-sm text-gray-300 space-y-2">
                <li>• 🤖 1. Custom GPT ინსტრუქცია <span class="float-right text-pink-400">30 ქულა</span></li>
                <li>• ⚙️ 2. რუტინის ავტომატიზაცია <span class="float-right text-pink-400">20 ქულა</span></li>
            </ul>
        </div>
        <div class="p-6" style="background:#1a2f42;">
            <h3 class="text-lg font-bold text-white mb-3 border-b border-white/10 pb-2">ბლოკი II: სტრატეგია (50 ქულა)</h3>
            <ul class="text-sm text-gray-300 space-y-2">
                <li>• 🛡️ 3. Shadow AI პოლიტიკა <span class="float-right text-pink-400">20 ქულა</span></li>
                <li>• 🚀 4. 3 Quick Wins <span class="float-right text-pink-400">30 ქულა</span></li>
            </ul>
        </div>
        <div class="p-6 flex flex-col items-center justify-center" style="background:linear-gradient(135deg, #E91E63 0%, #2196F3 100%);">
            <p class="text-white/80 font-bold uppercase tracking-wider text-xs mb-2">ჯამური ქულა</p>
            <div class="w-24 h-24 rounded-full bg-white/20 flex items-center justify-center border-4 border-white">
                <span class="text-3xl font-black text-white">100</span>
            </div>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     BLOCK I
═══════════════════════════════════════════════════ -->
<div class="py-8 border-b border-gray-200">
    <div class="section-header">
        <div class="flex items-center gap-4">
            <span class="text-4xl">🤖</span>
            <div>
                <h2 class="text-2xl font-bold text-white">ბლოკი I: კორპორატიული ასისტენტები</h2>
                <p class="text-gray-300 text-sm mt-1">სპეციფიკური AI აგენტების აწყობა და ავტომატიზაცია</p>
            </div>
        </div>
    </div>
</div>

<section id="ex1" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-practice">🤖 სავარჯიშო 1</span>
            <h2 class="text-2xl font-bold">Custom GPT / Gem ინსტრუქცია</h2>
        </div>
        <span class="font-black text-xl text-gray-400">30 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">Megalab-ის იურიდიულ დეპარტამენტს სჭირდება პერსონალური ასისტენტი (Gem), რომელიც შეამოწმებს შიდა ხელშეკრულებებს და იპოვის რისკებს JCI სტანდარტების მიხედვით.</p>

    <div class="card" style="background:#e3f2fd; border-left: 4px solid #2196F3;">
        <p class="font-bold text-blue-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">დაწერეთ "System Instruction" (ინსტრუქცია) ამ ასისტენტისთვის. როგორი უნდა იყოს მისი როლი, რა ფაილები უნდა ჩაეტვირთოს მას ცოდნის ბაზაში (Knowledge) და როგორი ფორმატით უნდა დააბრუნოს პასუხი?</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="ჩაწერეთ System Instruction..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans1').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans1" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">[Role] შენ ხარ Megalab-ის JCI და იურიდიული შესაბამისობის ექსპერტი. 
[Task] შენი მიზანია ატვირთული კონტრაქტების ანალიზი და რისკების იდენტიფიცირება JCI სტანდარტების მიხედვით.
[Knowledge] იხელმძღვანელე მხოლოდ შენში ატვირთული JCI აკრედიტაციის სახელმძღვანელოთი (PDF) და GDPR რეგულაციებით. თუ რამე არ წერია ამ დოკუმენტებში, უპასუხე "ინფორმაცია არ მოიძებნება".
[Format] პასუხი დააბრუნე ქართულად, შემდეგი სტრუქტურით: 1. კრიტიკული რისკები (წითელი) 2. გასასწორებელი პუნქტები (ყვითელი) 3. რეკომენდაცია.</div>
    </div>
</section>

<section id="ex2" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-quiz">⚙️ სავარჯიშო 2</span>
            <h2 class="text-2xl font-bold">რუტინის ავტომატიზაცია</h2>
        </div>
        <span class="font-black text-xl text-gray-400">20 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">დეპარტამენტული ეფექტიანობის ზრდა იწყება განმეორებადი პროცესების პოვნით.</p>

    <div class="card" style="background:#fff3e0; border-left: 4px solid #FF5722;">
        <p class="font-bold text-orange-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800 mb-2">გაიხსენეთ თქვენი დეპარტამენტის 1 კონკრეტული ყოველდღიური პროცესი, რომელსაც 1 საათზე მეტი მიაქვს (მაგ. მეილებზე სტანდარტული პასუხები, რეპორტების შეჯამება, მონაცემების შეყვანა). როგორ ჩართავდით AI-ს ამ რუტინის ავტომატიზაციაში?</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="აღწერეთ რუტინა და AI გამოსავალი..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans2').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans2" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხის მაგალითი (HR დეპარტამენტი):</p>
        <div class="code-block" style="font-size:0.85rem;">პრობლემა: კანდიდატების CV-ების პირველადი გადარჩევა და კრიტერიუმებთან შედარება მიაქვს დღეში 2 საათი.
AI ავტომატიზაცია: შევქმნი Gemini Gem-ს, სადაც ავტვირთავ Megalab-ის სტანდარტულ ვაკანსიის მოთხოვნებს (Knowledge). როდესაც ახალი CV-ები შემოვა, ერთიანად ჩავუგდებ და ვეტყვი: "ამოარჩიე ის კანდიდატები, ვისაც აქვს ლაბორატორიული გამოცდილება და გაუგზავნე სტანდარტული უარყოფის მეილი დანარჩენებს." ეს პროცესს შეამცირებს 10 წუთამდე.</div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     BLOCK II
═══════════════════════════════════════════════════ -->
<div class="py-8 border-b border-gray-200">
    <div class="section-header">
        <div class="flex items-center gap-4">
            <span class="text-4xl">🛡️</span>
            <div>
                <h2 class="text-2xl font-bold text-white">ბლოკი II: სტრატეგია და უსაფრთხოება</h2>
                <p class="text-gray-300 text-sm mt-1">Governance, Shadow AI და სწრაფი მოგებები</p>
            </div>
        </div>
    </div>
</div>

<section id="ex3" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-demo">🛡️ სავარჯიშო 3</span>
            <h2 class="text-2xl font-bold">Shadow AI და უსაფრთხოების პოლიტიკა</h2>
        </div>
        <span class="font-black text-xl text-gray-400">20 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">"Shadow AI" არის როდესაც თანამშრომლები მენეჯმენტისგან მალულად, პირადი ექაუნთებით იყენებენ AI-ს სამსახურებრივი საქმისთვის და ტვირთავენ სენსიტიურ დოკუმენტებს.</p>

    <div class="card" style="background:#fce4ec; border-left: 4px solid #E91E63;">
        <p class="font-bold text-pink-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">შეადგინეთ 3 მთავარი შეზღუდვის (წესის) სია Megalab-ის თანამშრომლებისთვის, რათა აირიდოთ კონფიდენციალური მონაცემების გაჟონვა ღია AI სისტემებში (მაგ. უფასო ChatGPT).</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="ჩაწერეთ 3 მთავარი წესი..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans3').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans3" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">1. კატეგორიულად იკრძალება პაციენტის პერსონალური მონაცემების (სახელი, გვარი, პირადი ნომერი, ანალიზის შედეგი) შეყვანა ნებისმიერ AI ჩატბოტში. ანალიზისთვის უნდა მოხდეს მონაცემების ანონიმიზაცია.
2. იკრძალება მეგალაბის ფინანსური მონაცემების, გაუხმაურებელი სტრატეგიული გეგმების და JCI აუდიტის შიდა დასკვნების ატვირთვა უფასო, ღია AI პლატფორმებზე (დასაშვებია მხოლოდ კორპორატიული, დაცული Enterprise ვერსიით).
3. ნებისმიერი AI-გენერირებული რეპორტი, იურიდიული დოკუმენტი თუ სამედიცინო რეკომენდაცია გაზიარებამდე აუცილებლად უნდა გაიაროს ადამიანის მიერ გადამოწმება (Human-in-the-loop).</div>
    </div>
</section>

<section id="ex4" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-practice">🚀 სავარჯიშო 4</span>
            <h2 class="text-2xl font-bold">დეპარტამენტული დანერგვა (3 Quick Wins)</h2>
        </div>
        <span class="font-black text-xl text-gray-400">30 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">წარმატებული ტრანსფორმაცია იწყება მცირე, მაგრამ სწრაფი და შესამჩნევი გამარჯვებებით (Quick wins).</p>

    <div class="card" style="background:#e8f5e9; border-left: 4px solid #4CAF50;">
        <p class="font-bold text-green-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">თქვენ ხართ თქვენი დეპარტამენტის ხელმძღვანელი. დაწერეთ <strong>AI-ის დანერგვის 3 სწრაფი პროექტი</strong>, რომელსაც ხვალვე შეასრულებთ და რომელიც უახლოეს 1 კვირაში რეალურ შედეგს (დროის დაზოგვას) მოგიტანთ.</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="ჩამოწერეთ 3 Quick Wins..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans4').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans4" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხის მაგალითი:</p>
        <div class="code-block" style="font-size:0.85rem;">1. PR / მარკეტინგი: შევქმნი საერთო C.R.E.A.T.E. შაბლონს სოციალური ქსელების პოსტებისთვის და Gamma-ს დახმარებით ყველა მარკეტინგულ პრეზენტაციას ავაჩქარებთ 50%-ით.
2. გაყიდვები (B2B): კლიენტებთან გასაგზავნი სტანდარტული კომერციული წინადადებების დრაფტების გენერირებას მივანდობ Claude-ს, რათა მენეჯერებმა დრო დახარჯონ მოლაპარაკებებზე და არა ტექსტის წერაზე.
3. ოპერაციები / ხარისხი: ავტვირთავ JCI სახელმძღვანელოს NotebookLM-ში, რათა თანამშრომლებს კითხვების გაჩენისას პირდაპირ ჰქონდეთ წვდომა ლოკალიზებულ AI-სთან, ნაცვლად 100 გვერდიანი დოკუმენტის კითხვისა.</div>
    </div>
</section>

<!-- END -->
<div class="mt-12 p-6 rounded-xl text-center" style="background:linear-gradient(135deg,#0f1f2e,#1a3a5c);">
    <p class="text-4xl mb-4">🏆</p>
    <p class="text-white font-bold text-2xl mb-2">გილოცავთ! ტრენინგის პრაქტიკული ნაწილი დასრულებულია.</p>
    <p class="text-gray-300 text-sm mb-6">თქვენ მზად ხართ Megalab-ში AI სტრატეგიის დასანერგად.</p>
    <a href="day-3-slides.html" class="inline-block bg-[#E91E63] hover:bg-[#C2185B] text-white font-bold py-3 px-8 rounded-lg transition-colors">← დაბრუნდი სლაიდებზე</a>
</div>
    
    </div>
</main>
'''
    html = html[:content_start] + new_content + html[content_end:]
    
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-3-exercises.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Day 3 Exercises built.")

if __name__ == '__main__':
    build_day3_exercises()
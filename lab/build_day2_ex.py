import re

def build_day2_exercises():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-exercises.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # The actual exercises for Day 2 based on the plan are:
    # 1. Reverse Brainstorming / Idea generation (10 ideas)
    # 2. Notion AI - Create a strategic document / SOP
    # 3. NotebookLM - Querying a complex document
    # 4. Rows AI / Excel analysis (Demo mostly, but could be a small exercise)
    
    # Let's replace the navigation first
    nav_old = '''        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ნაწილი I — თეორია</div>
        <a href="#ex1" class="nav-link">🧠 სავ. 1 · AI vs ტრადიციული</a>
        <a href="#ex2" class="nav-link">⚙️ სავ. 2 · LLM — True/False</a>
        <a href="#ex3" class="nav-link">🏥 სავ. 3 · JCI/GDPR სცენარები</a>
        <a href="#ex4" class="nav-link">⚠️ სავ. 4 · ჰალუცინაცია-ტესტი</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ნაწილი II — პრომპტინგი</div>
        <a href="#ex5" class="nav-link">📝 სავ. 5 · R.O.L.E. შეავსე</a>
        <a href="#ex6" class="nav-link">🏗️ სავ. 6 · C.R.E.A.T.E. დახარისხება</a>
        <a href="#ex7" class="nav-link">⚡ სავ. 7 · Before → After</a>
        <a href="#ex8" class="nav-link">🔄 სავ. 8 · Iterative Prompting</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ნაწილი III — რეალური სცენარები</div>
        <a href="#ex9" class="nav-link">💼 სავ. 9 · B2B / PR / მენეჯმენტი</a>
        <a href="#ex10" class="nav-link">📱 სავ. 10 · სოციალური მედია</a>
        <a href="#ex11" class="nav-link">🎨 სავ. 11 · Gamma.app</a>
        <a href="#ex12" class="nav-link">🏆 სავ. 12 · ბონუს-გამოწვევა</a>'''
        
    nav_new = '''        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი I — კრეატივი და SOP</div>
        <a href="#ex1" class="nav-link">🧠 სავ. 1 · შებრუნებული აზროვნება</a>
        <a href="#ex2" class="nav-link">📝 სავ. 2 · Few-Shot პრომპტინგი</a>
        <a href="#ex3" class="nav-link">📑 სავ. 3 · Notion AI სტრუქტურა</a>

        <div class="px-5 pt-4 pb-1 text-[10px] uppercase tracking-wider text-gray-500 font-bold">ბლოკი II — ანალიზი და კვლევა</div>
        <a href="#ex4" class="nav-link">🔍 სავ. 4 · Perplexity კვლევა</a>
        <a href="#ex5" class="nav-link">📚 სავ. 5 · NotebookLM დოკუმენტები</a>
        <a href="#ex6" class="nav-link">📊 სავ. 6 · მონაცემთა ანალიზი</a>'''
        
    html = html.replace(nav_old, nav_new)
    
    # Update title and descriptions in the header
    html = html.replace('12 სავარჯიშო სამ ნაწილად', '6 ინტენსიური პრაქტიკული დავალება')
    html = html.replace('12 სავარჯიშო', '6 სავარჯიშო')
    html = html.replace('12 სავარჯიშო · ყველა დონე', '6 დავალება · ტოპ-მენეჯმენტი')
    
    # Replace the actual content section
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
            <h3 class="text-lg font-bold text-white mb-3 border-b border-white/10 pb-2">ბლოკი I: კრეატივი და SOP (45 ქულა)</h3>
            <ul class="text-sm text-gray-300 space-y-2">
                <li>• 🧠 1. შებრუნებული აზროვნება <span class="float-right text-pink-400">15 ქულა</span></li>
                <li>• 📝 2. Few-Shot პრომპტინგი <span class="float-right text-pink-400">10 ქულა</span></li>
                <li>• 📑 3. Notion AI-ში მუშაობა <span class="float-right text-pink-400">20 ქულა</span></li>
            </ul>
        </div>
        <div class="p-6" style="background:#1a2f42;">
            <h3 class="text-lg font-bold text-white mb-3 border-b border-white/10 pb-2">ბლოკი II: ანალიზი (55 ქულა)</h3>
            <ul class="text-sm text-gray-300 space-y-2">
                <li>• 🔍 4. Perplexity.ai კვლევა <span class="float-right text-pink-400">15 ქულა</span></li>
                <li>• 📚 5. NotebookLM დოკუმენტები <span class="float-right text-pink-400">25 ქულა</span></li>
                <li>• 📊 6. მონაცემთა ექსტრაქცია <span class="float-right text-pink-400">15 ქულა</span></li>
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
            <span class="text-4xl">🧠</span>
            <div>
                <h2 class="text-2xl font-bold text-white">ბლოკი I: კრეატიული აზროვნება და SOP</h2>
                <p class="text-gray-300 text-sm mt-1">იდეების გენერაცია, შებრუნებული აზროვნება და დოკუმენტაციის მართვა</p>
            </div>
        </div>
    </div>
</div>

<section id="ex1" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-practice">🧠 სავარჯიშო 1</span>
            <h2 class="text-2xl font-bold">შებრუნებული აზროვნება (Reverse Brainstorming)</h2>
        </div>
        <span class="font-black text-xl text-gray-400">15 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">ნაცვლად იმისა, რომ AI-ს პირდაპირ ვთხოვოთ გამოსავალი, ვთხოვთ <strong>პრობლემის გამწვავების</strong> გზებს, რათა დავინახოთ ფარული რისკები.</p>

    <div class="card" style="background:#fff8e1; border-left: 4px solid #FF9800;">
        <p class="font-bold text-orange-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">Megalab-ს სურს პაციენტების რიგების მართვის (Customer Flow) გაუმჯობესება. დაწერეთ C.R.E.A.T.E. პრომპტი "შებრუნებული აზროვნების" ტექნიკით: სთხოვეთ AI-ს მოიფიქროს 5 ყველაზე ცუდი გზა, რითაც პაციენტის გამოცდილება მისაღებში <strong>გაუარესდება</strong>. შემდგომ კი — ამ 5 პუნქტის საპირისპირო ოქროს წესები.</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="ჩაწერეთ თქვენი პრომპტი აქ..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans1').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans1" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">[C] Megalab-ის მისაღებში დილის საათებში იქმნება დიდი რიგები. გვსურს პაციენტების გამოცდილების გაუმჯობესება.
[R] გამოიყენე "Reverse Brainstorming" ტექნიკა: ჯერ მოიფიქრე 5 ყველაზე ეფექტური გზა, თუ როგორ შეიძლება მისაღებში პაციენტის გამოცდილება მაქსიმალურად გავაუარესოთ და გავაბრაზოთ.
შემდეგ, თითოეული ამ ცუდი პრაქტიკის გასწვრივ დაწერე მისი საპირისპირო, საუკეთესო მოქმედების წესი (Best Practice).
[A] იმოქმედე როგორც Customer Experience ექსპერტმა.
[T] მენეჯმენტისთვის. სტრატეგიული და კრიტიკული.
[E] გამოიყენე მკაფიო კონტრასტული ცხრილი ან ბულეტები.</div>
    </div>
</section>

<section id="ex2" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-practice">📝 სავარჯიშო 2</span>
            <h2 class="text-2xl font-bold">Few-Shot Prompting (მაგალითებით სწავლება)</h2>
        </div>
        <span class="font-black text-xl text-gray-400">10 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">ხშირად AI-ს სჭირდება ჩვენი სტილის მაგალითები (Shots), რათა ზუსტად იგივე ტონში დაწეროს ტექსტი.</p>

    <div class="card" style="background:#f3e5f5; border-left: 4px solid #9C27B0;">
        <p class="font-bold text-purple-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800 mb-2">ააწყვეთ პრომპტი, რომელიც მიაწვდის AI-ს Megalab-ის PR პოსტის <strong>1 კარგ მაგალითს</strong>, და შემდეგ სთხოვს დაწეროს ახალი პოსტი "ალერგიის პანელის ფასდაკლებაზე".</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="ჩაწერეთ პრომპტი + მაგალითი..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans2').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans2" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">[C] Megalab იწყებს გაზაფხულის კამპანიას ალერგიის პანელზე 20%-იანი ფასდაკლებით.
[A] იმოქმედე როგორც სოციალური მედიის მენეჯერმა.

აქ არის ჩვენი წერის სტილის მაგალითი:
---
მაგალითი 1:
"რამდენად ხშირად ამოწმებთ ფარისებრ ჯირკვალს? 🦋 დროული დიაგნოსტიკა ჯანმრთელობის საწინდარია. Megalab-ში ფარისებრის სრული პანელი ახლა ხელმისაწვდომია. 📍 მობრძანდით ჩვენს ნებისმიერ ფილიალში წინასწარი ჩაწერის გარეშე. #Megalab #ჯანმრთელობა"
---

[R] ამ სტილის (მოკლე, ემოჯიებით, პირდაპირი CTA) მიბაძვით, დაწერე ახალი პოსტი გაზაფხულის ალერგიის პანელზე.
[T] მეგობრული, მზრუნველი.
[E] მაქსიმუმ 50 სიტყვა.</div>
    </div>
</section>

<section id="ex3" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-demo">📑 სავარჯიშო 3</span>
            <h2 class="text-2xl font-bold">Notion AI — SOP-ის სტრუქტურირება</h2>
        </div>
        <span class="font-black text-xl text-gray-400">20 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">Notion არის კომპანიის "ცოცხალი ტვინი". როგორ ვაიძულოთ Notion AI დაწეროს იდეალური სტანდარტული ოპერაციული პროცედურა (SOP)?</p>

    <div class="card" style="background:#e3f2fd; border-left: 4px solid #2196F3;">
        <p class="font-bold text-blue-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">თქვენ წერთ <strong>"კლიენტთა პერსონალური მონაცემების (GDPR) დაცვის SOP"</strong>-ს Megalab-ის რეგისტრატორებისთვის. დაწერეთ ის ზუსტი ბრძანება (Prompt), რომელსაც ჩაწერთ Notion AI-ში (Space ღილაკით), რათა მიიღოთ გამზადებული, სტრუქტურირებული დოკუმენტი.</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="Notion AI ბრძანება..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans3').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans3" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">დაწერე Standard Operating Procedure (SOP) დოკუმენტი თემაზე: "პაციენტის პერსონალური მონაცემების დაცვა რეგისტრატურაში JCI სტანდარტით". 
გამოიყენე Notion-ის Headings (H2, H3) და Checklists.
სტრუქტურა უნდა მოიცავდეს: 1. მიზანი 2. ვის ეხება 3. ნაბიჯ-ნაბიჯ ინსტრუქცია (ბულეტებით) 4. მკაცრად აკრძალული ქმედებები (Red Flags). 
ენა: ქართული, ოფიციალური, გასაგები.</div>
        <p class="text-xs text-gray-500 mt-2">* ამ ბრძანების Notion-ში ჩასმისთანავე მიიღებთ სრულად დაფორმატებულ Wiki-გვერდს.</p>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     BLOCK II
═══════════════════════════════════════════════════ -->
<div class="py-8 border-b border-gray-200">
    <div class="section-header">
        <div class="flex items-center gap-4">
            <span class="text-4xl">📊</span>
            <div>
                <h2 class="text-2xl font-bold text-white">ბლოკი II: კვლევა და მონაცემთა ანალიზი</h2>
                <p class="text-gray-300 text-sm mt-1">Perplexity, NotebookLM, ექსტრაქცია</p>
            </div>
        </div>
    </div>
</div>

<section id="ex4" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-quiz">🔍 სავარჯიშო 4</span>
            <h2 class="text-2xl font-bold">Perplexity.ai — სტრატეგიული კვლევა</h2>
        </div>
        <span class="font-black text-xl text-gray-400">15 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">Perplexity-ს აქვს პირდაპირი წვდომა ინტერნეტზე და იძლევა ზუსტ წყაროებს. როგორ მოვიძიოთ სანდო ინფორმაცია მენეჯმენტისთვის?</p>

    <div class="card" style="background:#e8f5e9; border-left: 4px solid #4CAF50;">
        <p class="font-bold text-green-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">Megalab განიხილავს ახალი ლაბორატორიული ტექნოლოგიების დანერგვას ევროპული გამოცდილებით. დაწერეთ Perplexity პრომპტი, რომელიც მოიძიებს 2025-2026 წლების უახლეს ტრენდებს სამედიცინო ლაბორატორიებში.</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="Perplexity.ai ძიების პრომპტი..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans4').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans4" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">მოიძიე 2025-2026 წლების ყველაზე გავრცელებული ინოვაციები და ტრენდები ევროპის წამყვან სამედიცინო ლაბორატორიებში (მაგ. ავტომატიზაცია, AI დიაგნოსტიკაში, ციფრული პათოლოგია).
მხოლოდ სანდო წყაროებზე დაყრდნობით (სამედიცინო ჟურნალები, ინდუსტრიული რეპორტები).
გამომიტანე ტოპ 3 ტრენდი და თითოეულზე დაურთე მოკლე ახსნა, თუ რატომ არის ის ეფექტური.
პასუხი დაწერე ქართულად.</div>
    </div>
</section>

<section id="ex5" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-demo">📚 სავარჯიშო 5</span>
            <h2 class="text-2xl font-bold">NotebookLM — ვრცელი დოკუმენტების ანალიზი</h2>
        </div>
        <span class="font-black text-xl text-gray-400">25 ქულა (პრაქტიკული სიმულაცია)</span>
    </div>
    
    <p class="text-gray-600 mb-4">თქვენ ატვირთეთ Google-ის NotebookLM-ში Megalab-ის ბოლო 3 წლის ფინანსური და ოპერაციული ანგარიში (PDF).</p>

    <div class="card" style="background:#fff3e0; border-left: 4px solid #FF5722;">
        <p class="font-bold text-orange-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800 mb-2">ეს დოკუმენტი 120 გვერდიანია. თქვენ ბორდის სხდომა გაქვთ 5 წუთში. რა კითხვას (Prompt) დაუსვამთ NotebookLM-ს, რომ სწრაფად ამოიღოთ <strong>მხოლოდ</strong> რისკები და ფინანსური ჩავარდნები?</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="კითხვა NotebookLM-ს..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans5').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans5" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">წყაროებზე დაყრდნობით, გამომიტანე მხოლოდ ის სექციები, სადაც ნახსენებია ფინანსური დანაკარგები, ოპერაციული შეფერხებები ან JCI აუდიტის რისკები. 
ჩამოწერე ბულეტებად და მიუთითე რომელ გვერდებზეა ეს ინფორმაცია. მაქსიმალურად ლაკონურად.</div>
    </div>
</section>

<section id="ex6" class="py-12 border-b border-gray-200 topic-card">
    <div class="flex justify-between items-start mb-4">
        <div>
            <span class="badge badge-quiz">📊 სავარჯიშო 6</span>
            <h2 class="text-2xl font-bold">მონაცემთა ექსტრაქცია და ფორმატირება</h2>
        </div>
        <span class="font-black text-xl text-gray-400">15 ქულა</span>
    </div>
    
    <p class="text-gray-600 mb-4">AI იდეალურია არასტრუქტურირებული ტექსტიდან მკაფიო ცხრილების მისაღებად.</p>

    <div class="card mb-4">
        <p class="font-bold text-sm mb-2 text-gray-500">ნედლი ტექსტი:</p>
        <p class="text-sm italic text-gray-600 border-l-4 border-gray-300 pl-3">"ორშაბათს გვქონდა 150 PCR ტესტი (შემოსავალი 15000 ლარი). სამშაბათს იყო 120 ტესტი (12000 ლარი) მაგრამ რეაქტივების პრობლემა იყო 2 ფილიალში. ოთხშაბათს რეკორდი - 200 ტესტი (20000 ლარი). ხუთშაბათს მხოლოდ 80 ტესტი."</p>
    </div>

    <div class="card" style="background:#fce4ec; border-left: 4px solid #E91E63;">
        <p class="font-bold text-pink-800 mb-2">🎯 დავალება:</p>
        <p class="text-sm text-gray-800">დაწერეთ პრომპტი, რომელიც ამ არეულ ტექსტს Excel-ისთვის გამოსადეგ <strong>ცხრილად</strong> (Table) აქცევს.</p>
    </div>

    <textarea class="ex-input mb-4" placeholder="პრომპტი ექსტრაქციისთვის..."></textarea>
    
    <button class="bg-[#2196F3] hover:bg-[#1976D2] text-white font-bold py-2 px-6 rounded-lg text-sm transition-colors" onclick="document.getElementById('ans6').style.display='block'">მაჩვენე პასუხი</button>

    <div id="ans6" class="answer-box">
        <p class="font-bold text-purple-800 mb-2">💡 იდეალური პასუხი:</p>
        <div class="code-block" style="font-size:0.85rem;">მოცემული ტექსტიდან ამოიღე მონაცემები და წარმოადგინე მკაფიო ცხრილის სახით.
ცხრილს უნდა ჰქონდეს შემდეგი სვეტები: "დღე", "ტესტების რაოდენობა", "შემოსავალი (ლარი)", "შენიშვნა/პრობლემა".
თუ რომელიმე დღეზე შენიშვნა არ წერია, დატოვე ცარიელი. ფორმატირება გააკეთე ისე, რომ პირდაპირ დავაკოპირო Excel-ში.</div>
    </div>
</section>

<!-- END -->
<div class="mt-12 p-6 rounded-xl text-center" style="background:linear-gradient(135deg,#0f1f2e,#1a3a5c);">
    <p class="text-4xl mb-4">🏆</p>
    <p class="text-white font-bold text-2xl mb-2">გილოცავთ! თქვენ დაასრულეთ მე-2 დღის სავარჯიშოები.</p>
    <p class="text-gray-300 text-sm mb-6">თუ დააგროვეთ 75 ქულაზე მეტი, თქვენ მზად ხართ სტრატეგიული AI ინსტრუმენტების გამოსაყენებლად.</p>
    <a href="day-2-slides.html" class="inline-block bg-[#E91E63] hover:bg-[#C2185B] text-white font-bold py-3 px-8 rounded-lg transition-colors">← დაბრუნდი სლაიდებზე</a>
</div>
    
    </div>
</main>
'''
    html = html[:content_start] + new_content + html[content_end:]
    
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-exercises.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Day 2 Exercises successfully built.")

if __name__ == '__main__':
    build_day2_exercises()
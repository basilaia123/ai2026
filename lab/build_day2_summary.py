import re

def build_day2_summary():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-summary.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Nav updates
    nav_old = '''        <a href="#slide-1"  class="nav-link">🤖 სლაიდი 1 · AI — რა და რატომ</a>
        <a href="#slide-2"  class="nav-link">⚙️ სლაიდი 2 · LLM-ის მუშაობა</a>
        <a href="#slide-3"  class="nav-link">🔍 სლაიდი 3 · AI მოდელები 2026</a>
        <a href="#slide-4"  class="nav-link">🔒 სლაიდი 4 · უსაფრთხოება & JCI</a>
        <a href="#slide-5"  class="nav-link">📝 სლაიდი 5 · R.O.L.E. ფრეიმვორქი</a>
        <a href="#slide-6"  class="nav-link">🏗️ სლაიდი 6 · C.R.E.A.T.E. სრული</a>
        <a href="#slide-7"  class="nav-link">💼 სლაიდი 7 · პრომპტები სამსახურში</a>
        <a href="#slide-8"  class="nav-link">📱 სლაიდი 8 · სოც. მედია & Iterative</a>
        <a href="#slide-9"  class="nav-link">🎨 სლაიდი 9 · Gamma.app</a>
        <a href="#slide-10" class="nav-link">🏆 სლაიდი 10 · გზამკვლევი & შემდეგი</a>
        <div class="mt-6 mx-4 mb-4 space-y-2">
            <a href="day-1-slides.html"    class="block text-center bg-white/5 hover:bg-white/10 text-gray-300 text-sm py-2 rounded">← სლაიდები</a>
            <a href="day-1-exercises.html" class="block text-center bg-white/5 hover:bg-white/10 text-gray-300 text-sm py-2 rounded">✏️ სავარჯიშოები</a>'''

    nav_new = '''        <a href="#slide-1"  class="nav-link">🧠 სლაიდი 1 · Thinking Partner</a>
        <a href="#slide-2"  class="nav-link">🎯 სლაიდი 2 · Few-Shot Prompting</a>
        <a href="#slide-3"  class="nav-link">💡 სლაიდი 3 · Reverse Brainstorming</a>
        <a href="#slide-4"  class="nav-link">📋 სლაიდი 4 · Notion AI (SOP)</a>
        <a href="#slide-5"  class="nav-link">🔍 სლაიდი 5 · Perplexity.ai</a>
        <a href="#slide-6"  class="nav-link">📚 სლაიდი 6 · NotebookLM</a>
        <a href="#slide-7"  class="nav-link">📊 სლაიდი 7 · Excel-ის ანალიზი</a>
        <a href="#slide-8"  class="nav-link">🖼️ სლაიდი 8 · ვიზუალები და იდეები</a>
        <div class="mt-6 mx-4 mb-4 space-y-2">
            <a href="day-2-slides.html"    class="block text-center bg-white/5 hover:bg-white/10 text-gray-300 text-sm py-2 rounded">← სლაიდები</a>
            <a href="day-2-exercises.html" class="block text-center bg-white/5 hover:bg-white/10 text-gray-300 text-sm py-2 rounded">✏️ სავარჯიშოები</a>'''

    html = html.replace(nav_old, nav_new)
    
    # Headers
    html = html.replace('დღე 1: შეჯამება', 'დღე 2: შეჯამება')
    html = html.replace('დღე 1: AI საფუძვლები', 'დღე 2: ოპერაციები და ანალიზი')
    html = html.replace('AI საფუძვლები, პრომპტინგი & ვიზუალები', 'სტრატეგიული ოპერაციები, ანალიზი და ვიზუალები')
    html = html.replace('10 სლაიდი', '8 სლაიდი')
    html = html.replace('10 სლაიდი · ძირითადი ცოდნა', '8 სლაიდი · ძირითადი ცოდნა')
    html = html.replace('Megalab-ის AI ტრენინგი — დღე 1 დასრულდა!', 'Megalab-ის AI ტრენინგი — დღე 2 დასრულდა!')

    # Content replacement
    content_start = html.find('<!-- ═══════════════════════════════════════════════════\n     SLIDE 1')
    content_end = html.find('<!-- END -->')
    
    if content_end == -1: # Fallback if standard end comment is missing
         content_end = html.find('<div class="mt-12 p-6 rounded-xl text-center"')
    
    new_content = '''<!-- ═══════════════════════════════════════════════════
     SLIDE 1: Thinking Partner
═══════════════════════════════════════════════════ -->
<section id="slide-1" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-blue"><span class="slide-number">1</span> კრეატივი</span>
    <h2 class="text-3xl font-bold mb-6">🧠 AI — Thinking Partner (აზროვნების პარტნიორი)</h2>

    <div class="card mb-5">
        <p class="text-gray-700">მენეჯერებისთვის AI-ის ყველაზე დიდი ღირებულება არის არა უბრალოდ ტექსტის დაწერა, არამედ <strong>იდეების გენერაცია, სტრატეგიის დაგეგმვა და ალტერნატიული პერსპექტივების დანახვა</strong>.</p>
    </div>

    <div class="two-column">
        <div class="card" style="border-left: 4px solid #4CAF50;">
            <p class="font-bold mb-3" style="color:#2E7D32;">როგორ გამოვიყენოთ:</p>
            <ul class="checklist">
                <li>ბრეინშტორმინგი ახალ იდეებზე</li>
                <li>პრობლემის ალტერნატიული კუთხით დანახვა</li>
                <li>გადაწყვეტილების მიღებისას რისკების ანალიზი</li>
                <li>სტრატეგიული გეგმის პირველადი მონახაზი (Draft)</li>
            </ul>
        </div>
        <div class="warning-box" style="margin:0;">
            <p class="font-bold mb-2">🔒 უსაფრთხოების წესი:</p>
            <p class="text-sm">Public (ღია) მოდელებში: <strong>Public/General კონტენტი.</strong><br>
            Enterprise (დაცულ) მოდელებში: <strong>Internal/Confidential კონტენტი.</strong><br>
            არასოდეს ატვირთოთ <strong>Restricted (სენსიტიური პერსონალური)</strong> მონაცემები!</p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 2: Few-Shot Prompting
═══════════════════════════════════════════════════ -->
<section id="slide-2" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-purple"><span class="slide-number">2</span> პრომპტინგი</span>
    <h2 class="text-3xl font-bold mb-6">🎯 Few-Shot Prompting — მაგალითებით სწავლება</h2>

    <p class="text-gray-600 mb-4">ნაცვლად იმისა, რომ AI-ს მხოლოდ მშრალი ინსტრუქცია მივცეთ (Zero-shot), ჩვენ ვაწვდით <strong>სასურველი შედეგის რამდენიმე მაგალითს</strong>. ეს უზრუნველყოფს ტონის და ფორმატის 100%-იან სიზუსტეს.</p>

    <div class="highlight-box">
        <p class="font-bold mb-2" style="color:#1565C0;">💡 პრომპტის სტრუქტურა:</p>
        <div class="code-block">[კონტექსტი] + [ინსტრუქცია] +
[მაგალითი 1 (Input/Output)] +
[მაგალითი 2 (Input/Output)] +
[ახალი დავალება]</div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 3: Reverse Brainstorming
═══════════════════════════════════════════════════ -->
<section id="slide-3" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-pink"><span class="slide-number">3</span> კრეატივი</span>
    <h2 class="text-3xl font-bold mb-6">🔄 Reverse Brainstorming (შებრუნებული აზროვნება)</h2>

    <div class="card mb-5" style="border-left: 4px solid #E91E63;">
        <p class="text-gray-700">ეფექტური ტექნიკა რისკების აღმოსაჩენად. ვთხოვთ AI-ს მოიფიქროს გზები, თუ <strong>როგორ გავაფუჭოთ საქმე</strong>, რათა დავინახოთ ის პრობლემები, რაზეც არ გვიფიქრია.</p>
    </div>

    <div class="highlight-box" style="background:#fce4ec; border-left-color:#C2185B;">
        <p class="font-bold mb-2" style="color:#880E4F;">💡 მაგალითი პრომპტი:</p>
        <div class="code-block">მოიფიქრე 5 ყველაზე ცუდი გზა, რითაც პაციენტის გამოცდილება მისაღებში გავაუარესოთ და გავაბრაზოთ. შემდეგ, თითოეული ამ ცუდი პრაქტიკის გასწვრივ დაწერე მისი საპირისპირო, საუკეთესო მოქმედების წესი.</div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 4: Notion AI
═══════════════════════════════════════════════════ -->
<section id="slide-4" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-teal"><span class="slide-number">4</span> SOP-ები</span>
    <h2 class="text-3xl font-bold mb-6">📋 Notion AI — SOP-ებისა და შაბლონების შექმნა</h2>

    <p class="text-gray-600 mb-4">Notion არის კომპანიის <strong>"ცოცხალი ტვინი"</strong>, სადაც ინახება ყველა სტანდარტული ოპერაციული პროცედურა (SOP) და დოკუმენტაცია. Notion AI პირდაპირ ტექსტურ რედაქტორში წერს, აფორმატებს და თარგმნის დოკუმენტებს.</p>

    <div class="two-column mb-4">
        <div class="card">
            <p class="font-bold mb-2 text-teal-700">🚀 მთავარი ბრძანებები:</p>
            <ul class="text-sm space-y-1">
                <li>• <strong>Space:</strong> AI-ის გამოძახება ცარიელ ხაზზე</li>
                <li>• <strong>Highlight + Ask AI:</strong> ტექსტის გაუმჯობესება/თარგმნა</li>
                <li>• <strong>/ai:</strong> AI ბლოკების ჩასმა (Summary, Action items)</li>
            </ul>
        </div>
        <div class="card">
            <p class="font-bold mb-2 text-teal-700">📑 რისთვის გამოვიყენოთ:</p>
            <ul class="checklist">
                <li>JCI სტანდარტების დოკუმენტირება</li>
                <li>HR ონბორდინგის სახელმძღვანელოები</li>
                <li>დეპარტამენტული სტრატეგიის მონახაზი</li>
            </ul>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 5: Perplexity.ai
═══════════════════════════════════════════════════ -->
<section id="slide-5" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-blue"><span class="slide-number">5</span> კვლევა</span>
    <h2 class="text-3xl font-bold mb-6">🔍 Perplexity.ai — კვლევა რეალურ დროში</h2>

    <div class="card mb-5" style="border-left: 4px solid #1E88E5;">
        <p class="text-gray-700">Perplexity არის AI-ზე დაფუძნებული საძიებო სისტემა. ChatGPT-ისგან განსხვავებით, ის პირდაპირ ეძებს ინფორმაციას ინტერნეტში და <strong>აუცილებლად ურთავს სანდო წყაროს ბმულებს (Citations)</strong> ყოველ წინადადებას.</p>
    </div>

    <div class="highlight-box">
        <p class="font-bold mb-2" style="color:#1565C0;">💡 გამოყენების მაგალითი:</p>
        <p class="text-sm text-gray-700 mb-2"><em>"მოიძიე 2026 წლის უახლესი ტრენდები ევროპის სამედიცინო ლაბორატორიებში ავტომატიზაციის კუთხით. დაეყრდენი მხოლოდ სამედიცინო და ინდუსტრიულ რეპორტებს."</em></p>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 6: NotebookLM
═══════════════════════════════════════════════════ -->
<section id="slide-6" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-orange"><span class="slide-number">6</span> დოკუმენტები</span>
    <h2 class="text-3xl font-bold mb-6">📚 NotebookLM — ვრცელი დოკუმენტების AI კონსულტანტი</h2>

    <p class="text-gray-600 mb-4">Google-ის NotebookLM საშუალებას გაძლევთ ატვირთოთ <strong>უზარმაზარი დოკუმენტები</strong> (PDF, ვებსაიტები, Drive ფაილები) და მხოლოდ ამ დოკუმენტებზე დაყრდნობით დასვათ კითხვები. ის არასოდეს ჰალუცინირებს და ყოველთვის უთითებს კონკრეტულ გვერდს, საიდანაც მოიტანა პასუხი.</p>

    <div class="two-column">
        <div class="card">
            <p class="font-bold mb-2 text-orange-800">✅ იდეალურია:</p>
            <ul class="checklist">
                <li>JCI-ის 500-გვერდიანი სახელმძღვანელოს გასარჩევად</li>
                <li>ფინანსური რეპორტების ანალიზისთვის</li>
                <li>რთული იურიდიული კონტრაქტების შესამოწმებლად</li>
            </ul>
        </div>
        <div class="warning-box" style="margin:0;">
            <p class="font-bold mb-2 text-pink-800">⚠️ ყურადღება:</p>
            <p class="text-sm text-gray-700">NotebookLM არის დახურული სისტემა (არ იყენებს თქვენს ფაილებს ტრენინგისთვის), თუმცა მაინც დაიცავით კორპორატიული პოლიტიკა სენსიტიურ (Restricted) პაციენტთა მონაცემებზე.</p>
        </div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 7: Excel Data Analysis
═══════════════════════════════════════════════════ -->
<section id="slide-7" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-green"><span class="slide-number">7</span> ანალიტიკა</span>
    <h2 class="text-3xl font-bold mb-6">📊 Claude / Excel — მონაცემთა ექსტრაქცია</h2>

    <div class="card mb-5" style="border-left: 4px solid #4CAF50;">
        <p class="text-gray-700">AI იდეალურია <strong>არასტრუქტურირებული ტექსტის</strong> (მაგ. მიმოწერის, შენიშვნების) მკაფიო <strong>Excel-ის ცხრილად</strong> (Table) გადასაქცევად.</p>
    </div>

    <div class="highlight-box" style="background:#e8f5e9; border-left-color:#2E7D32;">
        <p class="font-bold mb-2" style="color:#1B5E20;">💡 პრომპტის მაგალითი ექსტრაქციისთვის:</p>
        <div class="code-block">მოცემული არეული ტექსტიდან ამოიღე მონაცემები და წარმოადგინე მკაფიო ცხრილის სახით. სვეტები: "დღე", "ტესტების რაოდენობა", "შემოსავალი". ფორმატირება გააკეთე ისე, რომ პირდაპირ დავაკოპირო Excel-ში.</div>
    </div>
</section>

<!-- ═══════════════════════════════════════════════════
     SLIDE 8: Visuals & Brainstorming (Day 1 Leftovers)
═══════════════════════════════════════════════════ -->
<section id="slide-8" class="min-h-[80vh] flex flex-col justify-center py-14 border-b border-gray-200 slide">
    <span class="badge badge-purple"><span class="slide-number">8</span> ვიზუალები</span>
    <h2 class="text-3xl font-bold mb-6">🖼️ AI ვიზუალები და იდეები (Brainstorming)</h2>

    <div class="card mb-4">
        <p class="font-bold mb-2">🔑 გამოსახულების პრომპტის 4 ელემენტი:</p>
        <div class="grid grid-cols-2 gap-2 text-sm text-gray-700">
            <div class="p-2 bg-gray-50 rounded"><strong>1. სუბიექტი:</strong> ვინ/რა არის</div>
            <div class="p-2 bg-gray-50 rounded"><strong>2. სტილი:</strong> ფოტო/ილუსტრაცია</div>
            <div class="p-2 bg-gray-50 rounded"><strong>3. განათება/ფერები:</strong> ლურჯი, ნათელი</div>
            <div class="p-2 bg-gray-50 rounded"><strong>4. კომპოზიცია:</strong> close-up, wide shot</div>
        </div>
    </div>
    
    <div class="highlight-box" style="background:#fce4ec; border-left-color:#E91E63;">
        <p class="font-bold mb-2" style="color:#C2185B;">💡 ვიზუალის პრომპტის მაგალითი (DALL-E 3):</p>
        <p class="text-sm font-mono text-pink-800">"თანამედროვე სამედიცინო ლაბორატორია საქართველოში, სუფთა და პროფესიონალური, ლურჯი და თეთრი ფერები, ლაბორანტი თეთრ ხალათში მუშაობს თანამედროვე აპარატურასთან, ნათელი განათება, კორპორატიული სტილი, ტექსტის გარეშე"</p>
    </div>
</section>
'''
    html = html[:content_start] + new_content + html[content_end:]
    
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-summary.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Day 2 Summary successfully built.")

if __name__ == '__main__':
    build_day2_summary()
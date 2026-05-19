import re

def add_pricing_slide():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Insert in Navigation Menu
    nav_old = '<a href="#models" class="nav-link">🔍 AI მოდელების მიმოხილვა</a>'
    nav_new = '<a href="#models" class="nav-link">🔍 AI მოდელების მიმოხილვა</a>\n        <a href="#pricing" class="nav-link">💳 ფასიანი მოდელები და ტარიფები</a>'
    
    if nav_old in content and 'ფასიანი მოდელები და ტარიფები' not in content:
        content = content.replace(nav_old, nav_new)

    # 2. Create the Pricing Section
    pricing_section = '''<!-- PRICING SLIDE -->
<section id="pricing" class="min-h-[70vh] flex flex-col justify-center py-12 border-b border-gray-200 topic-card">
    <span class="badge badge-theory">💳 გამოწერა · 5 წუთი</span>
    <h2 class="text-3xl font-bold mb-6">💳 პოპულარული ფასიანი მოდელები</h2>
    <p class="text-gray-500 mb-6">ღირს თუ არა გადახდა? (სტანდარტული ფასი: $20 / თვეში)</p>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
        <!-- ChatGPT Plus -->
        <div class="card flex flex-col h-full" style="border-top: 4px solid #10a37f;">
            <div class="flex items-center gap-3 mb-3">
                <span class="text-3xl">🤖</span>
                <p class="font-bold text-lg" style="color:#0d8265;">ChatGPT Plus</p>
            </div>
            <p class="text-2xl font-black mb-3">$20<span class="text-sm font-normal text-gray-500">/თვე</span></p>
            <ul class="text-sm text-gray-700 space-y-2 flex-1">
                <li>✅ <strong>მოდელები:</strong> GPT-4o, o1, o3-mini</li>
                <li>✅ <strong>Advanced Data Analysis</strong> (ექსელის ფაილები)</li>
                <li>✅ <strong>DALL·E 3</strong> (სურათების გენერაცია)</li>
                <li>✅ <strong>Custom GPTs</strong> (პირადი ასისტენტების შექმნა)</li>
                <li>✅ საუკეთესო <strong>ხმოვანი რეჟიმი (Voice Mode)</strong></li>
            </ul>
        </div>
        
        <!-- Claude Pro -->
        <div class="card flex flex-col h-full" style="border-top: 4px solid #d97757;">
            <div class="flex items-center gap-3 mb-3">
                <span class="text-3xl">🧠</span>
                <p class="font-bold text-lg" style="color:#b2583d;">Claude Pro</p>
            </div>
            <p class="text-2xl font-black mb-3">$20<span class="text-sm font-normal text-gray-500">/თვე</span></p>
            <ul class="text-sm text-gray-700 space-y-2 flex-1">
                <li>✅ <strong>მოდელები:</strong> Claude 3.5 Sonnet / Opus</li>
                <li>✅ <strong>ყველაზე ჭკვიანი</strong> და ლოგიკური წერაში</li>
                <li>✅ <strong>Projects / Artifacts:</strong> დოკუმენტების და კოდის იდეალური მართვა</li>
                <li>✅ <strong>ქართული ენის</strong> საუკეთესო ცოდნა და ბუნებრივი ტონი</li>
                <li>❌ არ აქვს სურათების გენერაცია და ინტერნეტში ძიება</li>
            </ul>
        </div>

        <!-- Google One AI Premium -->
        <div class="card flex flex-col h-full" style="border-top: 4px solid #4285F4;">
            <div class="flex items-center gap-3 mb-3">
                <span class="text-3xl">✨</span>
                <p class="font-bold text-lg" style="color:#1565C0;">Google Gemini Adv.</p>
            </div>
            <p class="text-2xl font-black mb-3">$20<span class="text-sm font-normal text-gray-500">/თვე</span></p>
            <ul class="text-sm text-gray-700 space-y-2 flex-1">
                <li>✅ <strong>მოდელები:</strong> Gemini 1.5 Pro</li>
                <li>✅ <strong>ინტეგრაცია:</strong> Google Workspace (Docs, Gmail, Drive)</li>
                <li>✅ <strong>უზარმაზარი კონტექსტი:</strong> 2 მილიონი ტოკენი (შეუძლია მთელი წიგნის წაკითხვა ერთდროულად)</li>
                <li>✅ მოიცავს 2TB Google Drive მეხსიერებას (Google One AI Premium)</li>
            </ul>
        </div>
    </div>

    <div class="highlight-box" style="background:#e8f5e9; border-left-color:#4CAF50;">
        <p class="font-bold mb-1" style="color:#2E7D32;">💡 ტრენერის რჩევა Megalab-ისთვის:</p>
        <p class="text-sm text-gray-700">კორპორატიული ამოცანებისთვის, ტექსტების დასაწერად და თარგმნისთვის (PR, ოფიციალური მეილები) <strong>Claude Pro</strong> ქართულ ენაზე შეუდარებელია. თუმცა, თუ გჭირდებათ ექსელის ფაილების, პაციენტთა მონაცემების ანალიზი და მობილურიდან ხმით საუბარი, <strong>ChatGPT Plus</strong> უფრო უნივერსალურია.</p>
    </div>
</section>

'''

    # Insert before the lmarena section
    if '<section id="lmarena"' in content and 'PRICING SLIDE' not in content:
        content = content.replace('<section id="lmarena"', pricing_section + '<section id="lmarena"')

    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Pricing slide added.")

if __name__ == '__main__':
    add_pricing_slide()
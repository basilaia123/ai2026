import re

def update_gamma_outline():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Gamma card to mention Outline strategy
    old_gamma_card = '''<div class="card" style="border:2px solid #7C3AED;">
<p class="font-bold mb-3" style="color:#7C3AED;">✅ Gamma.app:</p>
<ul class="text-sm text-gray-600 space-y-1">
<li>• <strong>5-10 წუთი</strong> — სრული პრეზენტაცია</li>
<li>• AI ავტომატურად ადგენს სტრუქტურას</li>
<li>• AI ირჩევს სურათებს და დიზაინს</li>
<li>• ადვილი რედაქტირება</li>
</ul>
</div>'''

    new_gamma_card = '''<div class="card" style="border:2px solid #7C3AED;">
<p class="font-bold mb-3" style="color:#7C3AED;">✅ Gamma.app (ოქროს წესი):</p>
<ul class="text-sm text-gray-600 space-y-1">
<li>• <strong>5-10 წუთი</strong> — სრული პრეზენტაცია</li>
<li>• <strong>ნუ მიანდობთ სტრუქტურას (Outline) Gamma-ს!</strong></li>
<li>• <strong>ჯერ</strong> შექმენით დეტალური Outline Claude/ChatGPT-ში</li>
<li>• <strong>მერე</strong> ჩააკოპირეთ ის Gamma-ში (Text to Presentation)</li>
</ul>
</div>'''

    if old_gamma_card in content:
        content = content.replace(old_gamma_card, new_gamma_card)

    # 2. Update the Demo section to reflect this 2-step process
    old_demo_steps = '''<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#2196F3;">1</span>        
<div><p class="font-bold text-sm text-white">gamma.app → "New with AI"</p><p class="text-gray-400 text-xs">ან "Generate" ღილაკი</p></div>       
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#E91E63;">2</span>        
<div><p class="font-bold text-sm text-white">Outline-ის შეყვანა</p><p class="text-gray-400 text-xs font-mono text-xs">„Megalab-ის PCR ტესტირების სერვისი: სიჩქარე, სიზუსტე, JCI აკრედიტაცია. 6 სლაიდი."</p></div>
</div>'''

    new_demo_steps = '''<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#FF9800;">1</span>        
<div><p class="font-bold text-sm text-white">ნაბიჯი 1: ChatGPT / Claude</p><p class="text-gray-400 text-xs font-mono">"დამიწერე 6-სლაიდიანი პრეზენტაციის სტრუქტურა (Outline) Megalab-ის PCR სერვისებზე B2B პარტნიორებისთვის." → ვაკოპირებთ პასუხს.</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#2196F3;">2</span>        
<div><p class="font-bold text-sm text-white">ნაბიჯი 2: Gamma.app → "Paste in Text"</p><p class="text-gray-400 text-xs">ვირჩევთ "Paste in Text" (და არა Generate) და ვაგდებთ დაკოპირებულ Outline-ს.</p></div>       
</div>'''

    # Need to handle the fact that my regex matched multi-line nicely, but let's just do a direct replacement of step 1 and 2
    
    # Actually, let's just replace the whole divide-y block for safety.
    demo_old = '''<div class="divide-y divide-white/10">
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#2196F3;">1</span>        
<div><p class="font-bold text-sm text-white">gamma.app → "New with AI"</p><p class="text-gray-400 text-xs">ან "Generate" ღილაკი</p></div>       
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#E91E63;">2</span>        
<div><p class="font-bold text-sm text-white">Outline-ის შეყვანა</p><p class="text-gray-400 text-xs font-mono text-xs">„Megalab-ის PCR ტესტირების სერვისი: სიჩქარე, სიზუსტე, JCI აკრედიტაცია. 6 სლაიდი."</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#9C27B0;">3</span>        
<div><p class="font-bold text-sm text-white">თემის და ფერის არჩევა</p><p class="text-gray-400 text-xs">Professional / Healthcare სტილი</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#4CAF50;">4</span>        
<div><p class="font-bold text-sm text-white">Generate — პრეზენტაცია მზადაა!</p><p class="text-gray-400 text-xs">30-60 წამი</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#FF9800;">5</span>        
<div><p class="font-bold text-sm text-white">AI Agent ტრიუკი: Ctrl+E</p><p class="text-gray-400 text-xs">სლაიდზე ახალი ინსტრუქციის მიწოდება — ტექსტის ან სურათის ჩანაცვლება</p></div>
</div>
</div>'''

    demo_old = demo_old.replace('„', '"').replace('“', '"')
    demo_old2 = demo_old.replace('"Megalab-ის', '„Megalab-ის').replace('სლაიდი."', 'სლაიდი."')

    demo_new = '''<div class="divide-y divide-white/10">
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#FF9800;">1</span>        
<div><p class="font-bold text-sm text-white">შექმენი სტრუქტურა Claude-ში / ChatGPT-ში</p><p class="text-gray-400 text-xs font-mono">"დამიწერე 6-სლაიდიანი პრეზენტაციის სტრუქტურა (Outline) Megalab-ის PCR სერვისებზე B2B პარტნიორებისთვის." → დააკოპირეთ შედეგი.</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#2196F3;">2</span>        
<div><p class="font-bold text-sm text-white">gamma.app → "Paste in Text"</p><p class="text-gray-400 text-xs">აირჩიეთ "Paste in Text" (და არა Generate) და ჩასვით დაკოპირებული Outline.</p></div>       
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#9C27B0;">3</span>        
<div><p class="font-bold text-sm text-white">თემის და ფერის არჩევა</p><p class="text-gray-400 text-xs">აირჩიეთ Professional / Healthcare სტილი და ფერები.</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#4CAF50;">4</span>        
<div><p class="font-bold text-sm text-white">Generate — პრეზენტაცია მზადაა!</p><p class="text-gray-400 text-xs">AI თქვენს სტრუქტურას შეუსაბამებს დიზაინს და სურათებს (30 წამში).</p></div>
</div>
<div class="flex gap-4 p-4">
<span class="w-8 h-8 rounded-full flex items-center justify-center text-sm font-bold flex-shrink-0" style="background:#E91E63;">5</span>        
<div><p class="font-bold text-sm text-white">AI Agent ტრიუკი: Ctrl+E</p><p class="text-gray-400 text-xs">სლაიდზე დააჭირეთ Ctrl+E — სთხოვეთ AI-ს ტექსტის შემოკლება, სურათის შეცვლა ან სვეტის დამატება.</p></div>
</div>
</div>'''

    import re
    # Using regex to replace the divide-y block because of formatting/indentation variations
    pattern = re.compile(r'<div class="divide-y divide-white/10">.*?</div>\n</div>\n</section>', re.DOTALL)
    
    if pattern.search(content):
        content = pattern.sub(f'{demo_new}\n</div>\n</section>', content)
        
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Outline instructions added to Gamma section.')

if __name__ == '__main__':
    update_gamma_outline()
import re

def re_inject_tips():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. AI Math limitations & Human-in-the-Loop
    bias_card_end = '''AI — პირველი დრაფტი, ადამიანი — საბოლოო შემოწმება</span></p>
        </div>
    </div>'''
    
    math_card = '''AI — პირველი დრაფტი, ადამიანი — საბოლოო შემოწმება</span></p>
        </div>
    </div>
    
    <!-- Added Math Limitation -->
    <div class="card mb-6" style="border-left:4px solid #F44336; background:#fff3e0;">
        <p class="font-bold text-lg mb-2" style="color:#D84315;">🧮 მათემატიკა და ლოგიკა — სუსტი წერტილი</p>
        <p class="text-gray-700 text-sm mb-2">LLM ენობრივი მოდელია და არა კალკულატორი. ის <strong>ვერ ითვლის</strong>, არამედ "გამოიცნობს" შემდეგ ციფრს. ფინანსურ რეპორტებთან ან ტარიფებთან მუშაობისას, <strong>არასოდეს ენდოთ მის გამოთვლებს (ბიუჯეტი, ფასდაკლება, ჯამი)</strong> სპეციალური ხელსაწყოების (Advanced Data Analysis) ჩართვისა და ფიზიკურად გადამოწმების გარეშე!</p>
        <p class="font-bold text-sm" style="color:#C62828;">✅ ოქროს წესი: Human-in-the-Loop (ადამიანი მარყუჟში) — ყოველთვის გადაამოწმეთ ციფრები!</p>
    </div>'''
    
    if bias_card_end in content and 'მათემატიკა და ლოგიკა' not in content:
        content = content.replace(bias_card_end, math_card)

    # 2. Vision (Reading Labels)
    llm_warning = '''<div class="warning-box">
        <p class="font-bold mb-1">⚠️ მნიშვნელოვანი: AI არ ფიქრობს</p>
        <p class="text-gray-700">AI <strong>არ ,,ფიქრობს“</strong> და <strong>არ ,,იცის“</strong> — ის სტატისტიკურად ყველაზე სავარაუდო სიტყვის კომბინაციებს ირჩევს. ამიტომ შეიძლება ზოგჯერ <strong>ჰალუცინაციები</strong> (მცდარი ფაქტები) შექმნას.</p>
    </div>'''
    
    vision_card = '''<div class="warning-box">
        <p class="font-bold mb-1">⚠️ მნიშვნელოვანი: AI არ ფიქრობს</p>
        <p class="text-gray-700">AI <strong>არ ,,ფიქრობს“</strong> და <strong>არ ,,იცის“</strong> — ის სტატისტიკურად ყველაზე სავარაუდო სიტყვის კომბინაციებს ირჩევს. ამიტომ შეიძლება ზოგჯერ <strong>ჰალუცინაციები</strong> (მცდარი ფაქტები) შექმნას.</p>
    </div>

    <!-- Added Vision Card -->
    <div class="card mt-6" style="background:#e8eaf6; border-left:4px solid #3F51B5;">
        <p class="font-bold text-lg mb-2" style="color:#283593;">👁️ Vision: AI აღარ არის მხოლოდ ტექსტი</p>
        <p class="text-gray-700 text-sm mb-2">თანამედროვე მოდელებს (GPT-4o, Claude 3.5) შეუძლიათ <strong>სურათების დანახვა და გაანალიზება.</strong></p>
        <ul class="text-sm text-gray-700 space-y-1 list-disc list-inside ml-4">
            <li>ექიმის გაურკვეველი ხელნაწერის ან რეცეპტის გაშიფვრა ფოტოდან.</li>
            <li>ახალი ლაბორატორიული რეაქტივის (მაგ. ინგლისურ/გერმანულენოვანი) ეტიკეტის ფოტოს ატვირთვა და მისი სპეციფიკაციის ქართულად თარგმნა.</li>
            <li>გრაფიკებისა და ცხრილების ანალიზი პირდაპირ სქრინშოტიდან.</li>
        </ul>
    </div>'''
    
    if llm_warning in content and 'Vision: AI აღარ არის' not in content:
        content = content.replace(llm_warning, vision_card)

    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Re-injected tips successfully.")

if __name__ == '__main__':
    re_inject_tips()
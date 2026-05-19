import re

def add_gamma_examples():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    examples_card = '''
    <!-- AI Agent Examples -->
    <div class="card mt-6" style="border: 2px dashed #E91E63; background:#fff5f8;">
        <p class="font-bold text-lg mb-4" style="color:#C2185B;">🤖 AI Agent (Ctrl+E) გამოყენების 3 მაგალითი სლაიდზე:</p>
        <div class="space-y-4 text-sm text-gray-800">
            <div class="flex items-start gap-3">
                <span class="text-xl">1️⃣</span>
                <div>
                    <strong style="color:#C2185B;">ფორმატირება (ტექსტის გამარტივება):</strong><br> 
                    მონიშნეთ ვრცელი ტექსტი, დააჭირეთ Ctrl+E და დაუწერეთ:<br>
                    <span class="inline-block mt-1 px-2 py-1 bg-white border border-pink-200 rounded text-pink-700 font-mono text-xs">"ეს აბზაცი გადააკეთე 3 მოკლე ბულეტ-პუნქტად."</span>
                </div>
            </div>
            <div class="flex items-start gap-3">
                <span class="text-xl">2️⃣</span>
                <div>
                    <strong style="color:#C2185B;">ვიზუალის შეცვლა კონტექსტურად:</strong><br> 
                    მონიშნეთ სურათი (ან მთელი სლაიდი), დააჭირეთ Ctrl+E და დაუწერეთ:<br>
                    <span class="inline-block mt-1 px-2 py-1 bg-white border border-pink-200 rounded text-pink-700 font-mono text-xs">"შეცვალე ეს სურათი თანამედროვე სამედიცინო ლაბორატორიის ფოტოთი."</span>
                </div>
            </div>
            <div class="flex items-start gap-3">
                <span class="text-xl">3️⃣</span>
                <div>
                    <strong style="color:#C2185B;">თარგმნა / ტონის კალიბრაცია:</strong><br> 
                    მონიშნეთ მთელი სლაიდი, დააჭირეთ Ctrl+E და დაუწერეთ:<br>
                    <span class="inline-block mt-1 px-2 py-1 bg-white border border-pink-200 rounded text-pink-700 font-mono text-xs">"თარგმნე ეს სლაიდი ინგლისურად და გახადე უფრო ფორმალური B2B პარტნიორებისთვის."</span>
                </div>
            </div>
        </div>
    </div>
</section>'''

    pattern2 = re.compile(r'(<div class="flex gap-4 p-4">\s*<span[^>]*>5</span>\s*<div><p[^>]*>AI Agent ტრიუკი: Ctrl\+E.*?</p></div>\s*</div>\s*</div>\s*</div>)\s*</section>', re.DOTALL)
    match = pattern2.search(content)
    if match:
        new_content = pattern2.sub(r'\1\n' + examples_card, content)
        with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully added AI Agent examples.")
    else:
        print("Failed to find injection point.")

if __name__ == '__main__':
    add_gamma_examples()
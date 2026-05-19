import re

def update_agenda_and_tasks():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Update sidebar and agenda block II
    content = content.replace('ბლოკი II — ვიზუალები (90 წთ)', 'ბლოკი II — ვიზუალები და იდეები (90 წთ)')
    content = content.replace('✏️ პრაქტიკა 2: Gamma', '✏️ პრაქტიკა 2: Gamma (20 წთ)')
    content = content.replace('🎨 მიკრო-დავალება: სურათი', '💡 მიკრო-დავალება: Brainstorming (10 წთ)\n        <a href="#image-practice" class="nav-link">🎨 მიკრო-დავალება: სურათი</a>')
    content = content.replace('ბლოკი II: ვიზუალები', 'ბლოკი II: ვიზუალები და იდეები')
    content = content.replace('30 წთ</strong> — პრაქტიკა 2: პრეზენტაცია', '20 წთ</strong> — პრაქტიკა 2: პრეზენტაცია')

    target_li = '<li class="flex gap-2"><span style="color:#E91E63;">•</span><span><strong class="text-white">20 წთ</strong> — AI სურათების გენერაცია</span></li>'
    replacement_li = '<li class="flex gap-2"><span style="color:#E91E63;">•</span><span><strong class="text-white">10 წთ</strong> — მიკრო-დავალება: Brainstorming</span></li>\n                <li class="flex gap-2"><span style="color:#E91E63;">•</span><span><strong class="text-white">20 წთ</strong> — AI სურათების გენერაცია</span></li>'
    
    if target_li in content and 'მიკრო-დავალება: Brainstorming' not in content:
        content = content.replace(target_li, replacement_li)

    # Update Practice 2 title and timer
    content = content.replace('✏️ პრაქტიკა 2 · 30 წუთი', '✏️ პრაქტიკა 2 · 20 წუთი')
    content = content.replace("startTimer('timer2-display',30)", "startTimer('timer2-display',20)")

    # Insert new Brainstorming section before image generation
    brainstorming_section = '''
<!-- BRAINSTORMING MICRO-TASK -->
<section id="brainstorm" class="min-h-[70vh] flex flex-col justify-center py-12 border-b border-gray-200 topic-card">
    <span class="badge badge-practice" style="background:rgba(103,58,183,0.1); color:#512DA8; border:1px solid rgba(103,58,183,0.3);">💡 მიკრო-დავალება · 10 წუთი</span>
    <h2 class="text-3xl font-bold mb-2">💡 იდეების გენერაცია (Brainstorming)</h2>
    <p class="text-gray-500 mb-6">Megalab-ის შიდა კამპანია ნულოვანი ბიუჯეტით</p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div class="card" style="border-top: 4px solid #673AB7; margin:0;">
            <h4 class="font-bold text-lg mb-3" style="color:#512DA8;">🎯 სცენარი</h4>
            <p class="text-sm text-gray-700 leading-relaxed">
                Megalab-ს სჭირდება შიდა კორპორატიული კამპანია <strong>ხელის ჰიგიენის წესების პოპულარიზაციისთვის</strong> თანამშრომლებში.<br><br>
                ბიუჯეტი არის 0 ლარი. გვჭირდება სახალისო და ეფექტური იდეები, რომლებსაც დღესვე განვახორციელებთ.
            </p>
        </div>
        <div class="card" style="background:#f3e5f5; border:none; margin:0;">
            <h4 class="font-bold text-lg mb-3" style="color:#4A148C;">⏱️ დავალება (10 წთ)</h4>
            <ul class="text-sm text-gray-800 space-y-2">
                <li>1. გამოიყენეთ <strong>C.R.E.A.T.E.</strong> მოდელი.</li>
                <li>2. სთხოვეთ AI-ს მოიფიქროს <strong>5 კრეატიული იდეა/აქტივობა</strong>.</li>
                <li>3. დაუწესეთ შეზღუდვა (Edge): იდეები უნდა იყოს განხორციელებადი 24 საათში და უფასოდ.</li>
                <li>4. საუკეთესო იდეას განვიხილავთ ეკრანზე!</li>
            </ul>
        </div>
    </div>

    <div class="highlight-box" style="background:#ede7f6; border-left-color:#673AB7; margin-top:1.5rem;">
        <p class="font-bold mb-2" style="color:#4A148C;">💡 დახმარება პრომპტისთვის:</p>
        <div class="prompt-blueprint" style="background: #0f1f2e; border: 1px solid rgba(103,58,183,0.4); border-radius: 8px; padding: 1.25rem 1.5rem; margin: 1rem 0; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 0.5rem;">
        <span style="color: #b39ddb; font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em;">Prompt Blueprint</span>
        <button class="copy-btn" style="position: static; font-size: 0.7rem; background: rgba(103,58,183,0.2); color: #d1c4e9; border: 1px solid rgba(103,58,183,0.4); padding: 0.2rem 0.5rem; border-radius: 4px; cursor: pointer; transition: all 0.2s;" onmouseover="this.style.background='#673AB7'; this.style.color='#fff';" onmouseout="this.style.background='rgba(103,58,183,0.2)'; this.style.color='#d1c4e9';" onclick="copyText(this)">კოპირება</button>
    </div>
    <div class="code-content" style="font-family: 'Courier New', monospace; font-size: 0.85rem; color: #e2e8f0; white-space: pre-wrap; line-height: 1.6;">[C] გვჭირდება შიდა კამპანია ხელის ჰიგიენაზე Megalab-ის თანამშრომლებისთვის (ბიუჯეტი 0).
[R] მოიფიქრე 5 სახალისო და სწრაფი იდეა.
[E] უნდა იყოს განხორციელებადი 24 საათში.
[A] იმოქმედე, როგორც კრეატიულმა HR მენეჯერმა.
[T] ტონი: ენერგიული და წამახალისებელი.
[E] თითო იდეა მაქსიმუმ 2 წინადადებით ახსენი. ქართულად.</div>
</div>
    </div>
</section>
'''

    # Find the insertion point before the image generation section
    if '<section id="image-prompts"' in content and 'BRAINSTORMING MICRO-TASK' not in content:
        content = content.replace('<section id="image-prompts"', brainstorming_section + '\n\n<section id="image-prompts"')

    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print('Agenda and sections updated successfully.')

if __name__ == '__main__':
    update_agenda_and_tasks()

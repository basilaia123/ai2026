#!/usr/bin/env python3
"""Batch 3: L5 Deep Research/NotebookLM + L3/L4 year updates + L9 learning objectives"""
import re

def load(f):
    with open(f, 'rb') as fh: return fh.read().decode('utf-8')
def save(f, c):
    with open(f, 'wb') as fh: fh.write(c.encode('utf-8'))

# ══════════════════════════════════════════
# L5: Update Perplexity card + update slide 7 + add NotebookLM
# ══════════════════════════════════════════
print('=== L5: Perplexity Deep Research + NotebookLM ===')
c5 = load('lectures/lecture-5-slides.html')

# Update Perplexity tool card (slide 7) to add Deep Research
old_perp_card = '''            <div class="tool-card">
                <h4>Perplexity.ai 🔍</h4>
                <p><strong>საუკეთესოა:</strong> სწრაფი ფაქტების მოსაძიებლად</p>
                <ul>
                    <li>ინფორმაცია რეალურ დროში</li>
                    <li>წყაროების მითითება</li>
                    <li>მარტივი გამოყენება</li>
                </ul>
                <p><strong>გამოიყენეთ, როდესაც გჭირდებათ:</strong> "რა არის...", "როდის...", "რამდენია..."</p>
            </div>'''

new_perp_card = '''            <div class="tool-card">
                <h4>Perplexity AI 🔍 — Deep Research</h4>
                <p><strong>საუკეთესოა:</strong> ვერიფიცირებული კვლევა ციტირებებით</p>
                <ul>
                    <li>ინფორმაცია რეალურ დროში — წყაროების ბმულებით</li>
                    <li><strong>Deep Research mode:</strong> ასობით წყაროს სკანირება → ყოვლისმომცველი ანგარიში</li>
                    <li>Perplexity Pro: GPT-5.4 / Claude 4.6 / Gemini 3 — 300+ კითხვა/დღე</li>
                    <li>Market analysis, competitive intelligence პროფესიონალებისთვის</li>
                </ul>
                <p><strong>გამოიყენეთ:</strong> "Deep Research: [თემა]" → სრული ანგარიში 5 წუთში</p>
            </div>'''

if old_perp_card in c5:
    c5 = c5.replace(old_perp_card, new_perp_card, 1)
    print('  ✅ L5: Perplexity card updated with Deep Research')
else:
    print('  ⚠️  L5: Perplexity card not found verbatim')

# Update ChatGPT tool card to add Deep Research
old_chat_card = '''            <div class="tool-card">
                <h4>ChatGPT 💬</h4>
                <p><strong>საუკეთესოა:</strong> ახსნა-განმარტებებისთვის</p>
                <ul>
                    <li>რთული თემების ახსნა</li>
                    <li>ტექსტის შეჯამება</li>
                    <li>დამაზუსტებელი კითხვები</li>
                </ul>
                <p><strong>გამოიყენეთ, როდესაც გჭირდებათ:</strong> "ამიხსენი...", "შეაჯამე...", "გააანალიზე..."</p>
            </div>'''

new_chat_card = '''            <div class="tool-card">
                <h4>ChatGPT (GPT-5.4) 💬</h4>
                <p><strong>საუკეთესოა:</strong> ახსნა, ანალიზი, Agent Mode</p>
                <ul>
                    <li>რთული თემების ახსნა, ტექსტის შეჯამება</li>
                    <li><strong>Deep Research mode:</strong> ინტერნეტ-კვლევა + ანგარიში ციტირებებით</li>
                    <li><strong>Canvas:</strong> დოკუმენტების ინტერაქტიული რედაქტირება</li>
                    <li><strong>Projects:</strong> პერსისტენტური სამუშაო სივრცე ფაილებით</li>
                </ul>
                <p><strong>გამოიყენეთ:</strong> "ამიხსენი...", "შეაჯამე...", "Deep Research: [თემა]"</p>
            </div>'''

if old_chat_card in c5:
    c5 = c5.replace(old_chat_card, new_chat_card, 1)
    print('  ✅ L5: ChatGPT card updated with GPT-5.4 Deep Research')
else:
    print('  ⚠️  L5: ChatGPT card not found verbatim')

# Update Claude tool card
old_claude_card = '''            <div class="tool-card">
                <h4>Claude 📄</h4>
                <p><strong>საუკეთესოა:</strong> დიდი მოცულობის დოკუმენტებთან სამუშაოდ</p>
                <ul>
                    <li>PDF-ების ანალიზი</li>
                    <li>დიდი მოცულობის ტექსტები</li>
                    <li>დეტალური პასუხები</li>
                </ul>
                <p><strong>გამოიყენეთ, როდესაც:</strong> აანალიზებთ დოკუმენტებს</p>
            </div>'''

new_claude_card = '''            <div class="tool-card">
                <h4>Claude Sonnet 4.6 📄 + NotebookLM 📚</h4>
                <p><strong>საუკეთესოა:</strong> დოკუმენტები + კვლევის სინთეზი</p>
                <ul>
                    <li><strong>Claude Projects:</strong> ატვირთეთ PDF-ები → persistent context მრავალ session-ზე</li>
                    <li>დიდი მოცულობის ტექსტები (200K token context)</li>
                    <li><strong>NotebookLM Studio (2025):</strong> წყაროებიდან → Podcast, ვიდეო, Mind Map, Flashcards</li>
                    <li>NotebookLM Deep Research: ვების სკანირება + ციტირებები</li>
                </ul>
                <p><strong>გამოიყენეთ:</strong> კვლევისა და დოკუმენტების ანალიზისთვის</p>
            </div>'''

if old_claude_card in c5:
    c5 = c5.replace(old_claude_card, new_claude_card, 1)
    print('  ✅ L5: Claude card updated + NotebookLM Studio added')
else:
    print('  ⚠️  L5: Claude card not found verbatim')
    # Try partial
    if 'Claude 📄' in c5:
        c5 = c5.replace('<h4>Claude 📄</h4>', '<h4>Claude Sonnet 4.6 + NotebookLM Studio 📄</h4>', 1)
        print('  ✅ L5: Claude card title updated (partial)')

# Update the pro tip at the bottom of slide 7
old_tip = '<p>დაიწყეთ Perplexity.ai-ით სწრაფი ფაქტებისთვის, გამოიყენეთ ChatGPT ახსნა-განმარტებებისთვის და Claude — დიდი დოკუმენტების გასაანალიზებლად.</p>'
new_tip = '<p><strong>2026 workflow:</strong> Perplexity Deep Research → ფაქტები + ციტირებები | ChatGPT/Claude Deep Research → კომპლექსური ანალიზი | NotebookLM Studio → საკუთარი დოკუმენტების სინთეზი + Podcast/Mind Map</p>'
if old_tip in c5:
    c5 = c5.replace(old_tip, new_tip, 1)
    print('  ✅ L5: Pro tip updated')

save('lectures/lecture-5-slides.html', c5)

# ══════════════════════════════════════════
# L3: Update writing tool section
# ══════════════════════════════════════════
print('\n=== L3: Writing tools update ===')
c3 = load('lectures/lecture-3-slides.html')
model_refs = set(re.findall(r'(?:GPT-\d[\d.]*|Claude[\s]\d[\d.]*[\w]*|Gemini \d[\d.]*)', c3))
print(f'  Model refs in L3: {model_refs}')

# Update Claude 3.5 → 4.6
c3 = c3.replace('Claude 3.5 Sonnet', 'Claude Sonnet 4.6')
c3 = c3.replace('Claude 3.7', 'Claude 4.6')
c3 = c3.replace('Claude 3.5', 'Claude Sonnet 4.6')
# Update GPT-4 references
c3 = c3.replace('GPT-4 Turbo', 'GPT-5.4')
c3 = c3.replace('GPT-4o', 'GPT-5.4')

save('lectures/lecture-3-slides.html', c3)
print('  ✅ L3: Model versions updated')

# ══════════════════════════════════════════
# L4: Update model names
# ══════════════════════════════════════════
print('\n=== L4: Model versions ===')
c4 = load('lectures/lecture-4-slides.html')
model_refs = set(re.findall(r'(?:GPT-\d[\d.]*|Claude[\s]\d[\d.]*[\w]*|Gemini \d[\d.]*)', c4))
print(f'  Model refs in L4: {model_refs}')

c4 = c4.replace('Claude 3.5 Sonnet', 'Claude Sonnet 4.6')
c4 = c4.replace('Claude 3.7', 'Claude 4.6')
c4 = c4.replace('Claude 3.5', 'Claude Sonnet 4.6')
c4 = c4.replace('GPT-4 Turbo', 'GPT-5.4')
c4 = c4.replace('GPT-4o', 'GPT-5.4')

save('lectures/lecture-4-slides.html', c4)
print('  ✅ L4: Model versions updated')

# ══════════════════════════════════════════
# L9: Update learning objectives (slide 2) + title to include AI Agents
# ══════════════════════════════════════════
print('\n=== L9: Learning objectives update ===')
c9 = load('lectures/lecture-9-slides.html')

# Update title
c9 = c9.replace(
    '<h1>🤖 ავტომატიზაცია და No-Code ინსტრუმენტები</h1>',
    '<h1>🤖 ავტომატიზაცია, No-Code და AI Agents</h1>'
)

# Update objectives
old_obj = 'გაიაზრებთ AI-ზე დაფუძნებული ავტომატიზაციის მომავალს</li>'
new_obj = '''გაიაზრებთ AI-ზე დაფუძნებული ავტომატიზაციის მომავალს</li>
                    <li>გაეცნობით AI Agents-ს — ChatGPT Agent Mode, Claude Code, n8n Human-in-the-Loop</li>
                    <li>გაიგებთ Automation vs. Agents — განსხვავება და გამოყენების სცენარები</li>'''
if old_obj in c9:
    c9 = c9.replace(old_obj, new_obj, 1)
    print('  ✅ L9: AI Agents added to learning objectives')

save('lectures/lecture-9-slides.html', c9)
print('  ✅ L9: Title and objectives updated')

print('\n\n✅ Batch 3 complete!')

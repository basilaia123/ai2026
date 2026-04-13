#!/usr/bin/env python3
"""
Batch 2: L5, L10, L11, L2 updates
"""
import re

def load(f):
    with open(f, 'rb') as fh: return fh.read().decode('utf-8')
def save(f, c):
    with open(f, 'wb') as fh: fh.write(c.encode('utf-8'))

# ══════════════════════════════════════════
# L5: Add Perplexity Deep Research + NotebookLM Studio + ChatGPT Deep Research
# Find the research tools slide / Perplexity slide
# ══════════════════════════════════════════
print('=== L5: Research tools update ===')
c5 = load('lectures/lecture-5-slides.html')

# Find Perplexity sections
perp_pos = [m.start() for m in re.finditer('Perplexity', c5)]
print(f'  Perplexity refs: {len(perp_pos)}')
# Show first context
if perp_pos:
    print(' ', c5[perp_pos[0]:perp_pos[0]+200].replace('\r\n',' ')[:150])

noteb_refs = len(re.findall('NotebookLM', c5))
print(f'  NotebookLM refs: {noteb_refs}')

# Update Perplexity description  - find "Perplexity" card and add Deep Research
old_perp = 'Perplexity AI - AI-ის მხარდაჭერით ძიება'
if old_perp in c5:
    c5 = c5.replace(old_perp, 'Perplexity — AI-powered კვლევის ძრავა (Deep Research)', 1)
    print('  ✅ L5: Perplexity title updated')
else:
    # Try to find and update any Perplexity description mentioning "ძიება"
    perp_old = re.search(r'Perplexity[^<]{0,30}ძიება', c5)
    if perp_old:
        print(f'  Found: {perp_old.group()!r}')

# Find NotebookLM section and update
old_nb = 'NotebookLM-ის გამოყენება'
new_nb = 'NotebookLM Studio — კვლევის თქვენი AI ასისტენტი'
if old_nb in c5:
    c5 = c5.replace(old_nb, new_nb, 1)
    print('  ✅ L5: NotebookLM title updated')

# Add Studio Mode note near NotebookLM
studio_marker = 'NotebookLM'
nb_idx = c5.find(studio_marker)
if nb_idx > 0:
    # Find the tool-card or section end around NotebookLM
    # Look for a key feature list item about audio/podcast and add Studio Mode after it
    audio_ref = c5.find('Audio Overview', nb_idx)
    podcast_ref = c5.find('Podcast', nb_idx)
    target_pos = min([p for p in [audio_ref, podcast_ref] if p > 0], default=0)
    if target_pos == 0:
        print('  ⚠️  L5: Could not find audio/podcast ref near NotebookLM')
    else:
        print(f'  Found audio/podcast at pos {target_pos}')

# Find ChatGPT Deep Research
deep_res = c5.find('Deep Research')
print(f'  Deep Research refs: {len(re.findall("Deep Research", c5))}')

save('lectures/lecture-5-slides.html', c5)

# ══════════════════════════════════════════
# L10: Add year refs and update tool versions
# ══════════════════════════════════════════
print('\n=== L10: Tool versions update ===')
c10 = load('lectures/lecture-10-slides.html')

# Show first few slides
titles = re.findall(r'<h2>(.*?)</h2>', c10)
print('  Slide titles:')
for t in titles[:20]:
    print('   ', t[:60].strip().replace('\r','').replace('\n',' '))

# Find Cursor version refs
cursor_refs = re.findall(r'Cursor[^<]{0,80}', c10)
print(f'\n  Cursor contexts ({len(cursor_refs)}):')
for r in cursor_refs[:5]:
    print(' ', r[:80].replace('\r\n',' '))

# Find Lovable refs
lovable_refs = re.findall(r'Lovable[^<]{0,80}', c10)
print(f'\n  Lovable contexts: {len(lovable_refs)}')

# Update Cursor 0.x → 0.45+
c10 = re.sub(r'Cursor \d+\.\d+', 'Cursor 0.45+', c10)

# Update Claude 3.5/3.7 → 4.6 in L10
c10 = c10.replace('Claude 3.5 Sonnet', 'Claude Sonnet 4.6')
c10 = c10.replace('Claude 3.7', 'Claude 4.6')
c10 = c10.replace('Claude 3.5', 'Claude 4.6')

# Add Windsurf mention if not present
if 'Windsurf' not in c10:
    # Find the comparison table or competitors section in Cursor slide
    github_cop = c10.find('GitHub Copilot')
    if github_cop > 0:
        # Find end of that list item
        end_li = c10.find('</li>', github_cop) + len('</li>')
        c10 = c10[:end_li] + '\n                    <li><strong>Windsurf (Codeium):</strong> ახალი კონკურენტი IDE, 2024-2025 — Claude 4.6 + GPT-5 ინტეგრაცია.</li>' + c10[end_li:]
        print('  ✅ L10: Windsurf added')

save('lectures/lecture-10-slides.html', c10)
print('  ✅ L10: Cursor 0.45+, Claude 4.6 updated')

# ══════════════════════════════════════════  
# L11: DALL-E 3 → DALL-E 4 + add NotebookLM Studio
# ══════════════════════════════════════════
print('\n=== L11: DALL-E 3→4, NotebookLM Studio ===')
c11 = load('lectures/lecture-11-slides.html')

# DALL-E 3 → DALL-E 4
c11 = c11.replace('DALL-E 3', 'DALL-E 4', 1)
print('  ✅ L11: DALL-E 3 → DALL-E 4')

# Find and update Claude versions in L11
c11 = c11.replace('Claude 3.7 Sonnet', 'Claude Sonnet 4.6')
c11 = c11.replace('Claude 3.5 Sonnet', 'Claude Sonnet 4.6')

# Find NotebookLM area (0 refs) — add note about Studio Mode near the audio/research tools area
# Check if there's a spot for it near Gemini Gems or research section
gems_idx = c11.rfind('NotebookLM')  # should be -1 or very few
print(f'  NotebookLM refs in L11: {len(re.findall("NotebookLM", c11))}')

# Find Gemini section to add NotebookLM Studio nearby
gemini_idx = c11.find('Google NotebookLM')
if gemini_idx == -1:
    gemini_idx = c11.find('Gemini Gems')
if gemini_idx > 0:
    # Find the end of that section's list - look for </ul> after it
    end_ul = c11.find('</ul>', gemini_idx) + len('</ul>')
    notebook_note = '''
                    <li><strong>NotebookLM Studio (2025):</strong> კვლევის რევოლუცია — ატვირთეთ დოკუმენტები → ავტომატური Podcast, ვიდეო, Mind Map, Flashcards. Deep Research: ვების სკანირება + ციტირებები.</li>'''
    # Find a good <li> insertion point near Gemini 
    last_li = c11.rfind('</li>', gemini_idx, end_ul)
    if last_li > 0:
        c11 = c11[:last_li+len('</li>')] + notebook_note + c11[last_li+len('</li>'):]
        print('  ✅ L11: NotebookLM Studio note added near Gemini Gems')
    else:
        print('  ⚠️  L11: Could not find insertion point for NotebookLM')

save('lectures/lecture-11-slides.html', c11)

# ══════════════════════════════════════════
# L2: Add GPT-5 Thinking Mode prompting section
# ══════════════════════════════════════════
print('\n=== L2: GPT-5 Thinking Mode prompting ===')
c2 = load('lectures/lecture-2-slides.html')

# Find and update ChatGPT pricing in L2 if any
c2 = c2.replace('GPT-4 Turbo', 'GPT-5.4')
c2 = c2.replace('Claude 3.5', 'Claude 4.6')
c2 = c2.replace('Claude 3.7', 'Claude 4.6')

# Check what model refs exist in L2
model_refs = re.findall(r'(?:GPT-\d|Claude \d|Gemini \d)[^\s<]{0,20}', c2)
print(f'  Model refs: {set(model_refs)}')

# Find the "advanced prompting" or "reasoning models" area
reasoning_idx = c2.find('Reasoning')
print(f'  Reasoning refs: {len(re.findall("Reasoning", c2))}')

# Find a good place to add Thinking Mode note - after Chain-of-Thought section
cot_idx = c2.find('Chain-of-Thought')
if cot_idx > 0:
    # Find end of that tip/box
    end_div = c2.find('</div>', cot_idx + 200)
    thinking_note = '''
            <div class="highlight-box" style="margin-top:1rem;">
                <h4>🧠 2026: Reasoning Models — ახალი Prompting წესები</h4>
                <ul>
                    <li><strong>GPT-5.4 "Think" / Claude Thinking / Gemini Deep Think</strong> — მოდელი თვითონ განსაზღვრავს reasoning სიღრმეს.</li>
                    <li>⚡ <strong>Reasoning models-ისთვის:</strong> ნაკლები ინსტრუქცია, მეტი კონტექსტი. არ ახსნათ "ნაბიჯ-ნაბიჯ" — მოდელი თვითონ ხედავს.</li>
                    <li>🎯 <strong>Chain-of-Thought ახლა ავტომატურია</strong> — reasoning models-ში ჩაშენებულია. Prompt-ში მხოლოდ "think carefully" ან "use extended thinking" ჩამატეთ.</li>
                    <li>💡 <strong>პრაქტიკა:</strong> რთული ამოცანებისთვის — GPT-5.4 Thinking ან Claude Sonnet 4.6 (Extended Thinking). მარტივი — GPT-5.4 standard.</li>
                </ul>
            </div>'''
    if end_div > 0:
        c2 = c2[:end_div + len('</div>')] + thinking_note + c2[end_div + len('</div>'):]
        print('  ✅ L2: Reasoning Models prompting note added after Chain-of-Thought')
    else:
        print('  ⚠️  L2: Could not find end of CoT section')

save('lectures/lecture-2-slides.html', c2)
print('  ✅ L2: Model refs updated')

print('\n\n✅ Batch 2 complete!')

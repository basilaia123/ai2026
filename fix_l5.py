#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fix L5: Perplexity h4, ChatGPT h4, NotebookLM block"""
import re

with open('lectures/lecture-5-slides.html', 'rb') as f:
    c = f.read().decode('utf-8')

# 1) Perplexity h4
c = c.replace('<h4>Perplexity.ai 🔍</h4>', '<h4>Perplexity AI 🔍 — Deep Research</h4>', 1)
print('Perplexity h4 done')

# 2) Add Deep Research li in Perplexity's ul
perp_idx = c.find('Perplexity AI 🔍 — Deep Research')
if perp_idx > 0:
    ul_s = c.find('<ul>', perp_idx)
    ul_e = c.find('</ul>', ul_s)
    if ul_s > 0 and ul_e > 0:
        old_li = '<li>მარტივი გამოყენება</li>'
        new_li = '<li>მარტივი გამოყენება</li>\n                    <li><strong>Deep Research mode:</strong> ასობით წყაროს ავტო-სკანირება → სრული ანგარიში ციტირებებით 5 წუთში</li>'
        section = c[ul_s:ul_e+5]
        if old_li in section:
            c = c[:ul_s] + section.replace(old_li, new_li, 1) + c[ul_e+5:]
            print('Deep Research bullet added')

# 3) ChatGPT h4
c = c.replace('<h4>ChatGPT 💬</h4>', '<h4>ChatGPT (GPT-5.4) — Canvas + Deep Research 💬</h4>', 1)
print('ChatGPT h4 done')

# 4) NotebookLM Studio block — insert after the three-column closing div
# Find 'სწრაფი ფაქტებისთვის' pro tip div and add NotebookLM before it
marker = '        <div class="highlight-box">\n            <h4>💡 პროფესიონალური რჩევა:</h4>'
if marker in c:
    notebook_html = '''        <div class="key-points">
            <h4>📚 NotebookLM Studio (Google, 2025) — კვლევის AI ასისტენტი</h4>
            <ul>
                <li>ატვირთეთ PDF-ები, ვებ-გვერდები, YouTube ვიდეოები — AI ანალიზებს და პასუხობს</li>
                <li><strong>Audio Overview / Podcast:</strong> თქვენი დოკუმენტებიდან AI-პოდკასტი 1 დაწკაპუნებით</li>
                <li><strong>Studio Mode (2025):</strong> ვიდეო, Infographic, Flashcards, Mind Map — წყაროებიდან</li>
                <li><strong>NotebookLM Plus:</strong> მეტი notebook, ანალიტიკა, enterprise ფუნქციები</li>
            </ul>
            <p><strong>ქართული use case:</strong> ატვირთეთ 50-გვერდიანი ანგარიში → 10 წუთში Podcast + Mind Map!</p>
        </div>\n'''
    c = c.replace(marker, notebook_html + marker, 1)
    print('NotebookLM Studio block added')
else:
    print('Marker not found, searching...')
    idx = c.find('პროფესიონალური რჩევა')
    if idx > 0:
        print(f'Found at {idx}:', c[idx-30:idx+50].replace('\r\n',' '))

with open('lectures/lecture-5-slides.html', 'wb') as f:
    f.write(c.encode('utf-8'))
print('Done!')

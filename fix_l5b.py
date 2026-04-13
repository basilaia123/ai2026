#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert NotebookLM Studio block in L5"""

with open('lectures/lecture-5-slides.html', 'rb') as f:
    c = f.read().decode('utf-8')

marker = '        <div class="highlight-box">\r\n            <h4>💡 პროფესიონალური რჩევა:</h4>'
if marker in c:
    notebook_html = '        <div class="key-points">\r\n            <h4>📚 NotebookLM Studio (Google, 2025) — კვლევის AI ასისტენტი</h4>\r\n            <ul>\r\n                <li>ატვირთეთ PDF-ები, ვებ-გვერდები, YouTube ვიდეოები — AI ანალიზებს</li>\r\n                <li><strong>Audio Overview / Podcast:</strong> თქვენი დოკუმენტებიდან AI-პოდკასტი 1 კლიკით</li>\r\n                <li><strong>Studio Mode (2025):</strong> ვიდეო, Infographic, Flashcards, Mind Map — ავტომატურად</li>\r\n                <li><strong>NotebookLM Plus:</strong> 500+ notebook, enterprise analytics, higher limits</li>\r\n            </ul>\r\n            <p><strong>ქართული use case:</strong> ატვირთეთ 50-გვერდიანი ანგარიში → 10 წუთში Podcast + Mind Map!</p>\r\n        </div>\r\n\r\n'
    c = c.replace(marker, notebook_html + marker, 1)
    print('NotebookLM Studio block added!')
else:
    print('Marker not found with CRLF')

with open('lectures/lecture-5-slides.html', 'wb') as f:
    f.write(c.encode('utf-8'))
print('Done')

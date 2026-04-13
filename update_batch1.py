#!/usr/bin/env python3
"""
Batch update script: L6, L12, L2, L7
Run from ai2026/ directory
"""
import re, os

def patch(filepath, replacements):
    with open(filepath, 'rb') as f:
        c = f.read().decode('utf-8')
    changed = 0
    for old, new in replacements:
        if old in c:
            c = c.replace(old, new, 1)
            changed += 1
            print(f'  ✅ {filepath}: replaced "{old[:50].strip()}"')
        else:
            print(f'  ⚠️  {filepath}: NOT FOUND "{old[:50].strip()}"')
    with open(filepath, 'wb') as f:
        f.write(c.encode('utf-8'))
    return changed

total = 0

# ══════════════════════════════════════════
# L6: GPT-4 pricing → GPT-5.4
# ══════════════════════════════════════════
print('\n=== L6: GPT-4 → GPT-5.4 pricing ===')
total += patch('lectures/lecture-6-slides.html', [
    (
        '<strong>Pro ($20/თვე):</strong> ულიმიტო GPT-4.</li>',
        '<strong>Plus ($20/თვე):</strong> GPT-5.4 — ადაპტური reasoning, Canvas, Agent Mode, Deep Research.</li>'
    ),
])

# L6: Claude 3.5 Sonnet → Claude 4.6 Sonnet (Cursor context)
print('\n=== L6: Claude 3.5 (Cursor) → Claude 4.6 Sonnet ===')
total += patch('lectures/lecture-6-slides.html', [
    (
        'Claude 3.5-ს.</p>',
        'Claude 4.6 Sonnet-ს (Opus 4.6 — ყველაზე მძლავრი კოდ-agent 2026).</p>'
    ),
    (
        '<strong>Claude 3.5 Sonnet:</strong> კოდირებისთვის ერთ-ერთი უძლიერესი მოდელი.</li>',
        '<strong>Claude Sonnet 4.6:</strong> კოდირებისთვის #1 მოდელი (SWE-bench ლიდერი 2026).</li>'
    ),
    (
        'Claude 3.5-ის სიმძლავრის გამოყენება გსურთ.',
        'Claude 4.6-ის სიმძლავრის გამოყენება გსურთ.'
    ),
])

# ══════════════════════════════════════════
# L12: EU AI Act — add enforcement dates
# ══════════════════════════════════════════
print('\n=== L12: EU AI Act enforcement dates ===')
with open('lectures/lecture-12-slides.html', 'rb') as f:
    c12 = f.read().decode('utf-8')

old_eu = 'EU AI Act - 4-დონიანი risk-based მიდგომა:</h4>'
new_eu = 'EU AI Act - 4-დონიანი risk-based მიდგომა + განხორციელება 2025-2026:</h4>'

if old_eu in c12:
    c12 = c12.replace(old_eu, new_eu, 1)
    print('  ✅ L12: EU AI Act title updated')
    total += 1

# Insert enforcement timeline after the risk table (find the closing </table> in EU AI Act slide)
timeline_block = '''
            <div class="warning-box" style="margin-top:1.5rem;">
                <h4>⏰ EU AI Act — განხორციელების დრო (ახლა ამოქმედდა!):</h4>
                <ul>
                    <li>✅ <strong>2025 წლის 2 თებერვალი (ᲐᲛᲝᲥᲛᲔᲓᲓᲐ):</strong> Unacceptable Risk AI-ის აკრძალვა — Social scoring, ემოციების ამოცნობა სამსახურში, სახის მასობრივი იდენტიფიკაცია.</li>
                    <li>✅ <strong>2025 წლის 2 აგვისტო (ᲐᲛᲝᲥᲛᲔᲓᲓᲐ):</strong> GPAI (ChatGPT, Claude, Gemini) — გამჭვირვალობის ვალდებულება. ჯარიმების სისტემა ამოქმედდა.</li>
                    <li>🔜 <strong>2026 წლის 2 აგვისტო (4 თვე შემდეგ):</strong> High-Risk AI სისტემებისთვის სრული შესაბამისობა სავალდებულო. AI-გენერირებული კონტენტის გამჟღავნება.</li>
                    <li>💰 <strong>ჯარიმები:</strong> Prohibited practices — €35M ან გლობალური ბრუნვის 7%. High-risk — €15M ან 3%. არასწორი ინფო — €7.5M ან 1.5%.</li>
                </ul>
            </div>'''

# Find the end of the EU AI Act table
eu_table_end = c12.find('</table>', c12.find('EU AI Act'))
if eu_table_end > 0:
    insert_pos = c12.find('</div>', eu_table_end) + len('</div>')
    c12 = c12[:insert_pos] + timeline_block + c12[insert_pos:]
    print('  ✅ L12: EU Act enforcement timeline inserted')
    total += 1

# L12: DALL-E 3 → DALL-E 4
c12 = c12.replace('<strong>OpenAI (DALL-E 3)</strong>', '<strong>OpenAI (DALL-E 4 / GPT-5.4)</strong>', 1)
print('  ✅ L12: DALL-E 3 → DALL-E 4')
total += 1

with open('lectures/lecture-12-slides.html', 'wb') as f:
    f.write(c12.encode('utf-8'))

# ══════════════════════════════════════════
# L7: Claude 3 → Claude 4.6 (single ref)
# ══════════════════════════════════════════
print('\n=== L7: Claude 3 → Claude 4.6 ===')
with open('lectures/lecture-7-slides.html', 'rb') as f:
    c7 = f.read().decode('utf-8')

# Find Claude 3 in L7
claude3_in_l7 = re.findall('Claude 3[^.]*.{0,80}', c7)
for ref in claude3_in_l7[:5]:
    print('  Found:', ref[:80].replace('\r\n',' '))

# Generic replacement for Claude 3.5 Sonnet → Claude Sonnet 4.6
c7 = c7.replace('Claude 3.5 Sonnet', 'Claude Sonnet 4.6')
c7 = c7.replace('Claude 3.7', 'Claude 4.6')
with open('lectures/lecture-7-slides.html', 'wb') as f:
    f.write(c7.encode('utf-8'))
print('  ✅ L7: Claude 3.x → Claude 4.6 updated')
total += 1

print(f'\n\nDone. Total changes: {total}')

# -*- coding: utf-8 -*-
import sys

file_path = r'c:\Users\GBASILAIA\claude\ai2026\oppa\oppa-session5.html'
out_path = r'c:\Users\GBASILAIA\claude\ai2026\oppa\scratch\extracted_lines.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

keywords = [
    '7. მონიტორინგი',
    'PII მონაცების',
    'Out of Paper',
    'მესამე მხარის',
    'Ticket Text',
    'Free Plan',
    'Core/Pro',
    'Rate Limits',
    'ინკასაციის',
    'Reconciliation',
    'Auto-Reboot',
    'ჩატბოტი',
    'Compliance ანგარიშების',
    'Notion Knowledge',
    'Data Store არის',
    'სპამვა',
    'Haiku vs. Sonnet',
    'ROI-ს',
    '200 ტიკეტის',
    'INCOMPLETE',
    'ბრაუზინგ'
]

with open(out_path, 'w', encoding='utf-8') as out:
    for idx, line in enumerate(lines):
        for kw in keywords:
            if kw in line:
                out.write(f"Line {idx+1} ({kw}): {line.strip()}\n")
                break

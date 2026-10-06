import os
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

base_dir = r"c:\Users\GBASILAIA\claude\ai2026\lectures8"

print("--- 1. AUDITING HOMEWORK POINTS & TITLES ---")
for h in [1, 2, 3, 4, 5, 6, 7]:
    hw_path = os.path.join(base_dir, f"homework-{h}.html")
    if os.path.exists(hw_path):
        with open(hw_path, "r", encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")
            title = soup.title.string if soup.title else "No title"
            # find mentions of total points
            m_total = re.findall(r"(?:მაქსიმალური\s*შეფასება|სულ|Total|ქულა):\s*(\d+(?:\.\d+)?)\s*ქულა", content, re.I)
            # find points in badges/headers
            badges = [b.get_text(strip=True) for b in soup.find_all(class_=re.compile(r"badge|points|score"))]
            print(f"HW {h}: Title: '{title}' | Badges: {badges} | Total mentions: {m_total}")
    else:
        print(f"HW {h}: NOT FOUND")

print("\n--- 2. AUDITING SLIDE COUNTS & HOMEWORK SLIDES ---")
for s in [2, 3, 4, 5]:
    slide_path = os.path.join(base_dir, f"v2-lecture-{s}-slides.html")
    if os.path.exists(slide_path):
        with open(slide_path, "r", encoding="utf-8") as f:
            content = f.read()
            soup = BeautifulSoup(content, "html.parser")
            slides = soup.find_all(class_="slide")
            # find total slides in footer or script
            footers = soup.find_all(class_=re.compile(r"footer|slide-number|counter"))
            hw_slide = None
            for i, sl in enumerate(slides):
                if "საშინაო დავალება" in sl.get_text() or f"homework-{s}" in sl.get_text():
                    hw_slide = (i + 1, sl.get_text()[:200].replace("\n", " "))
            print(f"Slide deck {s}: {len(slides)} slides | HW slide: {hw_slide}")
    else:
        print(f"Slide deck {s}: NOT FOUND")

print("\n--- 3. AUDITING FILE EXISTENCE FOR LECTURES 2-5 ---")
files_to_check = [
    "v2-lecture-{i}-slides.html",
    "homework-{i}.html",
    "lecture-{i}-exercises.html",
    "lecture-{i}-quick-ref.html",
    "lecture-{i}-quick-ref.md",
    "lecture-{i}-summary.html",
    "lecture-{i}-summary.md",
    "lecture-{i}-study-guide.html",
    "lecture-{i}-study-guide.md",
    "lecture-{i}-lesson-plan.html"
]

for i in [2, 3, 4, 5]:
    print(f"\nLecture {i} files:")
    for pat in files_to_check:
        fname = pat.format(i=i)
        p = os.path.join(base_dir, fname)
        if os.path.exists(p):
            size = os.path.getsize(p)
            print(f"  OK: {fname} ({size} bytes)")
        else:
            print(f"  MISSING: {fname}")

print("\n--- 4. AUDITING SLIDE NUMBERS IN ALL DECKS ---")
for num in [2, 3, 4, 5]:
    filename = os.path.join(base_dir, f"v2-lecture-{num}-slides.html")
    with open(filename, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")
        slides = soup.find_all(class_="slide")
        print(f"\nLecture {num} ({len(slides)} slides total):")
        for i, s in enumerate(slides):
            headers = s.find_all(class_=re.compile(r"slide-header|header|slide-number"))
            h_text = " / ".join(h.get_text(strip=True) for h in headers) if headers else "NO_HEADER"
            # check any fraction like \d+/\d+
            m = re.findall(r"(\d+/\d+)", s.get_text())
            first_m = m[0] if m else "NO_FRACTION"
            if first_m != f"{i+1}/{len(slides)}":
                print(f"  MISMATCH at Slide {i+1}: found '{first_m}', expected '{i+1}/{len(slides)}' (header: {h_text})")

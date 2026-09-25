import glob, re, os, sys
sys.stdout.reconfigure(encoding='utf-8')

files = sorted(glob.glob(r"c:\Users\GBASILAIA\claude\ai2026\make\lecture-*-slides.html"))
for f in files:
    with open(f, "r", encoding="utf-8", errors="ignore") as fp:
        c = fp.read()
    nav_info = re.findall(r'<span class="nav-info">([^<]+)</span>', c)
    total_slides = re.findall(r'Slide \d+/(\d+)', c)
    fname = os.path.basename(f)
    print(f"{fname}: nav-info={nav_info}, total_slides={set(total_slides)}")

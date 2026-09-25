import os
import glob
import re

make_dir = r"c:\Users\GBASILAIA\claude\ai2026\make"
html_files = glob.glob(os.path.join(make_dir, "*.html"))

broken_links = []
external_links = set()

for hf in html_files:
    fname = os.path.basename(hf)
    with open(hf, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # href and src
    urls = re.findall(r'(?:href|src)=["\']([^"\']+)["\']', content)
    for u in urls:
        u_clean = u.split("#")[0].split("?")[0].strip()
        if not u_clean:
            continue
        if u_clean.startswith(("http://", "https://", "mailto:", "tel:", "data:", "javascript:")):
            external_links.add(u_clean)
        else:
            target = os.path.normpath(os.path.join(make_dir, u_clean))
            if not os.path.exists(target):
                broken_links.append((fname, u))

print(f"Total HTML files analyzed: {len(html_files)}")
print(f"Broken local references count: {len(broken_links)}")
for src, hr in broken_links:
    print(f"  [{src}] -> {hr}")

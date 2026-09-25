import re

with open(r"c:\Users\GBASILAIA\claude\ai2026\make\index.html", "r", encoding="utf-8") as f:
    c = f.read()

hrefs = set(re.findall(r'href=["\']([^"\']+)["\']', c))
print("All hrefs in index.html:")
for h in sorted(hrefs):
    print("  ", h)

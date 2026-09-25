import os, re

make_dir = r"c:\Users\GBASILAIA\claude\ai2026\make"
index_path = os.path.join(make_dir, "index.html")

with open(index_path, "r", encoding="utf-8") as f:
    c = f.read()

lec_links = sorted(set(re.findall(r'href=["\'](lecture-[^"\']+)["\']', c)))
hw_links = sorted(set(re.findall(r'href=["\'](homework-[^"\']+)["\']', c)))

print(f"Index.html size: {len(c)} bytes")
print("Lecture links in index.html (count = {}):".format(len(lec_links)))
for l in lec_links:
    print("  ", l)

print("Homework links in index.html (count = {}):".format(len(hw_links)))
for h in hw_links:
    print("  ", h)

# Check session counts mentioned in text
sessions = re.findall(r'(\d+)\s*(?:შეხვედრა|საათი|ლექცია)', c)
print("Session / hours mentions:", sessions[:15])

# Check for final project link
print("Final project in index.html:", "final-project.html" in c)

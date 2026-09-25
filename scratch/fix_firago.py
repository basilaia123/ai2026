import glob
import os

target = '<link href="https://fonts.googleapis.com/css2?family=FiraGO:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
replacement = '<link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet"/>'

make_dir = r"c:\Users\GBASILAIA\claude\ai2026\make"
files = glob.glob(os.path.join(make_dir, "**/*"), recursive=True)

modified_files = []
for f in files:
    if os.path.isfile(f):
        try:
            with open(f, "r", encoding="utf-8") as fp:
                content = fp.read()
            if target in content:
                new_content = content.replace(target, replacement)
                with open(f, "w", encoding="utf-8") as fp:
                    fp.write(new_content)
                modified_files.append(f)
        except Exception as e:
            print(f"Error processing {f}: {e}")

print(f"Successfully updated {len(modified_files)} files in make:")
for m in modified_files:
    print(f"  - {os.path.basename(m)}")

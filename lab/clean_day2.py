def remove_day1_leftovers():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-slides.html', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    start_idx = -1
    end_idx = -1
    
    # We want to remove everything from:
    # <div class="py-8 border-b border-gray-200">
    #     <div class="section-header" style="background: linear-gradient(135deg, #004D40 0%, #00796B 100%);">
    #         <div class="flex items-center gap-4">
    #             <span class="text-4xl">🎨</span>
    #             <div>
    #                 <p class="text-xs font-bold uppercase tracking-widest" style="color:#80cbc4;">დამატებითი მოდული</p>
    #                 <h2 class="text-2xl font-bold text-white">კრეატიული AI — ვიზუალები და იდეები</h2>
    
    # up to just before <section id="summary" class="min-h-[70vh] flex flex-col justify-center py-12 topic-card">

    for i, line in enumerate(lines):
        if 'კრეატიული AI — ვიზუალები და იდეები' in line and '<h2' in line:
            # Step back to find the starting div
            for j in range(i, i-10, -1):
                if '<div class="py-8 border-b border-gray-200">' in lines[j]:
                    start_idx = j
                    break
            if start_idx == -1:
                start_idx = i - 3 # Fallback
            break

    if start_idx != -1:
        for i in range(start_idx, len(lines)):
            if '<section id="summary"' in lines[i]:
                end_idx = i
                break

    if start_idx != -1 and end_idx != -1:
        new_lines = lines[:start_idx] + lines[end_idx:]
        with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-2-slides.html', 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Removed leftovers from line {start_idx} to {end_idx}.")
    else:
        print("Could not find the block to remove.")

if __name__ == '__main__':
    remove_day1_leftovers()
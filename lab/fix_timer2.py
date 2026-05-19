def fix_timer2():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    old_str = '<span id="timer2-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">30:00</span>'
    new_str = '<span id="timer2-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">20:00</span>'
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("Timer 2 display fixed.")
    else:
        print("Could not find the 30:00 string.")

if __name__ == '__main__':
    fix_timer2()
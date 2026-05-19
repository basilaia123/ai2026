def fix_timers():
    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Practice 1 fix initial display to 15:00
    content = content.replace('<span id="timer1-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">20:00</span>',
                              '<span id="timer1-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">15:00</span>')

    # Practice 2 fix initial display to 20:00
    content = content.replace('<span id="timer2-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">30:00</span>',
                              '<span id="timer2-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">20:00</span>')

    # Add a timer to the Brainstorming section
    old_brainstorm_header = '<h2 class="text-3xl font-bold mb-2">💡 იდეების გენერაცია (Brainstorming)</h2>'
    new_brainstorm_header = '''<div class="flex items-center justify-between mb-2">
    <h2 class="text-3xl font-bold">💡 იდეების გენერაცია (Brainstorming)</h2>
    <div id="timer3" class="flex items-center gap-2 px-4 py-2 rounded-xl" style="background:#0f1f2e;">
        <span class="text-2xl">⏱</span>
        <span id="timer3-display" class="font-black text-2xl" style="color:#E91E63;font-variant-numeric:tabular-nums;">10:00</span>
        <button onclick="startTimer('timer3-display',10)" class="text-xs px-3 py-1 rounded font-bold" style="background:#E91E63;color:white;">▶ დაწყება</button>
    </div>
</div>'''
    
    if old_brainstorm_header in content and 'timer3-display' not in content:
        content = content.replace(old_brainstorm_header, new_brainstorm_header)

    with open('c:/Users/GBASILAIA/claude/ai2026/lab/day-1-slides.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Timers updated.")

if __name__ == '__main__':
    fix_timers()
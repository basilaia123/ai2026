import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract agenda timeline content
agenda_m = re.search(r'<section\s+[^>]*id=["\']agenda-timeline["\'][^>]*>(.*?)</section>', text, re.DOTALL)
if agenda_m:
    print("=== AGENDA TIMELINE ===")
    clean_agenda = re.sub(r'<script.*?</script>', '', agenda_m.group(1), flags=re.DOTALL)
    # extract timeline items
    items = re.findall(r'<div[^>]*class="[^"]*timeline-item[^"]*"[^>]*>(.*?)</div>\s*</div>', clean_agenda, re.DOTALL)
    if not items:
        # try another pattern
        rows = re.findall(r'(\d{2}:\d{2}\s*[-–]\s*\d{2}:\d{2}.*?)(?=<div|$)', clean_agenda, re.DOTALL)
        for r in rows[:10]:
            print(re.sub(r'<.*?>', ' ', r).strip()[:150])
    print(re.sub(r'<.*?>', ' ', clean_agenda)[:1200])

# Count prompt boxes, interactive components, copy buttons
copy_btns = len(re.findall(r'copyToClipboard|copyPrompt|copy-btn', text))
prompt_boxes = len(re.findall(r'class="[^"]*prompt-[^"]*"|class="[^"]*code-[^"]*"', text))
task_cards = len(re.findall(r'id=["\']block-task-\d+["\']', text))
word_count = len(re.sub(r'<.*?>', ' ', text).split())

print(f"\nTotal words: {word_count}")
print(f"Total prompt / code boxes: {prompt_boxes}")
print(f"Copy buttons: {copy_btns}")
print(f"Task cards: {task_cards}")

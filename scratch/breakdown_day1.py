import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    text = f.read()

def print_block_summary(block_id):
    m = re.search(r'<section\s+[^>]*id=["\']' + block_id + r'["\'][^>]*>(.*?)</section>', text, re.DOTALL)
    if not m:
        print(f"=== {block_id}: NOT FOUND ===")
        return
    content = m.group(1)
    title = re.search(r'<h[23][^>]*>(.*?)</h[23]>', content, re.DOTALL)
    title_str = re.sub(r'<.*?>', '', title.group(1)).strip() if title else 'No title'
    prompts = re.findall(r'<pre[^>]*>(.*?)</pre>', content, re.DOTALL)
    words = len(re.sub(r'<.*?>', ' ', content).split())
    
    print(f"\n==========================================")
    print(f"BLOCK: {block_id}")
    print(f"TITLE: {title_str}")
    print(f"WORDS: {words} | CODE/PRE BLOCKS: {len(prompts)}")
    print(f"==========================================")
    
    subheadings = re.findall(r'<h[34][^>]*>(.*?)</h[34]>', content, re.DOTALL)
    for sh in subheadings[:8]:
        clean_sh = re.sub(r'<.*?>', '', sh).strip()
        print(f"  • {clean_sh}")
        
    for i, p in enumerate(prompts):
        clean_p = re.sub(r'<.*?>', '', p).strip()
        print(f"    [Prompt {i+1} preview, length {len(clean_p)} chars]: {clean_p[:120]}...")

blocks = ['agenda-timeline', 'block-assistant', 'block-task-1', 'block-flow', 'block-audio', 'block-task-2', 'block-prompt-bank']
for b in blocks:
    print_block_summary(b)

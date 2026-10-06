import os
from playwright.sync_api import sync_playwright

test_files = [
    'eu4dialogue/index.html',
    'eu4dialogue/peacebuilding/index.html',
    'eu4dialogue/pm/index.html'
]

viewports = [
    {"name": "Mobile Small (360px)", "width": 360, "height": 740},
    {"name": "Mobile Standard (375px)", "width": 375, "height": 812},
    {"name": "Mobile Modern (390px)", "width": 390, "height": 844},
    {"name": "Mobile Android (412px)", "width": 412, "height": 915},
    {"name": "Tablet (768px)", "width": 768, "height": 1024},
    {"name": "Desktop (1200px)", "width": 1200, "height": 800},
]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    all_passed = True
    
    for frel in test_files:
        html_path = os.path.abspath(frel)
        file_url = f'file:///{html_path.replace(os.sep, "/")}'
        print(f"\n================ Testing {frel} ================")
        
        for vp in viewports:
            page = browser.new_page(viewport={"width": vp["width"], "height": vp["height"]})
            page.goto(file_url, wait_until="networkidle")
            
            overflow_info = page.evaluate('''() => {
                const docWidth = document.documentElement.offsetWidth;
                const scrollWidth = document.documentElement.scrollWidth;
                const diff = scrollWidth - docWidth;
                
                const overflowing = [];
                if (diff > 0) {
                    const elements = document.querySelectorAll('*');
                    elements.forEach(el => {
                        const rect = el.getBoundingClientRect();
                        if (rect.right > docWidth + 1) {
                            overflowing.push({
                                tag: el.tagName,
                                id: el.id,
                                className: el.className,
                                right: rect.right,
                                width: rect.width
                            });
                        }
                    });
                }
                return { docWidth, scrollWidth, diff, overflowing: overflowing.slice(0, 5) };
            }''')
            
            diff = overflow_info["diff"]
            status = "PASSED" if diff <= 0 else "FAILED"
            print(f"[{status}] {vp['name']}: docWidth={overflow_info['docWidth']}, scrollWidth={overflow_info['scrollWidth']}, diff={diff}px")
            if diff > 0:
                all_passed = False
                print(f"  Overflowing elements: {overflow_info['overflowing']}")
                
            page.close()
            
    browser.close()
    
    if all_passed:
        print("\nALL FILES AND ALL VIEWPORTS PASSED WITH DIFF = 0px!")
    else:
        print("\nSOME TESTS FAILED!")

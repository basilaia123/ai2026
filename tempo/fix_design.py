import re

file_path = r'C:\Users\GBASILAIA\claude\ai2026\tempo\lecture-6-slides.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace HEAD style and config (everything between <script> tailwind.config... and </style>)
# We will just replace from `<script>\n        tailwind.config = {` to `</style>`
new_head = """    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        tempo: { 900: '#2A2C2E', 800: '#2C2C2C', 700: '#333333', sky: '#48B8BE', gold: '#C5A059', light: '#F0F0F0' }
                    },
                    fontFamily: {
                        sans: ['FiraGO', 'sans-serif'],
                        serif: ['Playfair Display', 'serif']
                    }
                }
            }
        }
    </script>
    <style>
        :root {
            --sky: #48B8BE;
            --sky-light: #A8DCDF;
            --cyan: #2C8B90;
            --teal: #1D5558;
            --green: #48B8BE;
            --deep: #F0F0F0;
            --mid: #1E1E1E;
            --bg: #F5F5F3;
            --surface: #FFFFFF;
            --border: rgba(0,0,0,0.10);
            --text-1: #1A1A1A;
            --text-2: #2C2C2C;
            --text-3: #A0A0A0;
            --shadow: 0 4px 15px rgba(0,0,0,0.05);
        }
        html { scroll-behavior: smooth; }
        #sidebar::-webkit-scrollbar { width: 4px; }
        #sidebar::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.2); border-radius: 2px; }
        .nav-link.active { background: rgba(197,160,89,0.15); border-left: 3px solid #C5A059; color: #C5A059; }
        .nav-link:hover { background: rgba(255,255,255,0.05); }
        .topic-card { border-left: 4px solid #C5A059; }
        pre { white-space: pre-wrap; word-wrap: break-word; }
        .prompt-container code { font-family: 'Courier New', monospace; }
        
        .prose p { margin-bottom: 1.25rem; line-height: 1.8; font-size: 1.15rem; }
        .prose ul { list-style-type: disc; padding-left: 1.5rem; margin-bottom: 1.25rem; }
        .prose li { margin-bottom: 0.75rem; font-size: 1.15rem; }
        .prose h3 { font-size: 2rem; font-weight: bold; margin-top: 2rem; margin-bottom: 1rem; }
        .prose h3:not([class*="text-"]) { color: #1A1A1A; }
        .prose h4 { font-size: 1.5rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.75rem; }
        .prose h4:not([class*="text-"]) { color: #2C2C2C; }
        
        .two-column { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5rem; margin-top: 1.5rem; }
        .three-column { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 2rem; margin-top: 1.5rem; }
        
        .highlight-box, .warning-box, .key-points {
            background: #F9F9F9;
            border: none;
            border-radius: 10px;
            padding: 2rem;
            margin: 2rem 0;
            border-left: 5px solid #C5A059;
            font-size: 1.1rem;
        }
        .warning-box { border-left-color: #1A1A1A; }
        
        .code-block {
            position: relative;
            font-family: 'Courier New', Courier, monospace;
            background: #1A1A1A;
            color: #F0F0F0;
            padding: 1.75rem;
            border-radius: 8px;
            font-size: 1.05rem;
            margin: 1.75rem 0;
            white-space: pre-wrap;
            line-height: 1.6;
        }
        .copy-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            background: rgba(255,255,255,0.1);
            border: 1px solid rgba(255,255,255,0.2);
            color: #A0A0A0;
            padding: 4px 10px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 0.75rem;
            font-weight: 600;
            transition: all 0.2s;
            text-transform: uppercase;
            z-index: 10;
        }
        .copy-btn:hover { background: #C5A059; color: #1A1A1A; border-color: #C5A059; }
        
        /* Prevent copy button overlap */
        .relative:has(.copy-btn) > p.uppercase { padding-right: 6rem; }
        .relative:has(.copy-btn) > pre.code-block { padding-right: 1rem; padding-top: 1rem; }
        
        @media (max-width: 768px) {
            .two-column, .three-column { grid-template-columns: 1fr; gap: 1.5rem; }
        }

        /* Fix: bg-tempo-800 (#2C2C2C) used as content card backgrounds had dark text invisible on dark bg. */
        .bg-tempo-800 { background-color: #FFFFFF !important; box-shadow: 0 4px 20px rgba(0,0,0,0.03) !important; border: 1px solid rgba(0,0,0,0.05) !important; }
        .hover\:bg-tempo-800:hover { background-color: #F8F9FA !important; }

        /* Legacy Lecture Specific Styles */
        .prompt-var {
            color: #C5A059;
            font-weight: bold;
            background: rgba(197, 160, 89, 0.1);
            padding: 2px 6px;
            border-radius: 4px;
            border-bottom: 2px solid #C5A059;
        }
        .badge {
            display: inline-flex;
            align-items: center;
            padding: 4px 12px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 1rem;
        }
        .badge-theory { background: rgba(72,184,190,0.1); border: 1px solid rgba(72,184,190,0.3); color: #2C8B90; }
        .badge-demo { background: rgba(217, 119, 6, 0.1); border: 1px solid rgba(217, 119, 6, 0.3); color: #B45309; }
        .badge-practice { background: rgba(5, 150, 105, 0.1); border: 1px solid rgba(5, 150, 105, 0.3); color: #047857; }
        .badge-tip { background: rgba(219, 39, 119, 0.1); border: 1px solid rgba(219, 39, 119, 0.3); color: #BE185D; }
    </style>"""

content = re.sub(r'    <script>\s*tailwind\.config = \{.*?</style>', new_head, content, flags=re.DOTALL)

# 2. Body class
content = content.replace('<body class="bg-gray-50">', '<body class="bg-[#F5F5F3] text-lg">')

# 3. Main headings inside sections
content = content.replace('class="text-3xl font-serif font-bold text-white', 'class="text-3xl font-serif font-bold text-tempo-900')

# 4. Glass cards to standard light design (in case any exist)
content = content.replace('class="glass-card p-8 rounded-2xl mb-10"', 'class="mb-10"')

# 5. Prose text colors (gray-400 to gray-700 in old files)
content = content.replace('class="prose max-w-none text-gray-400"', 'class="prose max-w-none text-gray-700"')

# 6. Specific hardcoded text colors in inner elements
content = content.replace('<h4 class="font-bold text-white', '<h4 class="font-bold text-tempo-900')
content = content.replace('<p class="text-gray-400', '<p class="text-gray-600')
content = content.replace('<span class="text-white', '<span class="text-tempo-900')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Migration script for Lecture 6 completed.")
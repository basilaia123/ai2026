# -*- coding: utf-8 -*-
"""
Enrichment script for vanilla_events/day-1-multimodal.html
1. Expands curriculum depth for 2 hours (120 minutes) with rich, professional modules from lecture-6
2. Makes all prompt boxes bilingual (Georgian and English) with tabbed switching
3. Adds a global language toggle (GEO / ENG) in the header
4. Strictly enforces ZERO em-dash (—) and ZERO en-dash (–)
5. Enforces Day / Light Theme high contrast
"""

import sys, re

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Header to add Language Toggle Button and expanded container
old_header_buttons = '''        <div class="flex items-center gap-2 sm:gap-3">
          <button onclick="toggleTheme()" id="theme-toggle-btn" class="day-btn-secondary px-3 py-1.5 rounded-full text-xs border border-brand-goldBorder flex items-center gap-1.5 transition-all" title="თემის გადართვა">
            <span id="theme-icon">☀️</span>
            <span id="theme-text" class="hidden sm:inline font-semibold uppercase text-[10px]">Day</span>
          </button>
          <a href="index.html" class="bronze-outline-btn px-4 py-1.5 rounded-full text-xs uppercase flex items-center gap-1">
            <span>&larr; მთავარი შეთავაზება</span>
          </a>
        </div>'''

new_header_buttons = '''        <div class="flex items-center gap-2 sm:gap-3">
          <!-- Global Language Switcher -->
          <div class="flex items-center sub-surface rounded-full border border-brand-goldBorder p-0.5 text-xs font-semibold">
            <button onclick="switchGlobalLang('en')" id="lang-btn-en" class="px-2.5 py-1 rounded-full text-[11px] font-bold uppercase transition-all bg-brand-gold text-white shadow-sm">
              ENG
            </button>
            <button onclick="switchGlobalLang('ka')" id="lang-btn-ka" class="px-2.5 py-1 rounded-full text-[11px] font-bold uppercase transition-all text-brand-cream/70 hover:text-white">
              GEO
            </button>
          </div>

          <!-- Day / Night Theme Toggle -->
          <button onclick="toggleTheme()" id="theme-toggle-btn" class="day-btn-secondary px-3 py-1.5 rounded-full text-xs border border-brand-goldBorder flex items-center gap-1.5 transition-all" title="თემის გადართვა">
            <span id="theme-icon">☀️</span>
            <span id="theme-text" class="hidden sm:inline font-semibold uppercase text-[10px]">Day</span>
          </button>

          <!-- Back to Hub -->
          <a href="index.html" class="bronze-outline-btn px-4 py-1.5 rounded-full text-xs uppercase flex items-center gap-1">
            <span>&larr; ჰაბი</span>
          </a>
        </div>'''

assert old_header_buttons in html, "Header buttons snippet not found"
html = html.replace(old_header_buttons, new_header_buttons)

# 2. Add Tab CSS to style tag
old_style_end = '''    html.theme-day .bronze-outline-btn:hover {
      color: #916942 !important;
    }
  </style>'''

new_style_end = '''    html.theme-day .bronze-outline-btn:hover {
      color: #916942 !important;
    }

    /* Bilingual Prompt Tabs Styling */
    .prompt-lang-tab {
      cursor: pointer;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.6875rem;
      font-weight: 700;
      letter-spacing: 0.05em;
      text-transform: uppercase;
      transition: all 0.2s ease;
      border: 1px solid rgba(172, 132, 93, 0.35);
      background: transparent;
      color: #8A827E;
    }
    .prompt-lang-tab.active-tab {
      background: #AC845D !important;
      color: #FFFFFF !important;
      border-color: #AC845D !important;
      box-shadow: 0 2px 6px rgba(172, 132, 93, 0.35);
    }
    html.theme-day .prompt-lang-tab {
      color: #6E625B;
      border-color: rgba(172, 132, 93, 0.3);
    }
    html.theme-day .prompt-lang-tab.active-tab {
      background: #AC845D !important;
      color: #FFFFFF !important;
    }

    /* Tab content panes */
    .prompt-pane {
      display: none;
    }
    .prompt-pane.active-pane {
      display: block;
    }

    /* Slide container width expansion */
    .day1-main-container {
      max-width: 1440px !important;
    }
  </style>'''

assert old_style_end in html, "Style end snippet not found"
html = html.replace(old_style_end, new_style_end)

# Also update main container width
html = html.replace(
    '<main class="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-14 space-y-12">',
    '<main class="flex-1 day1-main-container w-full mx-auto px-4 sm:px-6 lg:px-8 py-10 sm:py-14 space-y-12">'
)

print("Step 1 and Step 2 completed.")
with open('vanilla_events/day-1-multimodal.html', 'w', encoding='utf-8') as f:
    f.write(html)

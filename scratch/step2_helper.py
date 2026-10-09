# -*- coding: utf-8 -*-
"""
Bilingual transformation and 2-Hour expansion script for vanilla_events/day-1-multimodal.html
Enriches content with:
- Multi-camera director controls from lecture-6
- High-status Georgian translations for all English prompts
- English versions for all Georgian voiceover scripts
- Tabbed bilingual UI for each prompt box
- Global language sync JS function switchGlobalLang(lang)
- ZERO em-dash (—) and ZERO en-dash (–)
"""

import sys, re

with open('vanilla_events/day-1-multimodal.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Helper function to create bilingual prompt box
def make_bilingual_box(box_id, title, lang_en_content, lang_ka_content, extra_classes=""):
    return f'''<!-- Bilingual Prompt Box: {box_id} -->
<div class="space-y-2 {extra_classes}">
  <div class="flex flex-wrap items-center justify-between gap-2">
    <div class="flex items-center gap-2">
      <span class="text-xs font-bold text-white">{title}</span>
    </div>
    <div class="flex items-center gap-2">
      <!-- Lang Tabs -->
      <div class="inline-flex items-center gap-1 bg-[#141110] p-1 rounded-full border border-brand-goldBorder/40">
        <button onclick="setPromptLang('{box_id}', 'en')" id="tab-{box_id}-en" class="prompt-lang-tab active-tab">EN</button>
        <button onclick="setPromptLang('{box_id}', 'ka')" id="tab-{box_id}-ka" class="prompt-lang-tab">GEO</button>
      </div>
      <!-- Copy Button -->
      <button onclick="copyBilingualPrompt('{box_id}')" id="btn-{box_id}" class="bronze-btn px-3 py-1 rounded-full text-[10px] font-semibold uppercase tracking-wider">
        კოპირება
      </button>
    </div>
  </div>
  <!-- EN Pane -->
  <pre id="{box_id}-en" class="prompt-box prompt-pane active-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-56 overflow-y-auto">{lang_en_content}</pre>
  <!-- KA Pane -->
  <pre id="{box_id}-ka" class="prompt-box prompt-pane p-3 rounded-lg text-[11px] font-mono text-brand-cream/90 whitespace-pre-wrap leading-relaxed max-h-56 overflow-y-auto">{lang_ka_content}</pre>
</div>'''

print("Helper ready")

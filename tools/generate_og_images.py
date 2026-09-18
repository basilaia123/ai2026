#!/usr/bin/env python3
"""
Generates 1200x630 Open Graph (OG) social share preview images
for the 5 domains in the Giorgi Basilaia AI ecosystem using Pillow.
"""

from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OG_WIDTH = 1200
OG_HEIGHT = 630

SITES = [
    {
        "name": "chatgpt",
        "output_path": Path("c:/Users/GBASILAIA/claude/ai2026/chatgpt.ge/og-preview.png"),
        "bg_color": (3, 7, 18),
        "badge_color": (99, 102, 241),
        "badge_text": "AI IN PRACTICE * GIORGI BASILAIA",
        "title": "AI პრაქტიკაში - Generative Intelligence",
        "subtitle": "ChatGPT, Claude, Gemini, Midjourney, Make.com & 40+ Tools",
        "meta": "11 Lectures * 25+ Hours * Corporate Training * chatgpt.ge",
        "accent": (236, 72, 153),
        "icon": "🎓"
    },
    {
        "name": "make",
        "output_path": Path("c:/Users/GBASILAIA/claude/make/og-preview.png"),
        "bg_color": (10, 22, 40),
        "badge_color": (56, 189, 248),
        "badge_text": "NO-CODE AUTOMATION & AI AGENTS",
        "title": "AI ასისტენტები, აგენტები & Make.ge",
        "subtitle": "Make.com, n8n, Model Context Protocol (MCP) & Local LLMs",
        "meta": "7 Sessions * 17.5 Hours * Enterprise Automation * make.ge",
        "accent": (166, 255, 150),
        "icon": "⚡"
    },
    {
        "name": "elevenlabs",
        "output_path": Path("c:/Users/GBASILAIA/claude/ai2026/elevenlabs.ge/og-preview.png"),
        "bg_color": (5, 8, 17),
        "badge_color": (245, 158, 11),
        "badge_text": "VOICE AI & AUDIO PRODUCTION * GEORGIA",
        "title": "ElevenLabs - Voice AI & ხმის კლონირება",
        "subtitle": "Georgian Text-to-Speech, Voice Cloning, Dubbing & Audio Branding",
        "meta": "Georgian Speech Models * AI Agents * elevenlabs.ge",
        "accent": (251, 191, 36),
        "icon": "🎙️"
    },
    {
        "name": "perplexity",
        "output_path": Path("c:/Users/GBASILAIA/claude/ai2026/perplexity.ge/og-preview.png"),
        "bg_color": (6, 13, 23),
        "badge_color": (16, 185, 129),
        "badge_text": "AI SEARCH & DEEP RESEARCH * GEORGIA",
        "title": "Perplexity AI - ჭკვიანი ძიება & კვლევა",
        "subtitle": "Real-time Grounding, Academic Synthesis, Pro Search & Verification",
        "meta": "Verified Citations * Market Intelligence * perplexity.ge",
        "accent": (52, 211, 153),
        "icon": "🔍"
    },
    {
        "name": "basilaia",
        "output_path": Path("c:/Users/GBASILAIA/claude/ai2026/basilaia.com/og-preview.png"),
        "bg_color": (7, 10, 20),
        "badge_color": (236, 72, 153),
        "badge_text": "EXECUTIVE AUTHORITY & AI ADVISORY",
        "title": "გიორგი ბასილაია - Giorgi Basilaia",
        "subtitle": "Associate Professor, Free University of Tbilisi  *  IT Director",
        "meta": "25+ Years Experience  *  3388+ Citations  *  basilaia.com",
        "accent": (99, 102, 241),
        "icon": "🏛️"
    },
    {
        "name": "lovable",
        "output_path": Path("c:/Users/GBASILAIA/claude/ai2026/lovable.ge/og-preview.png"),
        "bg_color": (15, 8, 14),
        "badge_color": (255, 75, 114),
        "badge_text": "VIBE CODING & FULL-STACK AI APPS  *  GEORGIA",
        "title": "Lovable საქართველო - Vibe Coding & AI Apps",
        "subtitle": "Full-Stack Web Apps with React, Tailwind CSS, Supabase & GitHub",
        "meta": "Prompt to App  *  Zero-Code MVPs  *  lovable.ge",
        "accent": (244, 63, 94),
        "icon": "⚡"
    }
]

def create_og_image(site):
    img = Image.new("RGB", (OG_WIDTH, OG_HEIGHT), color=site["bg_color"])
    draw = ImageDraw.Draw(img)

    # 1. Subtle glow circles in background
    accent = site["accent"]
    glow_color = (accent[0] // 5, accent[1] // 5, accent[2] // 5)
    draw.ellipse([800, -100, 1300, 400], fill=glow_color)
    draw.ellipse([-100, 300, 400, 800], fill=(15, 20, 35))

    # 2. Border
    draw.rectangle([16, 16, OG_WIDTH - 16, OG_HEIGHT - 16], outline=(40, 50, 75), width=2)
    # Accent top highlight
    draw.line([16, 16, OG_WIDTH - 16, 16], fill=site["badge_color"], width=4)

    # Fonts
    try:
        font_badge = ImageFont.truetype("arial.ttf", 20)
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arial.ttf", 26)
        font_meta = ImageFont.truetype("arialbd.ttf", 20)
        font_logo = ImageFont.truetype("arialbd.ttf", 28)
    except Exception:
        font_badge = font_title = font_sub = font_meta = font_logo = ImageFont.load_default()

    # 3. Badge Pill
    bx, by = 60, 60
    draw.rounded_rectangle([bx, by, bx + 420, by + 36], radius=8, fill=(site["badge_color"][0] // 4, site["badge_color"][1] // 4, site["badge_color"][2] // 4), outline=site["badge_color"], width=1)
    draw.text((bx + 16, by + 7), site["badge_text"], fill=site["badge_color"], font=font_badge)

    # 4. Main Title
    draw.text((60, 160), site["title"], fill=(248, 250, 252), font=font_title)

    # 5. Subtitle
    draw.text((60, 250), site["subtitle"], fill=(203, 213, 225), font=font_sub)

    # 6. Separator line
    draw.line([60, 380, 1140, 380], fill=(45, 55, 80), width=1)

    # 7. Metadata / Stats Bar
    draw.text((60, 430), site["meta"], fill=site["accent"], font=font_meta)

    # 8. Bottom Brand watermark
    draw.text((60, 530), "BASILAIA AI NETWORK", fill=(148, 163, 184), font=font_logo)
    draw.text((OG_WIDTH - 280, 530), "Georgia * 2026", fill=(100, 116, 139), font=font_logo)

    site["output_path"].parent.mkdir(parents=True, exist_ok=True)
    img.save(site["output_path"], "PNG", optimize=True)
    print(f"Generated: {site['output_path']}")

def main():
    for site in SITES:
        create_og_image(site)

if __name__ == "__main__":
    main()

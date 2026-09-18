#!/usr/bin/env python3
"""
AEO & GEO Toolkit
Audits, validates, and verifies AEO (Answer Engine Optimization) & GEO (Generative Engine Optimization)
assets across the Giorgi Basilaia AI ecosystem:
- chatgpt.ge
- make.ge
- elevenlabs.ge
- perplexity.ge
- basilaia.com
"""

import os
import sys
import re
import json
from pathlib import Path

REQUIRED_AI_BOTS = [
    "OAI-SearchBot",
    "ChatGPT-User",
    "GPTBot",
    "PerplexityBot",
    "ClaudeBot",
    "Claude-SearchBot",
    "Google-Extended",
    "Applebot-Extended",
    "Meta-ExternalAgent"
]

DOMAINS = [
    {
        "domain": "chatgpt.ge",
        "path": Path("c:/Users/GBASILAIA/claude/ai2026/chatgpt.ge"),
        "html_files": ["index.html", "corporate-training.html"]
    },
    {
        "domain": "make.ge",
        "path": Path("c:/Users/GBASILAIA/claude/make"),
        "html_files": ["index.html"]
    },
    {
        "domain": "elevenlabs.ge",
        "path": Path("c:/Users/GBASILAIA/claude/ai2026/elevenlabs.ge"),
        "html_files": ["index.html"]
    },
    {
        "domain": "perplexity.ge",
        "path": Path("c:/Users/GBASILAIA/claude/ai2026/perplexity.ge"),
        "html_files": ["index.html"]
    },
    {
        "domain": "basilaia.com",
        "path": Path("c:/Users/GBASILAIA/claude/ai2026/basilaia.com"),
        "html_files": ["index.html"]
    },
    {
        "domain": "lovable.ge",
        "path": Path("c:/Users/GBASILAIA/claude/ai2026/lovable.ge"),
        "html_files": ["index.html"]
    }
]

def audit_domain(target):
    domain = target["domain"]
    base_path = target["path"]
    results = {
        "domain": domain,
        "robots_txt": False,
        "robots_bots_covered": [],
        "llms_txt": False,
        "llms_full_txt": False,
        "sitemap_xml": False,
        "html_alternate_llms": [],
        "schema_sameas_count": 0,
        "issues": []
    }

    if not base_path.exists():
        results["issues"].append(f"Directory not found: {base_path}")
        return results

    # 1. robots.txt
    robots_path = base_path / "robots.txt"
    if robots_path.exists():
        results["robots_txt"] = True
        content = robots_path.read_text(encoding="utf-8", errors="ignore")
        for bot in REQUIRED_AI_BOTS:
            if bot.lower() in content.lower():
                results["robots_bots_covered"].append(bot)
        if "sitemap:" not in content.lower():
            results["issues"].append("robots.txt missing Sitemap directive")
    else:
        results["issues"].append("Missing robots.txt")

    # 2. llms.txt
    llms_path = base_path / "llms.txt"
    if llms_path.exists():
        results["llms_txt"] = True
        content = llms_path.read_text(encoding="utf-8", errors="ignore")
        if not content.strip().startswith("#"):
            results["issues"].append("llms.txt does not start with # H1 title")
    else:
        results["issues"].append("Missing llms.txt")

    # 3. llms-full.txt
    llms_full_path = base_path / "llms-full.txt"
    if llms_full_path.exists():
        results["llms_full_txt"] = True
    else:
        results["issues"].append("Missing llms-full.txt")

    # 4. sitemap.xml
    sitemap_path = base_path / "sitemap.xml"
    if sitemap_path.exists():
        results["sitemap_xml"] = True
    else:
        results["issues"].append("Missing sitemap.xml")

    # 5. HTML checks
    for html_file in target["html_files"]:
        file_path = base_path / html_file
        if not file_path.exists():
            continue
        html = file_path.read_text(encoding="utf-8", errors="ignore")
        if 'rel="alternate"' in html and 'llms.txt' in html:
            results["html_alternate_llms"].append(html_file)
        # Check schema sameAs
        matches = re.findall(r'"sameAs"\s*:\s*\[([^\]]+)\]', html)
        if matches:
            results["schema_sameas_count"] += 1

    return results

def main():
    print("=" * 60)
    print("AEO & GEO Comprehensive Ecosystem Audit")
    print("=" * 60)

    total_score = 0
    max_possible = len(DOMAINS) * 100

    for item in DOMAINS:
        res = audit_domain(item)
        domain = res["domain"]
        score = 0

        if res["robots_txt"]: score += 20
        bot_coverage_ratio = len(res["robots_bots_covered"]) / len(REQUIRED_AI_BOTS)
        score += int(bot_coverage_ratio * 20)
        if res["llms_txt"]: score += 20
        if res["llms_full_txt"]: score += 15
        if res["sitemap_xml"]: score += 15
        if res["html_alternate_llms"]: score += 10

        total_score += score

        print(f"\n[Domain] {domain}")
        print(f"  Score: {score}/100")
        print(f"  robots.txt: {'OK' if res['robots_txt'] else 'FAIL'} (AI Bots: {len(res['robots_bots_covered'])}/{len(REQUIRED_AI_BOTS)})")
        print(f"  llms.txt: {'OK' if res['llms_txt'] else 'FAIL'}")
        print(f"  llms-full.txt: {'OK' if res['llms_full_txt'] else 'FAIL'}")
        print(f"  sitemap.xml: {'OK' if res['sitemap_xml'] else 'FAIL'}")
        print(f"  HTML <link rel=alternate>: {res['html_alternate_llms']}")
        print(f"  Schema sameAs: {res['schema_sameas_count']} found")
        if res["issues"]:
            print("  Issues:")
            for issue in res["issues"]:
                print(f"    - {issue}")

    overall_pct = (total_score / max_possible) * 100
    print("\n" + "=" * 60)
    print(f"Overall Ecosystem AEO Readiness: {overall_pct:.1f}%")
    print("=" * 60)

if __name__ == "__main__":
    main()

---
name: aeo-geo-optimizer
description: >-
  Audits, optimizes, and generates Answer Engine Optimization (AEO) and Generative Engine
  Optimization (GEO) assets for websites, including llms.txt, AI crawler robots.txt,
  entity-first JSON-LD schemas, SpeakableSpecification, and Princeton GEO-bench content patterns.
---

# AEO & GEO Optimizer Skill

This skill provides operational standards, checklist criteria, and automated audit methods for **Answer Engine Optimization (AEO)** and **Generative Engine Optimization (GEO)**.

## Core Objectives
1. Maximize visibility, citations, and accurate brand representation in AI Answer Engines:
   - ChatGPT Search & GPTBot
   - Perplexity AI & PerplexityBot
   - Google Gemini & Google AI Overviews
   - Claude Search & ClaudeBot
   - Apple Intelligence & Applebot
2. Maintain machine-readable standards (`llms.txt` and `llms-full.txt`).
3. Ensure zero-shot retrieval accuracy for LLM scrapers.

---

## 1. The `llms.txt` Standard (llmstxt.org)

Every domain must expose:
- `/llms.txt`: Token-efficient Markdown summary (~500–1,500 tokens).
  - `# <Brand / Domain>`
  - `> <1–2 sentence authoritative elevator pitch>`
  - Core navigation links with descriptive 1-sentence explanations.
  - Key factual anchors (Founder/Instructor, stats, credentials, pricing).
- `/llms-full.txt`: Comprehensive single-file Markdown document containing full syllabus, course descriptions, packages, FAQ, and background.

---

## 2. AI Crawler `robots.txt` Configuration

Ensure explicit `Allow: /` directives for:
- `OAI-SearchBot` (ChatGPT real-time search)
- `ChatGPT-User` (User on-demand web browsing)
- `GPTBot` (OpenAI model training & knowledge retrieval)
- `PerplexityBot` (Perplexity AI real-time search & citation)
- `ClaudeBot` & `Claude-SearchBot` (Anthropic AI retrieval)
- `Google-Extended` (Google Gemini training & overview retrieval)
- `Applebot-Extended` (Apple Intelligence)
- `Meta-ExternalAgent` (Meta AI)

Always append:
- Reference comments to `/llms.txt` and `/llms-full.txt`
- Canonical pointer to `Sitemap: https://<domain>/sitemap.xml`

---

## 3. Princeton GEO-bench Optimization Formula (+40% Citation Boost)

According to empirical research (KDD 2024 / Princeton University, Allen Institute):
1. **Statistics Addition:** High density of verifiable quantitative metrics (e.g. 25+ years experience, 3388+ citations, 14 scientific papers, 40+ tools, 7 sessions, +40% productivity).
2. **Quotation Addition:** Authoritative direct quotes from identified subject matter experts.
3. **Cite Sources:** Attribution to trusted third-party profiles (Google Scholar, LinkedIn, university affiliations).
4. **Direct Answer / TL;DR Blocks:** 40–60 word high-density factual answers directly beneath `<h2>` headers for zero-shot RAG retrieval.
5. **Entity Disambiguation:** Clear naming conventions (e.g., "Giorgi Basilaia", "Smart Academy", "Free University of Tbilisi").

---

## 4. In-Page Discovery & Schema Enhancements

In the `<head>` of HTML documents:
```html
<link rel="alternate" type="text/markdown" href="/llms.txt" title="AI Machine-Readable Summary">
<link rel="alternate" type="text/markdown" href="/llms-full.txt" title="AI Full Knowledge Context">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1">
```

In `JSON-LD`:
- Cross-domain entity linkage via `sameAs`.
- `SpeakableSpecification` pointing to quick-facts CSS selectors.
- `DefinedTerm` objects for domain concepts.

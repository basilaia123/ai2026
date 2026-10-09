# -*- coding: utf-8 -*-
import sys
import json
import re

sys.stdout.reconfigure(encoding='utf-8')

html_content = '''<!DOCTYPE html>
<html lang="ka">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EU4Dialogue | დღე 1: AI საფუძვლები, საგრანტო ციკლი & პროექტების მართვა (ინტერაქტიული სლაიდები & პოსტ-კურს გაიდები)</title>
  <meta name="description" content="EU4Dialogue Civic AI & Project Management Bootcamp - დღე 1-ის სრული ინტერაქტიული საპრეზენტაციო სლაიდები (37 სლაიდი, 4 მოდული, 10 სამაგიდო გაიდი კურსის შემდგომი გამოყენებისთვის).">
  
  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/gh/Loopple/FiraGO@1.0/cdn/FiraGO.css" rel="stylesheet">

  <style>
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    :root {
      --brand-blue: #005a9c;
      --brand-blue-hover: #004d85;
      --brand-blue-light: rgba(0, 90, 156, 0.08);
      --pm-emerald: #059669;
      --pm-emerald-light: rgba(16, 185, 129, 0.1);
      --accent-purple: #7c3aed;
      --accent-purple-light: rgba(124, 58, 237, 0.1);
      --accent-amber: #d97706;
      --accent-amber-light: rgba(217, 119, 6, 0.1);
      
      --bg-canvas: #0f172a;
      --bg-slide: #ffffff;
      --bg-subtle: #f8fafc;
      --bg-card: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-light: #94a3b8;
      --border-subtle: #e2e8f0;
      --border-card: #cbd5e1;
      
      --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.06);
      --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.12);
      --shadow-lg: 0 20px 40px rgba(0, 0, 0, 0.22);
      
      --radius-sm: 8px;
      --radius-md: 12px;
      --radius-lg: 18px;
      --radius-xl: 24px;
      
      --transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
    }

    body.night-mode {
      --bg-canvas: #020617;
      --bg-slide: #0b1329;
      --bg-subtle: #131d38;
      --bg-card: #182344;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-light: #64748b;
      --border-subtle: rgba(255, 255, 255, 0.1);
      --border-card: rgba(255, 255, 255, 0.16);
      --brand-blue: #38bdf8;
      --brand-blue-hover: #0284c7;
      --brand-blue-light: rgba(56, 189, 248, 0.15);
      --pm-emerald: #34d399;
      --pm-emerald-light: rgba(52, 211, 153, 0.15);
      --accent-purple: #c084fc;
      --accent-purple-light: rgba(192, 132, 252, 0.15);
    }

    body {
      font-family: 'FiraGO', 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      background: var(--bg-canvas);
      color: var(--text-main);
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      user-select: none;
    }

    /* TOP HEADER & CONTROLS */
    .deck-header {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 60px;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 20px;
      z-index: 1000;
      color: #ffffff;
    }

    .header-left {
      display: flex;
      align-items: center;
      gap: 14px;
    }

    .header-logo {
      display: flex;
      align-items: center;
      gap: 8px;
      font-weight: 800;
      font-size: 0.92rem;
      letter-spacing: -0.01em;
      text-decoration: none;
      color: #ffffff;
    }

    .header-logo span.badge {
      background: #005a9c;
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 800;
    }

    .header-module-tag {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.18);
      padding: 4px 10px;
      border-radius: 12px;
      font-size: 0.75rem;
      font-weight: 700;
      color: #cbd5e1;
      display: none;
    }

    @media (min-width: 768px) {
      .header-module-tag {
        display: inline-block;
      }
    }

    .header-center {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .slide-counter {
      font-size: 0.85rem;
      font-weight: 700;
      color: #e2e8f0;
      background: rgba(255, 255, 255, 0.08);
      padding: 4px 12px;
      border-radius: 20px;
      border: 1px solid rgba(255, 255, 255, 0.12);
    }

    .header-right {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .ctrl-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #ffffff;
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 0.95rem;
      transition: var(--transition);
      text-decoration: none;
    }

    .ctrl-btn:hover {
      background: rgba(255, 255, 255, 0.2);
      border-color: rgba(255, 255, 255, 0.35);
      transform: translateY(-1px);
    }

    .ctrl-btn:active {
      transform: scale(0.96);
    }

    /* TOP PROGRESS BAR */
    .progress-bar-container {
      position: fixed;
      top: 60px;
      left: 0;
      right: 0;
      height: 3px;
      background: rgba(255, 255, 255, 0.08);
      z-index: 999;
    }

    .progress-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #005a9c, #10b981, #7c3aed);
      width: 0%;
      transition: width 0.3s ease;
    }

    /* VIEWPORT & STAGE */
    .stage {
      flex: 1;
      margin-top: 63px;
      margin-bottom: 70px;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      min-height: calc(100vh - 133px);
    }

    .slide-viewport {
      width: 100%;
      max-width: 1180px;
      min-height: 640px;
      background: var(--bg-slide);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow-lg);
      border: 1px solid var(--border-subtle);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      position: relative;
      animation: slideIn 0.35s ease;
      user-select: text;
    }

    @keyframes slideIn {
      from {
        opacity: 0;
        transform: translateY(8px) scale(0.99);
      }
      to {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }

    /* SLIDE INNER STRUCTURE */
    .slide-header {
      padding: 24px 36px 14px 36px;
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 20px;
      background: linear-gradient(180deg, var(--bg-subtle) 0%, transparent 100%);
    }

    .slide-meta-row {
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
      margin-bottom: 6px;
    }

    .slide-pill {
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 3px 10px;
      border-radius: 12px;
      background: var(--brand-blue-light);
      color: var(--brand-blue);
      border: 1px solid rgba(0, 90, 156, 0.2);
    }

    .slide-pill.green {
      background: var(--pm-emerald-light);
      color: var(--pm-emerald);
      border-color: rgba(16, 185, 129, 0.25);
    }

    .slide-pill.purple {
      background: var(--accent-purple-light);
      color: var(--accent-purple);
      border-color: rgba(124, 58, 237, 0.25);
    }

    .slide-pill.amber {
      background: var(--accent-amber-light);
      color: var(--accent-amber);
      border-color: rgba(217, 119, 6, 0.25);
    }

    .slide-timing {
      font-size: 0.76rem;
      font-weight: 700;
      color: var(--text-muted);
    }

    .slide-title {
      font-size: clamp(1.35rem, 2.6vw, 1.85rem);
      font-weight: 900;
      color: var(--text-main);
      line-height: 1.25;
      letter-spacing: -0.015em;
    }

    .slide-subtitle {
      font-size: clamp(0.85rem, 1.4vw, 0.96rem);
      color: var(--text-muted);
      margin-top: 4px;
      line-height: 1.5;
    }

    .slide-badge-num {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      color: var(--brand-blue);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      font-weight: 900;
      flex-shrink: 0;
    }

    .slide-body {
      flex: 1;
      padding: 26px 36px 32px 36px;
      overflow-y: auto;
      max-height: 650px;
    }

    /* GUIDE BANNER & CARDS (POST-COURSE PLAYBOOK) */
    .guide-banner {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 12px 18px;
      border-radius: var(--radius-md);
      background: linear-gradient(90deg, rgba(0, 90, 156, 0.08) 0%, rgba(16, 185, 129, 0.08) 100%);
      border: 1px solid rgba(0, 90, 156, 0.25);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--brand-blue);
      margin-bottom: 18px;
    }

    body.night-mode .guide-banner {
      background: linear-gradient(90deg, rgba(56, 189, 248, 0.12) 0%, rgba(52, 211, 153, 0.12) 100%);
      border-color: rgba(56, 189, 248, 0.3);
      color: #38bdf8;
    }

    .guide-banner .guide-tag {
      background: #005a9c;
      color: #ffffff;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.72rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      flex-shrink: 0;
    }

    body.night-mode .guide-banner .guide-tag {
      background: #0284c7;
    }

    .guide-box {
      background: var(--bg-card);
      border: 1.5px solid rgba(0, 90, 156, 0.25);
      border-radius: var(--radius-md);
      padding: 20px;
      box-shadow: var(--shadow-sm);
      transition: var(--transition);
      position: relative;
    }

    .guide-box:hover {
      border-color: var(--brand-blue);
      box-shadow: var(--shadow-md);
    }

    .guide-box-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-subtle);
    }

    .guide-step-row {
      display: flex;
      align-items: flex-start;
      gap: 12px;
      margin-bottom: 12px;
    }

    .guide-step-num {
      width: 26px;
      height: 26px;
      border-radius: 50%;
      background: var(--brand-blue);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 800;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .guide-step-body {
      flex: 1;
      font-size: 0.85rem;
      line-height: 1.55;
      color: var(--text-main);
    }

    .guide-step-body strong {
      display: block;
      color: var(--text-main);
      margin-bottom: 2px;
      font-size: 0.88rem;
    }

    .checklist-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 10px;
      margin-top: 12px;
    }

    .checklist-item {
      background: var(--bg-subtle);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 10px 14px;
      display: flex;
      align-items: flex-start;
      gap: 10px;
      font-size: 0.82rem;
      line-height: 1.5;
    }

    .checklist-item .check-icon {
      color: var(--pm-emerald);
      font-weight: 900;
      flex-shrink: 0;
      margin-top: 1px;
    }

    /* GRID LAYOUTS INSIDE SLIDES */
    .grid-2col {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
    }

    .grid-3col {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }

    .grid-4col {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
    }

    /* CARDS & CONTAINERS INSIDE SLIDES */
    .card-box {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: var(--radius-md);
      padding: 20px;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      position: relative;
      transition: var(--transition);
    }

    .card-box:hover {
      border-color: var(--brand-blue);
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }

    .card-box-header {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 12px;
    }

    .card-icon {
      font-size: 1.35rem;
      line-height: 1;
    }

    .card-title {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      line-height: 1.3;
    }

    .card-desc {
      font-size: 0.88rem;
      color: var(--text-muted);
      line-height: 1.6;
    }

    .bullet-list {
      list-style: none;
      margin-top: 10px;
    }

    .bullet-list li {
      position: relative;
      padding-left: 20px;
      font-size: 0.86rem;
      color: var(--text-main);
      line-height: 1.55;
      margin-bottom: 8px;
    }

    .bullet-list li::before {
      content: "•";
      position: absolute;
      left: 4px;
      color: var(--brand-blue);
      font-size: 1.2rem;
      line-height: 1;
      top: 0;
    }

    .bullet-list li strong {
      color: var(--text-main);
    }

    /* HIGHLIGHT & CALLOUT BOXES */
    .callout-box {
      background: var(--bg-subtle);
      border-left: 4px solid var(--brand-blue);
      border-radius: 0 var(--radius-md) var(--radius-md) 0;
      padding: 14px 18px;
      margin: 14px 0;
      font-size: 0.88rem;
      line-height: 1.6;
      color: var(--text-main);
    }

    .callout-box.green {
      border-left-color: var(--pm-emerald);
      background: var(--pm-emerald-light);
    }

    .callout-box.purple {
      border-left-color: var(--accent-purple);
      background: var(--accent-purple-light);
    }

    .callout-box.amber {
      border-left-color: var(--accent-amber);
      background: var(--accent-amber-light);
    }

    /* PROMPT CODE BOX */
    .prompt-snippet {
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: var(--radius-md);
      padding: 16px;
      margin: 14px 0;
      position: relative;
      color: #e2e8f0;
    }

    .prompt-snippet-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
      padding-bottom: 8px;
      border-bottom: 1px solid #1e293b;
      font-size: 0.75rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .prompt-copy-btn {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 0.72rem;
      font-weight: 700;
      cursor: pointer;
      transition: var(--transition);
    }

    .prompt-copy-btn:hover {
      background: var(--pm-emerald);
      border-color: var(--pm-emerald);
    }

    .prompt-text {
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
      font-size: 0.82rem;
      line-height: 1.5;
      white-space: pre-wrap;
      word-break: break-word;
      color: #cbd5e1;
    }

    /* SLIDO LIVE POLL MOCKUP */
    .slido-box {
      background: linear-gradient(135deg, rgba(16, 185, 129, 0.06) 0%, rgba(0, 90, 156, 0.08) 100%);
      border: 2px dashed rgba(16, 185, 129, 0.35);
      border-radius: var(--radius-lg);
      padding: 22px;
      margin: 16px 0;
      display: flex;
      align-items: center;
      gap: 20px;
    }

    .slido-qr-frame {
      width: 110px;
      height: 110px;
      background: #ffffff;
      border-radius: 12px;
      padding: 8px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--border-subtle);
      box-shadow: var(--shadow-sm);
      flex-shrink: 0;
      text-align: center;
    }

    .slido-qr-code {
      width: 76px;
      height: 76px;
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 3px;
      margin-bottom: 4px;
    }

    .slido-qr-dot {
      background: #0f172a;
      border-radius: 2px;
    }

    .slido-qr-dot.accent {
      background: var(--pm-emerald);
    }

    .slido-content {
      flex: 1;
      min-width: 0;
    }

    .slido-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: #10b981;
      color: #ffffff;
      padding: 3px 10px;
      border-radius: 12px;
      font-size: 0.74rem;
      font-weight: 800;
      margin-bottom: 8px;
    }

    .slido-question {
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 6px;
      line-height: 1.35;
    }

    .slido-options {
      display: flex;
      flex-direction: column;
      gap: 6px;
      margin-top: 10px;
    }

    .slido-option-item {
      background: var(--bg-card);
      border: 1px solid var(--border-subtle);
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 0.82rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: var(--text-main);
    }

    /* WORKSHOP HANDS-ON CARD */
    .workshop-card {
      background: linear-gradient(180deg, rgba(0, 90, 156, 0.05) 0%, rgba(16, 185, 129, 0.05) 100%);
      border: 1.5px solid rgba(0, 90, 156, 0.25);
      border-radius: var(--radius-lg);
      padding: 22px;
      margin: 16px 0;
    }

    .workshop-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 14px;
      padding-bottom: 10px;
      border-bottom: 1px solid var(--border-subtle);
    }

    .workshop-title {
      font-size: 1.1rem;
      font-weight: 800;
      color: var(--brand-blue);
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .workshop-duration {
      font-size: 0.78rem;
      font-weight: 800;
      color: var(--text-muted);
      background: var(--bg-card);
      padding: 4px 10px;
      border-radius: 12px;
      border: 1px solid var(--border-subtle);
    }

    /* STEP PIPELINE */
    .step-pipeline {
      display: flex;
      align-items: center;
      gap: 12px;
      margin: 16px 0;
      overflow-x: auto;
      padding-bottom: 4px;
    }

    .step-node {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: var(--radius-md);
      padding: 14px 16px;
      min-width: 170px;
      flex: 1;
      text-align: center;
    }

    .step-num {
      width: 24px;
      height: 24px;
      background: var(--brand-blue);
      color: #ffffff;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.72rem;
      font-weight: 800;
      margin: 0 auto 6px auto;
    }

    .step-title {
      font-size: 0.85rem;
      font-weight: 800;
      color: var(--text-main);
      margin-bottom: 4px;
    }

    .step-desc {
      font-size: 0.75rem;
      color: var(--text-muted);
      line-height: 1.4;
    }

    .step-arrow {
      color: var(--text-muted);
      font-size: 1.1rem;
      font-weight: 800;
      flex-shrink: 0;
    }

    /* TABLE IN SLIDES */
    .slide-table-wrapper {
      width: 100%;
      overflow-x: auto;
      margin: 14px 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-subtle);
    }

    .slide-table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.84rem;
    }

    .slide-table th {
      background: var(--bg-subtle);
      padding: 12px 14px;
      font-weight: 800;
      color: var(--text-main);
      border-bottom: 1px solid var(--border-subtle);
      text-transform: uppercase;
      font-size: 0.74rem;
      letter-spacing: 0.04em;
    }

    .slide-table td {
      padding: 12px 14px;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-muted);
      vertical-align: top;
    }

    .slide-table tr:last-child td {
      border-bottom: none;
    }

    .slide-table td strong {
      color: var(--text-main);
    }

    /* BOTTOM CONTROLS DOCK */
    .deck-footer {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 70px;
      background: rgba(15, 23, 42, 0.92);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-top: 1px solid rgba(255, 255, 255, 0.1);
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0 24px;
      z-index: 1000;
      color: #ffffff;
    }

    .footer-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .footer-btn {
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #ffffff;
      padding: 8px 16px;
      border-radius: 10px;
      font-size: 0.84rem;
      font-weight: 700;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: var(--transition);
      text-decoration: none;
      min-height: 40px;
    }

    .footer-btn:hover {
      background: rgba(255, 255, 255, 0.2);
      border-color: rgba(255, 255, 255, 0.35);
    }

    .footer-btn.primary {
      background: #005a9c;
      border-color: #005a9c;
    }

    .footer-btn.primary:hover {
      background: #0284c7;
    }

    .footer-btn:disabled {
      opacity: 0.35;
      cursor: not-allowed;
      pointer-events: none;
    }

    .footer-center {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .keyboard-hint {
      font-size: 0.72rem;
      color: #94a3b8;
      display: none;
    }

    @media (min-width: 900px) {
      .keyboard-hint {
        display: block;
      }
    }

    .keyboard-badge {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(255, 255, 255, 0.2);
      padding: 2px 6px;
      border-radius: 4px;
      font-family: monospace;
      color: #e2e8f0;
      margin: 0 2px;
    }

    .footer-right {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    /* SLIDE OVERVIEW DRAWER / MODAL */
    .overview-drawer {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      z-index: 2000;
      display: none;
      flex-direction: column;
      padding: 30px;
      overflow-y: auto;
    }

    .overview-drawer.active {
      display: flex;
    }

    .overview-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 24px;
      color: #ffffff;
    }

    .overview-title {
      font-size: 1.4rem;
      font-weight: 900;
    }

    .overview-close-btn {
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #ffffff;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 1.2rem;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .overview-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 16px;
    }

    .overview-item {
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.12);
      border-radius: var(--radius-md);
      padding: 16px;
      cursor: pointer;
      transition: var(--transition);
      color: #e2e8f0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 120px;
    }

    .overview-item:hover, .overview-item.current {
      background: rgba(0, 90, 156, 0.4);
      border-color: #38bdf8;
      transform: translateY(-2px);
    }

    .overview-item-num {
      font-size: 0.74rem;
      font-weight: 800;
      color: #94a3b8;
      margin-bottom: 6px;
    }

    .overview-item-title {
      font-size: 0.88rem;
      font-weight: 800;
      line-height: 1.35;
      color: #ffffff;
    }

    .overview-item-mod {
      font-size: 0.72rem;
      color: #38bdf8;
      margin-top: 10px;
      font-weight: 700;
    }

    /* RESPONSIVENESS */
    @media (max-width: 768px) {
      .stage {
        padding: 10px;
        margin-top: 55px;
        margin-bottom: 65px;
        min-height: calc(100vh - 120px);
      }
      .slide-viewport {
        min-height: 520px;
        border-radius: var(--radius-lg);
      }
      .slide-header {
        padding: 18px 20px 12px 20px;
      }
      .slide-body {
        padding: 18px 20px;
      }
      .grid-2col, .grid-3col, .grid-4col {
        grid-template-columns: 1fr;
        gap: 14px;
      }
      .step-pipeline {
        flex-direction: column;
        align-items: stretch;
      }
      .step-arrow {
        transform: rotate(90deg);
        text-align: center;
        margin: -4px 0;
      }
      .slido-box {
        flex-direction: column;
        align-items: flex-start;
        gap: 14px;
      }
      .deck-footer {
        padding: 0 14px;
        height: 65px;
      }
      .footer-btn {
        padding: 6px 12px;
        font-size: 0.78rem;
      }
    }
  </style>
</head>
<body>

  <!-- HEADER -->
  <header class="deck-header">
    <div class="header-left">
      <a href="index.html" class="header-logo" title="EU4Dialogue PM შეთავაზებაზე დაბრუნება">
        <span>🇪🇺 🇺🇳 EU4Dialogue</span>
        <span class="badge">Bootcamp</span>
      </a>
      <span class="header-module-tag" id="headerModuleTag">მოდული 1: AI Fundamentals</span>
    </div>

    <div class="header-center">
      <div class="slide-counter" id="slideCounter">სლაიდი 1 / 37</div>
    </div>

    <div class="header-right">
      <button class="ctrl-btn" onclick="toggleOverview()" title="ყველა სლაიდის გადახედვა (O)" aria-label="სლაიდების სია">🗂️</button>
      <button class="ctrl-btn" onclick="toggleFullscreen()" title="სრული ეკრანი (F)" aria-label="სრული ეკრანი">⛶</button>
      <button class="ctrl-btn" onclick="toggleTheme()" title="დღის/ღამის რეჟიმი" aria-label="თემა">🌓</button>
      <a href="index.html" class="ctrl-btn" title="მთავარ გვერდზე დაბრუნება" aria-label="მთავარი">🏠</a>
    </div>
  </header>

  <!-- PROGRESS BAR -->
  <div class="progress-bar-container">
    <div class="progress-bar-fill" id="progressBar"></div>
  </div>

  <!-- STAGE / VIEWPORT -->
  <main class="stage">
    <div class="slide-viewport" id="slideViewport">
      <!-- Slides are injected/rendered dynamically by JS below -->
    </div>
  </main>

  <!-- FOOTER CONTROLS -->
  <footer class="deck-footer">
    <div class="footer-left">
      <button class="footer-btn" id="prevBtn" onclick="prevSlide()" disabled>← წინა</button>
      <button class="footer-btn primary" id="nextBtn" onclick="nextSlide()">შემდეგი →</button>
    </div>

    <div class="footer-center">
      <div class="keyboard-hint">
        გამოიყენეთ <span class="keyboard-badge">←</span> <span class="keyboard-badge">→</span> კლავიშები, <span class="keyboard-badge">Space</span> ან <span class="keyboard-badge">O</span> გადახედვისთვის
      </div>
    </div>

    <div class="footer-right">
      <button class="footer-btn" onclick="toggleOverview()">სლაიდების სია</button>
    </div>
  </footer>

  <!-- OVERVIEW DRAWER -->
  <div class="overview-drawer" id="overviewDrawer">
    <div class="overview-header">
      <div>
        <div class="overview-title">დღე 1: სლაიდები & პოსტ-კურს გაიდები</div>
        <div style="font-size: 0.85rem; color: #94a3b8; margin-top: 4px;">დააკლიკეთ სასურველ სლაიდზე ან სამაგიდო გაიდზე მყისიერი გადასვლისთვის</div>
      </div>
      <button class="overview-close-btn" onclick="toggleOverview()">✕</button>
    </div>
    <div class="overview-grid" id="overviewGrid">
      <!-- Injected by JS -->
    </div>
  </div>

  <!-- SLIDES DATA SCRIPT INJECTION POINT -->
  <script>
'''

print("Writing generator script...")

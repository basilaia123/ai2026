# Concept: Real-Time Voice Agents
- **Category:** Conversational AI 🎙️
- **Tag:** Voice-first, Realtime, OPPA terminals, Georgian STT/TTS
- **Georgian Description:** Real-Time Voice Agents — WebRTC-ზე დაფუძნებული, ~200ms latency-ით მომუშავე ხმოვანი AI-ასისტენტი, რომელიც streaming STT → LLM (function-calling) → TTS-ს ახორციელებს. OPPA-სთვის განკუთვნილია PayBox-ის ტერმინალებზე (Touch UI-ის ხმოვანი ალტერნატივა ხანდაზმული და შეზღუდული მომხმარებლებისთვის).
- **English Description:** Real-Time Voice Agents run over WebRTC with ~200ms latency, streaming STT → LLM (with function calling) → TTS. For OPPA: replace PowerBox touch UI for elderly/disabled users; supports Georgian via Whisper STT.
- **Sessions:** [[Session 6 - Lovable & Prod]]
- **Related Tools:** [[Tool - ChatGPT OpenAI]], [[Tool - Gemini Google]], [[Tool - ElevenLabs]], [[Tool - Notion MCP Server]]
- **Related Concepts:** [[Concept - Prompt Formula & Self-Critique]], [[Concept - PII Compliance & Security]]
- **Link:** [OpenAI Realtime Docs](https://platform.openai.com/docs/guides/realtime)

## რა არის Real-Time Voice Agent?
Real-Time Voice Agents — ეს არ არის "STT → LLM → TTS" 3-ეტაპიანი pipeline (როგორც Stage I-ის Make.com Whisper + Claude + ElevenLabs). ეს არის **streaming, low-latency (~200ms), interruption-aware, function-calling-იანი** პროტოკოლი, რომელიც WebRTC-ზე მუშაობს. AI-ს შეუძლია **შეწყვიტოს** მომხმარებელი, **დაელოდოს**, **გადაამუშავოს** intent-ი — როგორც ცოცხალ ადამიანს.

## 4 ლიდერი Provider 2025–2026

| Provider | API | Georgian STT/TTS | Latency | Tools | OPPA რეკომ. |
|---|---|---|---|---|---|
| **OpenAI** | Realtime (gpt-realtime + whisper-1 + TTS-1) | ✅ Whisper (ka) | ~200ms | ✅ Native | ⭐ Stage I |
| **Google** | Gemini Live (gemini-2.5-flash-native-audio) | ✅ Chirp 3 HD | ~250ms | ✅ Native | ⭐ ეკონომიური |
| **Anthropic** | (no native) + ElevenLabs TTS | ⚠️ Hybrid | ~600ms | ✅ Compos. | ⚠️ Late |
| **ElevenLabs** | Conversational AI v2 | ⚠️ Best voice | ~300ms | ✅ Native | Voice UX |

## OPPA PayBox Voice Assistant — კონცეფცია
PayBox-ის 8,000+ ტერმინალს ემატება 🎙️ Voice Mode, სადაც მომხმარებელი ქართულად ეუბნება AI-ს რა გადახდა სურს:

1. **Wake Word / Button** — "გამარჯობა" ან "ნინა"
2. **STT** — Whisper-1 (Whisper Georgian language="ka")
3. **LLM Brain** — GPT-Realtime + Function Tools (5 endpoints: lookup_biller, prepare_payment, check_balance, cancel_transaction, escalate_to_operator)
4. **UI Sync** — Function call-ის output → WebSocket → PayBox React screen
5. **TTS Stream** — Real-time ხმოვანი პასუხი ქართულად

## Voice Flow Example
- 🧑 "გამარჯობა, ენერგო პროს დენის გადახდა მინდა 60 ლარით"
- 🤖 "კარგი. ენერგო პრო, 60 ლარი. აბონენტის ნომერი?"
- 🧑 "12345678"
- 🤖 "ენერგო პრო 12345678, 60 ლარი. დაადასტურეთ ეკრანზე."
- [Function Call: prepare_payment → OPPA API → UI Sync → Payment Confirmation Screen]

## Safety Guardrails (NBG Compliance)
1. 🔒 **PII Filter** — ბარათის ნომერი, PIN, CVV არ წარმოითქვამს (Touch only)
2. 🔒 **Max Amount 100₾** — ხმით; ზემოთ Touch + PIN
3. 🔒 **Voice Biometrics** — voice embedding hash → OPPA Auth (Stage II)
4. 🔒 **Sensitive Flow Lock** — ბარათის დამატება / ტრანზაქციის გაუქმება → Touch UI
5. 🔒 **Audit Log** — ყველა session → JSONL → NBG audit storage

## OPPA Use Cases
| # | Use Case | Priority | Stage |
|---|---|---|---|
| 1 | კომუნალური Voice Pay (ენერგო პრო, GPB, წყალი) | ⭐⭐⭐ | I (Pilot) |
| 2 | 24/7 Support Triage Voice (PayBox-ის client-ები) | ⭐⭐⭐ | I |
| 3 | Accessibility Mode (ხანდაზმული, შშმ) | ⭐⭐ | I |
| 4 | Merchant Onboarding Voice (KYC) | ⭐⭐ | I → II |
| 5 | Operator Assist (call center auto-summary) | ⭐ | II |
| 6 | Multi-language (az, ru, hy) | ⭐ | II |

## ROI Projection

| მეტრიკა | Touch-only | Voice+Touch | Δ |
|---|---|---|---|
| საშ. გადახდის დრო | 34 წმ | 6 წმ | -82% |
| User errors / session | 1.8 | 0.3 | -83% |
| ხანდაზმული satisfaction (1-5) | 2.7 | 4.4 | +63% |
| Operator calls (terminal stuck) | 8/დღეში | 2/დღეში | -75% |
| Cost per terminal/თვე | $0 | ~$0.90 | +$0.90 |
| Volume capacity/terminal/დღე | 85 transactions | 210 transactions | +147% |

**Break-even**: ~8 თვე · **Scale**: 40+ terminals-დან

## ლაივ დემო Tools
- **Realtime Console** (zero setup) — https://platform.openai.com/audio/realtime/edit
- **Function Tools schema** — Stage I-ში: lookup_biller, prepare_payment, check_balance
- **Lovable UI** — React PayBox Voice-Ready UI (seg-voice.md prompt)
- **Make.com Hybrid** — Whisper STT → Claude API → ElevenLabs TTS (~2-3s latency, but already-built)

## Stage II-ისთვის
- Wake-word detection (Porcupine / Kaldi)
- Voice biometrics (voice embedding → OPPA Auth)
- Multi-language support (az, ru, hy)
- ElevenLabs Georgian voice clone (marketing-grade)
- NBG regulation: voice payment limit ≤100₾
- Offline mode (basic intents on-device Android shell)
- A/B test Voice vs Touch conversion rate

## Cross-Reference
- 📚 Session 6, SEG 7 (Real-Time Voice Agents) — სრული არქიტექტურა + კოდი
- 🎓 Session 6 Day6 Exercises #16, #17 — hands-on Voice Console test + safety design
- 📊 Slide 7 in day6-summary — Voice Agents + ROI table

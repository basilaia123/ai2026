/**
 * Groq Qwen 3.8 + Whisper Large V3 Turbo Edge Worker
 * Serverless Edge Voice Transcription & Real-Time AI Chat
 */

const DEFAULT_CHAT_MODEL = "qwen/qwen3.8-27b";
const DEFAULT_AUDIO_MODEL = "whisper-large-v3-turbo";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;
    const apiKey = env.GROQ_API_KEY;

    // CORS preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type, Authorization",
        },
      });
    }

    // 1. API: Audio Transcription (/api/transcribe & /v1/audio/transcriptions)
    if ((path === "/api/transcribe" || path === "/v1/audio/transcriptions") && request.method === "POST") {
      if (!apiKey) {
        return Response.json({ error: "GROQ_API_KEY is not configured" }, { status: 500 });
      }

      try {
        const formData = await request.formData();
        
        // Ensure default model if not provided
        if (!formData.get("model")) {
          formData.set("model", DEFAULT_AUDIO_MODEL);
        }

        const groqRes = await fetch("https://api.groq.com/openai/v1/audio/transcriptions", {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${apiKey}`,
          },
          body: formData,
        });

        const data = await groqRes.json();
        return Response.json(data, {
          status: groqRes.status,
          headers: { "Access-Control-Allow-Origin": "*" },
        });
      } catch (err) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // 2. API: Streaming Chat Completion (/api/chat & /v1/chat/completions)
    if ((path === "/api/chat" || path === "/v1/chat/completions") && request.method === "POST") {
      if (!apiKey) {
        return Response.json({ error: "GROQ_API_KEY is not configured" }, { status: 500 });
      }

      try {
        const body = await request.json();
        const model = body.model || env.DEFAULT_MODEL || DEFAULT_CHAT_MODEL;
        const messages = body.messages || [];
        const isStream = body.stream !== false;

        const groqPayload = {
          model: model,
          messages: messages,
          temperature: body.temperature ?? 0.7,
          max_tokens: body.max_tokens ?? 4096,
          stream: isStream,
        };

        const groqRes = await fetch("https://api.groq.com/openai/v1/chat/completions", {
          method: "POST",
          headers: {
            "Authorization": `Bearer ${apiKey}`,
            "Content-Type": "application/json",
          },
          body: JSON.stringify(groqPayload),
        });

        if (!groqRes.ok) {
          const errText = await groqRes.text();
          return new Response(errText, {
            status: groqRes.status,
            headers: { "Content-Type": "application/json", "Access-Control-Allow-Origin": "*" },
          });
        }

        if (isStream) {
          return new Response(groqRes.body, {
            headers: {
              "Content-Type": "text/event-stream; charset=utf-8",
              "Cache-Control": "no-cache",
              "Connection": "keep-alive",
              "Access-Control-Allow-Origin": "*",
            },
          });
        } else {
          const data = await groqRes.json();
          return Response.json(data, {
            headers: { "Access-Control-Allow-Origin": "*" },
          });
        }
      } catch (err) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // 3. API: Info
    if (path === "/api/info") {
      return Response.json({
        service: "Groq Voice + Qwen AI Edge Worker",
        models: {
          chat: DEFAULT_CHAT_MODEL,
          audio: DEFAULT_AUDIO_MODEL,
        },
        edgeColo: request.cf?.colo || "UNKNOWN",
        country: request.cf?.country || "UNKNOWN",
        status: "active",
      });
    }

    // 4. Web UI
    return new Response(APP_HTML, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "no-cache",
      },
    });
  },
};

const APP_HTML = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Groq Edge AI • Qwen 3.8 + Whisper Turbo</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
  <style>
    :root {
      --bg: #090d16;
      --sidebar: #0f172a;
      --card-bg: #131d33;
      --border: #1e293b;
      --accent: #f55036;
      --accent-glow: rgba(245, 80, 54, 0.25);
      --green: #10b981;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --font-mono: 'JetBrains Mono', monospace;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      height: 100vh;
      display: flex;
      overflow: hidden;
    }
    aside {
      width: 290px;
      background: var(--sidebar);
      border-right: 1px solid var(--border);
      display: flex;
      flex-direction: column;
      padding: 20px 16px;
      flex-shrink: 0;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      margin-bottom: 20px;
    }
    .brand-logo {
      width: 32px;
      height: 32px;
      background: linear-gradient(135deg, #f55036, #ff8c42);
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      color: #fff;
    }
    .brand-text h2 { font-size: 15px; font-weight: 800; }
    .brand-text p { font-size: 11px; color: var(--text-muted); }
    .nav-tabs {
      display: flex;
      gap: 6px;
      background: #090d16;
      padding: 4px;
      border-radius: 8px;
      margin-bottom: 16px;
    }
    .nav-tab {
      flex: 1;
      background: none;
      border: none;
      color: var(--text-muted);
      font-size: 12px;
      font-weight: 600;
      padding: 8px;
      border-radius: 6px;
      cursor: pointer;
      transition: 0.15s;
    }
    .nav-tab.active {
      background: var(--card-bg);
      color: #fff;
      box-shadow: 0 2px 8px rgba(0,0,0,0.4);
    }
    .presets-label {
      font-size: 11px;
      font-weight: 700;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-bottom: 8px;
    }
    .preset-btn {
      background: #1e293b;
      border: 1px solid #334155;
      color: var(--text);
      font-size: 13px;
      font-weight: 500;
      padding: 10px 12px;
      border-radius: 8px;
      text-align: left;
      cursor: pointer;
      margin-bottom: 8px;
      transition: all 0.15s;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .preset-btn:hover, .preset-btn.active {
      background: rgba(245, 80, 54, 0.15);
      border-color: var(--accent);
      color: #fff;
    }
    .sidebar-footer {
      margin-top: auto;
      padding-top: 16px;
      border-top: 1px solid var(--border);
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.6;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.15);
      color: var(--green);
      font-size: 11px;
      font-weight: 600;
      padding: 4px 8px;
      border-radius: 6px;
      margin-top: 6px;
    }
    main {
      flex: 1;
      display: flex;
      flex-direction: column;
      height: 100vh;
      position: relative;
    }
    header {
      padding: 14px 24px;
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: rgba(9, 13, 22, 0.8);
      backdrop-filter: blur(8px);
    }
    .header-info { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; }
    .model-tag {
      background: #1e293b;
      border: 1px solid #334155;
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 4px 8px;
      border-radius: 6px;
      color: #38bdf8;
    }
    .speed-tag {
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent);
    }
    /* Tab views */
    .tab-content {
      display: none;
      flex: 1;
      flex-direction: column;
      overflow-y: auto;
    }
    .tab-content.active {
      display: flex;
    }
    .chat-container {
      flex: 1;
      overflow-y: auto;
      padding: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }
    .msg {
      max-width: 800px;
      width: 100%;
      margin: 0 auto;
      display: flex;
      gap: 14px;
      line-height: 1.6;
    }
    .msg.user { justify-content: flex-end; }
    .msg-avatar {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 700;
      font-size: 13px;
      flex-shrink: 0;
    }
    .msg.user .msg-avatar { display: none; }
    .msg.assistant .msg-avatar { background: linear-gradient(135deg, #f55036, #ff8c42); color: #fff; }
    .msg-body {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 16px 20px;
      font-size: 14px;
    }
    .msg.user .msg-body {
      background: #1e293b;
      border-color: #334155;
      max-width: 80%;
    }
    .msg-body pre {
      background: #090d16;
      border: 1px solid #1e2638;
      border-radius: 8px;
      padding: 12px;
      overflow-x: auto;
      margin: 10px 0;
      font-family: var(--font-mono);
      font-size: 13px;
    }
    .msg-body code {
      font-family: var(--font-mono);
      background: #090d16;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 12px;
      color: #fca5a5;
    }
    .msg-body pre code { background: none; padding: 0; color: inherit; }
    .input-section {
      padding: 16px 24px 24px;
      max-width: 850px;
      width: 100%;
      margin: 0 auto;
    }
    .input-box {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 10px 14px;
      display: flex;
      gap: 10px;
      align-items: flex-end;
      box-shadow: 0 10px 30px rgba(0,0,0,0.4);
      transition: border-color 0.2s;
    }
    .input-box:focus-within { border-color: var(--accent); }
    textarea {
      flex: 1;
      background: none;
      border: none;
      color: var(--text);
      font-family: var(--font-sans);
      font-size: 14px;
      resize: none;
      min-height: 24px;
      max-height: 180px;
      outline: none;
      line-height: 1.5;
    }
    .icon-btn {
      background: #1e293b;
      border: 1px solid #334155;
      color: var(--text);
      border-radius: 8px;
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .icon-btn:hover { background: #334155; }
    .icon-btn.recording {
      background: #dc2626 !important;
      border-color: #ef4444 !important;
      animation: micPulse 1.5s infinite;
    }
    @keyframes micPulse {
      0%, 100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.4); }
      50% { transform: scale(1.08); box-shadow: 0 0 0 10px rgba(239, 68, 68, 0); }
    }
    .send-btn {
      background: var(--accent);
      color: #fff;
      border: none;
      border-radius: 8px;
      width: 36px;
      height: 36px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      flex-shrink: 0;
      transition: all 0.15s;
    }
    .send-btn:hover { filter: brightness(1.1); transform: scale(1.05); }
    .send-btn:disabled { opacity: 0.5; cursor: not-allowed; }
    /* Audio Transcribe Tab */
    .audio-view {
      max-width: 800px;
      width: 100%;
      margin: 30px auto;
      padding: 0 20px;
    }
    .dropzone {
      background: var(--card-bg);
      border: 2px dashed #334155;
      border-radius: 16px;
      padding: 40px 20px;
      text-align: center;
      cursor: pointer;
      transition: 0.2s;
    }
    .dropzone:hover, .dropzone.dragover {
      border-color: var(--accent);
      background: rgba(245, 80, 54, 0.05);
    }
    .dropzone h3 { font-size: 18px; margin-bottom: 6px; }
    .dropzone p { color: var(--text-muted); font-size: 13px; }
    .transcribe-card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 20px;
      margin-top: 20px;
      display: none;
    }
    .transcribe-text {
      background: #090d16;
      border: 1px solid #1e2638;
      border-radius: 8px;
      padding: 16px;
      font-size: 14px;
      line-height: 1.6;
      max-height: 250px;
      overflow-y: auto;
      margin-bottom: 16px;
      white-space: pre-wrap;
    }
    .transcribe-actions {
      display: flex;
      gap: 10px;
      justify-content: flex-end;
    }
    .btn {
      background: var(--accent);
      color: #fff;
      border: none;
      font-size: 13px;
      font-weight: 600;
      padding: 8px 16px;
      border-radius: 8px;
      cursor: pointer;
    }
    .btn.secondary { background: #1e293b; border: 1px solid #334155; }
    @media(max-width: 768px) { aside { display: none; } }
  </style>
</head>
<body>
  <aside>
    <div class="brand">
      <div class="brand-logo">Q</div>
      <div class="brand-text">
        <h2>Groq AI Edge</h2>
        <p>Qwen 3.8 + Whisper Turbo</p>
      </div>
    </div>

    <div class="nav-tabs">
      <button class="nav-tab active" id="tabChatBtn" onclick="switchTab('chat')">💬 Chat</button>
      <button class="nav-tab" id="tabAudioBtn" onclick="switchTab('audio')">🎙️ Audio Files</button>
    </div>

    <div class="presets-label">Prompt Presets</div>
    <button class="preset-btn active" onclick="setPreset('general')">
      <span>🤖</span> General Assistant
    </button>
    <button class="preset-btn" onclick="setPreset('georgian')">
      <span>🇬🇪</span> ქართული რედაქტორი
    </button>
    <button class="preset-btn" onclick="setPreset('coder')">
      <span>💻</span> Coding Expert
    </button>
    <button class="preset-btn" onclick="setPreset('summarizer')">
      <span>⚡</span> Summarize & Extract
    </button>

    <div class="sidebar-footer">
      <div>LLM: <strong>qwen/qwen3.8-27b</strong></div>
      <div>Voice: <strong>whisper-large-v3-turbo</strong></div>
      <div>Engine: <strong>Groq LPU Edge</strong></div>
      <div class="badge">● Cloudflare Edge Active</div>
    </div>
  </aside>

  <main>
    <header>
      <div class="header-info">
        <span class="model-tag">qwen3.8-27b</span>
        <span class="model-tag" style="color: #a78bfa;">whisper-v3-turbo</span>
        <span class="speed-tag" id="speedTag">Ready</span>
      </div>
      <div>
        <button class="preset-btn" style="padding: 6px 12px; margin: 0;" onclick="clearChat()">Clear Chat</button>
      </div>
    </header>

    <!-- Chat Tab View -->
    <div class="tab-content active" id="chatTab">
      <div class="chat-container" id="chatBox">
        <div class="msg assistant">
          <div class="msg-avatar">Q</div>
          <div class="msg-body">
            <p>Hello! I am <strong>Qwen 3.8</strong> integrated with <strong>Whisper Large V3 Turbo</strong> on Groq. You can type or click the <strong>🎙️ mic button</strong> to speak in Georgian, English, or any language!</p>
          </div>
        </div>
      </div>

      <div class="input-section">
        <div class="input-box">
          <button class="icon-btn" id="micBtn" onclick="toggleVoiceRecording()" title="Click to speak (Whisper Turbo)">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
          </button>
          <textarea id="promptInput" rows="1" placeholder="Type a message or click 🎙️ to talk..." onkeydown="handleKeyDown(event)" oninput="autoResize(this)"></textarea>
          <button class="send-btn" id="sendBtn" onclick="sendMessage()">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Audio Files Tab View -->
    <div class="tab-content" id="audioTab">
      <div class="audio-view">
        <div class="dropzone" id="audioDropzone" onclick="document.getElementById('fileInput').click()">
          <input type="file" id="fileInput" accept="audio/*" style="display:none" onchange="handleFileSelect(this)">
          <div style="font-size: 40px; margin-bottom: 12px;">🎙️</div>
          <h3>Upload Audio File for Whisper Turbo Transcription</h3>
          <p>Drag & drop MP3, WAV, M4A, WEBM, or FLAC (Transcribed in milliseconds on Groq)</p>
        </div>

        <div class="transcribe-card" id="transcribeCard">
          <h3 style="margin-bottom: 12px;">Transcription Result</h3>
          <div class="transcribe-text" id="transcribeResult">Transcribing audio with Whisper Turbo...</div>
          <div class="transcribe-actions">
            <button class="btn secondary" onclick="copyTranscription()">📋 Copy Text</button>
            <button class="btn" onclick="sendTranscriptionToChat()">💬 Send to Qwen 3.8 Chat</button>
          </div>
        </div>
      </div>
    </div>
  </main>

  <script>
    let messages = [];
    let systemPrompt = "You are a helpful, precise, and extremely knowledgeable AI assistant powered by Qwen 3.8 and Groq.";
    let isGenerating = false;
    let mediaRecorder = null;
    let audioChunks = [];
    let isRecording = false;

    const PRESETS = {
      general: "You are a helpful, precise, and extremely knowledgeable AI assistant powered by Qwen 3.8 and Groq.",
      georgian: "შენ ხარ ქართული ენის ექსპერტი, რედაქტორი და კორექტორი. შეასწორე გრამატიკული, სინტაქსური და სტილისტური შეცდომები, შეინარჩუნე ბუნებრივი და აკადემიური ტონი.",
      coder: "You are a world-class senior software architect. Provide clean, production-ready code with explanations and best practices.",
      summarizer: "You are an expert synthesizer. Provide ultra-clear bulleted summaries and extract key insights concisely."
    };

    function switchTab(tab) {
      document.querySelectorAll('.nav-tab').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));

      if (tab === 'chat') {
        document.getElementById('tabChatBtn').classList.add('active');
        document.getElementById('chatTab').classList.add('active');
      } else {
        document.getElementById('tabAudioBtn').classList.add('active');
        document.getElementById('audioTab').classList.add('active');
      }
    }

    function setPreset(name) {
      document.querySelectorAll('.preset-btn').forEach(b => b.classList.remove('active'));
      if (event && event.currentTarget) event.currentTarget.classList.add('active');
      systemPrompt = PRESETS[name] || PRESETS.general;
    }

    function autoResize(el) {
      el.style.height = 'auto';
      el.style.height = Math.min(el.scrollHeight, 180) + 'px';
    }

    function handleKeyDown(e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        sendMessage();
      }
    }

    function clearChat() {
      messages = [];
      document.getElementById('chatBox').innerHTML = \`
        <div class="msg assistant">
          <div class="msg-avatar">Q</div>
          <div class="msg-body"><p>Chat cleared. Ready for your next query!</p></div>
        </div>\`;
      document.getElementById('speedTag').innerText = 'Ready';
    }

    // Voice Recording with Whisper
    async function toggleVoiceRecording() {
      const micBtn = document.getElementById('micBtn');

      if (isRecording) {
        // Stop recording
        mediaRecorder.stop();
        isRecording = false;
        micBtn.classList.remove('recording');
        document.getElementById('speedTag').innerText = 'Transcribing voice with Whisper Turbo...';
      } else {
        // Start recording
        try {
          const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
          audioChunks = [];
          mediaRecorder = new MediaRecorder(stream);

          mediaRecorder.ondataavailable = (e) => {
            if (e.data.size > 0) audioChunks.push(e.data);
          };

          mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
            await transcribeAudioBlob(audioBlob);
            stream.getTracks().forEach(track => track.stop());
          };

          mediaRecorder.start();
          isRecording = true;
          micBtn.classList.add('recording');
          document.getElementById('speedTag').innerText = '🎙️ Listening... (Click mic to stop)';
        } catch (err) {
          alert('Microphone access error: ' + err.message);
        }
      }
    }

    async function transcribeAudioBlob(blob) {
      const formData = new FormData();
      formData.append('file', blob, 'voice.webm');
      formData.append('model', 'whisper-large-v3-turbo');

      const start = performance.now();
      try {
        const res = await fetch('/api/transcribe', {
          method: 'POST',
          body: formData,
        });

        const data = await res.json();
        const duration = ((performance.now() - start) / 1000).toFixed(2);

        if (data.text) {
          const input = document.getElementById('promptInput');
          input.value = (input.value ? input.value + ' ' : '') + data.text;
          autoResize(input);
          document.getElementById('speedTag').innerText = 'Transcribed in ' + duration + 's (Whisper Turbo)';
        } else {
          document.getElementById('speedTag').innerText = 'No speech detected';
        }
      } catch (err) {
        document.getElementById('speedTag').innerText = 'Transcription failed';
      }
    }

    // Audio File Upload
    async function handleFileSelect(input) {
      if (!input.files || !input.files[0]) return;
      const file = input.files[0];
      const card = document.getElementById('transcribeCard');
      const resultBox = document.getElementById('transcribeResult');
      
      card.style.display = 'block';
      resultBox.innerText = 'Uploading and transcribing ' + file.name + ' with Whisper Turbo...';

      const formData = new FormData();
      formData.append('file', file);
      formData.append('model', 'whisper-large-v3-turbo');

      const start = performance.now();
      try {
        const res = await fetch('/api/transcribe', {
          method: 'POST',
          body: formData,
        });
        const data = await res.json();
        const duration = ((performance.now() - start) / 1000).toFixed(2);

        if (data.text) {
          resultBox.innerText = data.text;
          document.getElementById('speedTag').innerText = 'Audio file transcribed in ' + duration + 's';
        } else {
          resultBox.innerText = 'Error: ' + JSON.stringify(data);
        }
      } catch (err) {
        resultBox.innerText = 'Failed to transcribe: ' + err.message;
      }
    }

    function copyTranscription() {
      const text = document.getElementById('transcribeResult').innerText;
      navigator.clipboard.writeText(text);
      alert('Transcription copied to clipboard!');
    }

    function sendTranscriptionToChat() {
      const text = document.getElementById('transcribeResult').innerText;
      switchTab('chat');
      const input = document.getElementById('promptInput');
      input.value = text;
      autoResize(input);
      input.focus();
    }

    // Chat Logic
    async function sendMessage() {
      if (isGenerating) return;
      const input = document.getElementById('promptInput');
      const text = input.value.trim();
      if (!text) return;

      input.value = '';
      input.style.height = 'auto';

      messages.push({ role: 'user', content: text });
      appendMessage('user', text);

      const assistantDiv = appendMessage('assistant', '');
      const bodyEl = assistantDiv.querySelector('.msg-body');
      const speedTag = document.getElementById('speedTag');
      speedTag.innerText = 'Connecting to Groq...';

      isGenerating = true;
      document.getElementById('sendBtn').disabled = true;

      const payloadMessages = [{ role: 'system', content: systemPrompt }, ...messages];
      const startTime = performance.now();
      let fullText = '';
      let tokenCount = 0;

      try {
        const response = await fetch('/api/chat', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            model: 'qwen/qwen3.8-27b',
            messages: payloadMessages,
            stream: true,
          }),
        });

        if (!response.ok) {
          const err = await response.json();
          bodyEl.innerHTML = '<span style="color:var(--accent);">Error: ' + (err.error || response.statusText) + '</span>';
          return;
        }

        const reader = response.body.getReader();
        const decoder = new TextDecoder();
        let buffer = '';

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;

          buffer += decoder.decode(value, { stream: true });
          const lines = buffer.split('\\n');
          buffer = lines.pop();

          for (const line of lines) {
            const clean = line.trim();
            if (!clean.startsWith('data:')) continue;
            const jsonStr = clean.replace(/^data:\s*/, '');
            if (jsonStr === '[DONE]') continue;

            try {
              const parsed = JSON.parse(jsonStr);
              const delta = parsed.choices[0]?.delta?.content || '';
              if (delta) {
                fullText += delta;
                tokenCount++;
                bodyEl.innerHTML = marked.parse(fullText);
                scrollToBottom();

                const elapsed = (performance.now() - startTime) / 1000;
                const speed = Math.round(tokenCount / Math.max(elapsed, 0.1));
                speedTag.innerText = speed + ' tokens/sec';
              }
            } catch (e) {}
          }
        }

        messages.push({ role: 'assistant', content: fullText });
        const totalDuration = ((performance.now() - startTime) / 1000).toFixed(2);
        speedTag.innerText = 'Completed in ' + totalDuration + 's (' + Math.round(tokenCount / totalDuration) + ' t/s)';
      } catch (err) {
        bodyEl.innerHTML = '<span style="color:var(--accent);">Fetch error: ' + err.message + '</span>';
      } finally {
        isGenerating = false;
        document.getElementById('sendBtn').disabled = false;
      }
    }

    function appendMessage(role, content) {
      const chatBox = document.getElementById('chatBox');
      const div = document.createElement('div');
      div.className = 'msg ' + role;
      if (role === 'assistant') {
        div.innerHTML = '<div class="msg-avatar">Q</div><div class="msg-body">' + (content ? marked.parse(content) : '<span style="color:var(--text-muted);">Thinking...</span>') + '</div>';
      } else {
        div.innerHTML = '<div class="msg-body">' + escapeHtml(content) + '</div>';
      }
      chatBox.appendChild(div);
      scrollToBottom();
      return div;
    }

    function scrollToBottom() {
      const chatBox = document.getElementById('chatBox');
      chatBox.scrollTop = chatBox.scrollHeight;
    }

    function escapeHtml(str) {
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }
  </script>
</body>
</html>`;

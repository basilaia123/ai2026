export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const pathname = url.pathname;

    // 1. Plain text ping endpoint: /ping
    if (pathname === "/ping") {
      return new Response("pong", {
        status: 200,
        headers: {
          "Content-Type": "text/plain; charset=utf-8",
          "Cache-Control": "no-store, no-cache, must-revalidate",
          "X-Edge-Colo": request.cf?.colo || "UNKNOWN",
        },
      });
    }

    // 2. Health check endpoint: /health
    if (pathname === "/health") {
      return Response.json(
        {
          status: "healthy",
          timestamp: new Date().toISOString(),
          uptime: "ok",
          colo: request.cf?.colo || "DEV",
        },
        {
          headers: {
            "Cache-Control": "no-store",
            "Access-Control-Allow-Origin": "*",
          },
        }
      );
    }

    // 3. API Ping endpoint: /api/ping
    if (pathname === "/api/ping" || url.searchParams.get("format") === "json") {
      return Response.json(
        {
          message: "pong",
          timestamp: Date.now(),
          isoTime: new Date().toISOString(),
          edge: {
            colo: request.cf?.colo || "LOCAL",
            city: request.cf?.city || "Unknown",
            country: request.cf?.country || "Unknown",
            continent: request.cf?.continent || "Unknown",
            asn: request.cf?.asOrganization || "Unknown",
            tlsVersion: request.cf?.tlsVersion || "N/A",
            httpProtocol: request.cf?.httpProtocol || "HTTP/2",
          },
          client: {
            ip: request.headers.get("CF-Connecting-IP") || "127.0.0.1",
            userAgent: request.headers.get("user-agent") || "Unknown",
          },
        },
        {
          headers: {
            "Content-Type": "application/json",
            "Cache-Control": "no-store",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
          },
        }
      );
    }

    // 4. Interactive Ping App UI (Home page)
    const html = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Edge Ping App • Cloudflare Workers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090d16;
      --card-bg: #111827;
      --card-border: #1f293d;
      --accent: #f38020; /* Cloudflare orange */
      --accent-glow: rgba(243, 128, 32, 0.25);
      --green: #10b981;
      --text: #f3f4f6;
      --text-muted: #9ca3af;
      --font-mono: 'JetBrains Mono', monospace;
      --font-sans: 'Inter', sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 40px 16px;
    }
    .container {
      max-width: 680px;
      width: 100%;
    }
    header {
      text-align: center;
      margin-bottom: 30px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(16, 185, 129, 0.15);
      border: 1px solid rgba(16, 185, 129, 0.3);
      color: var(--green);
      font-size: 12px;
      font-weight: 600;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 12px;
    }
    .pulse-dot {
      width: 8px;
      height: 8px;
      background: var(--green);
      border-radius: 50%;
      animation: pulse 2s infinite;
    }
    @keyframes pulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.8); }
    }
    h1 {
      font-size: 28px;
      font-weight: 700;
      letter-spacing: -0.5px;
      margin-bottom: 6px;
      background: linear-gradient(135deg, #fff, #9ca3af);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    header p {
      color: var(--text-muted);
      font-size: 14px;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 24px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.4);
      margin-bottom: 20px;
    }
    .rtt-display {
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 24px 0;
      border-bottom: 1px solid var(--card-border);
      margin-bottom: 20px;
    }
    .rtt-value {
      font-family: var(--font-mono);
      font-size: 56px;
      font-weight: 700;
      color: var(--accent);
      line-height: 1;
      margin-bottom: 8px;
    }
    .rtt-label {
      font-size: 13px;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: var(--text-muted);
    }
    .controls {
      display: flex;
      gap: 12px;
      justify-content: center;
      margin-bottom: 20px;
    }
    button {
      background: var(--accent);
      color: #fff;
      border: none;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 600;
      padding: 12px 24px;
      border-radius: 10px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.15s ease;
      box-shadow: 0 4px 14px var(--accent-glow);
    }
    button:hover {
      transform: translateY(-1px);
      filter: brightness(1.1);
    }
    button:active {
      transform: translateY(1px);
    }
    button.secondary {
      background: #1e293b;
      color: var(--text);
      box-shadow: none;
      border: 1px solid #334155;
    }
    button.secondary.active {
      background: #dc2626;
      border-color: #ef4444;
      color: #fff;
    }
    .stats-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-bottom: 20px;
    }
    .stat-box {
      background: #0d121f;
      border: 1px solid #1e2638;
      border-radius: 10px;
      padding: 12px;
      text-align: center;
    }
    .stat-num {
      font-family: var(--font-mono);
      font-size: 18px;
      font-weight: 700;
      color: #e5e7eb;
    }
    .stat-lbl {
      font-size: 11px;
      color: var(--text-muted);
      margin-top: 4px;
    }
    .chart-container {
      height: 90px;
      background: #0d121f;
      border: 1px solid #1e2638;
      border-radius: 10px;
      padding: 8px;
      position: relative;
      margin-bottom: 20px;
    }
    canvas {
      width: 100%;
      height: 100%;
    }
    .details-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 12px;
    }
    .detail-item {
      background: #0d121f;
      border: 1px solid #1e2638;
      border-radius: 8px;
      padding: 12px 14px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 13px;
    }
    .detail-item span:first-child {
      color: var(--text-muted);
    }
    .detail-item span:last-child {
      font-family: var(--font-mono);
      color: #60a5fa;
      font-weight: 500;
    }
    .endpoints-card {
      font-size: 13px;
    }
    .endpoints-card h3 {
      font-size: 14px;
      font-weight: 600;
      margin-bottom: 12px;
      color: var(--text);
    }
    .code-block {
      background: #0d121f;
      border: 1px solid #1e2638;
      border-radius: 8px;
      padding: 10px 14px;
      font-family: var(--font-mono);
      font-size: 12px;
      color: #a78bfa;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .code-block code {
      word-break: break-all;
    }
    .tag {
      font-size: 10px;
      background: #1e293b;
      color: #94a3b8;
      padding: 2px 6px;
      border-radius: 4px;
      margin-left: 8px;
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="badge"><div class="pulse-dot"></div> Edge Worker Operational</div>
      <h1>Cloudflare Ping App</h1>
      <p>Measure real-time global edge latency & network health</p>
    </header>

    <div class="card">
      <div class="rtt-display">
        <div class="rtt-value" id="rttDisplay">-- ms</div>
        <div class="rtt-label" id="rttStatus">Ready to Ping</div>
      </div>

      <div class="controls">
        <button id="pingBtn" onclick="triggerPing()">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
          Ping Edge
        </button>
        <button class="secondary" id="autoBtn" onclick="toggleAutoPing()">
          Auto Ping (1s)
        </button>
      </div>

      <div class="stats-row">
        <div class="stat-box">
          <div class="stat-num" id="statMin">--</div>
          <div class="stat-lbl">MIN RTT</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" id="statAvg">--</div>
          <div class="stat-lbl">AVG RTT</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" id="statMax">--</div>
          <div class="stat-lbl">MAX RTT</div>
        </div>
        <div class="stat-box">
          <div class="stat-num" id="statCount">0</div>
          <div class="stat-lbl">PACKETS</div>
        </div>
      </div>

      <div class="chart-container">
        <canvas id="pingChart"></canvas>
      </div>

      <div class="details-grid">
        <div class="detail-item">
          <span>Edge Datacenter:</span>
          <span id="edgeColo">${request.cf?.colo || "TBS"} (${request.cf?.city || "Tbilisi"})</span>
        </div>
        <div class="detail-item">
          <span>Country / Region:</span>
          <span id="edgeCountry">${request.cf?.country || "GE"}</span>
        </div>
        <div class="detail-item">
          <span>Client IP:</span>
          <span id="clientIp">${request.headers.get("CF-Connecting-IP") || "127.0.0.1"}</span>
        </div>
        <div class="detail-item">
          <span>HTTP Protocol:</span>
          <span id="httpProto">${request.cf?.httpProtocol || "HTTP/2"}</span>
        </div>
      </div>
    </div>

    <div class="card endpoints-card">
      <h3>Available API Endpoints</h3>
      <div class="code-block">
        <code>GET /ping</code>
        <span class="tag">Plain Text "pong"</span>
      </div>
      <div class="code-block">
        <code>GET /api/ping</code>
        <span class="tag">Full JSON Telemetry</span>
      </div>
      <div class="code-block">
        <code>GET /health</code>
        <span class="tag">Health Check JSON</span>
      </div>
    </div>
  </div>

  <script>
    const history = [];
    let autoInterval = null;
    const canvas = document.getElementById('pingChart');
    const ctx = canvas.getContext('2d');

    function resizeCanvas() {
      canvas.width = canvas.parentElement.clientWidth - 16;
      canvas.height = canvas.parentElement.clientHeight - 16;
      drawChart();
    }
    window.addEventListener('resize', resizeCanvas);
    setTimeout(resizeCanvas, 50);

    async function triggerPing() {
      const btn = document.getElementById('pingBtn');
      const start = performance.now();
      document.getElementById('rttStatus').innerText = 'Pinging...';

      try {
        const res = await fetch('/api/ping?t=' + Date.now());
        const duration = Math.round(performance.now() - start);
        const data = await res.json();

        document.getElementById('rttDisplay').innerText = duration + ' ms';
        document.getElementById('rttStatus').innerText = 'Pong received from ' + data.edge.colo;
        
        if (data.edge) {
          document.getElementById('edgeColo').innerText = data.edge.colo + ' (' + data.edge.city + ')';
          document.getElementById('edgeCountry').innerText = data.edge.country;
          document.getElementById('clientIp').innerText = data.client.ip;
          document.getElementById('httpProto').innerText = data.edge.httpProtocol;
        }

        recordStat(duration);
      } catch (err) {
        document.getElementById('rttStatus').innerText = 'Ping failed';
      }
    }

    function recordStat(ms) {
      history.push(ms);
      if (history.length > 30) history.shift();

      const min = Math.min(...history);
      const max = Math.max(...history);
      const avg = Math.round(history.reduce((a, b) => a + b, 0) / history.length);

      document.getElementById('statMin').innerText = min + ' ms';
      document.getElementById('statMax').innerText = max + ' ms';
      document.getElementById('statAvg').innerText = avg + ' ms';
      document.getElementById('statCount').innerText = history.length;

      drawChart();
    }

    function drawChart() {
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      if (history.length < 2) return;

      const maxVal = Math.max(...history, 100);
      ctx.strokeStyle = '#f38020';
      ctx.lineWidth = 2;
      ctx.beginPath();

      history.forEach((val, i) => {
        const x = (i / (Math.max(history.length - 1, 1))) * w;
        const y = h - (val / maxVal) * (h - 10) - 5;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.stroke();

      // Points
      history.forEach((val, i) => {
        const x = (i / (Math.max(history.length - 1, 1))) * w;
        const y = h - (val / maxVal) * (h - 10) - 5;
        ctx.fillStyle = '#f38020';
        ctx.beginPath();
        ctx.arc(x, y, 3, 0, Math.PI * 2);
        ctx.fill();
      });
    }

    function toggleAutoPing() {
      const btn = document.getElementById('autoBtn');
      if (autoInterval) {
        clearInterval(autoInterval);
        autoInterval = null;
        btn.classList.remove('active');
        btn.innerText = 'Auto Ping (1s)';
      } else {
        triggerPing();
        autoInterval = setInterval(triggerPing, 1000);
        btn.classList.add('active');
        btn.innerText = 'Stop Auto Ping';
      }
    }

    // Initial ping on load
    window.addEventListener('load', () => {
      setTimeout(triggerPing, 300);
    });
  </script>
</body>
</html>`;

    return new Response(html, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "no-store",
      },
    });
  },
};

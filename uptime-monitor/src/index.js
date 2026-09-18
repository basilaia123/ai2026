/**
 * Cloudflare Edge Uptime & SSL Monitor
 */

const DEFAULT_TARGETS = [
  {
    id: "cf-main",
    name: "Cloudflare",
    url: "https://www.cloudflare.com",
    expectedStatus: 200,
    timeoutMs: 8000,
  },
  {
    id: "github-api",
    name: "GitHub API",
    url: "https://api.github.com",
    expectedStatus: 200,
    timeoutMs: 8000,
  },
  {
    id: "google-dns",
    name: "Google Web",
    url: "https://dns.google",
    expectedStatus: 200,
    timeoutMs: 8000,
  },
];

export default {
  // 1. Cron Trigger Handler (Every 5 mins)
  async scheduled(event, env, ctx) {
    ctx.waitUntil(runAllChecks(env, "cron"));
  },

  // 2. HTTP Request Handler
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, DELETE, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
        },
      });
    }

    try {
      if (path === "/api/status") {
        const data = await getMonitorData(env);
        return jsonResponse(data);
      }

      if (path === "/api/check-now" && request.method === "POST") {
        const results = await runAllChecks(env, "manual");
        return jsonResponse({ success: true, results });
      }

      if (path === "/api/targets" && request.method === "POST") {
        const body = await request.json();
        if (!body.url || !body.name) {
          return jsonResponse({ error: "Name and URL are required" }, 400);
        }
        const targets = await getTargets(env);
        const newTarget = {
          id: body.id || "tgt-" + Date.now(),
          name: body.name,
          url: body.url.startsWith("http") ? body.url : "https://" + body.url,
          expectedStatus: parseInt(body.expectedStatus) || 200,
          timeoutMs: parseInt(body.timeoutMs) || 8000,
        };

        const existingIdx = targets.findIndex((t) => t.id === newTarget.id);
        if (existingIdx >= 0) {
          targets[existingIdx] = newTarget;
        } else {
          targets.push(newTarget);
        }

        await saveTargets(env, targets);
        return jsonResponse({ success: true, target: newTarget, targets });
      }

      if (path.startsWith("/api/targets/") && request.method === "DELETE") {
        const id = path.replace("/api/targets/", "");
        let targets = await getTargets(env);
        targets = targets.filter((t) => t.id !== id);
        await saveTargets(env, targets);
        return jsonResponse({ success: true, targets });
      }

      if (path === "/api/alerts/save" && request.method === "POST") {
        const body = await request.json();
        const alertConfig = {
          telegramBotToken: body.telegramBotToken || "",
          telegramChatId: body.telegramChatId || "",
          discordWebhookUrl: body.discordWebhookUrl || "",
        };
        await saveAlertConfig(env, alertConfig);
        return jsonResponse({ success: true, message: "Alert config saved" });
      }

      if (path === "/api/alerts/test" && request.method === "POST") {
        const alertConfig = await getAlertConfig(env);
        const testPayload = {
          type: "TEST",
          title: "Edge Monitor Test Alert",
          message: "Your Cloudflare Edge Uptime Monitor alert channels are connected and working!",
          targetName: "Test Target",
          targetUrl: "https://uptime-monitor.example.com",
          status: "UP",
          latency: 42,
          timestamp: new Date().toISOString(),
        };

        const res = await sendNotifications(env, alertConfig, testPayload);
        return jsonResponse({ success: true, details: res });
      }

      if (path.startsWith("/api/badge/")) {
        const id = path.replace("/api/badge/", "");
        const statusData = await getLatestResults(env);
        const targetRes = statusData[id];
        const isUp = targetRes && targetRes.status === "UP";
        const latency = targetRes ? targetRes.latency + "ms" : "N/A";
        const badgeColor = isUp ? "#10b981" : "#ef4444";
        const badgeText = isUp ? `online | ${latency}` : "offline";

        const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="130" height="20">
          <linearGradient id="b" x2="0" y2="100%"><stop offset="0" stop-color="#bbb" stop-opacity=".1"/><stop offset="1" stop-opacity=".1"/></linearGradient>
          <mask id="a"><rect width="130" height="20" rx="3" fill="#fff"/></mask>
          <g mask="url(#a)">
            <path fill="#555" d="M0 0h50v20H0z"/>
            <path fill="${badgeColor}" d="M50 0h80v20H50z"/>
            <path fill="url(#b)" d="M0 0h130v20H0z"/>
          </g>
          <g fill="#fff" text-anchor="middle" font-family="DejaVu Sans,Verdana,Geneva,sans-serif" font-size="11">
            <text x="25" y="15" fill="#010101" fill-opacity=".3">uptime</text>
            <text x="25" y="14">uptime</text>
            <text x="90" y="15" fill="#010101" fill-opacity=".3">${badgeText}</text>
            <text x="90" y="14">${badgeText}</text>
          </g>
        </svg>`;

        return new Response(svg, {
          headers: {
            "Content-Type": "image/svg+xml",
            "Cache-Control": "no-cache, no-store",
          },
        });
      }

      // Serve Dashboard
      return new Response(DASHBOARD_HTML, {
        headers: {
          "Content-Type": "text/html; charset=utf-8",
          "Cache-Control": "no-cache",
        },
      });
    } catch (err) {
      return jsonResponse({ error: err.message }, 500);
    }
  },
};

// ==================== CORE CHECK ENGINE ====================

async function runAllChecks(env, triggerType = "cron") {
  const targets = await getTargets(env);
  const alertConfig = await getAlertConfig(env);
  const previousResults = await getLatestResults(env);
  const newResults = {};

  for (const target of targets) {
    const result = await checkSingleTarget(target);
    newResults[target.id] = result;

    const prev = previousResults[target.id];
    if (prev && prev.status !== result.status) {
      if (result.status === "DOWN") {
        await sendNotifications(env, alertConfig, {
          type: "DOWN",
          title: `🔴 INCIDENT: ${target.name} is DOWN`,
          message: `Target ${target.name} (${target.url}) failed response check.\nError: ${result.error || `HTTP ${result.httpStatus}`}`,
          targetName: target.name,
          targetUrl: target.url,
          status: "DOWN",
          httpStatus: result.httpStatus,
          error: result.error,
          latency: result.latency,
          timestamp: result.timestamp,
        });
      } else if (result.status === "UP") {
        await sendNotifications(env, alertConfig, {
          type: "RECOVERY",
          title: `🟢 RECOVERED: ${target.name} is back ONLINE`,
          message: `Target ${target.name} has recovered. Response time: ${result.latency}ms`,
          targetName: target.name,
          targetUrl: target.url,
          status: "UP",
          httpStatus: result.httpStatus,
          latency: result.latency,
          timestamp: result.timestamp,
        });
      }
    }
  }

  if (env.MONITOR_KV) {
    await env.MONITOR_KV.put("status:latest", JSON.stringify(newResults));
    await env.MONITOR_KV.put("status:lastChecked", new Date().toISOString());
  }

  return newResults;
}

async function checkSingleTarget(target) {
  const start = performance.now();
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), target.timeoutMs || 8000);

  try {
    const response = await fetch(target.url, {
      method: "GET",
      signal: controller.signal,
      headers: {
        "User-Agent": "Cloudflare-Edge-Uptime-Monitor/1.0",
        "Accept": "*/*",
      },
    });

    clearTimeout(timeoutId);
    const latency = Math.round(performance.now() - start);
    const isExpectedStatus = response.status === (target.expectedStatus || 200) || (response.status >= 200 && response.status < 400);

    return {
      targetId: target.id,
      name: target.name,
      url: target.url,
      status: isExpectedStatus ? "UP" : "DOWN",
      httpStatus: response.status,
      latency,
      timestamp: new Date().toISOString(),
      error: isExpectedStatus ? null : `Unexpected HTTP status: ${response.status}`,
    };
  } catch (err) {
    clearTimeout(timeoutId);
    const latency = Math.round(performance.now() - start);
    return {
      targetId: target.id,
      name: target.name,
      url: target.url,
      status: "DOWN",
      httpStatus: 0,
      latency,
      timestamp: new Date().toISOString(),
      error: err.name === "AbortError" ? "Request Timeout (> " + target.timeoutMs + "ms)" : err.message,
    };
  }
}

// ==================== NOTIFICATIONS ====================

async function sendNotifications(env, config, alert) {
  const outcomes = { telegram: null, discord: null };

  if (config.telegramBotToken && config.telegramChatId) {
    try {
      const icon = alert.status === "UP" ? "🟢" : "🔴";
      const text = `${icon} *${alert.title}*\n\n` +
        `🌐 *Target:* [${alert.targetName}](${alert.targetUrl})\n` +
        `⏱ *Latency:* \`${alert.latency}ms\`\n` +
        `📡 *Status:* \`${alert.status}\` ${alert.httpStatus ? `(HTTP ${alert.httpStatus})` : ""}\n` +
        (alert.error ? `⚠️ *Error:* \`${alert.error}\`\n` : "") +
        `🕒 *Time:* \`${alert.timestamp}\``;

      const tgRes = await fetch(`https://api.telegram.org/bot${config.telegramBotToken}/sendMessage`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          chat_id: config.telegramChatId,
          text,
          parse_mode: "Markdown",
          disable_web_page_preview: true,
        }),
      });
      outcomes.telegram = await tgRes.json();
    } catch (e) {
      outcomes.telegram = { error: e.message };
    }
  }

  if (config.discordWebhookUrl) {
    try {
      const color = alert.status === "UP" ? 0x10b981 : 0xef4444;
      const discordRes = await fetch(config.discordWebhookUrl, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          embeds: [
            {
              title: alert.title,
              description: alert.message,
              url: alert.targetUrl,
              color,
              fields: [
                { name: "Target", value: alert.targetName, inline: true },
                { name: "Status", value: alert.status, inline: true },
                { name: "Response Time", value: `${alert.latency} ms`, inline: true },
                ...(alert.error ? [{ name: "Error Details", value: alert.error, inline: false }] : []),
              ],
              footer: { text: "Cloudflare Edge Uptime Monitor" },
              timestamp: alert.timestamp,
            },
          ],
        }),
      });
      outcomes.discord = { status: discordRes.status };
    } catch (e) {
      outcomes.discord = { error: e.message };
    }
  }

  return outcomes;
}

// ==================== STORAGE HELPERS ====================

async function getTargets(env) {
  if (env.MONITOR_KV) {
    const raw = await env.MONITOR_KV.get("config:targets");
    if (raw) return JSON.parse(raw);
  }
  return DEFAULT_TARGETS;
}

async function saveTargets(env, targets) {
  if (env.MONITOR_KV) {
    await env.MONITOR_KV.put("config:targets", JSON.stringify(targets));
  }
}

async function getAlertConfig(env) {
  if (env.MONITOR_KV) {
    const raw = await env.MONITOR_KV.get("config:alerts");
    if (raw) return JSON.parse(raw);
  }
  return {
    telegramBotToken: env.TELEGRAM_BOT_TOKEN || "",
    telegramChatId: env.TELEGRAM_CHAT_ID || "",
    discordWebhookUrl: env.DISCORD_WEBHOOK_URL || "",
  };
}

async function saveAlertConfig(env, config) {
  if (env.MONITOR_KV) {
    await env.MONITOR_KV.put("config:alerts", JSON.stringify(config));
  }
}

async function getLatestResults(env) {
  if (env.MONITOR_KV) {
    const raw = await env.MONITOR_KV.get("status:latest");
    if (raw) return JSON.parse(raw);
  }
  return {};
}

async function getMonitorData(env) {
  const targets = await getTargets(env);
  const results = await getLatestResults(env);
  const alertConfig = await getAlertConfig(env);
  let lastChecked = null;
  if (env.MONITOR_KV) {
    lastChecked = await env.MONITOR_KV.get("status:lastChecked");
  }

  return {
    targets,
    results,
    lastChecked,
    alertConfig: {
      hasTelegram: !!(alertConfig.telegramBotToken && alertConfig.telegramChatId),
      hasDiscord: !!alertConfig.discordWebhookUrl,
      telegramBotToken: alertConfig.telegramBotToken || "",
      telegramChatId: alertConfig.telegramChatId || "",
      discordWebhookUrl: alertConfig.discordWebhookUrl || "",
    },
  };
}

function jsonResponse(data, status = 200) {
  return Response.json(data, {
    status,
    headers: {
      "Content-Type": "application/json",
      "Access-Control-Allow-Origin": "*",
    },
  });
}

// ==================== DASHBOARD HTML UI ====================

const DASHBOARD_HTML = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Cloudflare Edge Uptime & SSL Monitor</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b0f19;
      --card-bg: #111827;
      --card-border: #1e293b;
      --accent: #f38020;
      --green: #10b981;
      --red: #ef4444;
      --text: #f9fafb;
      --text-muted: #94a3b8;
      --font-mono: 'JetBrains Mono', monospace;
      --font-sans: 'Plus Jakarta Sans', sans-serif;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: var(--font-sans);
      min-height: 100vh;
      padding: 40px 20px;
      display: flex;
      justify-content: center;
    }
    .container { max-width: 900px; width: 100%; }
    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .logo-group h1 {
      font-size: 26px;
      font-weight: 800;
      letter-spacing: -0.5px;
    }
    .logo-group p {
      color: var(--text-muted);
      font-size: 14px;
      margin-top: 4px;
    }
    .header-actions { display: flex; gap: 10px; }
    .btn {
      background: var(--accent);
      color: #fff;
      border: none;
      font-family: var(--font-sans);
      font-size: 14px;
      font-weight: 600;
      padding: 10px 18px;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s;
    }
    .btn:hover { filter: brightness(1.1); transform: translateY(-1px); }
    .btn.secondary { background: #1e293b; color: var(--text); }
    .btn.secondary:hover { background: #334155; }
    .metrics-summary {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      margin-bottom: 24px;
    }
    .metric-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 16px;
    }
    .metric-val {
      font-size: 26px;
      font-weight: 800;
      font-family: var(--font-mono);
      margin-bottom: 4px;
    }
    .metric-lbl {
      font-size: 12px;
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }
    .targets-section {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 20px;
      margin-bottom: 24px;
    }
    .section-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }
    .section-head h2 { font-size: 18px; font-weight: 700; }
    .target-list { display: flex; flex-direction: column; gap: 12px; }
    .target-card {
      background: #0d121f;
      border: 1px solid #1e2638;
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      transition: all 0.2s;
    }
    .target-card:hover { border-color: #334155; }
    .target-main { display: flex; align-items: center; gap: 14px; }
    .status-indicator {
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: var(--text-muted);
    }
    .status-indicator.up { background: var(--green); box-shadow: 0 0 10px var(--green); }
    .status-indicator.down { background: var(--red); box-shadow: 0 0 10px var(--red); }
    .target-name { font-size: 15px; font-weight: 700; margin-bottom: 2px; }
    .target-url { font-family: var(--font-mono); font-size: 12px; color: var(--text-muted); }
    .target-stats { display: flex; align-items: center; gap: 16px; }
    .stat-pill {
      font-family: var(--font-mono);
      font-size: 12px;
      background: #111827;
      padding: 6px 12px;
      border-radius: 6px;
      border: 1px solid #1f293d;
    }
    .icon-btn {
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      padding: 6px 10px;
      font-size: 14px;
      border-radius: 4px;
      transition: 0.2s;
    }
    .icon-btn:hover { color: var(--red); background: rgba(239, 68, 68, 0.1); }
    .modal-overlay {
      display: none;
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.75);
      backdrop-filter: blur(4px);
      justify-content: center;
      align-items: center;
      z-index: 999;
    }
    .modal-overlay.active {
      display: flex !important;
    }
    .modal-box {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 24px;
      max-width: 480px;
      width: 90%;
      box-shadow: 0 20px 40px rgba(0,0,0,0.6);
    }
    .modal-box h3 { font-size: 18px; margin-bottom: 16px; }
    .form-group { margin-bottom: 14px; }
    .form-group label {
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: var(--text-muted);
      margin-bottom: 6px;
      text-transform: uppercase;
    }
    .form-group input {
      width: 100%;
      background: #0d121f;
      border: 1px solid #1e2638;
      border-radius: 8px;
      padding: 10px 14px;
      color: #fff;
      font-size: 14px;
    }
    .form-group input:focus { outline: none; border-color: var(--accent); }
    .modal-btns { display: flex; justify-content: flex-end; gap: 10px; margin-top: 20px; }
    @media(max-width: 640px) {
      .metrics-summary { grid-template-columns: repeat(2, 1fr); }
      .target-card { flex-direction: column; align-items: flex-start; gap: 12px; }
      .target-stats { width: 100%; justify-content: space-between; }
    }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo-group">
        <h1>⚡ Edge Uptime & SSL Monitor</h1>
        <p>Automated 5-min global health checks via Cloudflare Workers Edge</p>
      </div>
      <div class="header-actions">
        <button class="btn secondary" id="btnOpenAlerts">⚙️ Alerts Config</button>
        <button class="btn" id="checkNowBtn">🔄 Check All Now</button>
      </div>
    </header>

    <div class="metrics-summary">
      <div class="metric-card">
        <div class="metric-val" id="metricTotal">--</div>
        <div class="metric-lbl">Monitors</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" style="color: var(--green);" id="metricUp">--</div>
        <div class="metric-lbl">Operational</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" style="color: var(--red);" id="metricDown">--</div>
        <div class="metric-lbl">Incidents</div>
      </div>
      <div class="metric-card">
        <div class="metric-val" id="metricAvgLatency">--</div>
        <div class="metric-lbl">Avg Response</div>
      </div>
    </div>

    <div class="targets-section">
      <div class="section-head">
        <h2>Monitored Endpoints</h2>
        <button class="btn secondary" style="padding: 6px 12px; font-size: 12px;" id="btnOpenAdd">+ Add Target</button>
      </div>
      <div class="target-list" id="targetList">
        <p style="color: var(--text-muted); text-align: center; padding: 20px;">Loading targets & telemetry...</p>
      </div>
    </div>
  </div>

  <!-- Add Target Modal -->
  <div class="modal-overlay" id="addModal">
    <div class="modal-box">
      <h3>Add Monitored Target</h3>
      <div class="form-group">
        <label>Service / Site Name</label>
        <input type="text" id="newTargetName" placeholder="e.g. My Website">
      </div>
      <div class="form-group">
        <label>Target URL</label>
        <input type="url" id="newTargetUrl" placeholder="https://example.com">
      </div>
      <div class="form-group">
        <label>Expected Status Code</label>
        <input type="number" id="newTargetStatus" value="200">
      </div>
      <div class="modal-btns">
        <button class="btn secondary" id="btnCancelAdd">Cancel</button>
        <button class="btn" id="btnSaveTarget">Add Target</button>
      </div>
    </div>
  </div>

  <!-- Alert Config Modal -->
  <div class="modal-overlay" id="alertModal">
    <div class="modal-box">
      <h3>Notification Channels</h3>
      <p style="color: var(--text-muted); font-size: 13px; margin-bottom: 16px;">Receive instant alerts on Telegram / Discord when endpoints fail.</p>
      <div class="form-group">
        <label>Telegram Bot Token</label>
        <input type="text" id="tgToken" placeholder="123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ">
      </div>
      <div class="form-group">
        <label>Telegram Chat ID</label>
        <input type="text" id="tgChatId" placeholder="e.g. -100123456789 or user ID">
      </div>
      <div class="form-group">
        <label>Discord Webhook URL</label>
        <input type="url" id="discordUrl" placeholder="https://discord.com/api/webhooks/...">
      </div>
      <div class="modal-btns">
        <button class="btn secondary" id="btnTestAlerts">🔔 Send Test</button>
        <button class="btn secondary" id="btnCancelAlerts">Cancel</button>
        <button class="btn" id="btnSaveAlerts">Save</button>
      </div>
    </div>
  </div>

  <script>
    var state = { targets: [], results: {}, alertConfig: {} };

    function loadStatus() {
      return fetch('/api/status')
        .then(function(res) { return res.json(); })
        .then(function(data) {
          state = data;
          render();
        })
        .catch(function(err) {
          console.error("Failed to load status:", err);
        });
    }

    function render() {
      var list = document.getElementById('targetList');
      var targets = state.targets || [];
      var results = state.results || {};

      var upCount = 0;
      var downCount = 0;
      var totalLatency = 0;
      var latencyCount = 0;

      if (targets.length === 0) {
        list.innerHTML = '<p style="color: var(--text-muted); text-align: center; padding: 20px;">No targets configured yet.</p>';
      } else {
        var html = '';
        for (var i = 0; i < targets.length; i++) {
          var t = targets[i];
          var r = results[t.id];
          var isUp = r ? r.status === 'UP' : null;
          var statusClass = isUp === true ? 'up' : (isUp === false ? 'down' : '');
          var statusText = isUp === true ? 'OPERATIONAL' : (isUp === false ? 'DOWN' : 'PENDING');
          var latency = r ? r.latency + ' ms' : '--';

          if (isUp === true) upCount++;
          if (isUp === false) downCount++;
          if (r && r.latency) {
            totalLatency += r.latency;
            latencyCount++;
          }

          var statColor = isUp === true ? 'var(--green)' : (isUp === false ? 'var(--red)' : 'var(--text-muted)');

          html += '<div class="target-card">' +
            '<div class="target-main">' +
              '<div class="status-indicator ' + statusClass + '"></div>' +
              '<div>' +
                '<div class="target-name">' + escapeHtml(t.name) + '</div>' +
                '<div class="target-url">' + escapeHtml(t.url) + '</div>' +
              '</div>' +
            '</div>' +
            '<div class="target-stats">' +
              '<div class="stat-pill" style="color:' + statColor + '">' + statusText + '</div>' +
              '<div class="stat-pill">' + latency + '</div>' +
              '<button class="icon-btn" data-delete-id="' + t.id + '" title="Delete">✕</button>' +
            '</div>' +
          '</div>';
        }
        list.innerHTML = html;

        // Bind delete buttons
        var delButtons = list.querySelectorAll('[data-delete-id]');
        delButtons.forEach(function(btn) {
          btn.addEventListener('click', function() {
            var id = this.getAttribute('data-delete-id');
            deleteTarget(id);
          });
        });
      }

      document.getElementById('metricTotal').innerText = targets.length;
      document.getElementById('metricUp').innerText = upCount;
      document.getElementById('metricDown').innerText = downCount;
      document.getElementById('metricAvgLatency').innerText = latencyCount > 0 ? Math.round(totalLatency / latencyCount) + ' ms' : '--';
    }

    function runCheckNow() {
      var btn = document.getElementById('checkNowBtn');
      btn.disabled = true;
      btn.innerText = 'Checking...';
      fetch('/api/check-now', { method: 'POST' })
        .then(function() { return loadStatus(); })
        .finally(function() {
          btn.disabled = false;
          btn.innerText = '🔄 Check All Now';
        });
    }

    function saveNewTarget() {
      var name = document.getElementById('newTargetName').value.trim();
      var url = document.getElementById('newTargetUrl').value.trim();
      var status = document.getElementById('newTargetStatus').value;

      if (!name || !url) return alert('Please enter both name and URL');

      fetch('/api/targets', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, url: url, expectedStatus: status })
      }).then(function() {
        document.getElementById('newTargetName').value = '';
        document.getElementById('newTargetUrl').value = '';
        closeModal('addModal');
        runCheckNow();
      });
    }

    function deleteTarget(id) {
      if (!confirm('Are you sure you want to delete this target?')) return;
      fetch('/api/targets/' + id, { method: 'DELETE' })
        .then(function() { loadStatus(); });
    }

    function openModal(id) {
      document.getElementById(id).classList.add('active');
    }

    function closeModal(id) {
      document.getElementById(id).classList.remove('active');
    }

    function saveAlerts() {
      var tgToken = document.getElementById('tgToken').value.trim();
      var tgChatId = document.getElementById('tgChatId').value.trim();
      var discordUrl = document.getElementById('discordUrl').value.trim();

      fetch('/api/alerts/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ telegramBotToken: tgToken, telegramChatId: tgChatId, discordWebhookUrl: discordUrl })
      }).then(function() {
        alert('Alert configurations saved successfully!');
        closeModal('alertModal');
        loadStatus();
      });
    }

    function testAlerts() {
      var tgToken = document.getElementById('tgToken').value.trim();
      var tgChatId = document.getElementById('tgChatId').value.trim();
      var discordUrl = document.getElementById('discordUrl').value.trim();

      // Save first so test runs against current inputs
      fetch('/api/alerts/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ telegramBotToken: tgToken, telegramChatId: tgChatId, discordWebhookUrl: discordUrl })
      })
      .then(function() {
        return fetch('/api/alerts/test', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: '{}' });
      })
      .then(function(res) { return res.json(); })
      .then(function(data) {
        alert('Test notification triggered! Check Telegram / Discord.');
      });
    }

    function escapeHtml(str) {
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }

    // Attach Event Listeners
    document.getElementById('btnOpenAdd').addEventListener('click', function() {
      openModal('addModal');
    });

    document.getElementById('btnOpenAlerts').addEventListener('click', function() {
      if (state.alertConfig) {
        if (state.alertConfig.telegramBotToken) document.getElementById('tgToken').value = state.alertConfig.telegramBotToken;
        if (state.alertConfig.telegramChatId) document.getElementById('tgChatId').value = state.alertConfig.telegramChatId;
        if (state.alertConfig.discordWebhookUrl) document.getElementById('discordUrl').value = state.alertConfig.discordWebhookUrl;
      }
      openModal('alertModal');
    });

    document.getElementById('btnCancelAdd').addEventListener('click', function() { closeModal('addModal'); });
    document.getElementById('btnSaveTarget').addEventListener('click', saveNewTarget);
    document.getElementById('btnCancelAlerts').addEventListener('click', function() { closeModal('alertModal'); });
    document.getElementById('btnSaveAlerts').addEventListener('click', saveAlerts);
    document.getElementById('btnTestAlerts').addEventListener('click', testAlerts);
    document.getElementById('checkNowBtn').addEventListener('click', runCheckNow);

    // Close on overlay backdrop click
    document.querySelectorAll('.modal-overlay').forEach(function(overlay) {
      overlay.addEventListener('click', function(e) {
        if (e.target === overlay) {
          overlay.classList.remove('active');
        }
      });
    });

    loadStatus();
    setInterval(loadStatus, 15000);
  </script>
</body>
</html>`;

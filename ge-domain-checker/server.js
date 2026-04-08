const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const net = require("node:net");
const { domainToASCII } = require("node:url");

const HOST = "0.0.0.0";
const PORT = Number(process.env.PORT || 3000);
const WHOIS_HOST = process.env.WHOIS_HOST || "whois.nic.ge";
const WHOIS_PORT = Number(process.env.WHOIS_PORT || 43);
const WHOIS_TIMEOUT_MS = Number(process.env.WHOIS_TIMEOUT_MS || 9000);
const PUBLIC_DIR = path.join(__dirname, "public");

function parseJsonBody(req) {
  return new Promise((resolve, reject) => {
    let raw = "";

    req.on("data", (chunk) => {
      raw += chunk;
      if (raw.length > 2_000_000) {
        reject(new Error("Request body is too large."));
        req.destroy();
      }
    });

    req.on("end", () => {
      if (!raw.trim()) {
        resolve({});
        return;
      }

      try {
        resolve(JSON.parse(raw));
      } catch {
        reject(new Error("Invalid JSON body."));
      }
    });

    req.on("error", reject);
  });
}

function sanitizeInput(value) {
  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/^https?:\/\//, "")
    .replace(/[/?#].*$/, "")
    .replace(/\.$/, "");
}

function normalizeDomain(input) {
  const cleaned = sanitizeInput(input);
  if (!cleaned) {
    return { ok: false, reason: "ცარიელი ჩანაწერია." };
  }

  let domain = cleaned;
  if (!domain.endsWith(".ge")) {
    domain = `${domain}.ge`;
  }

  const asciiDomain = domainToASCII(domain);
  if (!asciiDomain) {
    return { ok: false, reason: "დომენის ფორმატი არასწორია." };
  }

  if (!asciiDomain.endsWith(".ge")) {
    return { ok: false, reason: "მხოლოდ .ge დომენებია მხარდაჭერილი." };
  }

  const label = asciiDomain.slice(0, -3);
  const labelValid = /^[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?$/i.test(label);
  if (!labelValid) {
    return {
      ok: false,
      reason: "დომენი უნდა იყოს 1-63 სიმბოლო, მხოლოდ ასო/ციფრი/დეფისი."
    };
  }

  return {
    ok: true,
    label,
    asciiDomain: `${label}.ge`,
    displayDomain: cleaned.endsWith(".ge") ? cleaned : `${cleaned}.ge`
  };
}

function getPremiumTier(score) {
  if (score >= 85) return "premium";
  if (score >= 70) return "strong";
  if (score >= 55) return "good";
  if (score >= 40) return "average";
  return "weak";
}

function calculatePremiumScore(label) {
  const normalized = String(label || "").toLowerCase();
  const length = normalized.length;
  const lettersOnly = normalized.replace(/[^a-z]/g, "");
  const uniqueCount = new Set(normalized.replace(/-/g, "").split("")).size;
  const hyphenCount = (normalized.match(/-/g) || []).length;
  const digitCount = (normalized.match(/[0-9]/g) || []).length;
  const vowelCount = (lettersOnly.match(/[aeiouy]/g) || []).length;
  const consonantCount = Math.max(0, lettersOnly.length - vowelCount);
  const vowelRatio = lettersOnly.length ? vowelCount / lettersOnly.length : 0;
  const uniqueRatio = normalized.replace(/-/g, "").length
    ? uniqueCount / normalized.replace(/-/g, "").length
    : 0;

  let score = 50;

  if (length <= 4) score += 30;
  else if (length <= 6) score += 24;
  else if (length <= 8) score += 16;
  else if (length <= 12) score += 8;
  else if (length <= 18) score += 2;
  else score -= 8;

  if (hyphenCount === 0) score += 10;
  else score -= Math.min(18, hyphenCount * 8);

  if (digitCount === 0) score += 8;
  else if (digitCount === 1) score += 2;
  else score -= Math.min(12, digitCount * 3);

  if (vowelRatio >= 0.35 && vowelRatio <= 0.6) score += 8;
  else if (vowelRatio > 0 && vowelRatio < 0.2) score -= 6;

  if (consonantCount >= 2 && vowelCount >= 1) score += 3;
  if (uniqueRatio >= 0.7) score += 6;
  else if (uniqueRatio <= 0.4) score -= 6;

  if (/(.)\1\1/.test(normalized)) score -= 10;
  if (lettersOnly.length >= 10 && vowelCount <= 1) score -= 12;

  const safeScore = Math.max(0, Math.min(100, Math.round(score)));
  return {
    score: safeScore,
    tier: getPremiumTier(safeScore)
  };
}

function whoisLookup(domain) {
  return new Promise((resolve, reject) => {
    const socket = net.createConnection({ host: WHOIS_HOST, port: WHOIS_PORT });
    let response = "";
    let settled = false;

    const done = (err, data) => {
      if (settled) {
        return;
      }
      settled = true;
      socket.destroy();
      if (err) {
        reject(err);
        return;
      }
      resolve(data);
    };

    socket.setTimeout(WHOIS_TIMEOUT_MS);

    socket.on("connect", () => {
      socket.write(`${domain}\r\n`);
    });

    socket.on("data", (chunk) => {
      response += chunk.toString("utf8");
      if (response.length > 100_000) {
        done(null, response);
      }
    });

    socket.on("timeout", () => done(new Error("WHOIS timeout")));
    socket.on("error", (err) => done(err));
    socket.on("end", () => done(null, response));
  });
}

function parseWhoisResult(rawText) {
  const text = String(rawText || "");
  const upper = text.toUpperCase();

  if (
    upper.includes("NO MATCH FOR") ||
    upper.includes("NO ENTRIES FOUND") ||
    upper.includes("NOT FOUND")
  ) {
    return { status: "available", available: true };
  }

  if (
    upper.includes("DOMAIN NAME:") ||
    upper.includes("REGISTRY EXPIRY DATE:") ||
    upper.includes("REGISTRAR:")
  ) {
    return { status: "taken", available: false };
  }

  return {
    status: "unknown",
    available: null,
    note: "WHOIS პასუხი ვერ განისაზღვრა."
  };
}

async function checkSingleDomain(input) {
  const normalized = normalizeDomain(input);
  if (!normalized.ok) {
    return {
      input: String(input || ""),
      domain: null,
      status: "invalid",
      available: null,
      premiumScore: null,
      premiumTier: null,
      note: normalized.reason
    };
  }

  const premium = calculatePremiumScore(normalized.label);

  try {
    const raw = await whoisLookup(normalized.asciiDomain);
    const parsed = parseWhoisResult(raw);
    return {
      input: String(input || ""),
      domain: normalized.displayDomain,
      status: parsed.status,
      available: parsed.available,
      premiumScore: premium.score,
      premiumTier: premium.tier,
      note: parsed.note || null
    };
  } catch (error) {
    return {
      input: String(input || ""),
      domain: normalized.displayDomain,
      status: "error",
      available: null,
      premiumScore: premium.score,
      premiumTier: premium.tier,
      note: `WHOIS შეცდომა: ${error.message}`
    };
  }
}

async function checkDomainsInBatches(domains, batchSize = 8) {
  const results = [];
  for (let i = 0; i < domains.length; i += batchSize) {
    const chunk = domains.slice(i, i + batchSize);
    const chunkResults = await Promise.all(chunk.map((item) => checkSingleDomain(item)));
    results.push(...chunkResults);
  }
  return results;
}

function sendJson(res, statusCode, payload) {
  res.writeHead(statusCode, { "Content-Type": "application/json; charset=utf-8" });
  res.end(JSON.stringify(payload));
}

function serveStatic(req, res) {
  const filePath = req.url === "/" ? "/index.html" : req.url;
  const resolvedPath = path.join(PUBLIC_DIR, filePath);

  if (!resolvedPath.startsWith(PUBLIC_DIR)) {
    res.writeHead(403);
    res.end("Forbidden");
    return;
  }

  const extension = path.extname(resolvedPath).toLowerCase();
  const contentTypeByExt = {
    ".html": "text/html; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".js": "application/javascript; charset=utf-8"
  };

  fs.readFile(resolvedPath, (err, data) => {
    if (err) {
      res.writeHead(404);
      res.end("Not found");
      return;
    }
    res.writeHead(200, { "Content-Type": contentTypeByExt[extension] || "text/plain; charset=utf-8" });
    res.end(data);
  });
}

const server = http.createServer(async (req, res) => {
  if (req.method === "POST" && req.url === "/api/check") {
    try {
      const body = await parseJsonBody(req);
      const domains = Array.isArray(body.domains) ? body.domains : [];

      if (!domains.length) {
        sendJson(res, 400, { error: "დომენების სია ცარიელია." });
        return;
      }

      if (domains.length > 300) {
        sendJson(res, 400, { error: "ერთ ჯერზე მაქსიმუმ 300 დომენი გადაამოწმე." });
        return;
      }

      const results = await checkDomainsInBatches(domains);
      const summary = results.reduce(
        (acc, item) => {
          acc[item.status] = (acc[item.status] || 0) + 1;
          return acc;
        },
        { available: 0, taken: 0, unknown: 0, invalid: 0, error: 0 }
      );

      sendJson(res, 200, {
        checkedAt: new Date().toISOString(),
        summary,
        results
      });
    } catch (error) {
      sendJson(res, 500, { error: error.message || "Server error" });
    }
    return;
  }

  if (req.method === "GET") {
    serveStatic(req, res);
    return;
  }

  res.writeHead(405, { "Content-Type": "text/plain; charset=utf-8" });
  res.end("Method Not Allowed");
});

server.listen(PORT, HOST, () => {
  console.log(`GE domain checker running on http://localhost:${PORT}`);
});

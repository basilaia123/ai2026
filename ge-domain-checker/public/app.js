const domainsEl = document.getElementById("domains");
const checkBtn = document.getElementById("checkBtn");
const sampleBtn = document.getElementById("sampleBtn");
const copyAvailableBtn = document.getElementById("copyAvailableBtn");
const generateBtn = document.getElementById("generateBtn");
const keywordInputEl = document.getElementById("keywordInput");
const generateCountEl = document.getElementById("generateCount");
const allowSpecialCharsEl = document.getElementById("allowSpecialChars");

const copyResultsBtn = document.getElementById("copyResultsBtn");
const downloadCsvBtn = document.getElementById("downloadCsvBtn");
const downloadExcelBtn = document.getElementById("downloadExcelBtn");
const statusFilterEl = document.getElementById("statusFilter");

const copyFavoritesBtn = document.getElementById("copyFavoritesBtn");
const loadFavoritesBtn = document.getElementById("loadFavoritesBtn");
const favoritesListEl = document.getElementById("favoritesList");
const favoritesStatusEl = document.getElementById("favoritesStatus");

const statusEl = document.getElementById("status");
const summaryEl = document.getElementById("summary");
const resultsBodyEl = document.getElementById("resultsBody");

const FAVORITES_STORAGE_KEY = "ge_domain_checker_favorites_v1";

let latestResults = [];
let visibleResults = [];
let favoritesSet = loadFavorites();

function getBadgeClass(status) {
  if (status === "available") return "available";
  if (status === "taken") return "taken";
  return "other";
}

function statusLabel(status) {
  if (status === "available") return "თავისუფალია";
  if (status === "taken") return "დაკავებულია";
  if (status === "invalid") return "არასწორი";
  if (status === "error") return "შეცდომა";
  return "უცნობი";
}

function tierLabel(tier) {
  if (tier === "premium") return "Premium";
  if (tier === "strong") return "Strong";
  if (tier === "good") return "Good";
  if (tier === "average") return "Average";
  return "Weak";
}

function parseLines(text) {
  return text
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
}

function sanitizeDomainLike(value) {
  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/^https?:\/\//, "")
    .replace(/[/?#].*$/, "")
    .replace(/\.$/, "");
}

function toFavoriteKey(value) {
  const cleaned = sanitizeDomainLike(value);
  if (!cleaned) return null;
  if (/\s/.test(cleaned) || cleaned.includes("..")) return null;
  return cleaned.endsWith(".ge") ? cleaned : `${cleaned}.ge`;
}

function loadFavorites() {
  try {
    const raw = localStorage.getItem(FAVORITES_STORAGE_KEY);
    const items = JSON.parse(raw || "[]");
    if (!Array.isArray(items)) {
      return new Set();
    }
    return new Set(items.map((item) => toFavoriteKey(item)).filter(Boolean));
  } catch {
    return new Set();
  }
}

function persistFavorites() {
  localStorage.setItem(FAVORITES_STORAGE_KEY, JSON.stringify(Array.from(favoritesSet)));
}

function isFavoriteRow(row) {
  const key = toFavoriteKey(row.domain || row.input);
  return Boolean(key && favoritesSet.has(key));
}

function renderSummary(summary) {
  summaryEl.innerHTML = "";
  const items = [
    { key: "available", label: "თავისუფალი", type: "available" },
    { key: "taken", label: "დაკავებული", type: "taken" },
    { key: "unknown", label: "უცნობი", type: "other" },
    { key: "invalid", label: "არასწორი", type: "other" },
    { key: "error", label: "შეცდომა", type: "other" }
  ];

  for (const item of items) {
    const pill = document.createElement("span");
    pill.className = `pill ${item.type}`;
    pill.textContent = `${item.label}: ${summary[item.key] || 0}`;
    summaryEl.appendChild(pill);
  }
}

function createTd(text) {
  const td = document.createElement("td");
  td.textContent = text;
  return td;
}

function renderResults(results) {
  resultsBodyEl.innerHTML = "";

  if (!results.length) {
    const tr = document.createElement("tr");
    const td = document.createElement("td");
    td.colSpan = 6;
    td.textContent = "ფილტრის მიხედვით შედეგი არ მოიძებნა.";
    tr.appendChild(td);
    resultsBodyEl.appendChild(tr);
    return;
  }

  for (const row of results) {
    const tr = document.createElement("tr");
    const badgeClass = getBadgeClass(row.status);
    const favKey = toFavoriteKey(row.domain || row.input);
    const isFav = Boolean(favKey && favoritesSet.has(favKey));

    const favTd = document.createElement("td");
    const favBtn = document.createElement("button");
    favBtn.type = "button";
    favBtn.className = `favBtn ${isFav ? "active" : ""}`;
    favBtn.dataset.favoriteKey = favKey || "";
    favBtn.title = isFav ? "ფავორიტიდან წაშლა" : "ფავორიტში დამატება";
    favBtn.textContent = isFav ? "★" : "☆";
    favTd.appendChild(favBtn);
    tr.appendChild(favTd);

    tr.appendChild(createTd(row.input || "-"));
    tr.appendChild(createTd(row.domain || "-"));

    const scoreTd = document.createElement("td");
    if (typeof row.premiumScore === "number") {
      const score = document.createElement("span");
      const tier = row.premiumTier || "weak";
      score.className = `score ${tier}`;
      score.textContent = `${row.premiumScore}`;
      score.title = `Tier: ${tierLabel(tier)}`;
      scoreTd.appendChild(score);
    } else {
      scoreTd.textContent = "-";
    }
    tr.appendChild(scoreTd);

    const statusTd = document.createElement("td");
    const statusBadge = document.createElement("span");
    statusBadge.className = `badge ${badgeClass}`;
    statusBadge.textContent = statusLabel(row.status);
    statusTd.appendChild(statusBadge);
    tr.appendChild(statusTd);

    tr.appendChild(createTd(row.note || "-"));
    resultsBodyEl.appendChild(tr);
  }
}

function getFilteredResults(results) {
  const selected = statusFilterEl.value;
  if (selected === "all") {
    return results;
  }
  if (selected === "favorite") {
    return results.filter((item) => isFavoriteRow(item));
  }
  return results.filter((item) => item.status === selected);
}

function refreshResultsView() {
  visibleResults = getFilteredResults(latestResults);
  renderResults(visibleResults);
}

function renderFavorites() {
  favoritesListEl.innerHTML = "";
  const keys = Array.from(favoritesSet).sort((a, b) => a.localeCompare(b));

  if (!keys.length) {
    favoritesStatusEl.textContent = "ფავორიტი დომენები აქ გამოჩნდება.";
    return;
  }

  favoritesStatusEl.textContent = `ფავორიტებშია ${keys.length} დომენი.`;

  const lookup = new Map();
  for (const item of latestResults) {
    const key = toFavoriteKey(item.domain || item.input);
    if (key && !lookup.has(key)) {
      lookup.set(key, item);
    }
  }

  for (const key of keys) {
    const tag = document.createElement("span");
    tag.className = "favoriteItem";
    const info = lookup.get(key);
    if (info && typeof info.premiumScore === "number") {
      tag.textContent = `${key} (${info.premiumScore})`;
    } else {
      tag.textContent = key;
    }
    favoritesListEl.appendChild(tag);
  }
}

function mergeLines(existing, additions) {
  const seen = new Set(existing.map((item) => item.toLowerCase()));
  const merged = [...existing];
  let added = 0;

  for (const value of additions) {
    const clean = String(value || "").trim();
    const key = clean.toLowerCase();
    if (!clean || seen.has(key)) {
      continue;
    }
    merged.push(clean);
    seen.add(key);
    added += 1;
  }

  return { merged, added };
}

function sanitizeKeywordForGeneration(value, allowSpecialChars) {
  const spaceJoiner = allowSpecialChars ? "-" : "";
  const allowedPattern = allowSpecialChars ? /[^\p{L}\p{N}-]/gu : /[^\p{L}]/gu;

  return String(value || "")
    .trim()
    .toLowerCase()
    .replace(/\s+/g, spaceJoiner)
    .replace(allowedPattern, "")
    .replace(/-+/g, "-")
    .replace(/^-+|-+$/g, "");
}

function normalizeIdeaCandidate(candidate, allowSpecialChars) {
  const value = String(candidate || "").toLowerCase();
  const cleaned = allowSpecialChars
    ? value
      .replace(/[^\p{L}\p{N}-]/gu, "")
      .replace(/-+/g, "-")
      .replace(/^-+|-+$/g, "")
    : value.replace(/[^\p{L}]/gu, "");

  return cleaned;
}

function generateDomainIdeas(base, count, options = {}) {
  const allowSpecialChars = Boolean(options.allowSpecialChars);
  const ideas = new Set();
  const max = Number(count) || 30;

  const suffixes = [
    "app",
    "hub",
    "lab",
    "pro",
    "plus",
    "now",
    "smart",
    "go",
    "studio",
    "space",
    "market",
    "guide",
    "center",
    "base",
    "world",
    "line",
    "works",
    "team"
  ];
  const prefixes = ["my", "get", "the", "top", "best", "neo", "smart", "new", "prime", "ultra"];
  const words = ["group", "point", "zone", "studio", "space", "market", "guide", "labs", "cloud", "core"];
  const numericSuffixes = ["24", "360", "365", "101", "plus1"];

  const pushIdea = (candidate) => {
    const cleaned = normalizeIdeaCandidate(candidate, allowSpecialChars);
    if (!cleaned || cleaned.length > 63) {
      return;
    }
    ideas.add(cleaned);
  };

  pushIdea(base);
  suffixes.forEach((suffix) => {
    pushIdea(`${base}${suffix}`);
    if (allowSpecialChars) {
      pushIdea(`${base}-${suffix}`);
    }
  });
  prefixes.forEach((prefix) => {
    pushIdea(`${prefix}${base}`);
    if (allowSpecialChars) {
      pushIdea(`${prefix}-${base}`);
    }
  });
  words.forEach((word) => {
    if (allowSpecialChars) {
      pushIdea(`${base}-${word}`);
      pushIdea(`${word}-${base}`);
    } else {
      pushIdea(`${base}${word}`);
      pushIdea(`${word}${base}`);
    }
  });

  if (allowSpecialChars) {
    numericSuffixes.forEach((suffix) => {
      pushIdea(`${base}${suffix}`);
      pushIdea(`${base}-${suffix}`);
    });
  }

  for (let i = 0; ideas.size < max + 20 && i < prefixes.length; i += 1) {
    for (let j = 0; ideas.size < max + 20 && j < suffixes.length; j += 1) {
      if (allowSpecialChars) {
        pushIdea(`${prefixes[i]}-${base}-${suffixes[j]}`);
      } else {
        pushIdea(`${prefixes[i]}${base}${suffixes[j]}`);
      }
    }
  }

  return Array.from(ideas).slice(0, max);
}

function downloadFile(content, filename, mimeType) {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = filename;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

function csvEscape(value) {
  const text = String(value ?? "");
  if (/[",\n]/.test(text)) {
    return `"${text.replace(/"/g, "\"\"")}"`;
  }
  return text;
}

function getExportRows() {
  return visibleResults.map((item) => ({
    input: item.input || "",
    domain: item.domain || "",
    score: typeof item.premiumScore === "number" ? item.premiumScore : "",
    tier: item.premiumTier || "",
    status: statusLabel(item.status),
    note: item.note || "",
    favorite: isFavoriteRow(item) ? "yes" : "no"
  }));
}

function makeExportFileName(ext) {
  const stamp = new Date().toISOString().replace(/[:.]/g, "-");
  return `ge-domain-results-${stamp}.${ext}`;
}

async function runCheck() {
  const domains = parseLines(domainsEl.value);
  if (!domains.length) {
    statusEl.textContent = "ჯერ ჩასვი დომენების სია.";
    return;
  }

  checkBtn.disabled = true;
  statusEl.textContent = `მიმდინარეობს ${domains.length} დომენის შემოწმება...`;

  try {
    const res = await fetch("/api/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ domains })
    });

    const data = await res.json();
    if (!res.ok) {
      throw new Error(data.error || "შეცდომა");
    }

    latestResults = data.results || [];
    renderSummary(data.summary || {});
    refreshResultsView();
    renderFavorites();
    statusEl.textContent = `დასრულდა. შემოწმდა ${latestResults.length} დომენი, ნაჩვენებია ${visibleResults.length}.`;
  } catch (error) {
    statusEl.textContent = `შეცდომა: ${error.message}`;
  } finally {
    checkBtn.disabled = false;
  }
}

function fillSample() {
  domainsEl.value = ["chatgpt", "google.ge", "asdfghjkqwerty12345", "bad domain"].join("\n");
}

function handleGenerate() {
  const allowSpecialChars = Boolean(allowSpecialCharsEl?.checked);
  const keyword = sanitizeKeywordForGeneration(keywordInputEl.value, allowSpecialChars);
  const count = Number(generateCountEl.value || 30);

  if (!keyword) {
    statusEl.textContent = "გენერაციისთვის საკვანძო სიტყვა ჩაწერე.";
    return;
  }

  const generated = generateDomainIdeas(keyword, count, { allowSpecialChars });
  const existing = parseLines(domainsEl.value);
  const { merged, added } = mergeLines(existing, generated);
  domainsEl.value = merged.join("\n");
  statusEl.textContent = `გენერირდა ${generated.length} იდეა (${allowSpecialChars ? "დეფისი/ციფრები ჩართულია" : "მხოლოდ ასოები"}), სიას დაემატა ${added} ახალი დომენი.`;
}

async function copyAvailable() {
  const availableDomains = latestResults
    .filter((item) => item.status === "available" && item.domain)
    .map((item) => item.domain);

  if (!availableDomains.length) {
    statusEl.textContent = "თავისუფალი დომენი ჯერ არ არის შედეგებში.";
    return;
  }

  try {
    await navigator.clipboard.writeText(availableDomains.join("\n"));
    statusEl.textContent = `დაკოპირდა ${availableDomains.length} თავისუფალი დომენი.`;
  } catch {
    statusEl.textContent = "კოპირება ვერ მოხერხდა. ბრაუზერის უფლებები შეამოწმე.";
  }
}

async function copyResults() {
  if (!visibleResults.length) {
    statusEl.textContent = "კოპირებისთვის შედეგები არ არის (ფილტრი შეცვალე ან თავიდან შეამოწმე).";
    return;
  }

  const rows = visibleResults.map((item) =>
    [
      item.input || "-",
      item.domain || "-",
      typeof item.premiumScore === "number" ? item.premiumScore : "-",
      item.premiumTier || "-",
      statusLabel(item.status),
      item.note || "-",
      isFavoriteRow(item) ? "yes" : "no"
    ].join("\t")
  );

  const tsv = ["შეყვანა\t.ge დომენი\tქულა\ttier\tსტატუსი\tშენიშვნა\tfavorite", ...rows].join("\n");

  try {
    await navigator.clipboard.writeText(tsv);
    statusEl.textContent = `დაკოპირდა ${visibleResults.length} შედეგი (ფილტრის მიხედვით).`;
  } catch {
    statusEl.textContent = "შედეგების კოპირება ვერ მოხერხდა. ბრაუზერის უფლებები შეამოწმე.";
  }
}

function downloadCsv() {
  if (!visibleResults.length) {
    statusEl.textContent = "CSV export-ისთვის შედეგები არ არის.";
    return;
  }

  const header = ["Input", "Domain", "Score", "Tier", "Status", "Note", "Favorite"];
  const rows = getExportRows().map((row) =>
    [row.input, row.domain, row.score, row.tier, row.status, row.note, row.favorite]
      .map(csvEscape)
      .join(",")
  );
  const csv = `\uFEFF${[header.join(","), ...rows].join("\n")}`;
  downloadFile(csv, makeExportFileName("csv"), "text/csv;charset=utf-8;");
  statusEl.textContent = `CSV ფაილი ჩამოიტვირთა (${visibleResults.length} შედეგი).`;
}

function downloadExcel() {
  if (!visibleResults.length) {
    statusEl.textContent = "Excel export-ისთვის შედეგები არ არის.";
    return;
  }

  const header = ["Input", "Domain", "Score", "Tier", "Status", "Note", "Favorite"];
  const rows = getExportRows().map((row) =>
    [row.input, row.domain, row.score, row.tier, row.status, row.note, row.favorite].join("\t")
  );
  const tsv = `\uFEFF${[header.join("\t"), ...rows].join("\n")}`;
  downloadFile(tsv, makeExportFileName("xls"), "application/vnd.ms-excel;charset=utf-8;");
  statusEl.textContent = `Excel ფაილი ჩამოიტვირთა (${visibleResults.length} შედეგი).`;
}

function toggleFavorite(key) {
  if (!key) {
    return;
  }
  if (favoritesSet.has(key)) {
    favoritesSet.delete(key);
  } else {
    favoritesSet.add(key);
  }
  persistFavorites();
  renderFavorites();
  refreshResultsView();
}

async function copyFavorites() {
  const favoriteDomains = Array.from(favoritesSet).sort((a, b) => a.localeCompare(b));
  if (!favoriteDomains.length) {
    statusEl.textContent = "ფავორიტები ცარიელია.";
    return;
  }
  try {
    await navigator.clipboard.writeText(favoriteDomains.join("\n"));
    statusEl.textContent = `დაკოპირდა ${favoriteDomains.length} ფავორიტი დომენი.`;
  } catch {
    statusEl.textContent = "ფავორიტების კოპირება ვერ მოხერხდა.";
  }
}

function loadFavoritesToInput() {
  const favoriteDomains = Array.from(favoritesSet).sort((a, b) => a.localeCompare(b));
  if (!favoriteDomains.length) {
    statusEl.textContent = "ფავორიტები ცარიელია.";
    return;
  }

  const existing = parseLines(domainsEl.value);
  const { merged, added } = mergeLines(existing, favoriteDomains);
  domainsEl.value = merged.join("\n");
  statusEl.textContent = `სიაში ჩაიმატა ${added} ფავორიტი დომენი.`;
}

checkBtn.addEventListener("click", runCheck);
sampleBtn.addEventListener("click", fillSample);
generateBtn.addEventListener("click", handleGenerate);
copyAvailableBtn.addEventListener("click", copyAvailable);
copyResultsBtn.addEventListener("click", copyResults);
downloadCsvBtn.addEventListener("click", downloadCsv);
downloadExcelBtn.addEventListener("click", downloadExcel);
copyFavoritesBtn.addEventListener("click", copyFavorites);
loadFavoritesBtn.addEventListener("click", loadFavoritesToInput);

statusFilterEl.addEventListener("change", () => {
  refreshResultsView();
  statusEl.textContent = `ფილტრი განახლდა. ნაჩვენებია ${visibleResults.length} შედეგი.`;
});

resultsBodyEl.addEventListener("click", (event) => {
  const target = event.target.closest("button.favBtn");
  if (!target) {
    return;
  }
  toggleFavorite(target.dataset.favoriteKey || "");
});

renderFavorites();

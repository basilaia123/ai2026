let prompts = [];
let currentCat = "all";
let searchQuery = "";

// --- Storage ---
function loadPrompts(cb) {
  chrome.storage.local.get("prompts", (data) => {
    prompts = data.prompts || [];
    cb();
  });
}

function savePrompts() {
  chrome.storage.local.set({ prompts });
}

// --- Render ---
function getFiltered() {
  return prompts.filter(p => {
    const matchCat = currentCat === "all" || p.category === currentCat;
    const q = searchQuery.toLowerCase();
    const matchSearch = !q || p.title.toLowerCase().includes(q) || p.text.toLowerCase().includes(q) || p.tags.some(t => t.toLowerCase().includes(q));
    return matchCat && matchSearch;
  });
}

function render() {
  const list = document.getElementById("promptList");
  const empty = document.getElementById("emptyState");
  const filtered = getFiltered();

  // Remove existing cards (keep emptyState)
  [...list.querySelectorAll(".prompt-card")].forEach(el => el.remove());

  if (filtered.length === 0) {
    empty.style.display = "flex";
    return;
  }
  empty.style.display = "none";

  filtered.forEach(p => {
    const card = document.createElement("div");
    card.className = "prompt-card";
    card.dataset.id = p.id;

    const tagsHtml = (p.tags || []).map(t => `<span class="tag">${esc(t)}</span>`).join("");

    card.innerHTML = `
      <div class="card-top">
        <div class="card-title">${esc(p.title)}</div>
        <div class="card-actions">
          <button class="action-btn copy-btn" title="Copy prompt">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
              <rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>
            </svg>
          </button>
          <button class="action-btn delete delete-btn" title="Delete">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
              <polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M9 6V4h6v2"/>
            </svg>
          </button>
        </div>
      </div>
      <div class="card-preview">${esc(p.text)}</div>
      <div class="card-footer">
        <span class="cat-pill cat-${p.category}">${p.category}</span>
        <div class="card-tags">${tagsHtml}</div>
      </div>
    `;

    // Copy on card click or copy button
    card.querySelector(".copy-btn").addEventListener("click", (e) => {
      e.stopPropagation();
      copyPrompt(p, card.querySelector(".copy-btn"));
    });
    card.addEventListener("click", () => copyPrompt(p, card.querySelector(".copy-btn")));

    card.querySelector(".delete-btn").addEventListener("click", (e) => {
      e.stopPropagation();
      deletePrompt(p.id, card);
    });

    list.appendChild(card);
  });
}

function copyPrompt(p, btn) {
  navigator.clipboard.writeText(p.text).then(() => {
    // Increment usedCount
    const idx = prompts.findIndex(x => x.id === p.id);
    if (idx !== -1) { prompts[idx].usedCount = (prompts[idx].usedCount || 0) + 1; savePrompts(); }

    // Visual feedback
    btn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><polyline points="20 6 9 17 4 12"/></svg>`;
    btn.classList.add("copied");
    showToast("Copied to clipboard!");
    setTimeout(() => {
      btn.innerHTML = `<svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>`;
      btn.classList.remove("copied");
    }, 1500);
  });
}

function deletePrompt(id, cardEl) {
  prompts = prompts.filter(p => p.id !== id);
  savePrompts();
  cardEl.style.opacity = "0";
  cardEl.style.transform = "translateX(20px)";
  cardEl.style.transition = "all 0.2s ease";
  setTimeout(() => { cardEl.remove(); if (getFiltered().length === 0) document.getElementById("emptyState").style.display = "flex"; }, 200);
}

// --- Add Form ---
document.getElementById("toggleAdd").addEventListener("click", () => {
  const form = document.getElementById("addForm");
  const isVisible = form.style.display !== "none";
  form.style.display = isVisible ? "none" : "flex";
  if (!isVisible) document.getElementById("newTitle").focus();
});

document.getElementById("cancelAdd").addEventListener("click", () => {
  document.getElementById("addForm").style.display = "none";
  clearForm();
});

document.getElementById("saveNew").addEventListener("click", () => {
  const title = document.getElementById("newTitle").value.trim();
  const text = document.getElementById("newText").value.trim();
  if (!title || !text) { showToast("Title and text required", true); return; }

  const tagsRaw = document.getElementById("newTags").value;
  const tags = tagsRaw.split(",").map(t => t.trim()).filter(Boolean);
  const category = document.getElementById("newCategory").value;

  const newPrompt = { id: Date.now(), title, text, category, tags, createdAt: new Date().toISOString(), usedCount: 0 };
  prompts.unshift(newPrompt);
  savePrompts();

  document.getElementById("addForm").style.display = "none";
  clearForm();
  render();
  showToast("Prompt saved!");
});

function clearForm() {
  document.getElementById("newTitle").value = "";
  document.getElementById("newText").value = "";
  document.getElementById("newTags").value = "";
  document.getElementById("newCategory").value = "general";
}

// --- Search ---
document.getElementById("searchInput").addEventListener("input", (e) => {
  searchQuery = e.target.value;
  render();
});

// --- Tabs ---
document.querySelectorAll(".tab").forEach(tab => {
  tab.addEventListener("click", () => {
    document.querySelectorAll(".tab").forEach(t => t.classList.remove("active"));
    tab.classList.add("active");
    currentCat = tab.dataset.cat;
    render();
  });
});

// --- Toast ---
function showToast(msg, isError = false) {
  const toast = document.getElementById("toast");
  toast.textContent = msg;
  toast.style.background = isError ? "#ef4444" : "#22c55e";
  toast.classList.add("show");
  setTimeout(() => toast.classList.remove("show"), 2000);
}

// --- Util ---
function esc(str) {
  return String(str).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
}

// --- Init ---
loadPrompts(render);

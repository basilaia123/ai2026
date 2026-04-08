chrome.runtime.onInstalled.addListener(() => {
  chrome.contextMenus.create({
    id: "savePrompt",
    title: "Save as AI Prompt",
    contexts: ["selection"]
  });

  // Pre-load sample prompts on first install
  chrome.storage.local.get("prompts", (data) => {
    if (!data.prompts) {
      const samples = [
        {
          id: Date.now() + 1,
          title: "Explain Like I'm 5",
          text: "Explain the following concept in simple terms, as if you're explaining it to a 5-year-old:\n\n[TOPIC]",
          category: "general",
          tags: ["explain", "simple"],
          createdAt: new Date().toISOString(),
          usedCount: 0
        },
        {
          id: Date.now() + 2,
          title: "Professional Email",
          text: "Write a professional email for the following situation:\n\n[SITUATION]\n\nTone: formal but friendly. Keep it concise.",
          category: "work",
          tags: ["email", "writing"],
          createdAt: new Date().toISOString(),
          usedCount: 0
        },
        {
          id: Date.now() + 3,
          title: "Debug & Explain",
          text: "Debug the following code and explain what was wrong and why your fix works:\n\n```\n[CODE]\n```",
          category: "code",
          tags: ["debug", "code"],
          createdAt: new Date().toISOString(),
          usedCount: 0
        },
        {
          id: Date.now() + 4,
          title: "Generate Creative Ideas",
          text: "Generate 10 creative and unique ideas for:\n\n[TOPIC]\n\nFor each idea, provide a brief one-sentence description.",
          category: "creative",
          tags: ["ideas", "brainstorm"],
          createdAt: new Date().toISOString(),
          usedCount: 0
        }
      ];
      chrome.storage.local.set({ prompts: samples });
    }
  });
});

chrome.contextMenus.onClicked.addListener((info) => {
  if (info.menuItemId === "savePrompt" && info.selectionText) {
    chrome.storage.local.get("prompts", (data) => {
      const prompts = data.prompts || [];
      const newPrompt = {
        id: Date.now(),
        title: info.selectionText.slice(0, 50) + (info.selectionText.length > 50 ? "..." : ""),
        text: info.selectionText,
        category: "general",
        tags: [],
        createdAt: new Date().toISOString(),
        usedCount: 0
      };
      prompts.unshift(newPrompt);
      chrome.storage.local.set({ prompts });
    });
  }
});

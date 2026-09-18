import { GAME_HTML } from "./html.js";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS Preflight
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
        },
      });
    }

    // 1. API: Get Global High Scores Leaderboard
    if (path === "/api/scores" && request.method === "GET") {
      const scores = await getScores(env);
      return Response.json(scores, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Cache-Control": "no-cache",
        },
      });
    }

    // 2. API: Submit New Score
    if (path === "/api/score" && request.method === "POST") {
      try {
        const body = await request.json();
        const playerName = (body.name || "Bowler").trim().slice(0, 15);
        const score = Math.max(0, Math.min(300, parseInt(body.score) || 0));
        const strikes = Math.max(0, parseInt(body.strikes) || 0);
        const country = request.cf?.country || "GE";
        const colo = request.cf?.colo || "TBS";
        const city = request.cf?.city || "Tbilisi";

        const newEntry = {
          name: playerName,
          score,
          strikes,
          country,
          colo,
          city,
          date: new Date().toISOString(),
        };

        const updated = await addScore(env, newEntry);
        return Response.json({ success: true, entry: newEntry, leaderboard: updated }, {
          headers: { "Access-Control-Allow-Origin": "*" },
        });
      } catch (err) {
        return Response.json({ error: err.message }, { status: 400 });
      }
    }

    // 3. API: Character Roster Info
    if (path === "/api/characters" && request.method === "GET") {
      const characters = [
        { id: "penguin", name: "Penguin", description: "Tuxedo weeble with pink blush and gift box" },
        { id: "rubble", name: "Rubble", description: "Paw Patrol pup with yellow safety helmet" },
        { id: "spongebob", name: "SpongeBob", description: "Sunny sponge with spatula & Krabby Patty" },
        { id: "kitty_watermelon", name: "Watermelon Kitty", description: "Hello Kitty in watermelon rind suit" },
        { id: "kitty_strawberry", name: "Strawberry Kitty", description: "Hello Kitty with strawberry leaf cap" },
        { id: "astro_bot", name: "Astro Bot", description: "Cyber astronaut with glowing LED visor" },
      ];
      return Response.json(characters, {
        headers: { "Access-Control-Allow-Origin": "*", "Cache-Control": "public, max-age=3600" },
      });
    }

    // 4. Default: Serve 3D Bowling Game HTML at Edge
    return new Response(GAME_HTML, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "no-cache",
        "X-Edge-Region": request.cf?.colo || "EDGE",
      },
    });
  },
};

// ==================== KV STORAGE WITH IN-MEMORY FALLBACK ====================

const DEFAULT_SCORES = [
  { name: "Basilaia Pro", score: 278, strikes: 9, country: "GE", colo: "TBS" },
  { name: "SpongeStriker", score: 245, strikes: 7, country: "US", colo: "SJC" },
  { name: "KittyBowler", score: 210, strikes: 6, country: "DE", colo: "FRA" },
  { name: "AstroStrike", score: 195, strikes: 5, country: "JP", colo: "NRT" },
  { name: "RubbleDigger", score: 172, strikes: 4, country: "GB", colo: "LHR" },
];

let memoryScores = null;

async function getScores(env) {
  if (env && env.BOWLING_KV) {
    try {
      const raw = await env.BOWLING_KV.get("leaderboard");
      if (raw) return JSON.parse(raw);
    } catch (e) {
      console.warn("KV get error:", e);
    }
  }
  if (!memoryScores) {
    memoryScores = [...DEFAULT_SCORES];
  }
  return memoryScores;
}

async function addScore(env, newEntry) {
  const scores = await getScores(env);
  scores.push(newEntry);
  scores.sort((a, b) => b.score - a.score);
  const top15 = scores.slice(0, 15);

  if (env && env.BOWLING_KV) {
    try {
      await env.BOWLING_KV.put("leaderboard", JSON.stringify(top15));
    } catch (e) {
      console.warn("KV put error:", e);
    }
  }
  memoryScores = top15;
  return top15;
}

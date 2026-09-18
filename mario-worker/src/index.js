import { GAME_HTML } from "./html.js";

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // CORS
    if (request.method === "OPTIONS") {
      return new Response(null, {
        headers: {
          "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
          "Access-Control-Allow-Headers": "Content-Type",
        },
      });
    }

    // 1. API: Get Leaderboard
    if (path === "/api/scores" && request.method === "GET") {
      const scores = await getScores(env);
      return Response.json(scores, {
        headers: { "Access-Control-Allow-Origin": "*", "Cache-Control": "no-cache" },
      });
    }

    // 2. API: Submit High Score
    if (path === "/api/score" && request.method === "POST") {
      try {
        const body = await request.json();
        const playerName = (body.name || "Player").trim().slice(0, 15);
        const score = parseInt(body.score) || 0;
        const coins = parseInt(body.coins) || 0;
        const time = parseInt(body.time) || 0;
        const country = request.cf?.country || "GE";
        const colo = request.cf?.colo || "TBS";

        const newEntry = {
          name: playerName,
          score,
          coins,
          time,
          country,
          colo,
          date: new Date().toISOString(),
        };

        const updatedLeaderboard = await addScore(env, newEntry);
        return Response.json({ success: true, leaderboard: updatedLeaderboard }, {
          headers: { "Access-Control-Allow-Origin": "*" },
        });
      } catch (err) {
        return Response.json({ error: err.message }, { status: 500 });
      }
    }

    // 3. API: Get Speedrun Ghost Record
    if (path === "/api/ghost" && request.method === "GET") {
      try {
        let ghost = null;
        if (env.MARIO_KV) {
          const raw = await env.MARIO_KV.get("speedrun_ghost");
          if (raw) ghost = JSON.parse(raw);
        }
        return Response.json(ghost || {
          name: "EdgeChampion",
          time: 39.5,
          country: "GE",
          path: [],
        }, {
          headers: { "Access-Control-Allow-Origin": "*", "Cache-Control": "no-cache" },
        });
      } catch (e) {
        return Response.json({ error: e.message }, { status: 500 });
      }
    }

    // 4. API: Submit Speedrun Ghost Replay
    if (path === "/api/ghost" && request.method === "POST") {
      try {
        const body = await request.json();
        const time = parseFloat(body.time) || 999;
        const name = (body.name || "Runner").trim().slice(0, 15);
        const country = request.cf?.country || "GE";
        const pathData = Array.isArray(body.path) ? body.path.slice(0, 800) : [];

        let currentRecord = null;
        if (env.MARIO_KV) {
          const raw = await env.MARIO_KV.get("speedrun_ghost");
          if (raw) currentRecord = JSON.parse(raw);
        }

        const isNewRecord = !currentRecord || time < (currentRecord.time || 999);
        if (isNewRecord && env.MARIO_KV) {
          const newRecordData = { name, time, country, path: pathData, date: new Date().toISOString() };
          await env.MARIO_KV.put("speedrun_ghost", JSON.stringify(newRecordData));
          return Response.json({ success: true, newRecord: true, record: newRecordData }, {
            headers: { "Access-Control-Allow-Origin": "*" },
          });
        }

        return Response.json({ success: true, newRecord: false, record: currentRecord }, {
          headers: { "Access-Control-Allow-Origin": "*" },
        });
      } catch (e) {
        return Response.json({ error: e.message }, { status: 500 });
      }
    }

    // 5. Serve Game HTML
    return new Response(GAME_HTML, {
      headers: {
        "Content-Type": "text/html; charset=utf-8",
        "Cache-Control": "no-cache",
      },
    });
  },
};

// ==================== KV STORAGE ====================

const DEFAULT_SCORES = [
  { name: "MarioMaster", score: 12500, coins: 34, country: "GE", colo: "TBS" },
  { name: "LuigiSpeed", score: 9800, coins: 28, country: "US", colo: "SJC" },
  { name: "Peach101", score: 7400, coins: 19, country: "DE", colo: "FRA" },
  { name: "YoshiJump", score: 5200, coins: 14, country: "GB", colo: "LHR" },
];

async function getScores(env) {
  if (env.MARIO_KV) {
    const raw = await env.MARIO_KV.get("leaderboard");
    if (raw) return JSON.parse(raw);
  }
  return DEFAULT_SCORES;
}

async function addScore(env, newEntry) {
  const scores = await getScores(env);
  scores.push(newEntry);
  scores.sort((a, b) => b.score - a.score);
  const top10 = scores.slice(0, 10);

  if (env.MARIO_KV) {
    await env.MARIO_KV.put("leaderboard", JSON.stringify(top10));
  }
  return top10;
}

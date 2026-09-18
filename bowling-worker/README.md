# Weeble 3D Bowling • Cloudflare Worker

A full 3D bowling game starring the 6 collectible capsule wobbler characters, built with **Three.js** and **Cannon.js** physics, deployed to **Cloudflare Workers**.

---

## The 6 Characters
1. 🐧 **Penguin** (Tuxedo weeble with pink blush cheeks, green gift box & pink ribbon)
2. 👷 **Rubble** (Paw Patrol pup with yellow construction safety helmet & badge)
3. 🍔 **SpongeBob** (Porous sponge with chef spatula & Krabby Patty burger)
4. 🍉 **Watermelon Hello Kitty** (Watermelon rind hood, striped shell, melon slice)
5. 🍓 **Strawberry Hello Kitty** (Green leaf stem cap, strawberry seed suit, fresh strawberry)
6. 🤖 **Astro Bot** (Cyber astronaut with glowing neon-lime LED eyes & space suit)

---

## Local Development & Preview

### Option A: Open directly in your browser (No installation required)
```powershell
start bowling/index.html
```

### Option B: Run Cloudflare Worker locally with Wrangler
```powershell
cd bowling-worker
npx wrangler dev
```
Open `http://localhost:8787` in your browser.

---

## Deploy to Cloudflare Workers

1. Make sure you are logged into Cloudflare:
   ```powershell
   npx wrangler login
   ```

2. Create a KV namespace for the leaderboard (optional, has memory fallback):
   ```powershell
   npx wrangler kv:namespace create BOWLING_KV
   ```
   Paste the returned namespace ID into `wrangler.jsonc`.

3. Deploy globally:
   ```powershell
   npx wrangler deploy
   ```

---

## Worker Endpoints

- `GET /` — Serves the high-performance 3D game HTML worldwide at the edge (< 20ms latency).
- `GET /api/scores` — Returns top scores from the global leaderboard.
- `POST /api/score` — Submits a high score, automatically enriched with Cloudflare edge location (`country`, `city`, `colo`).
- `GET /api/characters` — Returns metadata for all 6 characters.

const fs = require('fs');
const path = require('path');

const gameHtml = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
  <title>Super Mario Edge • Cloudflare Workers</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; }
    body {
      background: #0f172a;
      color: #fff;
      font-family: 'Press Start 2P', cursive;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      overflow: hidden;
    }
    #gameWrapper {
      position: relative;
      width: 100%;
      max-width: 800px;
      background: #000;
      border: 4px solid #334155;
      border-radius: 12px;
      box-shadow: 0 20px 50px rgba(0,0,0,0.8);
      overflow: hidden;
    }
    canvas {
      display: block;
      width: 100%;
      height: auto;
      image-rendering: pixelated;
    }
    .hud {
      position: absolute;
      top: 10px;
      left: 0;
      width: 100%;
      display: flex;
      justify-content: space-around;
      font-size: 11px;
      text-shadow: 2px 2px #000;
      pointer-events: none;
      z-index: 10;
    }
    .hud-col { display: flex; flex-direction: column; align-items: center; gap: 4px; }
    .overlay {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(0,0,0,0.85);
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 20;
      text-align: center;
      padding: 20px;
    }
    .overlay.hidden { display: none !important; }
    .overlay h1 {
      font-size: 22px;
      color: #f87171;
      margin-bottom: 20px;
      text-shadow: 3px 3px #000;
      line-height: 1.4;
    }
    .overlay p {
      font-size: 10px;
      line-height: 1.8;
      color: #cbd5e1;
      margin-bottom: 20px;
    }
    .btn {
      font-family: 'Press Start 2P', cursive;
      font-size: 11px;
      background: #e11d48;
      color: #fff;
      border: 3px solid #fff;
      padding: 12px 20px;
      cursor: pointer;
      box-shadow: 0 4px #000;
      transition: all 0.1s;
      margin: 6px;
    }
    .btn:hover { background: #f43f5e; transform: translateY(-2px); }
    .btn:active { transform: translateY(2px); box-shadow: 0 0 #000; }
    .name-input {
      font-family: 'Press Start 2P', cursive;
      font-size: 12px;
      padding: 10px;
      background: #1e293b;
      border: 2px solid #fff;
      color: #fff;
      text-align: center;
      margin-bottom: 14px;
      outline: none;
      width: 240px;
    }
    .leaderboard-table {
      width: 100%;
      max-width: 460px;
      font-size: 9px;
      margin-bottom: 16px;
      border-collapse: collapse;
    }
    .leaderboard-table th, .leaderboard-table td {
      padding: 8px 6px;
      border-bottom: 1px solid #334155;
    }
    .leaderboard-table th { color: #f59e0b; }
    #mobileControls {
      display: none;
      width: 100%;
      max-width: 800px;
      margin-top: 10px;
      justify-content: space-between;
      padding: 0 10px;
    }
    .d-pad, .action-btns { display: flex; gap: 10px; }
    .m-btn {
      width: 55px;
      height: 55px;
      background: #1e293b;
      border: 2px solid #475569;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 14px;
      color: #fff;
      font-family: sans-serif;
      touch-action: manipulation;
    }
    .m-btn:active { background: #e11d48; }
    @media(max-width: 768px) {
      #mobileControls { display: flex; }
      .hud { font-size: 8px; }
      .overlay h1 { font-size: 18px; }
    }
  </style>
</head>
<body>

  <div id="gameWrapper">
    <div class="hud">
      <div class="hud-col">
        <span>MARIO</span>
        <span id="hudScore">000000</span>
      </div>
      <div class="hud-col">
        <span>COINS</span>
        <span id="hudCoins">x00</span>
      </div>
      <div class="hud-col">
        <span>WORLD</span>
        <span>1-1</span>
      </div>
      <div class="hud-col">
        <span>TIME</span>
        <span id="hudTime">400</span>
      </div>
      <div class="hud-col">
        <span>LIVES</span>
        <span id="hudLives">x3</span>
      </div>
    </div>

    <canvas id="gameCanvas" width="512" height="288"></canvas>

    <!-- Start Overlay -->
    <div class="overlay" id="startOverlay">
      <h1 style="color: #e11d48;">SUPER MARIO EDGE</h1>
      <p>Arrow Keys / WASD = Move<br>Space / Up / Z = Jump<br>Shift / X = Sprint / Fire</p>
      <button class="btn" id="btnStartGame">START GAME</button>
      <button class="btn" style="background:#3b82f6;" id="btnShowLeaderboard">LEADERBOARD</button>
    </div>

    <!-- Game Over Overlay -->
    <div class="overlay hidden" id="gameOverOverlay">
      <h1>GAME OVER</h1>
      <p id="finalScoreMsg">SCORE: 0</p>
      <input type="text" class="name-input" id="playerNameInput" placeholder="YOUR NAME" maxlength="12">
      <div>
        <button class="btn" id="btnSubmitScore">SAVE SCORE</button>
        <button class="btn" style="background:#475569;" id="btnRetryGame">RETRY</button>
      </div>
    </div>

    <!-- Victory Overlay -->
    <div class="overlay hidden" id="victoryOverlay">
      <h1 style="color: #22c55e;">STAGE CLEAR!</h1>
      <p id="victoryScoreMsg">YOU SAVED THE EDGE!</p>
      <input type="text" class="name-input" id="victoryNameInput" placeholder="YOUR NAME" maxlength="12">
      <div>
        <button class="btn" id="btnSubmitVictory">SUBMIT SCORE</button>
        <button class="btn" style="background:#475569;" id="btnPlayAgain">PLAY AGAIN</button>
      </div>
    </div>

    <!-- Leaderboard Overlay -->
    <div class="overlay hidden" id="leaderboardOverlay">
      <h1 style="color: #f59e0b;">TOP PLAYERS</h1>
      <table class="leaderboard-table">
        <thead>
          <tr><th>#</th><th>NAME</th><th>SCORE</th><th>COINS</th><th>REGION</th></tr>
        </thead>
        <tbody id="leaderboardBody">
          <tr><td colspan="5">Loading scores...</td></tr>
        </tbody>
      </table>
      <button class="btn" id="btnHideLeaderboard">BACK</button>
    </div>
  </div>

  <div id="mobileControls">
    <div class="d-pad">
      <div class="m-btn" id="mLeft">◀</div>
      <div class="m-btn" id="mRight">▶</div>
    </div>
    <div class="action-btns">
      <div class="m-btn" id="mFire" style="background:#f97316;">B</div>
      <div class="m-btn" id="mJump" style="background:#22c55e;">A</div>
    </div>
  </div>

  <script>
    // Audio Synth
    let audioCtx = null;
    function getAudio() {
      if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      return audioCtx;
    }

    function playSound(type) {
      try {
        const ctx = getAudio();
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.connect(gain);
        gain.connect(ctx.destination);
        const now = ctx.currentTime;

        if (type === 'jump') {
          osc.type = 'square';
          osc.frequency.setValueAtTime(150, now);
          osc.frequency.exponentialRampToValueAtTime(600, now + 0.15);
          gain.gain.setValueAtTime(0.15, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.15);
          osc.start(now);
          osc.stop(now + 0.15);
        } else if (type === 'coin') {
          osc.type = 'sine';
          osc.frequency.setValueAtTime(987.77, now);
          osc.frequency.setValueAtTime(1318.51, now + 0.08);
          gain.gain.setValueAtTime(0.2, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.35);
          osc.start(now);
          osc.stop(now + 0.35);
        } else if (type === 'stomp') {
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(200, now);
          osc.frequency.exponentialRampToValueAtTime(50, now + 0.1);
          gain.gain.setValueAtTime(0.25, now);
          gain.gain.exponentialRampToValueAtTime(0.01, now + 0.1);
          osc.start(now);
          osc.stop(now + 0.1);
        } else if (type === 'powerup') {
          const notes = [330, 392, 659, 523, 587, 784];
          notes.forEach((freq, idx) => {
            const o = ctx.createOscillator();
            const g = ctx.createGain();
            o.connect(g);
            g.connect(ctx.destination);
            o.frequency.setValueAtTime(freq, now + idx * 0.06);
            g.gain.setValueAtTime(0.15, now + idx * 0.06);
            g.gain.exponentialRampToValueAtTime(0.01, now + (idx + 1) * 0.06);
            o.start(now + idx * 0.06);
            o.stop(now + (idx + 1) * 0.06);
          });
        } else if (type === 'gameover') {
          const notes = [400, 350, 300, 200];
          notes.forEach((freq, idx) => {
            const o = ctx.createOscillator();
            const g = ctx.createGain();
            o.connect(g);
            g.connect(ctx.destination);
            o.type = 'triangle';
            o.frequency.setValueAtTime(freq, now + idx * 0.12);
            g.gain.setValueAtTime(0.2, now + idx * 0.12);
            g.gain.exponentialRampToValueAtTime(0.01, now + (idx + 1) * 0.12);
            o.start(now + idx * 0.12);
            o.stop(now + (idx + 1) * 0.12);
          });
        }
      } catch (e) {}
    }

    // Canvas & Game Variables
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const TILE_SIZE = 16;
    const LEVEL_WIDTH = 220;
    const LEVEL_HEIGHT = 18;

    let gameState = 'START';
    let cameraX = 0;
    let score = 0;
    let coins = 0;
    let lives = 3;
    let timeLeft = 400;
    let timerInterval = null;

    const keys = { left: false, right: false, jump: false, fire: false };

    const mario = {
      x: 40,
      y: 190,
      vx: 0,
      vy: 0,
      w: 12,
      h: 16,
      isGrounded: false,
      isBig: false,
      facing: 'right',
      invulnerableTimer: 0,
    };

    let enemies = [];
    let items = [];
    let levelGrid = [];

    function buildLevel() {
      levelGrid = Array.from({ length: LEVEL_HEIGHT }, () => Array(LEVEL_WIDTH).fill(0));
      enemies = [];
      items = [];

      for (let x = 0; x < LEVEL_WIDTH; x++) {
        if ((x >= 68 && x <= 70) || (x >= 86 && x <= 89) || (x >= 150 && x <= 153)) continue;
        levelGrid[16][x] = 1;
        levelGrid[17][x] = 1;
      }

      addBlock(16, 12, 3);
      addBlock(20, 12, 2);
      addBlock(22, 12, 4);
      addBlock(24, 12, 2);
      addBlock(23, 8, 3);

      addPipe(28, 14, 2);
      addPipe(38, 13, 3);
      addPipe(46, 12, 4);

      enemies.push({ type: 'goomba', x: 22 * 16, y: 15 * 16, vx: -0.6, alive: true, flatTimer: 0 });
      enemies.push({ type: 'goomba', x: 34 * 16, y: 15 * 16, vx: -0.6, alive: true, flatTimer: 0 });
      enemies.push({ type: 'koopa', x: 52 * 16, y: 15 * 16, vx: -0.7, alive: true });

      for (let x = 77; x <= 84; x++) addBlock(x, 12, (x === 78 || x === 82) ? 3 : 2);
      for (let x = 80; x <= 87; x++) addBlock(x, 8, 2);

      enemies.push({ type: 'goomba', x: 92 * 16, y: 15 * 16, vx: -0.6, alive: true, flatTimer: 0 });
      enemies.push({ type: 'goomba', x: 95 * 16, y: 15 * 16, vx: -0.6, alive: true, flatTimer: 0 });
      enemies.push({ type: 'koopa', x: 105 * 16, y: 15 * 16, vx: -0.7, alive: true });

      for (let step = 1; step <= 8; step++) {
        for (let row = 16 - step; row < 16; row++) levelGrid[row][135 + step] = 1;
      }
      for (let step = 1; step <= 8; step++) {
        for (let row = 16 - (9 - step); row < 16; row++) levelGrid[row][145 + step] = 1;
      }

      for (let y = 3; y < 16; y++) levelGrid[y][190] = 9;
      for (let y = 11; y < 16; y++) {
        for (let x = 198; x < 205; x++) levelGrid[y][x] = 10;
      }
    }

    function addBlock(x, y, type) {
      if (y < LEVEL_HEIGHT && x < LEVEL_WIDTH) levelGrid[y][x] = type;
    }

    function addPipe(x, y, height) {
      levelGrid[y][x] = 5;
      levelGrid[y][x+1] = 6;
      for (let r = y + 1; r < 16; r++) {
        levelGrid[r][x] = 7;
        levelGrid[r][x+1] = 8;
      }
    }

    function startGame() {
      hideAllOverlays();
      getAudio();
      score = 0;
      coins = 0;
      lives = 3;
      timeLeft = 400;
      resetMario();
      buildLevel();
      gameState = 'PLAYING';

      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {
        if (gameState === 'PLAYING') {
          timeLeft--;
          document.getElementById('hudTime').innerText = String(timeLeft).padStart(3, '0');
          if (timeLeft <= 0) killMario();
        }
      }, 1000);

      requestAnimationFrame(gameLoop);
    }

    function resetMario() {
      mario.x = 40;
      mario.y = 190;
      mario.vx = 0;
      mario.vy = 0;
      mario.h = mario.isBig ? 24 : 16;
      mario.isGrounded = false;
      mario.invulnerableTimer = 0;
      cameraX = 0;
    }

    function update() {
      if (gameState !== 'PLAYING') return;

      const maxSpeed = keys.fire ? 3.0 : 2.0;
      const accel = 0.15;
      const friction = 0.85;

      if (keys.left) {
        mario.vx -= accel;
        mario.facing = 'left';
      } else if (keys.right) {
        mario.vx += accel;
        mario.facing = 'right';
      } else {
        mario.vx *= friction;
        if (Math.abs(mario.vx) < 0.05) mario.vx = 0;
      }

      mario.vx = Math.max(-maxSpeed, Math.min(maxSpeed, mario.vx));
      mario.vy += 0.45;
      if (mario.vy > 8) mario.vy = 8;

      if (keys.jump && mario.isGrounded) {
        mario.vy = -7.8;
        mario.isGrounded = false;
        playSound('jump');
      }

      mario.x += mario.vx;
      handleTileCollision(true);

      mario.y += mario.vy;
      mario.isGrounded = false;
      handleTileCollision(false);

      if (mario.x - cameraX > 200) cameraX = mario.x - 200;
      if (mario.x < cameraX) mario.x = cameraX;

      if (mario.y > 300) killMario();
      if (mario.x >= 190 * 16 && gameState === 'PLAYING') victory();

      enemies.forEach((enemy) => {
        if (!enemy.alive) {
          if (enemy.flatTimer > 0) enemy.flatTimer--;
          return;
        }

        enemy.x += enemy.vx;
        const tileX = Math.floor((enemy.x + (enemy.vx > 0 ? 14 : 0)) / 16);
        const tileY = Math.floor((enemy.y + 8) / 16);
        if (getTile(tileX, tileY) > 0) enemy.vx *= -1;

        const dx = (mario.x + mario.w/2) - (enemy.x + 8);
        const dy = (mario.y + mario.h/2) - (enemy.y + 8);
        const dist = Math.sqrt(dx*dx + dy*dy);

        if (dist < 14) {
          if (mario.vy > 0 && mario.y + mario.h - mario.vy <= enemy.y + 6) {
            enemy.alive = false;
            enemy.flatTimer = 30;
            mario.vy = -5.5;
            score += 200;
            playSound('stomp');
          } else if (mario.invulnerableTimer === 0) {
            if (mario.isBig) {
              mario.isBig = false;
              mario.h = 16;
              mario.invulnerableTimer = 60;
              playSound('powerup');
            } else {
              killMario();
            }
          }
        }
      });

      items.forEach((item) => {
        item.y += item.vy || 0;
        item.x += item.vx || 0;
        const dx = (mario.x + mario.w/2) - (item.x + 8);
        const dy = (mario.y + mario.h/2) - (item.y + 8);
        if (Math.sqrt(dx*dx + dy*dy) < 14) {
          item.collected = true;
          if (item.type === 'mushroom') {
            mario.isBig = true;
            mario.h = 24;
            score += 1000;
            playSound('powerup');
          }
        }
      });
      items = items.filter(i => !i.collected);

      if (mario.invulnerableTimer > 0) mario.invulnerableTimer--;

      document.getElementById('hudScore').innerText = String(score).padStart(6, '0');
      document.getElementById('hudCoins').innerText = 'x' + String(coins).padStart(2, '0');
      document.getElementById('hudLives').innerText = 'x' + lives;
    }

    function handleTileCollision(isXAxis) {
      const leftTile = Math.floor(mario.x / TILE_SIZE);
      const rightTile = Math.floor((mario.x + mario.w - 1) / TILE_SIZE);
      const topTile = Math.floor(mario.y / TILE_SIZE);
      const bottomTile = Math.floor((mario.y + mario.h - 1) / TILE_SIZE);

      for (let ty = topTile; ty <= bottomTile; ty++) {
        for (let tx = leftTile; tx <= rightTile; tx++) {
          const tile = getTile(tx, ty);
          if (tile > 0 && tile !== 9 && tile !== 10) {
            if (isXAxis) {
              if (mario.vx > 0) mario.x = tx * TILE_SIZE - mario.w;
              else if (mario.vx < 0) mario.x = (tx + 1) * TILE_SIZE;
              mario.vx = 0;
            } else {
              if (mario.vy > 0) {
                mario.y = ty * TILE_SIZE - mario.h;
                mario.vy = 0;
                mario.isGrounded = true;
              } else if (mario.vy < 0) {
                mario.y = (ty + 1) * TILE_SIZE;
                mario.vy = 0;
                bumpBlock(tx, ty, tile);
              }
            }
          }
        }
      }
    }

    function getTile(x, y) {
      if (x < 0 || x >= LEVEL_WIDTH || y < 0 || y >= LEVEL_HEIGHT) return 0;
      return levelGrid[y][x];
    }

    function bumpBlock(tx, ty, tile) {
      if (tile === 3) {
        levelGrid[ty][tx] = 1;
        coins++;
        score += 200;
        playSound('coin');
      } else if (tile === 4) {
        levelGrid[ty][tx] = 1;
        items.push({ type: 'mushroom', x: tx * 16, y: (ty - 1) * 16, vx: 0.8, vy: 0 });
        playSound('powerup');
      } else if (tile === 2) {
        if (mario.isBig) {
          levelGrid[ty][tx] = 0;
          score += 50;
        }
        playSound('stomp');
      }
    }

    function killMario() {
      lives--;
      playSound('gameover');
      if (lives <= 0) {
        gameState = 'GAMEOVER';
        document.getElementById('finalScoreMsg').innerText = 'FINAL SCORE: ' + score;
        document.getElementById('gameOverOverlay').classList.remove('hidden');
      } else {
        resetMario();
      }
    }

    function victory() {
      gameState = 'VICTORY';
      score += timeLeft * 50;
      playSound('powerup');
      document.getElementById('victoryScoreMsg').innerText = 'FINAL SCORE: ' + score + ' (BONUS: +' + (timeLeft * 50) + ')';
      document.getElementById('victoryOverlay').classList.remove('hidden');
    }

    function render() {
      ctx.fillStyle = '#5c94fc';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      ctx.save();
      ctx.translate(-Math.floor(cameraX), 0);

      renderScenery();

      const startCol = Math.floor(cameraX / 16);
      const endCol = startCol + Math.ceil(canvas.width / 16) + 1;

      for (let y = 0; y < LEVEL_HEIGHT; y++) {
        for (let x = startCol; x < endCol; x++) {
          const tile = getTile(x, y);
          if (tile > 0) drawTile(tile, x * 16, y * 16);
        }
      }

      items.forEach(item => {
        ctx.fillStyle = '#ef4444';
        ctx.beginPath();
        ctx.arc(item.x + 8, item.y + 8, 7, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#fff';
        ctx.fillRect(item.x + 6, item.y + 6, 4, 4);
      });

      enemies.forEach(enemy => {
        if (!enemy.alive && enemy.flatTimer <= 0) return;
        if (enemy.type === 'goomba') {
          if (!enemy.alive) {
            ctx.fillStyle = '#9a3412';
            ctx.fillRect(enemy.x, enemy.y + 10, 16, 6);
          } else {
            ctx.fillStyle = '#9a3412';
            ctx.beginPath();
            ctx.arc(enemy.x + 8, enemy.y + 7, 7, Math.PI, 0);
            ctx.fill();
            ctx.fillStyle = '#fed7aa';
            ctx.fillRect(enemy.x + 3, enemy.y + 7, 10, 6);
            ctx.fillStyle = '#000';
            ctx.fillRect(enemy.x + 4, enemy.y + 6, 2, 4);
            ctx.fillRect(enemy.x + 10, enemy.y + 6, 2, 4);
          }
        } else if (enemy.type === 'koopa') {
          ctx.fillStyle = '#22c55e';
          ctx.fillRect(enemy.x + 2, enemy.y + 4, 12, 12);
          ctx.fillStyle = '#fef08a';
          ctx.fillRect(enemy.x + 4, enemy.y, 8, 6);
        }
      });

      if (mario.invulnerableTimer % 4 < 2) {
        drawMario(mario.x, mario.y, mario.w, mario.h, mario.facing, mario.isBig);
      }

      ctx.restore();
    }

    function renderScenery() {
      ctx.fillStyle = '#22c55e';
      for (let i = 0; i < LEVEL_WIDTH; i += 40) {
        ctx.beginPath();
        ctx.arc(i * 16, 256, 48, Math.PI, 0);
        ctx.fill();
      }
      ctx.fillStyle = 'rgba(255,255,255,0.85)';
      for (let i = 10; i < LEVEL_WIDTH; i += 30) {
        ctx.beginPath();
        ctx.arc(i * 16, 50, 16, 0, Math.PI * 2);
        ctx.arc(i * 16 + 14, 46, 20, 0, Math.PI * 2);
        ctx.arc(i * 16 + 28, 50, 16, 0, Math.PI * 2);
        ctx.fill();
      }
    }

    function drawTile(tile, x, y) {
      if (tile === 1) {
        ctx.fillStyle = '#b45309';
        ctx.fillRect(x, y, 16, 16);
        ctx.fillStyle = '#d97706';
        ctx.fillRect(x + 1, y + 1, 14, 14);
        ctx.fillStyle = '#78350f';
        ctx.strokeRect(x, y, 16, 16);
      } else if (tile === 2) {
        ctx.fillStyle = '#b91c1c';
        ctx.fillRect(x, y, 16, 16);
        ctx.strokeStyle = '#000';
        ctx.strokeRect(x, y, 16, 16);
      } else if (tile === 3 || tile === 4) {
        ctx.fillStyle = '#f59e0b';
        ctx.fillRect(x, y, 16, 16);
        ctx.strokeStyle = '#000';
        ctx.strokeRect(x, y, 16, 16);
        ctx.fillStyle = '#fff';
        ctx.font = '10px "Press Start 2P"';
        ctx.fillText('?', x + 4, y + 12);
      } else if (tile >= 5 && tile <= 8) {
        ctx.fillStyle = '#15803d';
        ctx.fillRect(x, y, 16, 16);
        ctx.fillStyle = '#22c55e';
        ctx.fillRect(x + 2, y, 4, 16);
        ctx.strokeStyle = '#000';
        ctx.strokeRect(x, y, 16, 16);
      } else if (tile === 9) {
        ctx.fillStyle = '#fff';
        ctx.fillRect(x + 7, y, 2, 16);
        if (y === 3) {
          ctx.fillStyle = '#22c55e';
          ctx.beginPath();
          ctx.arc(x + 8, y, 5, 0, Math.PI * 2);
          ctx.fill();
        }
      } else if (tile === 10) {
        ctx.fillStyle = '#64748b';
        ctx.fillRect(x, y, 16, 16);
        ctx.strokeStyle = '#334155';
        ctx.strokeRect(x, y, 16, 16);
      }
    }

    function drawMario(x, y, w, h, facing, isBig) {
      ctx.fillStyle = '#e11d48';
      ctx.fillRect(x, y, w, isBig ? 8 : 5);
      ctx.fillStyle = '#fed7aa';
      ctx.fillRect(facing === 'right' ? x + 4 : x, y + (isBig ? 6 : 4), 8, isBig ? 6 : 4);
      ctx.fillStyle = '#2563eb';
      ctx.fillRect(x + 2, y + (isBig ? 12 : 8), w - 4, isBig ? 8 : 5);
      ctx.fillStyle = '#78350f';
      ctx.fillRect(x, y + h - 3, w, 3);
    }

    function gameLoop() {
      update();
      render();
      if (gameState === 'PLAYING') {
        requestAnimationFrame(gameLoop);
      }
    }

    // Keyboard
    window.addEventListener('keydown', (e) => {
      if (e.code === 'ArrowLeft' || e.code === 'KeyA') keys.left = true;
      if (e.code === 'ArrowRight' || e.code === 'KeyD') keys.right = true;
      if (e.code === 'ArrowUp' || e.code === 'Space' || e.code === 'KeyW' || e.code === 'KeyZ') keys.jump = true;
      if (e.code === 'ShiftLeft' || e.code === 'ShiftRight' || e.code === 'KeyX') keys.fire = true;
    });

    window.addEventListener('keyup', (e) => {
      if (e.code === 'ArrowLeft' || e.code === 'KeyA') keys.left = false;
      if (e.code === 'ArrowRight' || e.code === 'KeyD') keys.right = false;
      if (e.code === 'ArrowUp' || e.code === 'Space' || e.code === 'KeyW' || e.code === 'KeyZ') keys.jump = false;
      if (e.code === 'ShiftLeft' || e.code === 'ShiftRight' || e.code === 'KeyX') keys.fire = false;
    });

    // Touch Controls
    const mLeft = document.getElementById('mLeft');
    const mRight = document.getElementById('mRight');
    const mJump = document.getElementById('mJump');
    const mFire = document.getElementById('mFire');

    mLeft.addEventListener('touchstart', (e) => { e.preventDefault(); keys.left = true; });
    mLeft.addEventListener('touchend', (e) => { e.preventDefault(); keys.left = false; });
    mRight.addEventListener('touchstart', (e) => { e.preventDefault(); keys.right = true; });
    mRight.addEventListener('touchend', (e) => { e.preventDefault(); keys.right = false; });
    mJump.addEventListener('touchstart', (e) => { e.preventDefault(); keys.jump = true; getAudio(); });
    mJump.addEventListener('touchend', (e) => { e.preventDefault(); keys.jump = false; });
    mFire.addEventListener('touchstart', (e) => { e.preventDefault(); keys.fire = true; });
    mFire.addEventListener('touchend', (e) => { e.preventDefault(); keys.fire = false; });

    // Overlay Event Listeners
    function hideAllOverlays() {
      document.querySelectorAll('.overlay').forEach(el => el.classList.add('hidden'));
    }

    document.getElementById('btnStartGame').addEventListener('click', startGame);
    document.getElementById('btnRetryGame').addEventListener('click', startGame);
    document.getElementById('btnPlayAgain').addEventListener('click', startGame);

    document.getElementById('btnShowLeaderboard').addEventListener('click', async () => {
      hideAllOverlays();
      document.getElementById('leaderboardOverlay').classList.remove('hidden');
      const tbody = document.getElementById('leaderboardBody');
      tbody.innerHTML = '<tr><td colspan="5">Loading scores...</td></tr>';
      try {
        const res = await fetch('/api/scores');
        const scores = await res.json();
        tbody.innerHTML = scores.map((s, idx) => \`
          <tr>
            <td>\${idx + 1}</td>
            <td style="color:#38bdf8;">\${escapeHtml(s.name)}</td>
            <td style="color:#f59e0b;">\${s.score}</td>
            <td>\${s.coins || 0}</td>
            <td>\${s.country || 'GE'}</td>
          </tr>
        \`).join('');
      } catch (e) {
        tbody.innerHTML = '<tr><td colspan="5">Failed to load</td></tr>';
      }
    });

    document.getElementById('btnHideLeaderboard').addEventListener('click', () => {
      hideAllOverlays();
      document.getElementById('startOverlay').classList.remove('hidden');
    });

    document.getElementById('btnSubmitScore').addEventListener('click', async () => {
      const name = document.getElementById('playerNameInput').value.trim() || 'Mario';
      await fetch('/api/score', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, score, coins, time: 400 - timeLeft }),
      });
      document.getElementById('btnShowLeaderboard').click();
    });

    document.getElementById('btnSubmitVictory').addEventListener('click', async () => {
      const name = document.getElementById('victoryNameInput').value.trim() || 'Hero';
      await fetch('/api/score', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, score, coins, time: 400 - timeLeft }),
      });
      document.getElementById('btnShowLeaderboard').click();
    });

    function escapeHtml(str) {
      return String(str).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
    }
  </script>
</body>
</html>`;

const out = `export const GAME_HTML = ${JSON.stringify(gameHtml)};\n`;
fs.writeFileSync(path.join(__dirname, 'src', 'html.js'), out, 'utf8');
console.log('src/html.js written successfully');

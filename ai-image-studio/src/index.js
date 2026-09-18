import { STUDIO_HTML } from './html.js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    // 1. Serve Studio Web App
    if (url.pathname === '/' || url.pathname === '/index.html') {
      return new Response(STUDIO_HTML, {
        headers: { 'Content-Type': 'text/html; charset=utf-8' },
      });
    }

    // 2. Prompt Enhancer using Groq LLM
    if (url.pathname === '/api/enhance-prompt' && request.method === 'POST') {
      try {
        const { prompt, style } = await request.json();
        if (!prompt) return jsonResponse({ error: 'Prompt is required' }, 400);

        const groqKey = env.GROQ_API_KEY;
        const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${groqKey}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: 'qwen/qwen3.8-27b',
            temperature: 0.7,
            max_tokens: 250,
            messages: [
              {
                role: 'system',
                content: 'You are an elite prompt engineer for FLUX and Midjourney. Expand the user prompt into a visually breathtaking, detailed prompt with lighting, camera angle, atmospheric textures, and mood. If a style is specified, lean heavily into that aesthetic. Output ONLY the enhanced prompt, no quotes, no conversational text.',
              },
              {
                role: 'user',
                content: `Base idea: "${prompt}". Style: "${style || 'photorealistic'}". Generate enhanced prompt:`,
              },
            ],
          }),
        });

        const data = await res.json();
        const enhanced = data.choices?.[0]?.message?.content?.trim() || prompt;
        return jsonResponse({ enhanced_prompt: enhanced });
      } catch (err) {
        return jsonResponse({ error: err.message }, 500);
      }
    }

    // 3. Image Generation via Workers AI
    if (url.pathname === '/api/generate' && request.method === 'POST') {
      try {
        const body = await request.json();
        const rawPrompt = body.prompt?.trim();
        if (!rawPrompt) return jsonResponse({ error: 'Prompt is required' }, 400);

        const model = body.model || '@cf/black-forest-labs/flux-1-schnell';
        const style = body.style || 'none';
        const ratio = body.aspect_ratio || '1:1';
        const negativePrompt = body.negative_prompt || 'blurry, bad anatomy, deformed, distorted, low quality, watermark';
        const steps = Math.min(Math.max(parseInt(body.steps) || 4, 4), 20);
        const seed = body.seed ? parseInt(body.seed) : Math.floor(Math.random() * 1000000);

        // Style modifiers
        let prompt = rawPrompt;
        const styleModifiers = {
          photorealistic: ', 8k uhd, cinematic lighting, 35mm photo, ultra-realistic, highly detailed, masterwork photography',
          cyberpunk: ', cyberpunk city, neon glowing reflections, volumetric fog, futuristic aesthetic, chromatic aberration',
          anime: ', makoto shinkai studio ghibli anime aesthetic, vibrant saturated colors, breathtaking scenery, hand-drawn digital art',
          pixar: ', 3D Pixar animated film style, octane render, soft subsurface scattering, cute expressive character design, ray-traced lighting',
          oil_painting: ', dramatic oil on canvas, expressive impasto brushstrokes, rich textures, chiaroscuro lighting, classic masterpiece',
          dark_fantasy: ', dark fantasy epic concept art, ominous moody atmosphere, elden ring aesthetic, detailed medieval architecture, rim light',
          synthwave: ', 1980s retro synthwave, neon grid, magenta and cyan lighting, VHS tape distortion aesthetic, sunset highway',
          architecture: ', modern architectural digest photography, minimalist luxury interior, warm ambient light, clean lines, archdaily award winner',
        };

        if (styleModifiers[style]) {
          prompt += styleModifiers[style];
        }

        // Dimensions
        let width = 1024;
        let height = 1024;
        if (ratio === '16:9') { width = 1024; height = 576; }
        else if (ratio === '9:16') { width = 576; height = 1024; }
        else if (ratio === '4:3') { width = 1024; height = 768; }
        else if (ratio === '3:4') { width = 768; height = 1024; }

        const startTime = Date.now();

        // Run Cloudflare Workers AI
        let aiInput = { prompt };
        if (model.includes('flux')) {
          aiInput = { prompt, steps: steps || 4 };
        } else {
          aiInput = { prompt, negative_prompt: negativePrompt, num_steps: steps, width, height, seed };
        }

        const imageBuffer = await env.AI.run(model, aiInput);
        const durationSec = ((Date.now() - startTime) / 1000).toFixed(2);

        // Convert binary image to base64 data URL
        let base64Image = '';
        if (imageBuffer instanceof ReadableStream || imageBuffer.getReader) {
          const response = new Response(imageBuffer);
          const arrayBuffer = await response.arrayBuffer();
          base64Image = arrayBufferToBase64(arrayBuffer);
        } else if (imageBuffer.image) {
          base64Image = imageBuffer.image;
        } else if (imageBuffer instanceof Uint8Array || imageBuffer instanceof ArrayBuffer) {
          base64Image = arrayBufferToBase64(imageBuffer);
        }

        const imageId = 'img_' + Date.now() + '_' + Math.random().toString(36).substring(2, 7);
        const record = {
          id: imageId,
          prompt: rawPrompt,
          enhancedPrompt: prompt,
          model,
          style,
          ratio,
          seed,
          durationSec,
          createdAt: new Date().toISOString(),
          country: request.cf?.country || 'US',
          colo: request.cf?.colo || 'EDGE',
        };

        // Save metadata to KV Gallery
        ctx.waitUntil((async () => {
          try {
            if (env.STUDIO_KV) {
              const galleryList = (await env.STUDIO_KV.get('recent_creations', { type: 'json' })) || [];
              galleryList.unshift(record);
              if (galleryList.length > 30) galleryList.length = 30;
              await env.STUDIO_KV.put('recent_creations', JSON.stringify(galleryList));
            }
          } catch (e) {}
        })());

        return jsonResponse({
          success: true,
          image: `data:image/jpeg;base64,${base64Image}`,
          metadata: record,
        });

      } catch (err) {
        return jsonResponse({ error: err.message || 'Image generation failed' }, 500);
      }
    }

    // 4. Get Recent Community Gallery
    if (url.pathname === '/api/gallery' && request.method === 'GET') {
      try {
        const gallery = (await env.STUDIO_KV.get('recent_creations', { type: 'json' })) || [];
        return jsonResponse(gallery);
      } catch (e) {
        return jsonResponse([]);
      }
    }

    return new Response('Not Found', { status: 404 });
  },
};

function arrayBufferToBase64(buffer) {
  let binary = '';
  const bytes = new Uint8Array(buffer);
  const len = bytes.byteLength;
  for (let i = 0; i < len; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return btoa(binary);
}

function jsonResponse(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    },
  });
}

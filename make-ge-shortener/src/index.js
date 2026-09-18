import { DASHBOARD_HTML } from './html.js';

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname;

    // 1. Dashboard Homepage
    if (path === '/' || path === '/index.html') {
      return new Response(DASHBOARD_HTML, {
        headers: { 'Content-Type': 'text/html; charset=utf-8' },
      });
    }

    // 2. Groq AI: Suggest Vanity Slugs from Long URL
    if (path === '/api/ai/suggest-slugs' && request.method === 'POST') {
      try {
        const { targetUrl } = await request.json();
        if (!targetUrl) return jsonResponse({ error: 'Target URL is required' }, 400);

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
            max_tokens: 150,
            messages: [
              {
                role: 'system',
                content: 'You are an expert digital marketer. Given a URL, generate exactly 4 short, punchy, memorable vanity slugs suitable for make.ge/slug. Return ONLY a JSON array of 4 lowercase strings with hyphens/numbers allowed (e.g. ["deal-2026", "summer-vip", "smart-promo", "join-now"]). No markdown, no explanation, only raw JSON array.',
              },
              {
                role: 'user',
                content: `URL: ${targetUrl}`,
              },
            ],
          }),
        });

        const data = await res.json();
        const rawContent = data.choices?.[0]?.message?.content?.trim() || '[]';
        let slugs = [];
        try {
          // Extract JSON array
          const match = rawContent.match(/\[.*\]/s);
          if (match) slugs = JSON.parse(match[0]);
        } catch (e) {
          slugs = ['promo', 'go', 'link', 'vip'];
        }
        return jsonResponse({ slugs });
      } catch (err) {
        return jsonResponse({ error: err.message }, 500);
      }
    }

    // 3. Groq AI: Traffic Intelligence & Marketing Insights
    if (path === '/api/ai/traffic-insights' && request.method === 'POST') {
      try {
        const { slug } = await request.json();
        if (!slug) return jsonResponse({ error: 'Slug is required' }, 400);

        const link = await env.SHORTENER_KV.get(`link:${slug}`, { type: 'json' });
        if (!link) return jsonResponse({ error: 'Link not found' }, 404);

        const clicks = (await env.SHORTENER_KV.get(`clicks:${slug}`, { type: 'json' })) || [];
        const analytics = processAnalytics(clicks, link);

        const groqKey = env.GROQ_API_KEY;
        const promptContext = `
Link: make.ge/${slug} -> ${link.url}
Total Clicks: ${analytics.totalClicks}
Top Referrers: ${JSON.stringify(analytics.referrers)}
Top Countries: ${JSON.stringify(analytics.countries)}
Top Cities: ${JSON.stringify(analytics.cities.map(c => `${c.city}: ${c.count}`))}
Devices: ${JSON.stringify(analytics.devices)}
OS: ${JSON.stringify(analytics.osList)}
`;

        const res = await fetch('https://api.groq.com/openai/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${groqKey}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            model: 'qwen/qwen3.8-27b',
            temperature: 0.6,
            max_tokens: 450,
            messages: [
              {
                role: 'system',
                content: 'You are an elite Growth & Analytics Strategist. Analyze the provided link telemetry data and provide a concise, high-impact executive breakdown with: 1) Key Audience Takeaway (where they come from, device habits), 2) Top Performing Channel, and 3) Three actionable growth recommendations to scale conversions. Format with clean bullet points and emojis.',
              },
              {
                role: 'user',
                content: promptContext,
              },
            ],
          }),
        });

        const data = await res.json();
        const insights = data.choices?.[0]?.message?.content?.trim() || 'No insights generated.';
        return jsonResponse({ insights });
      } catch (err) {
        return jsonResponse({ error: err.message }, 500);
      }
    }

    // 4. API: Create Short Link
    if (path === '/api/links' && request.method === 'POST') {
      try {
        const body = await request.json();
        let targetUrl = body.url?.trim();
        if (!targetUrl) return jsonResponse({ error: 'Target URL is required' }, 400);

        if (!/^https?:\/\//i.test(targetUrl)) {
          targetUrl = 'https://' + targetUrl;
        }

        try { new URL(targetUrl); } catch (e) {
          return jsonResponse({ error: 'Invalid URL format' }, 400);
        }

        let slug = (body.slug || '').trim().toLowerCase();
        if (slug) {
          slug = slug.replace(/[^a-z0-9-_]/g, '');
          if (slug.length < 2 || slug.length > 50) {
            return jsonResponse({ error: 'Custom slug must be between 2 and 50 characters' }, 400);
          }
          const reserved = ['api', 'admin', 'index', 'qr', 'analytics', 'favicon.ico', 'static'];
          if (reserved.includes(slug)) {
            return jsonResponse({ error: 'This custom slug is reserved' }, 400);
          }
          const existing = await env.SHORTENER_KV.get(`link:${slug}`, { type: 'json' });
          if (existing) {
            return jsonResponse({ error: 'Slug already taken. Please choose another.' }, 409);
          }
        } else {
          slug = generateRandomSlug(6);
          while (await env.SHORTENER_KV.get(`link:${slug}`)) {
            slug = generateRandomSlug(6);
          }
        }

        const title = body.title?.trim() || targetUrl.replace(/^https?:\/\//, '').split('/')[0];
        const linkData = {
          slug,
          url: targetUrl,
          title,
          createdAt: new Date().toISOString(),
          clicks: 0,
        };

        await env.SHORTENER_KV.put(`link:${slug}`, JSON.stringify(linkData));

        const index = (await env.SHORTENER_KV.get('links_index', { type: 'json' })) || [];
        if (!index.includes(slug)) {
          index.unshift(slug);
          await env.SHORTENER_KV.put('links_index', JSON.stringify(index));
        }

        return jsonResponse({ success: true, link: linkData });
      } catch (err) {
        return jsonResponse({ error: err.message }, 500);
      }
    }

    // 5. API: List All Links
    if (path === '/api/links' && request.method === 'GET') {
      try {
        const index = (await env.SHORTENER_KV.get('links_index', { type: 'json' })) || [];
        const links = [];
        for (const slug of index.slice(0, 50)) {
          const item = await env.SHORTENER_KV.get(`link:${slug}`, { type: 'json' });
          if (item) links.push(item);
        }
        return jsonResponse(links);
      } catch (err) {
        return jsonResponse({ error: err.message }, 500);
      }
    }

    // 6. API: Detailed Analytics for a Slug
    if (path.startsWith('/api/analytics/') && request.method === 'GET') {
      const slug = path.replace('/api/analytics/', '').trim();
      const link = await env.SHORTENER_KV.get(`link:${slug}`, { type: 'json' });
      if (!link) return jsonResponse({ error: 'Link not found' }, 404);

      const clicks = (await env.SHORTENER_KV.get(`clicks:${slug}`, { type: 'json' })) || [];
      const analytics = processAnalytics(clicks, link);
      return jsonResponse(analytics);
    }

    // 7. API: Global Map Telemetry
    if (path === '/api/all-analytics' && request.method === 'GET') {
      try {
        const globalPings = (await env.SHORTENER_KV.get('global_pings', { type: 'json' })) || [];
        return jsonResponse(globalPings);
      } catch (e) {
        return jsonResponse([]);
      }
    }

    // 8. API: Delete Link
    if (path.startsWith('/api/links/') && request.method === 'DELETE') {
      const slug = path.replace('/api/links/', '').trim();
      await env.SHORTENER_KV.delete(`link:${slug}`);
      await env.SHORTENER_KV.delete(`clicks:${slug}`);

      let index = (await env.SHORTENER_KV.get('links_index', { type: 'json' })) || [];
      index = index.filter(s => s !== slug);
      await env.SHORTENER_KV.put('links_index', JSON.stringify(index));
      return jsonResponse({ success: true });
    }

    // 9. Sub-10ms Edge Link Redirection (/:slug)
    const slug = path.substring(1).split('/')[0];
    if (slug && !slug.includes('.') && !slug.startsWith('api')) {
      const link = await env.SHORTENER_KV.get(`link:${slug}`, { type: 'json' });
      if (link) {
        const cf = request.cf || {};
        const userAgent = request.headers.get('user-agent') || '';
        const referer = request.headers.get('referer') || 'Direct';

        const clickEvent = {
          timestamp: new Date().toISOString(),
          country: cf.country || 'GE',
          city: cf.city || 'Tbilisi',
          lat: cf.latitude ? parseFloat(cf.latitude) : 41.7151,
          lon: cf.longitude ? parseFloat(cf.longitude) : 44.8271,
          colo: cf.colo || 'TBS',
          timezone: cf.timezone || 'Asia/Tbilisi',
          referrer: parseReferrer(referer),
          rawReferer: referer,
          ...parseUserAgent(userAgent),
        };

        ctx.waitUntil((async () => {
          try {
            link.clicks = (link.clicks || 0) + 1;
            await env.SHORTENER_KV.put(`link:${slug}`, JSON.stringify(link));

            const clicks = (await env.SHORTENER_KV.get(`clicks:${slug}`, { type: 'json' })) || [];
            clicks.unshift(clickEvent);
            if (clicks.length > 200) clicks.length = 200;
            await env.SHORTENER_KV.put(`clicks:${slug}`, JSON.stringify(clicks));

            const globalPings = (await env.SHORTENER_KV.get('global_pings', { type: 'json' })) || [];
            globalPings.unshift({
              slug,
              title: link.title,
              city: clickEvent.city,
              country: clickEvent.country,
              lat: clickEvent.lat,
              lon: clickEvent.lon,
              referrer: clickEvent.referrer,
              timestamp: clickEvent.timestamp,
            });
            if (globalPings.length > 100) globalPings.length = 100;
            await env.SHORTENER_KV.put('global_pings', JSON.stringify(globalPings));
          } catch (e) {}
        })());

        return Response.redirect(link.url, 302);
      }
    }

    return new Response(DASHBOARD_HTML, {
      headers: { 'Content-Type': 'text/html; charset=utf-8' },
    });
  },
};

function generateRandomSlug(len = 6) {
  const chars = '23456789abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ';
  let out = '';
  for (let i = 0; i < len; i++) {
    out += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return out;
}

function parseReferrer(ref) {
  if (!ref || ref === 'Direct') return 'Direct';
  const lower = ref.toLowerCase();
  if (lower.includes('facebook.com') || lower.includes('fb.me')) return 'Facebook';
  if (lower.includes('instagram.com')) return 'Instagram';
  if (lower.includes('t.me') || lower.includes('telegram')) return 'Telegram';
  if (lower.includes('linkedin.com') || lower.includes('lnkd.in')) return 'LinkedIn';
  if (lower.includes('twitter.com') || lower.includes('x.com') || lower.includes('t.co')) return 'Twitter / X';
  if (lower.includes('google.')) return 'Google';
  if (lower.includes('youtube.com') || lower.includes('youtu.be')) return 'YouTube';
  if (lower.includes('tiktok.com')) return 'TikTok';
  if (lower.includes('reddit.com')) return 'Reddit';
  try {
    const host = new URL(ref).hostname.replace(/^www\./, '');
    return host || 'Other';
  } catch (e) {
    return 'Other';
  }
}

function parseUserAgent(ua) {
  let device = 'Desktop';
  let os = 'Unknown OS';
  let browser = 'Unknown';

  if (/mobile|android|iphone|ipad|ipod/i.test(ua)) device = 'Mobile';
  if (/ipad|tablet/i.test(ua)) device = 'Tablet';

  if (/iphone|ipad|ipod/i.test(ua)) os = 'iOS';
  else if (/android/i.test(ua)) os = 'Android';
  else if (/macintosh|mac os x/i.test(ua)) os = 'macOS';
  else if (/windows/i.test(ua)) os = 'Windows';
  else if (/linux/i.test(ua)) os = 'Linux';

  if (/edg/i.test(ua)) browser = 'Edge';
  else if (/chrome|crios/i.test(ua)) browser = 'Chrome';
  else if (/firefox|fxios/i.test(ua)) browser = 'Firefox';
  else if (/safari/i.test(ua)) browser = 'Safari';

  return { device, os, browser };
}

function processAnalytics(clicks, link) {
  const referrers = {};
  const countries = {};
  const cities = [];
  const devices = { Desktop: 0, Mobile: 0, Tablet: 0 };
  const osList = {};
  const browsers = {};
  const recentLogs = clicks.slice(0, 30);

  clicks.forEach(c => {
    referrers[c.referrer] = (referrers[c.referrer] || 0) + 1;
    countries[c.country] = (countries[c.country] || 0) + 1;
    if (c.device) devices[c.device] = (devices[c.device] || 0) + 1;
    if (c.os) osList[c.os] = (osList[c.os] || 0) + 1;
    if (c.browser) browsers[c.browser] = (browsers[c.browser] || 0) + 1;

    if (c.lat && c.lon) {
      const found = cities.find(item => item.city === c.city && item.country === c.country);
      if (found) {
        found.count++;
      } else {
        cities.push({
          city: c.city,
          country: c.country,
          lat: c.lat,
          lon: c.lon,
          count: 1,
        });
      }
    }
  });

  return {
    link,
    totalClicks: link.clicks || clicks.length,
    referrers,
    countries,
    cities,
    devices,
    osList,
    browsers,
    recentLogs,
  };
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

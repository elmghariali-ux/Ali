const crypto = require('crypto');
const { read, fields, defaults, loadSaved } = require('./_lib');

const same = (a, b) => {
  const x = Buffer.from(String(a)), y = Buffer.from(String(b));
  return x.length === y.length && crypto.timingSafeEqual(x, y);
};

module.exports = async (req, res) => {
  try { await handle(req, res); } catch (e) { res.statusCode = 500; res.setHeader('Content-Type','application/json'); res.end(JSON.stringify({ error: 'Server error: ' + e.message })); }
};

async function handle(req, res) {
  const FIELDS = fields();
  res.setHeader('Cache-Control', 'no-store');
  const pass = process.env.ADMIN_PASSWORD;
  const given = req.headers['x-admin-password'] || '';
  if (!pass || !same(given, pass)) { res.status(401).json({ error: 'Wrong password' }); return; }

  const base = defaults(read('index.html'));
  if (req.method === 'GET') {
    const saved = await loadSaved();
    res.status(200).json({ fields: FIELDS, defaults: base, values: Object.assign({}, base, saved) });
    return;
  }
  if (req.method === 'POST') {
    let body = req.body;
    if (typeof body === 'string') { try { body = JSON.parse(body); } catch (e) { body = null; } }
    const incoming = body && body.values;
    if (!incoming || typeof incoming !== 'object') { res.status(400).json({ error: 'Nothing to save' }); return; }
    const values = {};
    for (const f of FIELDS) {
      const v = incoming[f.key];
      if (typeof v === 'string' && v.length <= 4000 && v.trim() && v.trim() !== base[f.key]) values[f.key] = v.trim();
    }
    const { put } = require('@vercel/blob');
    await put('content/argana.json', JSON.stringify({ values, savedAt: new Date().toISOString() }), {
      access: 'public', addRandomSuffix: false, allowOverwrite: true, contentType: 'application/json', cacheControlMaxAge: 60,
    });
    res.status(200).json({ ok: true, changed: Object.keys(values).length });
    return;
  }
  res.status(405).json({ error: 'Method not allowed' });
}

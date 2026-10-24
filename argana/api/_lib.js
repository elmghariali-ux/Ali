const fs = require('fs');
const path = require('path');

const ROOTS = [path.join(process.cwd(), 'tpl'), path.join(__dirname, '..', 'tpl'), path.join(process.cwd(), 'argana', 'tpl')];
const read = (f) => {
  for (const r of ROOTS) { const p = path.join(r, f); if (fs.existsSync(p)) return fs.readFileSync(p, 'utf8'); }
  throw new Error('Template not found: ' + f + ' in ' + ROOTS.join(', ') + ' cwd=' + process.cwd() + ' ls=' + fs.readdirSync(process.cwd()).join(','));
};
let _fields;
const fields = () => (_fields = _fields || JSON.parse(read('fields.json')));
const MARK = /<!--e:([a-z_]+)-->([\s\S]*?)<!--\/e:\1-->/g;

const esc = (t) => String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const inline = (t) => esc(t.trim()).replace(/\*([^*\n]+)\*/g, '<em>$1</em>');

// Template HTML → plain text the editor shows
function toText(html) {
  const paras = html.match(/<p[^>]*>([\s\S]*?)<\/p>/g);
  const strip = (h) => h.replace(/<em>([\s\S]*?)<\/em>/g, '*$1*').replace(/<[^>]+>/g, '')
    .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/\s+/g, ' ').trim();
  return paras ? paras.map(strip).join('\n\n') : strip(html);
}

// Plain text → HTML for a marked block
function toHtml(key, text, original) {
  if (/<p[^>]*>/.test(original)) {
    const cls = (original.match(/<p([^>]*)>/) || [, ''])[1];
    return text.split(/\n\s*\n/).filter((p) => p.trim()).map((p) => `<p${cls}>${inline(p.replace(/\n/g, ' '))}</p>`).join('\n      ');
  }
  return inline(text.replace(/\n/g, ' '));
}

function defaults(tpl) {
  const d = {}; let m; MARK.lastIndex = 0;
  while ((m = MARK.exec(tpl))) d[m[1]] = toText(m[2]);
  return d;
}

async function loadSaved() {
  if (!process.env.BLOB_READ_WRITE_TOKEN) return {};
  try {
    const { head } = require('@vercel/blob');
    const h = await head('content/argana.json');
    const r = await fetch(h.url + '?v=' + Date.now(), { cache: 'no-store' });
    if (!r.ok) return {};
    const j = await r.json();
    return j && typeof j === 'object' ? (j.values || {}) : {};
  } catch (e) { return {}; }
}

function render(tpl, values) {
  return tpl.replace(MARK, (all, key, inner) => {
    const v = values[key];
    if (typeof v !== 'string' || !v.trim()) return inner;
    return toHtml(key, v, inner);
  });
}

module.exports = { read, fields, defaults, loadSaved, render };

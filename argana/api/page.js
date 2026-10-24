const { read, loadSaved, render } = require('./_lib');

module.exports = async (req, res) => {
  let tpl;
  try { tpl = read('index.html'); } catch (e) { res.statusCode = 500; res.setHeader('Content-Type','text/plain'); res.end(e.message); return; }
  let html = tpl;
  try { html = render(tpl, await loadSaved()); } catch (e) { html = tpl; }
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('Cache-Control', 'public, max-age=0, s-maxage=30, stale-while-revalidate=300');
  res.statusCode = 200; res.end(html);
};

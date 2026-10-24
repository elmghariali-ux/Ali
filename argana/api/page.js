const { read, loadSaved, render } = require('./_lib');

module.exports = async (req, res) => {
  const tpl = read('index.html');
  let html = tpl;
  try { html = render(tpl, await loadSaved()); } catch (e) { html = tpl; }
  res.setHeader('Content-Type', 'text/html; charset=utf-8');
  res.setHeader('Cache-Control', 'public, max-age=0, s-maxage=30, stale-while-revalidate=300');
  res.status(200).send(html);
};

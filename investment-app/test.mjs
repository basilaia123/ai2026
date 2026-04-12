import yahooFinance from 'yahoo-finance2';

async function run() {
  const q = await yahooFinance.quote('AAPL');
  console.log('Quote:', q.regularMarketPrice, q.shortName);
  
  const dateStr = new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString().split('T')[0];
  const c = await yahooFinance.chart('AAPL', { period1: dateStr });
  console.log('Chart quotes:', c.quotes.slice(0, 2));

  const s = await yahooFinance.search('AAPL');
  console.log('Search news length:', s.news.length);
  if (s.news.length > 0) console.log(s.news[0]);
}

run();

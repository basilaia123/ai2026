import { YahooFinance } from 'yahoo-finance2';
const yahooFinance = new YahooFinance();

async function run() {
  const quotes = await yahooFinance.quote(['AAPL', 'MSFT', 'NVDA']);
  console.log("Quotes fetched:");
  quotes.forEach(q => console.log(q.symbol, q.regularMarketPrice, q.regularMarketChangePercent));
}

run();

async function run() {
  const res = await fetch("https://query1.finance.yahoo.com/v7/finance/quote?symbols=AAPL,MSFT,NVDA");
  const data = await res.json();
  const quotes = data.quoteResponse.result;
  console.log("Quotes fetched:", quotes.length);
  quotes.forEach(q => console.log(q.symbol, q.regularMarketPrice, q.regularMarketChangePercent));
}

run();

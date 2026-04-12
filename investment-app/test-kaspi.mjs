async function checkTicker(ticker) {
  const res = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?interval=1d&range=3mo`);
  const d = await res.json();
  console.log(ticker, d.chart.error ? 'ERROR: ' + d.chart.error.description : 'OK: ' + d.chart.result[0].meta.symbol + " - " + d.chart.result[0].meta.regularMarketPrice);
}

async function run() {
  await checkTicker('KSPI');
  await checkTicker('KSPI.IL');
  await checkTicker('KAZ.L');
}

run();

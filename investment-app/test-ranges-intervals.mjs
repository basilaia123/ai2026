async function checkRange(r, interval) {
  const res = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=${interval}&range=${r}`);
  const d = await res.json();
  console.log(r, interval, d.chart.error ? 'ERROR: ' + d.chart.error.description : 'OK: ' + d.chart.result[0].timestamp.length);
}

async function run() {
  await checkRange('1d', '5m');
  await checkRange('1wk', '15m');
  await checkRange('2wk', '30m');
  await checkRange('1mo', '1d');
}

run();

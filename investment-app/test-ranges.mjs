async function checkRange(r, interval = "1d") {
  const res = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=${interval}&range=${r}`);
  const d = await res.json();
  console.log(r, d.chart.error ? 'ERROR: ' + d.chart.error.description : 'OK');
}

async function run() {
  await checkRange('1d', '1m');   // 1 day with 1 minute interval usually
  await checkRange('5d', '5m');   // 5 days (1 week roughly)
  await checkRange('1wk', '1d');  // 1 week
  await checkRange('2wk', '1d');  // 2 weeks
  await checkRange('14d', '1d');
}

run();

async function run() {
  const chartRes = await fetch("https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=1d&range=1mo");
  const chartData = await chartRes.json();
  const meta = chartData.chart.result[0].meta;
  const quote = chartData.chart.result[0].indicators.quote[0];
  const timestamps = chartData.chart.result[0].timestamp;
  console.log("Price:", meta.regularMarketPrice);

  const searchRes = await fetch("https://query2.finance.yahoo.com/v1/finance/search?q=AAPL&quotesCount=0&newsCount=5");
  const searchData = await searchRes.json();
  console.log("News:", searchData.news?.length, searchData.news?.[0]?.title);
}

run();

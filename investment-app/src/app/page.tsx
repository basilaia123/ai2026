import StockHeader from "@/components/StockHeader";
import PriceChart from "@/components/PriceChart";
import { MessageSquare, MoreHorizontal, Share2, Bookmark, ArrowUpRight, ArrowDownRight } from "lucide-react";
import Link from "next/link";
import { cookies } from "next/headers";
import { Language, getTranslation } from "@/lib/i18n";

const CATEGORY_TICKERS: Record<string, string[]> = {
  "SPY": ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "BRK-B", "LLY", "AVGO", "JPM", "UNH", "XOM", "V", "MA", "PG", "JNJ"],
  "XLK": ["MSFT", "AAPL", "NVDA", "AVGO", "ADBE", "CRM", "AMD", "INTC", "CSCO", "QCOM", "TXN", "AMAT", "IBM", "NOW", "INTU", "MU"],
  "BOTZ": ["NVDA", "ISRG", "ABB", "KEY", "CRWD", "PLTR", "U", "PATH", "SYK", "CGNX", "ROK", "IRBT", "SYM", "HON", "APP"],
  "XLF": ["BRK-B", "JPM", "V", "MA", "BAC", "WFC", "GS", "MS", "C", "BLK", "AXP", "CB", "MMC", "SPGI", "PGR", "USB", "SCHW"],
  "XLV": ["LLY", "UNH", "JNJ", "ABBV", "MRK", "TMO", "DHR", "PFE", "AMGN", "ISRG", "SYK", "MDT", "VRTX", "BSX", "ZTS", "GILD", "BDX"],
  "SMH": ["NVDA", "TSM", "AVGO", "ASML", "AMD", "QCOM", "INTC", "TXN", "AMAT", "LRCX", "MU", "ADI", "KLAC", "NXPI", "MRVL", "SNPS", "CDNS"],
  "GAMR": ["EA", "TTWO", "RBLX", "NTES", "SONY", "SE", "APP", "BILI", "PLTK", "CRSR", "LOGI", "U", "NCTY"],
  "XLE": ["XOM", "CVX", "COP", "SLB", "EOG", "MPC", "OXY", "VLO", "WMB", "PSX", "KMI", "HES", "HAL", "BKR"],
};

const CATEGORY_NAMES: Record<string, string> = {
  "SPY": "Market Overview",
  "XLK": "Technology Stocks",
  "BOTZ": "AI & Robotics",
  "XLF": "Financial Sector",
  "XLV": "Healthcare Sector",
  "SMH": "Semiconductors",
  "GAMR": "Gaming & Entertainment",
  "XLE": "Energy Sector"
}

async function fetchStockData(ticker: string) {
  try {
    const res = await fetch(`https://query1.finance.yahoo.com/v8/finance/chart/${ticker}?interval=1d&range=3mo`, { cache: 'no-store' });
    const data = await res.json();
    
    if (!data.chart.result) return null;
    
    const result = data.chart.result[0];
    const meta = result.meta;
    const quotes = result.indicators.quote[0];
    const timestamps = result.timestamp;
    
    const chartData = [];
    if (timestamps && quotes) {
      for (let i = 0; i < timestamps.length; i++) {
        if (quotes.close[i] !== null) {
          const date = new Date(timestamps[i] * 1000);
          chartData.push({
            date: date.toISOString().split('T')[0],
            price: Number(quotes.close[i].toFixed(2))
          });
        }
      }
    }

    const previousClose = meta.previousClose || meta.chartPreviousClose || meta.regularMarketPrice || 1;
    const currentPrice = meta.regularMarketPrice || 0;
    let change = currentPrice - previousClose;
    let changePercent = (change / previousClose) * 100;

    if (isNaN(change)) change = 0;
    if (isNaN(changePercent)) changePercent = 0;

    return {
      stockInfo: {
        ticker: meta.symbol,
        name: meta.shortName || meta.symbol,
        price: currentPrice,
        change: change,
        changePercent: changePercent,
        isPositive: change >= 0
      },
      chartData
    };
  } catch (err) {
    console.error(err);
    return null;
  }
}

async function fetchNewsData(ticker: string) {
  try {
    const res = await fetch(`https://query2.finance.yahoo.com/v1/finance/search?q=${ticker}&quotesCount=0&newsCount=5`, { cache: 'no-store' });
    const data = await res.json();
    if (!data.news) return [];
    
    return data.news.map((item: any, idx: number) => ({
      id: item.uuid || idx,
      title: item.title,
      source: item.publisher,
      time: new Date(item.providerPublishTime * 1000).toLocaleString(),
      badge: idx === 0 ? "Latest" : "Trending",
      badgeColor: idx === 0 ? "bg-orange-500" : "bg-green-500",
      image: item.thumbnail?.resolutions?.[0]?.url || "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=300&auto=format&fit=crop",
      link: item.link
    }));
  } catch (err) {
    console.error(err);
    return [];
  }
}

export default async function Home(props: { searchParams?: Promise<{ ticker?: string, category?: string }> }) {
  const searchParams = await props.searchParams;
  const ticker = searchParams?.ticker?.toUpperCase();
  const category = searchParams?.category?.toUpperCase();
  
  const cookieStore = await cookies();
  const lang = (cookieStore.get("lang")?.value || "ge") as Language;
  const t = getTranslation(lang);

  // SINGLE STOCK VIEW
  if (ticker) {
    const stockResult = await fetchStockData(ticker);
    const newsList = await fetchNewsData(ticker);

    if (!stockResult) {
      return (
        <div className="pb-12 max-w-5xl mt-10">
          <h1 className="text-3xl font-bold text-red-500 mb-2">{t("Failed to load data for")} {ticker}</h1>
          <p className="text-muted">{t("Please check the ticker symbol and try again.")}</p>
        </div>
      );
    }

    return (
      <div className="pb-12 max-w-5xl">
        <StockHeader stockInfo={stockResult.stockInfo} lang={lang} />
        <div className="mb-8">
           <PriceChart data={stockResult.chartData} />
        </div>

        <div>
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-xl font-bold text-white tracking-tight">{t("Latest News")} ({ticker})</h2>
          </div>

          <div className="space-y-4">
             {newsList.map((news: any) => (
               <a href={news.link} target="_blank" rel="noopener noreferrer" key={news.id} className="block bg-card hover:bg-activeCard transition-colors rounded-2xl border border-white/5 p-4 flex flex-col md:flex-row gap-6 group">
                 <div className="relative w-full md:w-64 h-40 md:h-auto rounded-xl overflow-hidden flex-shrink-0 border border-white/10">
                   {/* eslint-disable-next-line @next/next/no-img-element */}
                   <img src={news.image} alt={news.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                 </div>
                 
                 <div className="flex-1 flex flex-col justify-center">
                   <div className="flex items-center gap-3 mb-3">
                     <span className={`px-2.5 py-0.5 rounded-md text-xs font-semibold ${news.badgeColor} text-white/90 shadow-sm`}>
                       {news.badge}
                     </span>
                     <span className="text-xs font-semibold text-muted uppercase tracking-wider">{news.source}</span>
                   </div>
                   
                   <h3 className="text-xl font-bold text-white mb-2 leading-tight group-hover:text-green-400 transition-colors">
                     {news.title}
                   </h3>
                   
                   <div className="mt-auto flex items-center justify-between text-xs text-muted pt-4 border-t border-white/5">
                     <div className="flex items-center gap-4">
                       <span>{news.time}</span>
                       <div className="flex items-center gap-1 hover:text-white transition-colors">
                         <MessageSquare className="w-4 h-4" />
                         <span>{Math.floor(Math.random() * 50) + 5}</span>
                       </div>
                     </div>
                     <div className="flex items-center gap-3">
                       <Bookmark className="w-4 h-4 hover:text-white transition-colors" />
                       <Share2 className="w-4 h-4 hover:text-white transition-colors" />
                       <MoreHorizontal className="w-4 h-4 hover:text-white transition-colors" />
                     </div>
                   </div>
                 </div>
               </a>
             ))}
             {newsList.length === 0 && (
               <p className="text-muted">{t("No recent news found for")} {ticker}.</p>
             )}
          </div>
        </div>
      </div>
    );
  }

  // CATEGORY VIEW
  const activeCategory = category || "SPY";
  const categoryNameEN = CATEGORY_NAMES[activeCategory] || "Category Overview";
  const categoryName = t(categoryNameEN as any) || t("Category Overview");
  const tickersToFetch = CATEGORY_TICKERS[activeCategory] || CATEGORY_TICKERS["SPY"];
  
  // Fetch quotes for all tickers in category simultaneously
  const categoryStocks = (await Promise.all(
    tickersToFetch.map(t => fetchStockData(t))
  )).filter(Boolean);

  return (
    <div className="pb-12 max-w-5xl">
       <div className="mt-4 mb-8">
         <h1 className="text-3xl font-bold text-white tracking-tight mb-2">{categoryName}</h1>
         <p className="text-muted">{t("Discover the top trending stocks in this sector.")}</p>
       </div>

       <div className="grid grid-cols-1 lg:grid-cols-2 xl:grid-cols-3 gap-4">
         {categoryStocks.map((res: any, idx: number) => {
           const info = res.stockInfo;
           return (
             <Link href={`/?ticker=${info.ticker}`} key={info.ticker}>
               <div className="bg-card hover:bg-activeCard transition-colors rounded-2xl border border-white/5 p-5 flex flex-col group cursor-pointer h-full">
                 
                 <div className="flex justify-between items-start mb-4">
                   <div className="flex items-center gap-3">
                     <div className="w-10 h-10 rounded-xl shrink-0 bg-background border border-white/10 flex items-center justify-center font-bold text-white shadow-inner">
                       {info.ticker[0]}
                     </div>
                     <div>
                       <h3 className="text-white font-bold leading-tight group-hover:text-green-400 transition-colors line-clamp-2">{info.name}</h3>
                       <span className="text-xs font-semibold text-muted uppercase">#{idx + 1} {t("Featured")}</span>
                     </div>
                   </div>
                   <span className="px-2.5 py-1 rounded-md bg-background border border-white/5 text-xs font-semibold text-muted tracking-wider">
                     {info.ticker}
                   </span>
                 </div>

                 <div className="mt-auto">
                    <span className="text-sm font-medium text-muted">{t("Current Price")}</span>
                    <div className="flex items-end justify-between mt-1">
                      <span className="text-2xl font-bold text-white">${info.price.toFixed(2)}</span>
                      <div className={`flex items-center gap-1 text-xs font-medium px-2 py-1 rounded-full ${info.isPositive ? 'bg-green-500/10 text-green-500' : 'bg-red-500/10 text-red-500'}`}>
                        {info.isPositive ? <ArrowUpRight className="w-3 h-3" /> : <ArrowDownRight className="w-3 h-3" />}
                        <span>{Math.abs(info.changePercent).toFixed(2)}%</span>
                      </div>
                    </div>
                 </div>

               </div>
             </Link>
           );
         })}
       </div>
    </div>
  );
}

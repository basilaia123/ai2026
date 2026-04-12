import { ArrowUpRight, ArrowDownRight } from "lucide-react";
import { Language, getTranslation } from "@/lib/i18n";

interface StockHeaderProps {
  stockInfo: {
    ticker: string;
    name: string;
    price: number;
    change: number;
    changePercent: number;
    isPositive: boolean;
  };
  lang: Language;
}

export default function StockHeader({ stockInfo, lang }: StockHeaderProps) {
  const { ticker, name, price, change, changePercent, isPositive } = stockInfo;
  const t = getTranslation(lang);
  
  return (
    <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-6 mt-4">
      <div>
        <div className="flex items-center gap-3 mb-1">
          <h1 className="text-3xl font-bold text-white tracking-tight">{name}</h1>
          <span className="px-2.5 py-1 rounded-md bg-card border border-white/10 text-xs font-semibold text-muted tracking-wider">
            {ticker}
          </span>
        </div>
      </div>
      
      <div className="flex items-center gap-4">
        <div className="flex flex-col items-end">
          <span className="text-sm font-medium text-muted">{t("Current Price")}</span>
          <div className="flex items-end gap-3 mt-1">
            <span className="text-3xl font-bold text-white">${price.toFixed(2)}</span>
            <div className={`flex items-center gap-1 text-sm font-medium px-2 py-1 rounded-full mb-1 ${isPositive ? 'bg-green-500/10 text-green-500' : 'bg-red-500/10 text-red-500'}`}>
              {isPositive ? <ArrowUpRight className="w-4 h-4" /> : <ArrowDownRight className="w-4 h-4" />}
              <span>${Math.abs(change).toFixed(2)} ({Math.abs(changePercent).toFixed(2)}%)</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

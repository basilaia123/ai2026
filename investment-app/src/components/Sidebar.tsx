"use client";

import { Grip, Activity, Compass, Code, Gamepad, BookOpen, LayoutDashboard, Terminal, MessageSquare, Zap, HeartPulse, Building2 } from "lucide-react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Suspense } from "react";
import { Language, getTranslation } from "@/lib/i18n";

const RAW_CATEGORIES = [
  { icon: <Grip className="w-4 h-4" />, labelKey: "Market Overview", ticker: "SPY", count: 7 },
  { icon: <Code className="w-4 h-4" />, labelKey: "Technology", ticker: "XLK", count: 7 },
  { icon: <Zap className="w-4 h-4" />, labelKey: "AI & Robotics", ticker: "BOTZ", count: 6 },
  { icon: <Building2 className="w-4 h-4" />, labelKey: "Finance", ticker: "XLF", count: 7 },
  { icon: <HeartPulse className="w-4 h-4" />, labelKey: "Healthcare", ticker: "XLV", count: 7 },
  { icon: <Terminal className="w-4 h-4" />, labelKey: "Semiconductors", ticker: "SMH", count: 7 },
  { icon: <Gamepad className="w-4 h-4" />, labelKey: "Gaming", ticker: "GAMR", count: 5 },
  { icon: <Compass className="w-4 h-4" />, labelKey: "Energy", ticker: "XLE", count: 6 },
] as const;

function SidebarContent({ className, lang }: { className?: string; lang: Language }) {
  const searchParams = useSearchParams();
  const currentCategory = (searchParams.get("category") || "SPY").toUpperCase();
  const currentTicker = searchParams.get("ticker");
  
  const t = getTranslation(lang);

  return (
    <aside className={`h-full bg-background flex flex-col ${className}`}>
      {/* Brand */}
      <div className="h-16 flex items-center px-6 shrink-0">
        <Link href="/" className="text-xl font-bold tracking-tight text-white flex items-center gap-2 hover:opacity-80 transition-opacity">
           <LayoutDashboard className="text-green-500 w-5 h-5"/>
           Invest<span className="text-green-500">Pro</span>
        </Link>
      </div>

      <div className="flex-1 overflow-y-auto py-4 px-4 space-y-8 no-scrollbar">
        {/* Categories Section */}
        <div>
          <h2 className="text-xs font-semibold text-muted uppercase tracking-wider mb-4 px-2">
            {t("Market Sectors")}
          </h2>
          <nav className="space-y-1">
            {RAW_CATEGORIES.map((cat) => (
              <NavItem 
                key={cat.ticker}
                icon={cat.icon} 
                label={t(cat.labelKey as any)} 
                ticker={cat.ticker}
                count={cat.count} 
                active={!currentTicker && currentCategory === cat.ticker} 
              />
            ))}
          </nav>
        </div>
        
        {/* Time Period Section */}
        <div>
            <h2 className="text-xs font-semibold text-muted uppercase tracking-wider mb-4 px-2">
                {t("Time Period Context")}
            </h2>
            <div className="flex flex-wrap gap-2 px-2">
                <button className="px-3 py-1 rounded-full text-xs font-medium bg-green-500 text-black">{t("1 Month")}</button>
                <button className="px-3 py-1 rounded-full text-xs font-medium text-muted hover:text-white border border-card hover:bg-card transition-colors">{t("3 Months")}</button>
                <button className="px-3 py-1 rounded-full text-xs font-medium text-muted hover:text-white border border-card hover:bg-card transition-colors">{t("1 Year")}</button>
            </div>
        </div>
      </div>
    </aside>
  );
}

function NavItem({ icon, label, ticker, count, active }: { icon: React.ReactNode; label: string; ticker: string; count?: number; active?: boolean }) {
  return (
    <Link
      href={`/?category=${ticker}`}
      className={`flex items-center justify-between px-3 py-2 rounded-lg text-sm transition-colors ${
        active
          ? "bg-activeCard text-green-400 border border-green-500/20"
          : "text-muted hover:text-white hover:bg-card border border-transparent"
      }`}
    >
      <div className="flex items-center gap-3">
        <span className={active ? "text-green-400" : "text-muted transition-colors"}>{icon}</span>
        <span className={active ? "font-medium" : ""}>{label}</span>
      </div>
      {count !== undefined && (
        <span className={`text-xs ${active ? "text-green-500/80" : "text-muted"}`}>
          {count}
        </span>
      )}
    </Link>
  );
}

export default function Sidebar({ className, lang }: { className?: string, lang: Language }) {
  return (
    <Suspense fallback={<aside className={`h-full bg-background flex flex-col ${className}`} />}>
      <SidebarContent className={className} lang={lang} />
    </Suspense>
  );
}

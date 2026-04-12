"use client";

import { Grip, Activity, Compass, Code, Gamepad, BookOpen, LayoutDashboard, Terminal, MessageSquare, Zap, HeartPulse, Building2 } from "lucide-react";
import Link from "next/link";
import { useSearchParams } from "next/navigation";
import { Suspense } from "react";
import { Language, getTranslation } from "@/lib/i18n";

const RAW_CATEGORIES = [
  { icon: <Grip className="w-4 h-4" />, labelKey: "Market Overview", ticker: "SPY", count: 17 },
  { icon: <Code className="w-4 h-4" />, labelKey: "Technology", ticker: "XLK", count: 16 },
  { icon: <Zap className="w-4 h-4" />, labelKey: "AI & Robotics", ticker: "BOTZ", count: 15 },
  { icon: <Building2 className="w-4 h-4" />, labelKey: "Finance", ticker: "XLF", count: 17 },
  { icon: <HeartPulse className="w-4 h-4" />, labelKey: "Healthcare", ticker: "XLV", count: 17 },
  { icon: <Terminal className="w-4 h-4" />, labelKey: "Semiconductors", ticker: "SMH", count: 17 },
  { icon: <Gamepad className="w-4 h-4" />, labelKey: "Gaming", ticker: "GAMR", count: 13 },
  { icon: <Compass className="w-4 h-4" />, labelKey: "Energy", ticker: "XLE", count: 14 },
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
                <Link href={`/?${new URLSearchParams({...Object.fromEntries(searchParams.entries()), range: "1d"}).toString()}`} className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${searchParams.get("range") === "1d" ? "bg-green-500 text-black" : "text-muted hover:text-white border border-card hover:bg-card"}`}>
                  {t("1 Day" as any)}
                </Link>
                <Link href={`/?${new URLSearchParams({...Object.fromEntries(searchParams.entries()), range: "1wk"}).toString()}`} className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${searchParams.get("range") === "1wk" ? "bg-green-500 text-black" : "text-muted hover:text-white border border-card hover:bg-card"}`}>
                  {t("1 Week" as any)}
                </Link>
                <Link href={`/?${new URLSearchParams({...Object.fromEntries(searchParams.entries()), range: "2wk"}).toString()}`} className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${searchParams.get("range") === "2wk" ? "bg-green-500 text-black" : "text-muted hover:text-white border border-card hover:bg-card"}`}>
                  {t("2 Weeks" as any)}
                </Link>
                <Link href={`/?${new URLSearchParams({...Object.fromEntries(searchParams.entries()), range: "1mo"}).toString()}`} className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${searchParams.get("range") === "1mo" ? "bg-green-500 text-black" : "text-muted hover:text-white border border-card hover:bg-card"}`}>
                  {t("1 Month")}
                </Link>
                <Link href={`/?${new URLSearchParams({...Object.fromEntries(searchParams.entries()), range: "3mo"}).toString()}`} className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${(searchParams.get("range") || "3mo") === "3mo" ? "bg-green-500 text-black" : "text-muted hover:text-white border border-card hover:bg-card"}`}>
                  {t("3 Months")}
                </Link>
                <Link href={`/?${new URLSearchParams({...Object.fromEntries(searchParams.entries()), range: "1y"}).toString()}`} className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${searchParams.get("range") === "1y" ? "bg-green-500 text-black" : "text-muted hover:text-white border border-card hover:bg-card"}`}>
                  {t("1 Year")}
                </Link>
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

"use client";

import { Search, Bell, User, Globe } from "lucide-react";
import { useRouter } from "next/navigation";
import { useState } from "react";
import { setLanguage } from "@/app/actions";
import { Language, getTranslation } from "@/lib/i18n";

interface TopBarProps {
  lang: Language;
}

export default function TopBar({ lang }: TopBarProps) {
  const router = useRouter();
  const [ticker, setTicker] = useState("");
  const t = getTranslation(lang);

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault();
    if (ticker.trim()) {
      router.push(`/?ticker=${ticker.trim()}`);
    }
  };

  const toggleLanguage = async () => {
    const newLang = lang === "ge" ? "en" : "ge";
    await setLanguage(newLang);
    router.refresh();
  };

  return (
    <header className="h-16 flex-shrink-0 flex items-center justify-between px-6 border-b border-card bg-background/80 backdrop-blur-md sticky top-0 z-10 w-full">
      {/* Search Input */}
      <div className="flex-1 max-w-2xl flex items-center mt-2 mb-2">
        <form onSubmit={handleSearch} className="relative w-full">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-muted" />
          <input
            type="text"
            value={ticker}
            onChange={(e) => setTicker(e.target.value)}
            placeholder={t("Search placeholder")}
            className="w-full bg-card border border-transparent hover:border-activeCard focus:border-green-500/50 focus:bg-activeCard focus:outline-none transition-colors rounded-full py-2.5 pl-10 pr-4 text-sm text-white placeholder:text-muted shadow-sm shadow-black/20"
          />
        </form>
      </div>

      {/* Right Actions */}
      <div className="flex items-center gap-4 pl-4">
        {/* Language Switcher */}
        <button 
          onClick={toggleLanguage}
          title="Switch Language"
          className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-card border border-white/5 hover:border-white/20 text-xs font-semibold text-white transition-colors"
        >
          <Globe className="w-3.5 h-3.5 text-green-500" />
          <span>{lang === "ge" ? "GE" : "EN"}</span>
        </button>
        
        <button className="p-2 text-muted hover:text-white hover:bg-card rounded-full transition-colors hidden sm:block">
          <Bell className="w-5 h-5" />
        </button>
        <div className="w-9 h-9 rounded-full bg-green-500/10 border border-green-500/20 text-green-500 flex items-center justify-center cursor-pointer hover:bg-green-500/20 transition-colors ml-1">
          <User className="w-4 h-4" />
        </div>
      </div>
    </header>
  );
}

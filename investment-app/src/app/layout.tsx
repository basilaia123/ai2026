import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Sidebar from "@/components/Sidebar";
import TopBar from "@/components/TopBar";
import { cookies } from "next/headers";
import { Language } from "@/lib/i18n";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "InvestPro - Dashboard",
  description: "Stock ticker and news dashboard",
};

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const cookieStore = await cookies();
  const lang = (cookieStore.get("lang")?.value || "ge") as Language;

  return (
    <html lang={lang} className={`${inter.variable} h-full antialiased`}>
      <body className="min-h-full flex bg-background text-white font-sans overflow-hidden">
        <Sidebar className="w-64 border-r border-card flex-shrink-0 hidden md:flex" lang={lang} />
        <div className="flex flex-col flex-1 h-screen overflow-hidden">
          <TopBar lang={lang} />
          <main className="flex-1 overflow-y-auto w-full mx-auto p-6 scroll-smooth bg-background">
            {children}
          </main>
        </div>
      </body>
    </html>
  );
}

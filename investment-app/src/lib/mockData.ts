export const mockChartData = Array.from({ length: 30 }).map((_, i) => {
  const date = new Date();
  date.setDate(date.getDate() - (29 - i));
  return {
    date: date.toISOString().split("T")[0],
    price: 150 + Math.random() * 20 + i * 0.5,
  };
});

export const mockNews = [
  {
    id: 1,
    title: "Tech Giant Announces Record Q3 Earnings With Massive Revenue Jump",
    source: "Bloomberg",
    time: "2 hours ago",
    badge: "Trending",
    badgeColor: "bg-green-500",
    image: "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?q=80&w=300&auto=format&fit=crop"
  },
  {
    id: 2,
    title: "New AI Integration Unveiled: How It Will Change the Landscape",
    source: "Reuters",
    time: "5 hours ago",
    badge: "Featured",
    badgeColor: "bg-blue-500",
    image: "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?q=80&w=300&auto=format&fit=crop"
  },
  {
    id: 3,
    title: "Market Reacts Positively to the Latest Smartphone Product Launch",
    source: "CNBC",
    time: "1 day ago",
    badge: "Top 10",
    badgeColor: "bg-orange-500",
    image: "https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?q=80&w=300&auto=format&fit=crop"
  }
];

export const mockStockInfo = {
  ticker: "AAPL",
  name: "Apple Inc.",
  price: 189.25,
  change: 2.34,
  changePercent: 1.25,
  isPositive: true,
};

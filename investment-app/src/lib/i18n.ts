export type Language = "ge" | "en";

export const dict = {
  ge: {
    // General Categories
    "Market Overview": "ბაზრის მიმოხილვა",
    "Technology Stocks": "ტექნოლოგიები",
    "Technology": "ტექნოლოგიები",
    "AI & Robotics": "ხელოვნური ინტელექტი",
    "Financial Sector": "ფინანსები",
    "Finance": "ფინანსები",
    "Healthcare Sector": "ჯანდაცვა",
    "Healthcare": "ჯანდაცვა",
    "Semiconductors": "ნახევარგამტარები",
    "Gaming & Entertainment": "გეიმინგი და გართობა",
    "Gaming": "გეიმინგი",
    "Energy Sector": "ენერგეტიკა",
    "Energy": "ენერგეტიკა",
    
    // Sidebar
    "Market Sectors": "ბაზრის სექტორები",
    "Time Period Context": "დროის პერიოდი",
    "1 Day": "1 დღე",
    "1 Week": "1 კვირა",
    "2 Weeks": "2 კვირა",
    "1 Month": "1 თვე",
    "3 Months": "3 თვე",
    "1 Year": "1 წელი",

    // TopBar
    "Search placeholder": "მოძებნეთ Ticker (მაგ. AAPL, TSLA)...",

    // Home / Category View
    "Category Overview": "კატეგორიის მიმოხილვა",
    "Discover the top trending stocks in this sector.": "აღმოაჩინეთ ტრენდული აქციები ამ სექტორში.",
    "Featured": "რჩეული",
    "Current Price": "მიმდინარე ფასი",
    
    // Single Stock View
    "Latest News": "ბოლო სიახლეები",
    "No recent news found for": "ბოლო სიახლეები ვერ მოიძებნა ამ Ticker-სთვის:",
    "Failed to load data for": "მონაცემების ჩატვირთვა ვერ მოხერხდა Ticker-ისთვის:",
    "Please check the ticker symbol and try again.": "გთხოვთ, შეამოწმოთ Ticker და სცადოთ ხელახლა.",
    
    // Key Statistics
    "Key Statistics": "ძირითადი სტატისტიკა",
    "Volume": "მოცულობა",
    "52-Week High": "52-კვირის მაქსიმუმი",
    "52-Week Low": "52-კვირის მინიმუმი",
    "Day's Range": "დღის დიაპაზონი",
    "Moving Average (SMA20)": "მცოცავი საშუალო (SMA20)"
  },
  en: {
    // General
    "Market Overview": "Market Overview",
    "Technology Stocks": "Technology Stocks",
    "Technology": "Technology",
    "AI & Robotics": "AI & Robotics",
    "Financial Sector": "Financial Sector",
    "Finance": "Finance",
    "Healthcare Sector": "Healthcare Sector",
    "Healthcare": "Healthcare",
    "Semiconductors": "Semiconductors",
    "Gaming & Entertainment": "Gaming & Entertainment",
    "Gaming": "Gaming",
    "Energy Sector": "Energy Sector",
    "Energy": "Energy",
    
    // Sidebar
    "Market Sectors": "Market Sectors",
    "Time Period Context": "Time Period Context",
    "1 Day": "1 Day",
    "1 Week": "1 Week",
    "2 Weeks": "2 Weeks",
    "1 Month": "1 Month",
    "3 Months": "3 Months",
    "1 Year": "1 Year",

    // TopBar
    "Search placeholder": "Search for a stock ticker (e.g. AAPL, TSLA)...",

    // Home / Category View
    "Category Overview": "Category Overview",
    "Discover the top trending stocks in this sector.": "Discover the top trending stocks in this sector.",
    "Featured": "Featured",
    "Current Price": "Current Price",
    
    // Single Stock View
    "Latest News": "Latest News",
    "No recent news found for": "No recent news found for",
    "Failed to load data for": "Failed to load data for",
    "Please check the ticker symbol and try again.": "Please check the ticker symbol and try again.",

    // Key Statistics
    "Key Statistics": "Key Statistics",
    "Volume": "Volume",
    "52-Week High": "52-Week High",
    "52-Week Low": "52-Week Low",
    "Day's Range": "Day's Range",
    "Moving Average (SMA20)": "Moving Average (SMA20)"
  }
};

export function getTranslation(lang: Language) {
  return (key: keyof typeof dict.en): string => {
    return dict[lang]?.[key] || dict.en[key] || key;
  };
}

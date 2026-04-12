/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "#0A0A0A", // Main extremely dark background
        card: "#141414", // Slightly lighter component backgrounds
        activeCard: "#1E1E1E", // Hover state background
        green: {
          400: "#4ade80",
          500: "#22c55e", // Main accent green from screenshot
          600: "#16a34a",
        },
        muted: "#A1A1AA", // zinc-400
      },
      fontFamily: {
        sans: ["var(--font-inter)", "sans-serif"],
      },
    },
  },
  plugins: [],
};

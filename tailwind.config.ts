import { type Config } from "tailwindcss";

export default {
  content: ["./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        beige: '#F7F7F1',
        midblue: '#93C5FD',
        darkblue: '#172554',
      },
    },
  },
  plugins: [],
} satisfies Config;

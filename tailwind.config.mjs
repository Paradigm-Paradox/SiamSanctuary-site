/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        brand: {
          pink: '#f286aa',
          champagne: '#d9c1a3',
          dark: '#181818',
          black: '#000000',
          charcoal: '#222222',
          red: '#c3161b',
          yellow: '#e1dbcb',
          green: '#42bf80',
          muted: '#888888',
        },
      },
      fontFamily: {
        sans: ['Jost', 'system-ui', '-apple-system', 'sans-serif'],
        serif: ['"Cormorant Infant"', 'Georgia', 'serif'],
        script: ['Quentin', 'cursive'],
      },
    },
  },
  plugins: [],
}

# DreamNails.Asia — Modernized Static Web Platform

Ultra-fast, zero-dependency modern static website for **DreamNails.Asia**, reverse-engineered from WordPress with 1:1 design fidelity preservation, built on **Astro 4**, **Tailwind CSS**, and edge-ready for **Cloudflare Pages**.

---

## 💅 Key Highlights & Design Preservation

- **100% Design & Aesthetic Fidelity**: Preserves the exact luxury dark salon palette (`#f286aa` rose pink, `#d9c1a3` champagne gold, `#181818` deep luxury slate), signature **Quentin** calligraphy font accents, **Jost** body typography, and **Cormorant Infant** luxury serif headings.
- **Complete Content Migration**:
  - **Hero & Philosophy**: Founder heritage of Joey & Onanong Jones, Phuket roots, 54 Professional Techniques, and clinical hospital-grade sanitation guarantee.
  - **10 Signature Services & Price Menu**: Express Manicure (฿250), Pedicure (฿350), Regular Manicure (฿350), Nail Art (฿400~600), Gel Extensions (฿400), Nail Protection (฿350), PVC Extensions (฿499), Spa Care (฿350), Acrylic Extensions (฿999), Spa & Art Combo (฿699).
  - **Client Nail Art Lookbook / Gallery**: Filterable showcase featuring 40+ high-resolution nail art, gel, and acrylic sculpt designs.
  - **Organic Beauty Shop**: All 12 authentic WooCommerce products (Craft Soaps, Hair Balsams, Creams, Oils) with pricing and order inquiry routing.
  - **6 Global Salon Hubs**: Mayagüez (Puerto Rico), Phuket (Thailand), Pattaya (Thailand), Bali (Indonesia), Dubai (UAE), and Douala (Cameroon).
  - **Interactive Global Map**: Zero-dependency Leaflet map (replaces heavy Google Maps API).
  - **Beauty & Nail Tips Blog**: All 6 articles on nail strengthening, seasonal tips, and gel polish care.
- **Zero Server Overhead**: 0 PHP, 0 MySQL databases, 0 vulnerable plugins. Instant sub-millisecond static page delivery.

---

## 🚀 Quick Start & Development

### 1. Start Local Development Server
```bash
./start-dev.sh
# Or run:
npm run dev
```
Preview will be live at: `http://localhost:4321/`

### 2. Build for Production
```bash
npm run build
```
Generates pure static HTML, CSS, fonts, and WebP/PNG assets in `dist/`.

### 3. Deploy to Cloudflare Pages
```bash
./deploy.sh
# Or run:
npx wrangler pages deploy dist --project-name=dreamnails-asia
```

---

## 📁 Project Architecture

```text
dreamnails-site/
├── public/
│   ├── fonts/               # Quentin calligraphy & LTE theme webfonts
│   ├── css/                 # Legacy & theme styling references
│   └── uploads/             # 150+ high-res photography assets
├── src/
│   ├── components/
│   │   ├── Header.astro     # Responsive luxury navigation & booking CTA
│   │   ├── Hero.astro       # Signature hero section
│   │   ├── Philosophy.astro # Founder story & hospital-grade pledge
│   │   ├── ServicesMenu.astro # 10 signature services & pricing grid
│   │   ├── PortfolioGallery.astro # Filterable nail art lookbook
│   │   ├── CosmeticsBanner.astro # Clean organic beauty banner
│   │   ├── LocationsSection.astro # 6 global salon branches
│   │   ├── Testimonials.astro # Client reviews & ratings
│   │   └── Footer.astro     # Brand footer & salon operating hours
│   ├── layouts/
│   │   └── Layout.astro     # Core HTML shell & interactive booking modal
│   ├── pages/
│   │   ├── index.astro      # Modernized Home
│   │   ├── about-us.astro   # About Joey & Onanong Jones & studio history
│   │   ├── services.astro   # Complete 8 service categories & price menu
│   │   ├── shop.astro       # Organic cosmetics e-commerce catalog
│   │   ├── contacts.astro   # Contact hubs & Leaflet interactive map
│   │   ├── news.astro       # Beauty & Nail Tips articles
│   │   └── privacy.astro    # Privacy policy
│   └── styles/
│       └── global.css       # Design variables, typography & luxury buttons
├── astro.config.mjs
├── tailwind.config.mjs
└── wrangler.jsonc
```

# Nail Art Showcase Runbook — How to Add New Photos

This guide explains how to easily add new client photos to the DreamNails showcase so that women can browse your latest nail art, gel, and acrylic creations.

---

## 📸 Step 1: Save the New Photo

1. Place your new photo in:
   ```text
   public/uploads/gallery/your-new-photo.jpg (or .png / .webp)
   ```
   *(You can also place it in any month folder like `public/uploads/2026/10/`)*

---

## 📝 Step 2: Add Entry in `src/data/gallery.json`

Open `src/data/gallery.json` and add a new item at the top of the list:

```json
{
  "id": "nail-design-new-01",
  "title": "Rose Quartz Chrome Almond",
  "category": "chrome",
  "categoryName": "Chrome & Glazed",
  "image": "/uploads/gallery/your-new-photo.jpg",
  "thumbnail": "/uploads/gallery/your-new-photo.jpg",
  "tags": ["Chrome", "Almond", "Glazed", "Trending"],
  "description": "Rose gold chrome overlay with high-gloss mirror finish."
}
```

### Available Categories:
* `"nail-art"` — Intricate Hand-Painted Art
* `"gel"` — Gel Polish & High Gloss Overlays
* `"acrylic"` — Sculpted Length & Stiletto
* `"french"` — Classic French & Soft Ombré
* `"chrome"` — Chrome, Iridescent & Glazed
* `"glam"` — Crystals, Gemstones & 3D Charms

---

## 🚀 Step 3: Deploy

Run the deployment script:
```bash
./deploy.sh
```
Or push to GitHub:
```bash
git add .
git commit -m "feat: add 5 new nail art photos to showcase"
git push origin main
```
Cloudflare Pages will automatically detect the commit, compile the new photos, and publish them to the live website within 60 seconds!

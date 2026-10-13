#!/usr/bin/env python3
import json
import re
import html

DATA_SRC = "/mnt/data/AI_Workspace/projects/Websites/dreamnails-data/json"
OUT_DIR = "/mnt/data/AI_Workspace/projects/Websites/dreamnails-site/src/data"

def clean_html_and_urls(content_str):
    if not content_str:
        return ""
    # Replace remote WP upload URLs with root-relative /uploads/
    s = re.sub(r'https?://(?:i[0-9]\.wp\.com/)?(?:www\.)?dreamnails\.asia/wp-content/uploads/', '/uploads/', content_str)
    # Strip image query params
    s = re.sub(r'(/uploads/[^\"\x27\s\)]+)\?[^\"\x27\s\)]+', r'\1', s)
    return s

# 1. Process Posts
with open(f"{DATA_SRC}/posts.json", "r", encoding="utf-8") as f:
    raw_posts = json.load(f)

posts = []
post_images = {
    "the-best-beach-ready-nails": "/uploads/2021/12/blog_03.jpg",
    "the-best-travel-friendly-nails": "/uploads/2021/12/blog_09.jpg",
    "making-a-statement-with-nail-art": "/uploads/2021/12/blog_11.jpg",
    "popular-nail-stamping-techniques-2": "/uploads/2021/09/nail-art-stamping-process-manicure-master-makes-s-2023-11-27-05-26-19-utc-1.jpg",
    "myths-about-gel-polish": "/uploads/2021/09/close-up-of-woman-s-hand-with-grey-nail-polish-2023-11-27-05-19-43-utc.jpg",
    "20-ways-to-strengthen-nails": "/uploads/2021/12/blog_14.jpg"
}

for p in raw_posts:
    slug = p.get("slug")
    title = html.unescape(p.get("title", {}).get("rendered", ""))
    content = clean_html_and_urls(p.get("content", {}).get("rendered", ""))
    excerpt = clean_html_and_urls(p.get("excerpt", {}).get("rendered", ""))
    # strip tags from excerpt
    plain_excerpt = re.sub(r'<[^>]+>', '', excerpt).strip()
    
    posts.append({
        "id": p.get("id"),
        "slug": slug,
        "title": title,
        "date": p.get("date", "").split("T")[0],
        "image": post_images.get(slug, "/uploads/2021/12/blog_03.jpg"),
        "excerpt": plain_excerpt,
        "content": content
    })

with open(f"{OUT_DIR}/posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=2)
print(f"Saved {len(posts)} posts to src/data/posts.json")

# 2. Process Services
with open(f"{DATA_SRC}/services.json", "r", encoding="utf-8") as f:
    raw_services = json.load(f)

service_meta = {
    "nail-care-artistry": {
        "icon": "fa-paint-brush",
        "tag": "Signature Core",
        "image": "/uploads/2022/01/serv_01_02.jpg",
        "fallback_content": "<p>Discover the height of nail elegance with Dream Nails. From classic manicures to advanced gel and acrylic nail sculpting, each service is performed with hospital-grade sterilized instruments and premium imported polishes.</p><p>Our master nail technicians customize every shape, color palette, and intricate hand-painted design to complement your individual style.</p>"
    },
    "waxing-hair-removal": {
        "icon": "fa-feather-alt",
        "tag": "Gentle Care",
        "image": "/uploads/2023/12/closeup-hand-applying-green-hot-wax-on-woman-butto-2023-11-27-05-17-53-utc-e1703953431339.jpg"
    },
    "skincare-facial-treatments": {
        "icon": "fa-spa",
        "tag": "Rejuvenating",
        "image": "/uploads/2021/12/inner_header_01.jpg"
    },
    "lashes-brows": {
        "icon": "fa-eye",
        "tag": "High Definition",
        "image": "/uploads/2023/12/young-woman-during-procedure-of-permanent-eyebrow-2023-11-28-23-02-41-utc.jpg"
    },
    "hair-services": {
        "icon": "fa-cut",
        "tag": "Salon Styling",
        "image": "/uploads/2023/12/hairstyling-in-hair-salon-2023-11-27-04-52-40-utc-e1703953619118.jpg"
    },
    "makeup-beauty-enhancements": {
        "icon": "fa-magic",
        "tag": "Editorial & Glam",
        "image": "/uploads/2024/01/fast-beauty-service-beautiful-ginger-girl-having-2023-11-27-05-21-12-utc.jpg"
    },
    "body-treatments-wellness": {
        "icon": "fa-heart",
        "tag": "Holistic Health",
        "image": "/uploads/2023/12/closeup-of-diverse-women-s-legs-sitting-in-studio-2023-11-27-05-18-57-utc-e1703953263386.jpg"
    },
    "specialized-vip-services": {
        "icon": "fa-crown",
        "tag": "Exclusive Luxury",
        "image": "/uploads/2022/05/AboutUS-1.jpg"
    }
}

services = []
for s in raw_services:
    slug = s.get("slug")
    title = html.unescape(s.get("title", {}).get("rendered", ""))
    content = clean_html_and_urls(s.get("content", {}).get("rendered", ""))
    meta = service_meta.get(slug, {})
    if not content:
        content = meta.get("fallback_content", "<p>Full specialized service details available upon consultation.</p>")
    
    # generate plain excerpt
    plain_excerpt = re.sub(r'<[^>]+>', '', content).strip()[:180] + "..."

    services.append({
        "id": s.get("id"),
        "slug": slug,
        "title": title,
        "icon": meta.get("icon", "fa-star"),
        "tag": meta.get("tag", "Service"),
        "image": meta.get("image", "/uploads/2022/01/serv_01_02.jpg"),
        "excerpt": plain_excerpt,
        "content": content
    })

with open(f"{OUT_DIR}/services.json", "w", encoding="utf-8") as f:
    json.dump(services, f, indent=2)
print(f"Saved {len(services)} services to src/data/services.json")

# 3. Process Products
with open(f"{DATA_SRC}/products.json", "r", encoding="utf-8") as f:
    raw_products = json.load(f)

products = []
for p in raw_products:
    name = html.unescape(p.get("name", ""))
    if name == "Reverse Withdrawal Payment":
        continue
    price_cents = int(p.get("prices", {}).get("price", "0"))
    price_str = f"${price_cents / 100:.2f}"
    images = [clean_html_and_urls(img.get("src", "")) for img in p.get("images", [])]
    img = images[0] if images else "/uploads/2021/12/shop-01.jpg"
    desc = clean_html_and_urls(p.get("description", ""))
    plain_desc = re.sub(r'<[^>]+>', '', desc).strip()
    
    slug = p.get("slug") or re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

    products.append({
        "id": p.get("id"),
        "slug": slug,
        "name": name,
        "price": price_str,
        "image": img,
        "category": p.get("categories", [{}])[0].get("name", "Beauty Care") if p.get("categories") else "Beauty Care",
        "description": plain_desc or "Natural luxury formulation created with clean botanical ingredients."
    })

with open(f"{OUT_DIR}/products.json", "w", encoding="utf-8") as f:
    json.dump(products, f, indent=2)
print(f"Saved {len(products)} products to src/data/products.json")

# 4. Locations Data
locations = [
  {
    "city": "Mayaguez",
    "name": "Mayagüez, Puerto Rico",
    "country": "Puerto Rico, USA",
    "code": "MAZ",
    "address": "Mayagüez, PR 00680",
    "phone": "+1 (787) 906-8800",
    "email": "info.maz@dreamnails.asia",
    "tagline": "Caribbean Luxury & Coastal Nail Art",
    "hours": "Monday - Friday & Sunday: 9:00 AM - 5:00 PM",
    "badge": "Active Hub",
    "lat": 18.2013,
    "lng": -67.1452,
    "description": "Our Caribbean oasis offering premium manicures, pedicure spa rituals, and coastal nail artistry in the historic city of Mayagüez."
  },
  {
    "city": "Phuket",
    "name": "Phuket, Thailand",
    "country": "Thailand",
    "code": "HKT",
    "address": "Phuket, Thailand 83000",
    "phone": "+66.76.321.456",
    "email": "info.hkt@dreamnails.asia",
    "tagline": "Founding Studio & Master Artists",
    "hours": "Monday - Friday & Sunday: 9:00 AM - 5:00 PM",
    "badge": "Flagship Heritage",
    "lat": 7.8804,
    "lng": 98.3923,
    "description": "The birthplace of Dream Nails Asia. Seasoned masters with over 15+ years crafting intricate nail designs in tropical paradise."
  },
  {
    "city": "Pattaya",
    "name": "Pattaya, Thailand",
    "country": "Thailand",
    "code": "PTY",
    "address": "Pattaya, Thailand 20150",
    "phone": "+66.38.654.321",
    "email": "info.pty@dreamnails.asia",
    "tagline": "Vibrant Coastal Beauty Bar",
    "hours": "Monday - Friday & Sunday: 9:00 AM - 5:00 PM",
    "badge": "Active Studio",
    "lat": 12.9276,
    "lng": 100.8771,
    "description": "Trendsetting nail studio catering to discerning locals and world travelers with high-speed express care and glam enhancements."
  },
  {
    "city": "Bali",
    "name": "Bali, Indonesia",
    "country": "Indonesia",
    "code": "DPS",
    "address": "Bali, Indonesia 80361",
    "phone": "+62.361.789.012",
    "email": "info.dps@dreamnails.asia",
    "tagline": "Tropical Island Wellness Sanctuary",
    "hours": "Monday - Friday & Sunday: 9:00 AM - 5:00 PM",
    "badge": "Wellness Destination",
    "lat": -8.4095,
    "lng": 115.1889,
    "description": "Holistic island retreat blending organic botanical scrubs, hot stone pedicures, and eco-conscious nail care."
  },
  {
    "city": "Dubai",
    "name": "Dubai, UAE",
    "country": "United Arab Emirates",
    "code": "DXB",
    "address": "Dubai, United Arab Emirates",
    "phone": "+971.4.555.0199",
    "email": "info.uxb@dreamnails.asia",
    "tagline": "Ultra-Luxury Nail Lounge & 24K Treatments",
    "hours": "Monday - Friday & Sunday: 9:00 AM - 5:00 PM",
    "badge": "VIP Luxury",
    "lat": 25.2048,
    "lng": 55.2708,
    "description": "High-fashion nail lounge featuring 24K gold foil embellishments, private VIP suites, and precision Russian manicures."
  },
  {
    "city": "Douala",
    "name": "Douala, Cameroon",
    "country": "Cameroon",
    "code": "DLA",
    "address": "Douala, Cameroon 237",
    "phone": "+237.233.421.900",
    "email": "info.dla@dreamnails.asia",
    "tagline": "West African Flagship Beauty Hub",
    "hours": "Monday - Friday & Sunday: 9:00 AM - 5:00 PM",
    "badge": "Global Expansion",
    "lat": 4.0511,
    "lng": 9.7679,
    "description": "State-of-the-art beauty sanctuary delivering international nail artistry, extensions, and luxury spa treatments in Douala."
  }
]

with open(f"{OUT_DIR}/locations.json", "w", encoding="utf-8") as f:
    json.dump(locations, f, indent=2)
print(f"Saved {len(locations)} locations to src/data/locations.json")

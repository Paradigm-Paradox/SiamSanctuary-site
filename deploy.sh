#!/usr/bin/env bash
# Deploy static site directly to Cloudflare Pages
set -e
cd "$(dirname "$0")"
echo "Building DreamNails.Asia static site..."
npm run build

echo "Deploying to Cloudflare Pages..."
npx wrangler pages deploy dist --project-name=dreamnails-asia

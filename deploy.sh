#!/usr/bin/env bash
# Deploy static site directly to Cloudflare Pages
set -e
cd "$(dirname "$0")"

echo "==========================================="
echo " DreamNails.Asia — Cloudflare Pages Deploy"
echo "==========================================="

if [ -z "$CLOUDFLARE_API_TOKEN" ]; then
  echo "Checking Wrangler authentication status..."
  if ! npx wrangler whoami >/dev/null 2>&1; then
    echo ""
    echo "⚠️  You are not authenticated with Cloudflare yet."
    echo "Choose one of the following methods to authenticate:"
    echo ""
    echo "Method 1 (API Token - Recommended):"
    echo "  export CLOUDFLARE_API_TOKEN=\"your-api-token\""
    echo "  ./deploy.sh"
    echo ""
    echo "Method 2 (OAuth Login):"
    echo "  npx wrangler login"
    echo "  ./deploy.sh"
    echo ""
    exit 1
  fi
fi

echo "Building DreamNails.Asia static site (39 routes)..."
npm run build

echo "Deploying to Cloudflare Pages project 'dreamnails-asia'..."
npx wrangler pages deploy dist --project-name=dreamnails-asia --commit-dirty=true

echo ""
echo "🎉 Deployment to Cloudflare Pages complete!"

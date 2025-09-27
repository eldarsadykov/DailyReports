#!/usr/bin/env bash
set -e  # Exit immediately if a command fails

echo "🚀 Building static assets..."

# Create directories
echo "📁 Creating static files directories..."
mkdir -p tasks/static/{js,css}

# Copy JS dependencies
echo "📦 Copying JS dependencies..."
cp node_modules/htmx.org/dist/htmx.min.js tasks/static/js/
cp node_modules/alpinejs/dist/cdn.min.js tasks/static/js/alpinejs.min.js

# Build Tailwind CSS (minified)
echo "🎨 Building Tailwind CSS..."
npx tailwindcss -i src/input.css -o tasks/static/css/output.css --minify

echo "✅ Build complete!"

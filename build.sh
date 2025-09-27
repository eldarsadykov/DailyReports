echo "Creating static files directory..." &&
mkdir -p tasks/static/js &&
echo "Copying minified htmx.org sources..." &&
cp node_modules/htmx.org/dist/htmx.min.js tasks/static/js &&
echo "Copying minified alpinejs sources..." &&
cp node_modules/alpinejs/dist/cdn.min.js tasks/static/js/alpinejs.min.js
tailwindcss -i src/input.css -o tasks/static/css/output.css --minify
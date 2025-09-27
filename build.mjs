#!/usr/bin/env node
import { mkdirSync, copyFileSync } from 'fs';
import { execSync } from 'child_process';

console.log('🚀 Building static assets...');

// Create directories
console.log('📁 Creating directories...');
mkdirSync('tasks/static/js', { recursive: true });
mkdirSync('tasks/static/css', { recursive: true });

// Copy dependencies
console.log('📦 Copying JS dependencies...');
copyFileSync('node_modules/htmx.org/dist/htmx.min.js', 'tasks/static/js/htmx.min.js');
copyFileSync('node_modules/alpinejs/dist/cdn.min.js', 'tasks/static/js/alpinejs.min.js');

// Build Tailwind
console.log('🎨 Building Tailwind CSS...');
execSync('tailwindcss -i src/input.css -o tasks/static/css/output.css --minify', { stdio: 'inherit' });

console.log('✅ Build complete!');

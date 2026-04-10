const fs = require('fs');
const path = 'c:\\Users\\GBASILAIA\\claude\\ai2026\\tempo\\lecture-3-slides.html';
let html = fs.readFileSync(path, 'utf8');

html = html.replace(/<button class="copy-btn absolute top-2 right-2 bg-white\/10 hover:bg-tempo-gold hover:text-tempo-900 text-white px-3 py-1 rounded text-xs transition-colors">კოპირება<\/button>/g, '');

fs.writeFileSync(path, html);
console.log("Removed hardcoded copy buttons.");

const fs = require('fs');
const glob = require('glob');

const files = glob.sync('c:/Users/GBASILAIA/claude/ai2026/tempo/**/*.html');
let count = 0;

files.forEach(file => {
    let content = fs.readFileSync(file, 'utf8');
    if (content.includes('.prose h4 {')) {
        let original = content;
        
        // Remove color from the general rules and add specificity rules for colors
        content = content.replace(
            /\.prose h3\s*\{\s*font-size:\s*1\.5rem;\s*font-weight:\s*bold;\s*margin-top:\s*1\.5rem;\s*margin-bottom:\s*0\.75rem;\s*color:\s*#1A1A1A;\s*\}/g,
            '.prose h3 { font-size: 1.5rem; font-weight: bold; margin-top: 1.5rem; margin-bottom: 0.75rem; }\n        .prose h3:not([class*="text-"]) { color: #1A1A1A; }'
        );

        content = content.replace(
            /\.prose h4\s*\{\s*font-size:\s*1\.25rem;\s*font-weight:\s*bold;\s*margin-top:\s*1\.25rem;\s*margin-bottom:\s*0\.5rem;\s*color:\s*#2C2C2C;\s*\}/g,
            '.prose h4 { font-size: 1.25rem; font-weight: bold; margin-top: 1.25rem; margin-bottom: 0.5rem; }\n        .prose h4:not([class*="text-"]) { color: #2C2C2C; }'
        );

        if (content !== original) {
            fs.writeFileSync(file, content);
            console.log('Fixed CSS in ' + file);
            count++;
        }
    }
});

console.log(`Total files fixed: ${count}`);

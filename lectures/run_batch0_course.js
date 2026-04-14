const fs = require('fs');
const { proofread } = require('./proofreader_module.js');

// Process files one by one, print report for each
const targets = [
    'index.html',
    'course-info.html',
    'course-description.html',
    'final-project-ideas.html',
];

let totalChanges = 0;

for (const file of targets) {
    if (!fs.existsSync(file)) {
        console.log(`⚠️  SKIP: ${file} (not found)`);
        continue;
    }
    const changes = proofread(file);
    if (changes.length === 0) {
        console.log(`✅ ${file} — შეცდომების გარეშეა`);
    } else {
        console.log(`\n📄 ${file} — ${changes.length} ტიპის ცვლილება:`);
        changes.forEach(c => console.log(`   • ${c}`));
        totalChanges += changes.length;
    }
}
console.log(`\n✔️  დასრულდა. სულ: ${totalChanges} ტიპის ცვლილება.`);

const fs = require('fs');
const { proofread } = require('./proofreader_module.js');

const targets = [
    'lecture-1-slides.html',
    'lecture-1-summary.html',
    'lecture-1-study-guide.html',
    'lecture-1-exercises.html',
    'lecture-1-quick-ref.html',
    'lecture-1-lesson-plan.html',
    'homework-1.html',
];

let totalChanges = 0;
for (const file of targets) {
    if (!fs.existsSync(file)) { console.log(`⚠️  SKIP: ${file}`); continue; }
    const changes = proofread(file);
    if (changes.length === 0) {
        console.log(`✅ ${file} — შეცდომების გარეშეა`);
    } else {
        console.log(`\n📄 ${file} — ${changes.length} ტიპის ცვლილება:`);
        changes.forEach(c => console.log(`   • ${c}`));
        totalChanges += changes.length;
    }
}
console.log(`\n✔️  ლექცია 1 დასრულდა. სულ: ${totalChanges} ტიპის ცვლილება.`);

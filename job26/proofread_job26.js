const fs = require('fs');

function proofread(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Spaces around punctuation: Space before punctuation should be removed
    content = content.replace(/\s+([.,!?:;])(?=\s|<|$)/g, '$1');
    
    // Quotations (standardizing to commas at the start ,,...")
    // Exclude if it breaks typical HTML classes or attributes
    content = content.replace(/(^|[\s>])\"([ა-ჰ][^"]+[ა-ჰ])\"/g, '$1,,$2"');

    // Passive overuse / over-formalization
    content = content.replace(/\bწარმოადგენს\b/g, 'არის');
    content = content.replace(/\bწარმოადგენდნენ\b/g, 'იყვნენ');
    content = content.replace(/\bწარმოადგენდეს\b/g, 'იყოს');
    
    // Loanwords & Barabarisms
    content = content.replace(/\bთასქებ([ა-ჰ]*)/gi, 'დავალებ$1');
    content = content.replace(/\bთასქს\b/gi, 'დავალებას');
    content = content.replace(/\bთასქი\b/gi, 'დავალება');
    content = content.replace(/\bდეფოლტად\b/g, 'სტანდარტულად');
    
    // Typical syntax calques
    content = content.replace(/აზრი აქვს/g, 'მიზანშეწონილია'); 
    
    // Abbreviation prohibition Rule (AGENTS.md)
    content = content.replace(/AI-სთან/g, 'ხელოვნურ ინტელექტთან');
    content = content.replace(/AI-ს/g, 'ხელოვნურ ინტელექტს');
    content = content.replace(/AI-ით/g, 'ხელოვნური ინტელექტით');
    // For English prompt tags (like Prompts vs პრომპტი) - mostly handled
    content = content.replace(/\(მაგ:/g, '(მაგალითად:');
    content = content.replace(/\(მაგ\./g, '(მაგალითად:');
    content = content.replace(/\sმაგ\./g, ' მაგალითად:');
    content = content.replace(/სთ\./g, 'საათი');
    content = content.replace(/კვ\./g, 'კვარტალში');
    content = content.replace(/2-3x/g, '2-3-ჯერ');
    content = content.replace(/10x/gi, '10-ჯერ');
    
    // Spelling fixes seen previously in other files
    content = content.replace(/დაიაფფასიანი/g, 'და იაფფასიანი');

    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Proofread: ' + filePath);
}

const targetFiles = [
    'index.html', 
    'cv-samples.html', 
    'job-hunting-training-60min-exercises.html', 
    'job-hunting-training-60min-quick-ref.html', 
    'job-hunting-training-lesson-plan.html'
];

targetFiles.forEach(f => {
    if(fs.existsSync(f)) {
        proofread(f);
    } else {
        console.log('Skipping ' + f + ' (not found)');
    }
});

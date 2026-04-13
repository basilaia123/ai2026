const fs = require('fs');

function proofread(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Spaces around punctuation: Space before punctuation should be removed
    content = content.replace(/\s+([.,!?:;])(?=\s|<|$)/g, '$1');
    
    // Quotations (standardizing to commas at the start ,,...")
    // This looks for quoted Georgian text not inside HTML angular brackets
    // It's dangerous so I will limit it to standard quotes used in typical text.
    // Replace "TEXT" with ,,TEXT"
    content = content.replace(/(^|[\s>])\"([ა-ჰ][^"]+[ა-ჰ])\"/g, '$1,,$2"');

    // Passive overuse - in Georgian, "წარმოადგენს" is a bit heavy, "არის" is better
    content = content.replace(/\bწარმოადგენს\b/g, 'არის');
    content = content.replace(/\bწარმოადგენდნენ\b/g, 'იყვნენ');
    
    // Loanwords
    content = content.replace(/\bთასქებ/g, 'დავალებ'); // თასქები -> დავალებები
    content = content.replace(/\bთასქს/g, 'დავალებას');
    content = content.replace(/\bთასქი/g, 'დავალება');
    content = content.replace(/\bდეფოლტად\b/g, 'სტანდარტულად');
    
    // Typical syntax calques
    content = content.replace(/აზრი აქვს/g, 'მიზანშეწონილია'); 

    fs.writeFileSync(filePath, content, 'utf8');
    console.log('Proofread: ' + filePath);
}

['index.html', 'oppa-training.html'].forEach(f => {
    if(fs.existsSync(f)) {
        proofread(f);
    }
});

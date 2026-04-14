const fs = require('fs');
const path = require('path');

function proofread(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    let changes = [];

    // ==========================================
    // georgian-proofreader.skill RULES APPLIED
    // ==========================================

    // === RULE 5: DASHES ===
    // Em-dash and en-dash are banned in Georgian; replace with simple hyphen
    // But be careful not to break HTML entities like &mdash; or CSS borders
    let emDashCount = (content.match(/—/g) || []).length;
    let enDashCount = (content.match(/–/g) || []).length;
    content = content.replace(/—/g, '-');
    content = content.replace(/–/g, '-');
    if (emDashCount > 0) changes.push(`Em-dash (—) → hyphen: ${emDashCount} ჯერ`);
    if (enDashCount > 0) changes.push(`En-dash (–) → hyphen: ${enDashCount} ჯერ`);

    // === RULE 5: ABBREVIATIONS ===
    // მაგ. / მაგ: → მაგალითად:
    let magCount = (content.match(/\(მაგ\.|მაგ\.|, მაგ\.|; მაგ\./g) || []).length;
    content = content.replace(/\(მაგ\./g, '(მაგალითად:');
    content = content.replace(/,\s*მაგ\./g, ', მაგალითად:');
    content = content.replace(/;\s*მაგ\./g, '; მაგალითად:');
    content = content.replace(/\bმაგ\.\s/g, 'მაგალითად: ');
    content = content.replace(/\(მაგ:/g, '(მაგალითად:');
    if (magCount > 0) changes.push(`"მაგ." → "მაგალითად:": ${magCount} ჯერ`);

    // სთ. → საათი
    let stCount = (content.match(/\bსთ\./g) || []).length;
    content = content.replace(/\bსთ\./g, 'საათი');
    if (stCount > 0) changes.push(`"სთ." → "საათი": ${stCount} ჯერ`);

    // ციტ. → ციტატა
    let citCount = (content.match(/ციტ\./g) || []).length;
    content = content.replace(/ციტ\./g, 'ციტატა');
    if (citCount > 0) changes.push(`"ციტ." → "ციტატა": ${citCount} ჯერ`);

    // გვ. → გვერდი (only clear text abbreviations, not inside strings)
    let gvCount = (content.match(/\bგვ\./g) || []).length;
    content = content.replace(/\bგვ\.\s/g, 'გვერდი ');
    if (gvCount > 0) changes.push(`"გვ." → "გვერდი": ${gvCount} ჯერ`);

    // პ. (paragraph abbreviation) → პუნქტი
    let pCount = (content.match(/\sპ\.\s/g) || []).length;
    content = content.replace(/\sპ\.\s/g, ' პუნქტი ');
    if (pCount > 0) changes.push(`"პ." → "პუნქტი": ${pCount} ჯერ`);

    // განყ. → განყოფილება
    let gany = (content.match(/განყ\./g) || []).length;
    content = content.replace(/განყ\./g, 'განყოფილება');
    if (gany > 0) changes.push(`"განყ." → "განყოფილება": ${gany} ჯერ`);

    // ვნახე / ვდ. → ვნახე / და სხვა
    let vd = (content.match(/ვდ\./g) || []).length;
    content = content.replace(/ვდ\./g, 'და სხვა');
    if (vd > 0) changes.push(`"ვდ." → "და სხვა": ${vd} ჯერ`);

    // === RULE 5: AI SUFFIXES ===
    let aiSuffixes = (content.match(/AI-სთან|AI-ს|AI-ით|AI-ებ[ა-ჰ]*/g) || []).length;
    content = content.replace(/AI-სთან/g, 'ხელოვნურ ინტელექტთან');
    content = content.replace(/AI-ს\b/g, 'ხელოვნურ ინტელექტს');
    content = content.replace(/AI-ით\b/g, 'ხელოვნური ინტელექტით');
    if (aiSuffixes > 0) changes.push(`AI-ს/AI-ით/AI-სთან → სრული ფორმა: ${aiSuffixes} ჯერ`);

    // === RULE 5: NUMERIC MODIFIERS ===
    let numMod = (content.match(/\d+x\b/gi) || []).length;
    content = content.replace(/(\d+)x\b/gi, '$1-ჯერ');
    if (numMod > 0) changes.push(`Nx → N-ჯერ: ${numMod} ჯერ`);

    // === RULE 4: OVER-FORMALIZATION ===
    let repr = (content.match(/\bწარმოადგენს\b/g) || []).length;
    content = content.replace(/\bწარმოადგენს\b/g, 'არის');
    if (repr > 0) changes.push(`"წარმოადგენს" → "არის": ${repr} ჯერ`);

    // === RULE 4: BARBARISMS / CORPORATE LOANWORDS ===
    let task = (content.match(/\bთასქ[ა-ჰ]*/g) || []).length;
    content = content.replace(/\bთასქ([ა-ჰ]*)/g, 'დავალებ$1');
    if (task > 0) changes.push(`"თასქ..." → "დავალებ...": ${task} ჯერ`);

    let def = (content.match(/\bდეფოლტად\b/g) || []).length;
    content = content.replace(/\bდეფოლტად\b/g, 'სტანდარტულად');
    if (def > 0) changes.push(`"დეფოლტად" → "სტანდარტულად": ${def} ჯერ`);

    // === RULE 3: UNNATURAL PHRASES ===
    let azmr = (content.match(/აზრი აქვს/g) || []).length;
    content = content.replace(/აზრი აქვს/g, 'მიზანშეწონილია');
    if (azmr > 0) changes.push(`"აზრი აქვს" → "მიზანშეწონილია": ${azmr} ჯერ`);

    // === RULE 5: SPACING before punctuation ===
    let spacePunct = (content.match(/ +[.,!?:;](?=\s|<|$)/g) || []).length;
    content = content.replace(/ +([.,!?:;])(?=\s|<|$)/g, '$1');
    if (spacePunct > 0) changes.push(`Space-before-punct გასწ: ${spacePunct} ჯერ`);

    fs.writeFileSync(filePath, content, 'utf8');
    return changes;
}

module.exports = { proofread };

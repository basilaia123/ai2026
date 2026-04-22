const fs = require('fs');

const biosPath = 'c:/Users/GBASILAIA/claude/ai2026/unlimited/bios.txt';
const indexPath = 'c:/Users/GBASILAIA/claude/ai2026/unlimited/index.html';

const biosText = fs.readFileSync(biosPath, 'utf8');

// Robust parsing of bios.txt
// It seems to be formatted as:
// NUMBER. NAME [ICON] [WORKSHOP]
// BIO_TEXT
// Summit-ზე ...
const bioSections = biosText.split(/\n\d+\.\s+/);
const bioMap = {};

const speakersToMatch = [
    { indexName: "Tornike Bolokadze", fileNames: ["Tornike Bolokadze"] },
    { indexName: "Salome Argvliani", fileNames: ["Salome Argvliani"] },
    { indexName: "Khatuna Mdinaradze", fileNames: ["Khatuna Mdinaradze", "ხათუნა მდინარაძე"] },
    { indexName: "Davit Jijavadze", fileNames: ["Davit Jijavadze"] },
    { indexName: "Davit Tsilosani", fileNames: ["Davit Tsilosani"] },
    { indexName: "Victoria Sakurova", fileNames: ["Victoria Sakurova"] },
    { indexName: "Anri S. (Anzor S.)", fileNames: ["Anzor S.", "Anri S."] },
    { indexName: "Salome Sulaberidze", fileNames: ["Salome Sulaberidze"] },
    { indexName: "David Chikvaidze", fileNames: ["David Chikvaidze"] },
    { indexName: "Guro Davitlidze", fileNames: ["Guro Davitlidze"] },
    { indexName: "Alex Chikovani", fileNames: ["Alex Chikovani"] },
    { indexName: "Nodo Ivanidze", fileNames: ["Nodo Ivanidze"] },
    { indexName: "Irina Gagoshidze", fileNames: ["Irina Gagoshidze"] },
    { indexName: "Maria Ghlonti", fileNames: ["Maria Ghlonti"] },
    { indexName: "Mariam Zumbadze", fileNames: ["Mariam Zumbadze"] },
    { indexName: "Giorgi Razmadze", fileNames: ["Giorgi Razmadze"] },
    { indexName: "Maka Makhatadze", fileNames: ["Maka Makhatadze"] },
    { indexName: "Salome Bortsvadze", fileNames: ["Salome Bortsvadze"] },
    { indexName: "Nino Gorgadze", fileNames: ["Nino Gorgadze"] },
    { indexName: "David Chiaberashvili", fileNames: ["David Chiaberashvili"] },
    { indexName: "Zurab Pertaia", fileNames: ["Zurab Pertaia"] },
    { indexName: "Natia Skhvitaridze", fileNames: ["Natia Skhvitaridze"] },
    { indexName: "Giorgi Gurgenidze", fileNames: ["Giorgi Gurgenidze", "გიორგი გურგენიძე"] },
    { indexName: "Nino Tsitlanadze", fileNames: ["Nino Tsitlanadze"] },
    { indexName: "Alex M Dascalu", fileNames: ["Alex M Dascalu"] },
    { indexName: "Maka Natsvlishvili", fileNames: ["Maka Natsvlishvili"] },
    { indexName: "Giorgi Basilaia", fileNames: ["Giorgi Basilaia"] },
    { indexName: "Levan Nikolaishvili", fileNames: ["Levan Nikolaishvili"] },
    { indexName: "Levan Giorgadze", fileNames: ["Levan Giorgadze"] },
    { indexName: "Nina Pertenava", fileNames: ["Nina Pertenava"] },
    { indexName: "Levan Koberidze", fileNames: ["Levan Koberidze", "Levan KOBERIDZE"] },
    { indexName: "Levan Meskhishvili", fileNames: ["Levan Meskhishvili"] },
    { indexName: "Giorgi Vekua", fileNames: ["Giorgi Vekua"] },
    { indexName: "Irakli Tchavtchanidze", fileNames: ["Irakli Tchavtchanidze", "ირაკლი ჭავჭანიძე"] },
    { indexName: "George Batsiashvili", fileNames: ["George (Giorgi) Batsiashvili"] },
    { indexName: "Aleksandre Chomakhidze", fileNames: ["Aleksandre Chomakhidze"] },
    { indexName: "Gigi Kurtanidze", fileNames: ["Gigi Kurtanidze"] },
    { indexName: "Luka Khaladze", fileNames: ["Luka Khaladze"] },
    { indexName: "Natia Beridze", fileNames: ["Natia Beridze"] },
    { indexName: "Natia Giorgadze", fileNames: ["Natia Giorgadze"] },
    { indexName: "Medea Janjghava", fileNames: ["Medea Janjghava"] },
    { indexName: "Luka Lomsadze", fileNames: ["Luka Lomsadze"] },
    { indexName: "Gvantsa Gabaidze", fileNames: ["Gvantsa Gabaidze"] },
    { indexName: "Genadi Shamugia", fileNames: ["Genadi Shamugia"] },
    { indexName: "Konstantine Dvalishvili", fileNames: ["Konstantine Dvalishvili"] }
];

bioSections.forEach(section => {
    const lines = section.split('\n').map(l => l.trim()).filter(l => l);
    if (lines.length < 2) return;
    
    const header = lines[0];
    const match = speakersToMatch.find(s => s.fileNames.some(fn => header.includes(fn)));
    
    if (match) {
        let bioLines = [];
        for (let i = 1; i < lines.length; i++) {
            if (lines[i].includes("Summit-ზე") || lines[i].includes("Unlimited Summit-ზე")) break;
            bioLines.push(lines[i]);
        }
        if (bioLines.length > 0) {
            bioMap[match.indexName] = bioLines.join(' ').trim();
        }
    }
});

let indexContent = fs.readFileSync(indexPath, 'utf8');

// Apply updates
Object.keys(bioMap).forEach(speakerName => {
    const escapedName = speakerName.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    const regex = new RegExp(`(speaker:\\s*"${escapedName}"[^}]*?bio:\\s*")[^"]*(")`, 'g');
    indexContent = indexContent.replace(regex, (m, p1, p2) => p1 + bioMap[speakerName] + p2);
});

fs.writeFileSync(indexPath, indexContent);
console.log("Surgical bio update complete.");

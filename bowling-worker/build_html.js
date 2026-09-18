import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const sourcePath = path.join(__dirname, '..', 'bowling', 'index.html');
const destPath = path.join(__dirname, 'src', 'html.js');

const htmlContent = fs.readFileSync(sourcePath, 'utf8');
const moduleContent = `export const GAME_HTML = ${JSON.stringify(htmlContent)};\n`;

fs.writeFileSync(destPath, moduleContent, 'utf8');
console.log(`Successfully compiled bowling/index.html into bowling-worker/src/html.js (${(moduleContent.length / 1024).toFixed(1)} KB)`);

// Original offline example for this specific v1.0.0 release. No network or HTML execution.
import { createHash } from 'node:crypto';
import { lstatSync, readFileSync } from 'node:fs';
import { resolve, join } from 'node:path';

const [directory, mode, extra] = process.argv.slice(2);
if (!directory || extra || (mode && mode !== '--documents-only')) {
  console.error('Usage: node verify-downloads.mjs DIRECTORY [--documents-only]');
  process.exit(2);
}
const expected = [
  ['workshop-planning-template.zip', 10570, '4ef74c4eace9f9725e9bbad0deb324845decfc7dc8f7864129eafa63b2fe5ed1'],
  ['workshop-planning-worksheet.html', 4742, '76ed0abab9a067a9f0f98bd91407b16dfbe2f4e503aa7c609a10aca83fbd674b'],
  ['workshop-planning-worksheet.md', 2729, '3a536ee9017a0187b48d3ce89898667c6ff541cbab09e3e04a0294b95eea9c2e'],
];
let failed = false;
for (const [name, bytes, digest] of expected) {
  if (mode === '--documents-only' && name.endsWith('.zip')) continue;
  try {
    const file = join(resolve(directory), name);
    const info = lstatSync(file);
    if (!info.isFile() || info.isSymbolicLink() || info.size !== bytes) throw new Error('file type or byte count differs');
    const actual = createHash('sha256').update(readFileSync(file)).digest('hex');
    if (actual !== digest) throw new Error('SHA-256 differs');
    console.log(`PASS ${name} (${bytes} bytes)`);
  } catch (error) {
    failed = true;
    console.error(`FAIL ${name}: ${error.code || error.message}`);
  }
}
process.exitCode = failed ? 1 : 0;

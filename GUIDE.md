# Verify a workshop download pack with Node.js, then edit HTML and Markdown separately

**AI disclosure:** This guide and its original verification script were drafted primarily by an AI agent from the actual saved files. The code was checked locally. This is a reproducible file-handling example, not a firsthand classroom report.

A developer running a workshop may need an editable text handout and a print draft. Keeping those formats in one ZIP is convenient, but a file inventory, a CRC32 value and a SHA-256 digest answer different questions. This walkthrough uses one small, free Japanese worksheet to make those checks concrete.

The blank planner has three sections, six prompts and eighteen answer lines. It asks a facilitator to plan an audience, one observable task, materials, practice, a check and reflection. Its 3 + 9 + 3 minute schedule is an editable example. You can change the prompts and timing for your session; no participant answers or teaching results are supplied.

## 1. Save the three reference files

Use the assets in the [v1.0.0 release](https://github.com/kumiromiscythespec/workshop-planning-worksheet/releases/tag/v1.0.0). Save these three files together in a folder such as `downloads`:

- [workshop-planning-template.zip](https://github.com/kumiromiscythespec/workshop-planning-worksheet/releases/download/v1.0.0/workshop-planning-template.zip)
- [workshop-planning-worksheet.html](https://github.com/kumiromiscythespec/workshop-planning-worksheet/releases/download/v1.0.0/workshop-planning-worksheet.html)
- [workshop-planning-worksheet.md](https://github.com/kumiromiscythespec/workshop-planning-worksheet/releases/download/v1.0.0/workshop-planning-worksheet.md)

The document text is Japanese. Node.js is needed for the optional check below; no npm packages, account, purchase or network call from the script is needed.

## 2. Check the exact downloaded bytes

Save this original example as `verify-downloads.mjs`. It only reads the three fixed filenames. It checks file type and byte count before hashing; it does not execute HTML, extract a ZIP or modify a file.

```js
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
```

Run it from the folder containing the script, passing the folder containing the downloads:

```sh
node verify-downloads.mjs ./downloads
```

For the unchanged release, the expected output is:

```text
PASS workshop-planning-template.zip (10570 bytes)
PASS workshop-planning-worksheet.html (4742 bytes)
PASS workshop-planning-worksheet.md (2729 bytes)
```

A mismatch gives exit code `1`; a missing or invalid command argument gives `2`. A successful check means the files match the reference bytes embedded in this script. The reference values must come from a source you trust. A digest match does not establish who authored a file, that its content is harmless, or that it will render correctly.

## 3. Read the ZIP inventory without confusing its checks

Extract the ZIP using your usual archive tool, then read `README.txt`. The saved pack contains exactly:

```text
README.txt
manifest.json
files/workshop-planning-worksheet.html
files/workshop-planning-worksheet.md
```

`manifest.json` records the two document paths, byte counts and CRC32 values:

| Document | Bytes | CRC32 |
|---|---:|---|
| files/workshop-planning-worksheet.html | 4742 | df63f676 |
| files/workshop-planning-worksheet.md | 2729 | 49d95190 |

Those CRC32 values help check accidental corruption. They are not cryptographic authenticity checks. The manifest is an inventory supplied with the pack; it is not a signed identity statement and does not contain SHA-256 values.

The script above checks the SHA-256 of the entire ZIP and of the two directly downloaded documents. It does not parse ZIP headers or validate the manifest's CRC32 values. To check the two documents after extraction against the same published SHA-256 references, run:

```sh
node verify-downloads.mjs ./extracted/files --documents-only
```

Replace `./extracted/files` with your actual extracted `files` directory. The ZIP is stored without compression or encryption, so its 10,570 bytes exceed the 7,471 bytes of the two source documents.

## 4. Edit a working copy of each format

Keep the checked originals and edit copies. Open the Markdown in a text editor and replace a bracketed prompt or write a plan beneath it. Markdown renders user-entered text here as literal indented blocks; it has no live form or automatic synchronizer.

The HTML is a separate print draft with blank answer lines. Changing the Markdown does not update it. Apply the same change separately, or recreate both formats with your authoring tool. The reference hashes intentionally stop matching after an edit; they describe the original release rather than your new version.

The original HTML bytes were checked for the expected text and static structure. Standalone browser rendering, print pagination and PDF output were **not verified**. Before sharing, check Japanese font display, wrapping, page breaks and your intended paper settings in your own environment. No one-page result is promised.

For a revised pack, write opening notes that name the formats and their separate-editing behavior, and generate a new inventory and reference hashes for the revised bytes. Keep personal participant information out of this blank planning example.

## Scope and disclosure

The account owner made this blank sample and its two authoring tools with AI assistance. Separate tool pages contain optional Payhip referral advertising that may pay the owner; using these release files or this script requires no purchase or referral click. This guide contains no affiliate links and makes no user-adoption, savings or income claim.

You may save and edit the blank sample for your own workshop preparation. The short verification snippet is original code supplied here for checking and adapting this example. It does not distribute or grant a licence to the hosted tools' implementation. The original v1.0.0 assets remain unchanged.

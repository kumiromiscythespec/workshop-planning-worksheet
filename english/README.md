# English workshop planner - v1.1.0

A blank planning aid for independent tutors and workshop facilitators. Three sections, six prompts, eighteen answer lines. The 3+9+3 minute schedule is an example you can change; it is not an assurance about session length or learning outcomes. Keep participant names and identifying information out of your plan.

## Choose a file

- PDF: a static one-page A4 sheet for writing by hand; no fillable form fields. Review the content, print scale, margins and paper size on your own printer.
- Markdown: editable text with the same prompts and blank answer lines.
- ZIP: the two files, README.txt and checksums.sha256, stored without compression or encryption.

Use the [public download pack](https://github.com/kumiromiscythespec/workshop-planning-worksheet/releases/tag/v1.1.0). The original Japanese v1.0.0 release, its HTML and its guide remain separate and unchanged. Files and edited copies do not synchronize. Do not use the old Japanese pack verifier for this English ZIP.

## Optional manual editor

[Open the English worksheet editor](https://workbook-sheet-studio-1111.crisp-llama-2628.chatgpt.site/en/?utm_source=owned_blog&utm_medium=referral) to arrange your own prompts and answer space, then make separate HTML or Markdown drafts. It has no automatic import of this planner and no direct PDF export. This prepared PDF was made separately with the companion ReportLab script.

## Optional PDF regeneration

With Python 3 and the reportlab package installed, run from the repository root:

```text
python english/generate_pdf.py --data english/planner-data.json --output planner-en.pdf
```

The script reads local JSON and writes a local static PDF; it makes no network requests. The fixed layout expects three sections, six prompts and answer-line counts 2,2,3,4,4,3. It rejects text that would overflow its safe layout; review any changed PDF yourself. A separately edited Markdown file does not update the JSON or PDF automatically. Output bytes may differ with dependency versions.

## Use and disclosure

You may save and edit this blank example for your own workshop preparation. It is not participant work or a completed curriculum. I maintain the resource and used AI assistance. Optional, labeled Payhip referral ads are on the separate tool pages and may pay the maker for qualifying activity; the PDF, Markdown and ZIP contain no referral advertisements. No account, purchase or referral click is needed. The hosted worksheet editor source is not included or offered as open source here.

#!/usr/bin/env python3
"""Make one static English planning sheet. Requires Python 3 and reportlab.

Example: python generate_pdf.py --data planner-data.json --output planner-en.pdf
This program reads a local JSON file and writes a local PDF. No network is used.
"""
import argparse
import json
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.pdfgen import canvas

BLUE = colors.HexColor('#2048d8')
INK = colors.HexColor('#17243d')
MUTED = colors.HexColor('#526079')
RULE = colors.HexColor('#bfcee3')
PALE = colors.HexColor('#eef3ff')
EDITOR = 'https://workbook-sheet-studio-1111.crisp-llama-2628.chatgpt.site/en/'

def clean(text):
    value = str(text)
    for dash in '\u2010\u2011\u2012\u2013\u2014\u2015\u2212':
        value = value.replace(dash, '-')
    return value

def make_sheet(data, output, layout_report=None):
    width, height = A4
    left, right = 42, width - 42
    writing_left = left + 25
    blocks, rules = [], []
    y = height - 40
    items = [item for section in data['sections'] for item in section['items']]
    if len(data['sections']) != 3 or len(items) != 6 or [x['lines'] for x in items] != [2, 2, 3, 4, 4, 3]:
        raise ValueError('This one-page layout expects 3 sections, 6 prompts and 18 answer lines.')
    if any(item['kind'] not in ('short', 'long') for item in items):
        raise ValueError('This planning-sheet layout supports short and long answer areas.')

    def text(value, x, baseline, font='Helvetica', size=10, color=INK):
        value = clean(value)
        line_width = stringWidth(value, font, size)
        if x < left - .1 or x + line_width > right + .1:
            raise ValueError('Text does not fit the page width: ' + value)
        blocks.append({'text': value, 'x': x, 'baseline': baseline, 'font': font, 'size': size, 'width': line_width, 'color': color.hexval()})

    def paragraph(value, x, baseline, max_width, size=10, leading=13, color=INK):
        for line in simpleSplit(clean(value), 'Helvetica', size, max_width):
            text(line, x, baseline, size=size, color=color)
            baseline -= leading
        return baseline

    text('WORKBOOK SHEET STUDIO / FREE PLANNING RESOURCE', left, y, 'Helvetica-Bold', 8, BLUE)
    y -= 28
    text(data['title'], left, y, 'Helvetica-Bold', 21, INK)
    y -= 21
    y = paragraph(data['audience'], left, y, right-left, size=9.5, leading=12, color=MUTED)
    y -= 4
    y = paragraph(data['instructions'], left, y, right-left, size=9.5, leading=12, color=MUTED)
    y -= 4
    timeline_top = y + 1
    text('EDITABLE TIMING EXAMPLE', left + 9, y - 12, 'Helvetica-Bold', 7.5, BLUE)
    text('Opening 3 min  +  Practice 9 min  +  Review 3 min', left + 153, y - 12, size=8.5, color=INK)
    y -= 39
    section_positions = []
    item_number = 0
    for section_number, section in enumerate(data['sections'], 1):
        section_positions.append({'x': left, 'y': y, 'width': right-left})
        text(f'{section_number:02d}  ' + section['title'], left + 9, y - 1, 'Helvetica-Bold', 10.5, BLUE)
        y -= 24
        for item in section['items']:
            item_number += 1
            text(f'{item_number:02d}', left, y, 'Helvetica-Bold', 9, BLUE)
            y = paragraph(item['prompt'], writing_left, y, right-writing_left, size=10, leading=12.5)
            y -= 1
            for _ in range(item['lines']):
                y -= 16
                rules.append({'x0': writing_left, 'x1': right, 'y': y})
            y -= 13
        y -= 1
    lowest_writing_y = min(line['y'] for line in rules)
    if lowest_writing_y < 70:
        raise ValueError(f'Writing areas would collide with the footer ({lowest_writing_y:.1f} pt remaining).')
    if any(block['baseline'] < 40 or block['baseline'] + block['size'] > height-24 for block in blocks):
        raise ValueError('Text lies outside the safe page area.')

    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    pdf = canvas.Canvas(str(output), pagesize=A4, pageCompression=1, invariant=1)
    pdf.setTitle(clean(data['title']))
    pdf.setAuthor('Workbook Sheet Studio')
    pdf.setSubject('An editable example of a 15-minute workshop plan with blank writing space')
    pdf.setCreator('Workbook Sheet Studio - standalone planning-resource generator')
    pdf.setFillColor(PALE)
    pdf.roundRect(left, timeline_top-22, right-left, 23, 4, fill=1, stroke=0)
    for section in section_positions[:1]:
        pdf.setStrokeColor(RULE)
        pdf.setLineWidth(.55)
        pdf.line(section['x'], section['y']+12, section['x']+section['width'], section['y']+12)
    for block in blocks:
        pdf.setFont(block['font'], block['size'])
        pdf.setFillColor(colors.HexColor(block['color']))
        pdf.drawString(block['x'], block['baseline'], block['text'])
    pdf.setStrokeColor(RULE)
    pdf.setLineWidth(.45)
    for line in rules:
        pdf.line(line['x0'], line['y'], line['x1'], line['y'])
    pdf.line(left, 52, right, 52)
    pdf.setFillColor(MUTED)
    pdf.setFont('Helvetica', 7.5)
    pdf.drawString(left, 39, 'Blank planning example. Adapt the timing and prompts; review before sharing.')
    pdf.setFillColor(BLUE)
    pdf.setFont('Helvetica', 7)
    pdf.drawString(left, 27, EDITOR)
    pdf.linkURL(EDITOR, (left, 25, left+stringWidth(EDITOR,'Helvetica',7), 34), relative=0, thickness=0)
    pdf.setFillColor(MUTED)
    pdf.setFont('Helvetica', 7.5)
    pdf.drawRightString(right, 27, '1 / 1')
    pdf.showPage()
    pdf.save()
    layout = {'page': 'A4 portrait', 'width_pt': width, 'height_pt': height, 'body_font_pt': 10, 'sections': 3, 'prompts': item_number, 'answer_lines': len(rules), 'answer_line_step_pt': 16, 'lowest_content_y_pt': lowest_writing_y, 'trailing_cursor_y_pt': y, 'text_blocks': blocks, 'writing_rules': rules, 'interactive_form': False, 'network_used': False}
    if layout_report:
        destination = Path(layout_report)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(json.dumps(layout, indent=2)+'\n', encoding='utf-8')
    return layout

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--data', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--layout-report', type=Path)
    args = parser.parse_args()
    data = json.loads(args.data.read_text(encoding='utf-8-sig'))
    layout = make_sheet(data, args.output, args.layout_report)
    print(json.dumps({'status':'GENERATED','pages':1,'sections':layout['sections'],'prompts':layout['prompts'],'answer_lines':layout['answer_lines'],'lowest_content_y_pt':layout['lowest_content_y_pt']}))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(paragraph, styles["BodyText"])
    table_style = [('GRID', (0, 0), (-1, -1), 1, colors.black), ('FONTNAME', (0, 0), (-1, 0), 'Arial'), ('ALIGN', (0, 0), (-1, -1), 'CENTER')]
    line_break = Spacer(1, 20)

    report.build([report_title, line_break, report_info])
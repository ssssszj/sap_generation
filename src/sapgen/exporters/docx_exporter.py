from __future__ import annotations

import re
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

from sapgen.domain.models import SAPIR, TFLSpec


def _set_cell_shading(cell, fill: str) -> None:
    properties = cell._tc.get_or_add_tcPr()
    shading = properties.find(qn("w:shd"))
    if shading is None:
        shading = OxmlElement("w:shd")
        properties.append(shading)
    shading.set(qn("w:fill"), fill)


def _set_cell_margins(
    cell, top: int = 100, start: int = 120, bottom: int = 100, end: int = 120
) -> None:
    properties = cell._tc.get_or_add_tcPr()
    margins = properties.first_child_found_in("w:tcMar")
    if margins is None:
        margins = OxmlElement("w:tcMar")
        properties.append(margins)
    for name, value in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = margins.find(qn(f"w:{name}"))
        if node is None:
            node = OxmlElement(f"w:{name}")
            margins.append(node)
        node.set(qn("w:w"), str(value))
        node.set(qn("w:type"), "dxa")


def _zero_table_paragraph_indent(paragraph) -> None:
    """Enforce the user's standing rule: no blank indentation inside table cells."""
    fmt = paragraph.paragraph_format
    fmt.left_indent = Pt(0)
    fmt.right_indent = Pt(0)
    fmt.first_line_indent = Pt(0)
    paragraph.text = paragraph.text.lstrip(" \t")
    for run in paragraph.runs:
        run.font.name = "Arial"
        run.font.size = Pt(9)


def _format_table(table) -> None:
    table.autofit = True
    for row_index, row in enumerate(table.rows):
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            _set_cell_margins(cell)
            if row_index == 0:
                _set_cell_shading(cell, "1F4E78")
            elif row_index % 2 == 0:
                _set_cell_shading(cell, "EAF2F8")
            for paragraph in cell.paragraphs:
                _zero_table_paragraph_indent(paragraph)
                if row_index == 0:
                    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for run in paragraph.runs:
                        run.font.bold = True
                        run.font.color.rgb = RGBColor(255, 255, 255)


def _configure_document(document: Document) -> None:
    section = document.sections[0]
    section.top_margin = Inches(0.75)
    section.bottom_margin = Inches(0.75)
    section.left_margin = Inches(0.8)
    section.right_margin = Inches(0.8)
    styles = document.styles
    normal = styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(10.5)
    normal.paragraph_format.space_after = Pt(6)
    for style_name, size in (("Title", 20), ("Heading 1", 15), ("Heading 2", 12)):
        style = styles[style_name]
        style.font.name = "Arial"
        style.font.size = Pt(size)
        style.font.color.rgb = RGBColor(0, 0, 0)


def _add_markdown(document: Document, markdown: str) -> None:
    for raw_line in markdown.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue
        if line.startswith("## "):
            document.add_heading(line[3:].strip(), level=2)
        elif line.startswith("# "):
            document.add_heading(line[2:].strip(), level=1)
        elif line.startswith("- "):
            document.add_paragraph(line[2:].strip(), style="List Bullet")
        else:
            paragraph = document.add_paragraph()
            match = re.match(r"^([^:]{1,60}):\s*(.*)$", line)
            if match:
                paragraph.add_run(match.group(1) + ": ").bold = True
                paragraph.add_run(match.group(2))
            else:
                paragraph.add_run(line)


class SAPDocxExporter:
    def export(self, ir: SAPIR, output_path: Path) -> Path:
        output_path = output_path.resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        document = Document()
        _configure_document(document)
        title = document.add_paragraph(style="Title")
        title.add_run("Statistical Analysis Plan")
        subtitle = document.add_paragraph()
        subtitle.alignment = WD_ALIGN_PARAGRAPH.CENTER
        subtitle.add_run(ir.study.title).bold = True
        document.add_paragraph(f"Study identifier: {ir.study.study_id}")
        for section in ir.generated_sections:
            document.add_heading(section.title, level=1)
            _add_markdown(document, section.body_markdown)
        document.save(output_path)
        return output_path


class TFLDocxExporter:
    def export(self, specs: list[TFLSpec], output_path: Path) -> Path:
        output_path = output_path.resolve()
        output_path.parent.mkdir(parents=True, exist_ok=True)
        document = Document()
        _configure_document(document)
        document.add_paragraph("TFL Shell Specifications", style="Title")
        for spec in specs:
            document.add_heading(f"{spec.number} {spec.title}", level=1)
            document.add_paragraph(f"Population: {spec.population_id}")
            document.add_paragraph(f"Denominator: {spec.denominator}")
            self._add_shell(document, spec)
            for footnote in spec.footnotes:
                paragraph = document.add_paragraph()
                paragraph.add_run("Footnote: ").bold = True
                paragraph.add_run(footnote)
        document.save(output_path)
        return output_path

    @staticmethod
    def _add_shell(document: Document, spec: TFLSpec) -> None:
        headers = ["Row"] + (spec.columns or ["Result"])
        table = document.add_table(rows=1, cols=len(headers))
        table.style = "Table Grid"
        for index, header in enumerate(headers):
            table.rows[0].cells[index].text = header.strip()
        rows = spec.rows or ["Result"]
        statistic_text = ", ".join(spec.statistics)
        for row_label in rows:
            cells = table.add_row().cells
            cells[0].text = row_label.strip()
            for index in range(1, len(cells)):
                cells[index].text = f"<{statistic_text}>".strip()
        _format_table(table)

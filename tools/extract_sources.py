from __future__ import annotations

import argparse
import json
from pathlib import Path

from docx import Document
from pptx import Presentation


def extract_docx(path: Path) -> dict:
    document = Document(path)
    paragraphs = []
    for index, paragraph in enumerate(document.paragraphs, start=1):
        text = paragraph.text.strip()
        if text:
            paragraphs.append(
                {
                    "index": index,
                    "style": paragraph.style.name if paragraph.style else None,
                    "text": text,
                }
            )

    tables = []
    for table_index, table in enumerate(document.tables, start=1):
        rows = []
        for row in table.rows:
            rows.append([cell.text.strip() for cell in row.cells])
        tables.append({"index": table_index, "rows": rows})

    return {"paragraphs": paragraphs, "tables": tables}


def extract_pptx(path: Path) -> dict:
    presentation = Presentation(path)
    slides = []
    for slide_index, slide in enumerate(presentation.slides, start=1):
        elements = []
        for shape_index, shape in enumerate(slide.shapes, start=1):
            entry = {
                "index": shape_index,
                "name": shape.name,
                "type": str(shape.shape_type),
            }
            if getattr(shape, "has_text_frame", False):
                text = "\n".join(
                    paragraph.text.strip()
                    for paragraph in shape.text_frame.paragraphs
                    if paragraph.text.strip()
                )
                if text:
                    entry["text"] = text
            if getattr(shape, "has_table", False):
                entry["table"] = [
                    [cell.text.strip() for cell in row.cells]
                    for row in shape.table.rows
                ]
            if len(entry) > 3:
                elements.append(entry)

        notes = []
        if slide.has_notes_slide:
            for shape in slide.notes_slide.shapes:
                if getattr(shape, "has_text_frame", False):
                    text = shape.text.strip()
                    if text:
                        notes.append(text)

        slides.append(
            {
                "index": slide_index,
                "elements": elements,
                "notes": notes,
            }
        )
    return {"slide_count": len(slides), "slides": slides}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--docx", type=Path, required=True)
    parser.add_argument("--pptx", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    payload = {
        "docx": extract_docx(args.docx),
        "pptx": extract_pptx(args.pptx),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()

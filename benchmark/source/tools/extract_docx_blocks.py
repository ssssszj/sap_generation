#!/usr/bin/env python3
"""Extract stable paragraph and table-row locators from a DOCX.

The extractor deliberately does not claim page numbers. DOCX pagination depends on
fonts and the rendering engine. Paragraph IDs are one-based positions in
python-docx's paragraph collection and remain stable while the source file is
unchanged; the document manifest hash makes that condition auditable.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import unicodedata

from docx import Document


def clean_text(value: str) -> str:
    value = unicodedata.normalize("NFKC", value or "")
    return " ".join(value.replace("\u00a0", " ").split())


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_blocks(path: Path, document_id: str):
    doc = Document(path)
    file_hash = sha256(path)
    for index, paragraph in enumerate(doc.paragraphs, start=1):
        text = clean_text(paragraph.text)
        if text:
            yield {
                "document_id": document_id,
                "document_sha256": file_hash,
                "locator": f"p{index:04d}",
                "block_type": "paragraph",
                "text": text,
            }
    for table_index, table in enumerate(doc.tables, start=1):
        for row_index, row in enumerate(table.rows, start=1):
            cells = [clean_text(cell.text) for cell in row.cells]
            if any(cells):
                yield {
                    "document_id": document_id,
                    "document_sha256": file_hash,
                    "locator": f"t{table_index:03d}-r{row_index:03d}",
                    "block_type": "table_row",
                    "cells": cells,
                    "text": " | ".join(cells),
                }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("docx", type=Path)
    parser.add_argument("--document-id", required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--text-only",
        action="store_true",
        help="Emit normalized text only, suitable for candidate scoring.",
    )
    args = parser.parse_args()

    if not args.docx.is_file():
        parser.error(f"DOCX not found: {args.docx}")

    blocks = list(iter_blocks(args.docx, args.document_id))
    if args.text_only:
        payload = "\n".join(block["text"] for block in blocks) + "\n"
    else:
        payload = "".join(json.dumps(block, ensure_ascii=False) + "\n" for block in blocks)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

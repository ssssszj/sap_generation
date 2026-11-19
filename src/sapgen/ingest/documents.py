from __future__ import annotations

import hashlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import ClassVar

from docx import Document
from pypdf import PdfReader


@dataclass(frozen=True, slots=True)
class EvidenceChunk:
    source_id: str
    document_name: str
    locator: str
    text: str


@dataclass(slots=True)
class EvidenceCorpus:
    chunks: list[EvidenceChunk] = field(default_factory=list)

    def to_prompt(self, max_chars: int = 120_000) -> str:
        blocks: list[str] = []
        used = 0
        for chunk in self.chunks:
            block = (
                f"[SOURCE {chunk.source_id} | {chunk.document_name} | {chunk.locator}]\n"
                f"{chunk.text}\n"
            )
            if used + len(block) > max_chars:
                remaining = max_chars - used
                if remaining > 200:
                    blocks.append(block[:remaining])
                break
            blocks.append(block)
            used += len(block)
        return "\n".join(blocks)

    def search(self, terms: list[str], limit: int = 8) -> list[EvidenceChunk]:
        lowered = [term.lower() for term in terms]
        scored = []
        for chunk in self.chunks:
            text = chunk.text.lower()
            score = sum(text.count(term) for term in lowered)
            if score:
                scored.append((score, chunk))
        scored.sort(key=lambda item: item[0], reverse=True)
        return [chunk for _, chunk in scored[:limit]]


class DocumentIngestor:
    supported_suffixes: ClassVar[set[str]] = {".docx", ".pdf", ".txt", ".md"}

    def ingest(self, paths: list[Path]) -> EvidenceCorpus:
        corpus = EvidenceCorpus()
        for path in paths:
            resolved = path.resolve()
            if not resolved.exists():
                raise FileNotFoundError(resolved)
            suffix = resolved.suffix.lower()
            if suffix not in self.supported_suffixes:
                raise ValueError(f"Unsupported input format: {resolved.suffix}")
            source_id = hashlib.sha256(resolved.read_bytes()).hexdigest()[:16]
            if suffix == ".docx":
                corpus.chunks.extend(self._docx_chunks(resolved, source_id))
            elif suffix == ".pdf":
                corpus.chunks.extend(self._pdf_chunks(resolved, source_id))
            else:
                corpus.chunks.extend(self._text_chunks(resolved, source_id))
        return corpus

    @staticmethod
    def _docx_chunks(path: Path, source_id: str) -> list[EvidenceChunk]:
        document = Document(path)
        chunks: list[EvidenceChunk] = []
        for index, paragraph in enumerate(document.paragraphs, start=1):
            text = paragraph.text.strip()
            if text:
                style = paragraph.style.name if paragraph.style else "Unknown"
                chunks.append(
                    EvidenceChunk(
                        source_id=source_id,
                        document_name=path.name,
                        locator=f"paragraph {index} ({style})",
                        text=text,
                    )
                )
        for table_index, table in enumerate(document.tables, start=1):
            for row_index, row in enumerate(table.rows, start=1):
                values = [cell.text.strip() for cell in row.cells]
                if any(values):
                    chunks.append(
                        EvidenceChunk(
                            source_id=source_id,
                            document_name=path.name,
                            locator=f"table {table_index}, row {row_index}",
                            text=" | ".join(values),
                        )
                    )
        return chunks

    @staticmethod
    def _pdf_chunks(path: Path, source_id: str) -> list[EvidenceChunk]:
        reader = PdfReader(path)
        chunks: list[EvidenceChunk] = []
        for page_number, page in enumerate(reader.pages, start=1):
            text = (page.extract_text() or "").strip()
            if not text:
                continue
            paragraphs = [value.strip() for value in text.split("\n\n") if value.strip()]
            for index, paragraph in enumerate(paragraphs, start=1):
                chunks.append(
                    EvidenceChunk(
                        source_id=source_id,
                        document_name=path.name,
                        locator=f"page {page_number}, block {index}",
                        text=paragraph,
                    )
                )
        return chunks

    @staticmethod
    def _text_chunks(path: Path, source_id: str) -> list[EvidenceChunk]:
        text = path.read_text(encoding="utf-8-sig")
        blocks = [value.strip() for value in text.split("\n\n") if value.strip()]
        return [
            EvidenceChunk(
                source_id=source_id,
                document_name=path.name,
                locator=f"block {index}",
                text=block,
            )
            for index, block in enumerate(blocks, start=1)
        ]

from __future__ import annotations

import zipfile

from lxml import etree

from sapgen.exporters import TFLDocxExporter
from sapgen.modules import AnalysisDesignModule, SafetyAnalysisModule, TFLGenerationModule

NS = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}


def test_table_cell_paragraphs_have_zero_indent_and_no_blank_prefix(tmp_path, demo_ir) -> None:
    ir = demo_ir.model_copy(deep=True)
    AnalysisDesignModule().enrich(ir)
    SafetyAnalysisModule().enrich(ir)
    TFLGenerationModule().enrich(ir)
    output = tmp_path / "tfl.docx"
    TFLDocxExporter().export(ir.tfl_specs, output)

    with zipfile.ZipFile(output) as archive:
        root = etree.fromstring(archive.read("word/document.xml"))
    for paragraph in root.xpath(".//w:tc//w:p", namespaces=NS):
        text = "".join(paragraph.xpath(".//w:t/text()", namespaces=NS))
        assert text == text.lstrip(" \t")
        indent = paragraph.find("./w:pPr/w:ind", namespaces=NS)
        assert indent is not None
        for name in ("left", "right", "firstLine"):
            assert indent.get(f"{{{NS['w']}}}{name}") in {"0", None}

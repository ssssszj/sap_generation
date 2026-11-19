from __future__ import annotations

import argparse
import json
from pathlib import Path

from sapgen.domain.models import SAPIR
from sapgen.domain.rules import RuleEngine
from sapgen.exporters import SAPDocxExporter, TFLDocxExporter
from sapgen.generation import SectionGenerator
from sapgen.modules import (
    AnalysisDesignModule,
    ComplexDataModule,
    DerivationSupportModule,
    EstimandDecisionModule,
    MethodSpecificationModule,
    MultiplicityModule,
    RobustnessDecisionModule,
    SafetyAnalysisModule,
    SafetySpecificationModule,
    SamplePopulationSpecificationModule,
    TFLGenerationModule,
    TFLSpecificationModule,
)


def load_ir(path: Path) -> SAPIR:
    return SAPIR.model_validate_json(path.read_text(encoding="utf-8"))


def save_ir(ir: SAPIR, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(ir.model_dump_json(indent=2), encoding="utf-8")


def enrich(ir: SAPIR) -> SAPIR:
    for module in (
        AnalysisDesignModule(),
        SamplePopulationSpecificationModule(),
        EstimandDecisionModule(),
        MethodSpecificationModule(),
        ComplexDataModule(),
        RobustnessDecisionModule(),
        MultiplicityModule(),
        SafetyAnalysisModule(),
        SafetySpecificationModule(),
        DerivationSupportModule(),
        TFLGenerationModule(),
        TFLSpecificationModule(),
    ):
        ir = module.enrich(ir)
    return ir


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--ir", type=Path, required=True)
    enrich_parser = subparsers.add_parser("enrich")
    enrich_parser.add_argument("--ir", type=Path, required=True)
    enrich_parser.add_argument("--output", type=Path, required=True)
    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--ir", type=Path, required=True)
    export_parser.add_argument("--output", type=Path, required=True)
    tfl_parser = subparsers.add_parser("export-tfl")
    tfl_parser.add_argument("--ir", type=Path, required=True)
    tfl_parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    ir = load_ir(args.ir)
    if args.command == "validate":
        report = RuleEngine().validate(ir)
        print(
            json.dumps(
                {"ok": not report.has_errors, "report": report.model_dump(mode="json")},
                ensure_ascii=False,
            )
        )
    elif args.command == "enrich":
        ir = enrich(ir)
        save_ir(ir, args.output)
        print(json.dumps({"ok": True, "output": str(args.output.resolve())}, ensure_ascii=False))
    elif args.command == "export":
        SectionGenerator().generate(ir)
        SAPDocxExporter().export(ir, args.output)
        print(json.dumps({"ok": True, "output": str(args.output.resolve())}, ensure_ascii=False))
    elif args.command == "export-tfl":
        TFLDocxExporter().export(ir.tfl_specs, args.output)
        print(json.dumps({"ok": True, "output": str(args.output.resolve())}, ensure_ascii=False))


if __name__ == "__main__":
    main()

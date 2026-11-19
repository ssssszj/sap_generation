from __future__ import annotations

import shutil
import uuid
from pathlib import Path

from sapgen.domain.models import SAPIR, PipelineResult
from sapgen.domain.rules import RuleEngine
from sapgen.exporters import SAPDocxExporter, TFLDocxExporter
from sapgen.generation import HarnessChapterGenerator, HarnessDraftReviewer, SectionGenerator
from sapgen.harness.base import HarnessAdapter
from sapgen.ingest import DocumentIngestor, SAPIRExtractor
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
from sapgen.repair import ValidationRepairer
from sapgen.storage import ProjectStore


class SAPGenerationPipeline:
    def __init__(
        self,
        *,
        data_dir: Path,
        store: ProjectStore,
        harness: HarnessAdapter | None = None,
    ) -> None:
        self.data_dir = data_dir.resolve()
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.store = store
        self.harness = harness
        self.ingestor = DocumentIngestor()
        self.extractor = SAPIRExtractor(harness)
        self.modules = [
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
        ]
        self.rules = RuleEngine()
        self.section_generator = SectionGenerator()

    def run(
        self,
        *,
        project_id: str,
        input_paths: list[Path],
        seed_ir: SAPIR | None = None,
        allow_harness_fallback: bool = True,
    ) -> PipelineResult:
        harness_session_id = f"sapgen-{project_id}-{uuid.uuid4().hex[:8]}"
        run_id = self.store.start_run(
            project_id,
            harness_session_id=harness_session_id if self.harness else None,
        )
        project_dir = self.data_dir / project_id
        inputs_dir = project_dir / "inputs"
        run_dir = project_dir / "runs" / run_id
        inputs_dir.mkdir(parents=True, exist_ok=True)
        run_dir.mkdir(parents=True, exist_ok=True)
        try:
            copied_inputs = self._copy_inputs(input_paths, inputs_dir)
            self._event(run_id, "inputs.accepted", {"files": [str(p) for p in copied_inputs]})
            corpus = self.ingestor.ingest(copied_inputs)
            self._event(run_id, "evidence.indexed", {"chunks": len(corpus.chunks)})

            used_harness = False
            if seed_ir is None:
                ir, used_harness = self.extractor.extract(
                    corpus,
                    session_id=harness_session_id,
                    allow_fallback=allow_harness_fallback,
                )
            else:
                ir = seed_ir.model_copy(deep=True)
            self._event(
                run_id,
                "ir.extracted",
                {
                    "used_harness": used_harness,
                    "endpoints": len(ir.endpoints),
                    "estimands": len(ir.estimands),
                },
            )

            for module in self.modules:
                ir = module.enrich(ir)
                self._event(
                    run_id,
                    "module.completed",
                    {"module": module.__class__.__name__},
                )

            report = self.rules.validate(ir)
            if report.has_errors and self.harness is not None:
                repairer = ValidationRepairer(self.harness)
                for attempt in range(1, 3):
                    ir = repairer.repair(
                        ir,
                        report,
                        source_context=corpus.to_prompt(),
                        session_id=f"{harness_session_id}-repair-{attempt}",
                    )
                    report = self.rules.validate(ir)
                    self._event(
                        run_id,
                        "validation.repaired",
                        {"attempt": attempt, **report.counts()},
                    )
                    if not report.has_errors:
                        break
            self._event(run_id, "validation.completed", report.counts())
            if report.has_errors:
                error_codes = sorted(
                    {item.code for item in report.issues if item.severity.value == "error"}
                )
                raise ValueError(
                    "SAP-IR still has blocking validation errors after repair: "
                    + ", ".join(error_codes)
                )
            if self.harness is not None:
                HarnessChapterGenerator(self.harness).generate(
                    ir,
                    session_id=f"{harness_session_id}-chapters",
                )
                HarnessDraftReviewer(self.harness).review(
                    ir,
                    session_id=f"{harness_session_id}-final-review",
                )
            else:
                self.section_generator.generate(ir)
            markdown = self.section_generator.render_document(ir)

            ir_path = run_dir / "sap-ir.json"
            validation_path = run_dir / "validation-report.json"
            markdown_path = run_dir / "sap-draft.md"
            docx_path = run_dir / "sap-draft.docx"
            tfl_docx_path = run_dir / "tfl-shells.docx"
            ir_path.write_text(ir.model_dump_json(indent=2), encoding="utf-8")
            validation_path.write_text(report.model_dump_json(indent=2), encoding="utf-8")
            markdown_path.write_text(markdown, encoding="utf-8")
            SAPDocxExporter().export(ir, docx_path)
            TFLDocxExporter().export(ir.tfl_specs, tfl_docx_path)
            self._event(
                run_id,
                "artifacts.exported",
                {
                    "ir": str(ir_path),
                    "draft": str(docx_path),
                    "tfl": str(tfl_docx_path),
                },
            )

            result = PipelineResult(
                project_id=project_id,
                run_id=run_id,
                ir_path=str(ir_path),
                draft_markdown_path=str(markdown_path),
                docx_path=str(docx_path),
                tfl_docx_path=str(tfl_docx_path),
                validation_path=str(validation_path),
                report=report,
                harness_session_id=harness_session_id if used_harness else None,
                metadata={
                    "used_harness": used_harness,
                    "evidence_chunks": len(corpus.chunks),
                    "open_clarifications": sum(
                        item.status.value == "open" for item in ir.clarifications
                    ),
                },
            )
            self.store.finish_run(run_id, result.model_dump(mode="json"))
            return result
        except Exception as exc:
            self.store.fail_run(run_id, f"{type(exc).__name__}: {exc}")
            raise

    @staticmethod
    def load_ir(path: Path) -> SAPIR:
        return SAPIR.model_validate_json(path.read_text(encoding="utf-8"))

    @staticmethod
    def save_ir(ir: SAPIR, path: Path) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(ir.model_dump_json(indent=2), encoding="utf-8")
        return path

    @staticmethod
    def _copy_inputs(paths: list[Path], inputs_dir: Path) -> list[Path]:
        copied = []
        for source in paths:
            resolved = source.resolve()
            destination = inputs_dir / resolved.name
            if resolved != destination.resolve():
                shutil.copy2(resolved, destination)
            copied.append(destination)
        return copied

    def _event(self, run_id: str, event_type: str, payload: dict) -> None:
        self.store.append_event(run_id, event_type, payload)

from __future__ import annotations

import csv
import os
import re
import time
import urllib.request
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from sapgen.experiment.adapters import (
    DirectLLMNativeAdapter,
    DSHSAPAdapter,
    GenerationOutcome,
    LegacyHTTPAdapter,
)
from sapgen.experiment.dataset import (
    build_experiment_package,
    load_json,
    load_jsonl,
    sha256,
    write_json,
)
from sapgen.experiment.judge import SemanticJudge
from sapgen.experiment.llm import OpenAIChatClient
from sapgen.ingest import DocumentIngestor, EvidenceCorpus

METHODS = ("direct_llm_native", "sap_ver1", "dsh_sap")

SAP_RELEVANCE_TERMS: tuple[tuple[str, int], ...] = (
    ("statistical analysis", 12),
    ("analysis population", 10),
    ("primary endpoint", 10),
    ("primary outcome", 10),
    ("sample size", 9),
    ("power", 7),
    ("randomization", 6),
    ("randomisation", 6),
    ("estimand", 9),
    ("missing data", 9),
    ("imputation", 8),
    ("multiplicity", 8),
    ("interim analysis", 8),
    ("sensitivity analysis", 8),
    ("adverse event", 7),
    ("safety population", 8),
    ("confidence interval", 6),
    ("alpha", 5),
    ("covariate", 5),
    ("stratification", 5),
    ("endpoint", 4),
    ("outcome", 4),
    ("objective", 4),
    ("baseline", 3),
    ("follow-up", 3),
    ("follow up", 3),
    ("visit", 2),
)


def _repair_fragmented_words(text: str) -> str:
    """Repair PDF text such as 's t a t i s t i c a l' without changing normal prose."""

    pattern = re.compile(r"(?<![A-Za-z])(?:[A-Za-z]{1,2}\s+){3,}[A-Za-z]{1,2}(?![A-Za-z])")

    def repair(match: re.Match[str]) -> str:
        tokens = match.group(0).split()
        # True PDF glyph fragmentation contains many one-letter tokens. This guard avoids
        # collapsing ordinary phrases made from short words, such as "to be in a".
        if sum(len(token) == 1 for token in tokens) / len(tokens) < 0.5:
            return match.group(0)
        return "".join(tokens)

    return pattern.sub(repair, text)


def _is_legible(text: str) -> bool:
    if not text.strip():
        return False
    length = len(text)
    alpha_ratio = sum(character.isalpha() for character in text) / length
    control_ratio = sum(not character.isprintable() for character in text) / length
    encoded_glyph_ratio = len(re.findall(r"/(?:i\d+|\d+)", text)) / length
    return alpha_ratio >= 0.20 and control_ratio <= 0.02 and encoded_glyph_ratio <= 0.02


def _protocol_excerpt(corpus: EvidenceCorpus, maximum: int) -> tuple[str, dict[str, int]]:
    """Select a source-ordered, domain-balanced protocol excerpt from the whole document."""

    prepared: list[tuple[int, str, int]] = []
    rejected = 0
    for index, chunk in enumerate(corpus.chunks):
        repaired = _repair_fragmented_words(chunk.text.strip())
        if not _is_legible(repaired):
            rejected += 1
            continue
        lowered = repaired.lower()
        score = sum(weight * lowered.count(term) for term, weight in SAP_RELEVANCE_TERMS)
        block = f"[SOURCE {chunk.document_name} | {chunk.locator}]\n{repaired}"
        prepared.append((index, block, score))

    if not prepared:
        plain = "\n\n".join(chunk.text for chunk in corpus.chunks)
        return plain[:maximum], {
            "chunks_available": len(corpus.chunks),
            "chunks_selected": 0,
            "chunks_rejected_unreadable": len(corpus.chunks),
        }

    mandatory: list[int] = []
    # Preserve identity/design context and obtain at least one strong block from each document quartile.
    for index, _block, _score in prepared[:3]:
        mandatory.append(index)
    quartile_size = max(1, (len(prepared) + 3) // 4)
    for start in range(0, len(prepared), quartile_size):
        window = prepared[start : start + quartile_size]
        if window:
            mandatory.append(max(window, key=lambda item: (item[2], -item[0]))[0])

    ranked = sorted(prepared, key=lambda item: (item[2], -item[0]), reverse=True)
    blocks_by_index = {index: block for index, block, _score in prepared}
    accepted: list[int] = []
    used = 0
    # Mandatory context first, then relevance-ranked blocks, while accounting for the hard budget.
    priority = list(dict.fromkeys(mandatory))
    priority.extend(
        index for index, _block, _score in ranked if index not in set(priority)
    )
    for index in priority:
        if index in accepted:
            continue
        block_length = len(blocks_by_index[index]) + 2
        if used + block_length > maximum:
            continue
        accepted.append(index)
        used += block_length

    accepted.sort()
    excerpt = "\n\n".join(blocks_by_index[index] for index in accepted)
    return excerpt, {
        "chunks_available": len(corpus.chunks),
        "chunks_selected": len(accepted),
        "chunks_rejected_unreadable": rejected,
    }


def _env_value(path: Path, name: str) -> str | None:
    if not path.exists():
        return None
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if not line.strip() or line.lstrip().startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip() == name:
            return value.strip().strip('"').strip("'") or None
    return None


def _write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


class ExperimentRunner:
    def __init__(self, project_root: Path) -> None:
        self.project_root = project_root.resolve()
        self.benchmark_root = self.project_root / "benchmark"
        self.source_root = self.benchmark_root / "source"
        self.experiment_root = self.benchmark_root / "experiment"
        self.config_path = self.experiment_root / "config.json"
        self.sample_path = self.experiment_root / "sample.json"

    def prepare(self, *, sample_size: int = 20, seed: int = 20261108) -> dict[str, Any]:
        build_experiment_package(self.benchmark_root, sample_size=sample_size, seed=seed)
        default_node = Path(
            r"C:\Users\Jason\.cache\codex-runtimes\codex-primary-runtime\dependencies\node\bin\node.exe"
        )
        config = {
            "experiment_id": "sap-three-arm-20-v1",
            "model": "deepseek/deepseek-v4.1-flash",
            "judge_model": "deepseek/deepseek-v4.1-flash",
            "api_base_url": "https://api.qnaigc.com",
            "max_output_tokens": 32768,
            "temperature_policy": "provider_default_omitted",
            "input_char_limit": 60000,
            "legacy_base_url": "http://127.0.0.1:3100",
            "legacy_env_file": r"D:\Lab\sap_generation\.env.local",
            "legacy_project": r"D:\Lab\sap_generation",
            "dsh_node": str(default_node) if default_node.exists() else None,
            "dsh_js": str(
                (
                    self.project_root / "node_modules" / "@deepseek-ai" / "dsh" / "lib" / "bin.js"
                ).resolve()
            ),
            "concurrency": 1,
            "methods": list(METHODS),
        }
        write_json(self.config_path, config)
        sample = load_json(self.sample_path)
        sample["generation_config"] = {
            key: config[key]
            for key in ("model", "max_output_tokens", "temperature_policy", "input_char_limit")
        }
        write_json(self.sample_path, sample)
        return sample

    def _config(self) -> dict[str, Any]:
        return load_json(self.config_path)

    def _sample(self) -> dict[str, Any]:
        return load_json(self.sample_path)

    def _documents(self) -> dict[str, dict[str, Any]]:
        return {
            item["document_id"]: item
            for item in load_jsonl(self.source_root / "manifests" / "documents.jsonl")
        }

    def _source_path(self, document: dict[str, Any]) -> Path:
        relative = Path(document["path"].replace("\\", "/"))
        prefix = Path("research/benchmark")
        try:
            relative = relative.relative_to(prefix)
        except ValueError:
            pass
        return self.source_root / relative

    def fetch_inputs(self, *, overwrite: bool = False) -> dict[str, Any]:
        documents = self._documents()
        downloaded = 0
        reused = 0
        failures = []
        for question in self._sample()["questions"]:
            for document_id in question["input_document_ids"]:
                document = documents[document_id]
                target = self._source_path(document)
                if target.exists() and not overwrite and sha256(target) == document["sha256"]:
                    reused += 1
                    continue
                target.parent.mkdir(parents=True, exist_ok=True)
                temporary = target.with_suffix(target.suffix + ".part")
                try:
                    with urllib.request.urlopen(document["source_url"], timeout=180) as response:
                        temporary.write_bytes(response.read())
                    actual = sha256(temporary)
                    if actual != document["sha256"]:
                        raise ValueError(
                            f"SHA-256 mismatch for {document_id}: expected {document['sha256']}, got {actual}"
                        )
                    temporary.replace(target)
                    downloaded += 1
                except Exception as exc:  # noqa: BLE001 - persist per-document failure
                    temporary.unlink(missing_ok=True)
                    failures.append({"document_id": document_id, "error": str(exc)})
        result = {"downloaded": downloaded, "reused": reused, "failures": failures}
        write_json(self.experiment_root / "fetch-report.json", result)
        if failures:
            raise RuntimeError(f"Failed to fetch {len(failures)} benchmark inputs")
        return result

    def prepare_inputs(self) -> dict[str, Any]:
        config = self._config()
        documents = self._documents()
        ingestor = DocumentIngestor()
        prepared = []
        for question in self._sample()["questions"]:
            study_id = question["study_id"]
            source_paths = [
                self._source_path(documents[item]) for item in question["input_document_ids"]
            ]
            missing = [str(path) for path in source_paths if not path.exists()]
            if missing:
                raise FileNotFoundError(f"Missing inputs for {study_id}: {missing}")
            corpus = ingestor.ingest(source_paths)
            plain = "\n\n".join(chunk.text for chunk in corpus.chunks)
            visible, selection = _protocol_excerpt(corpus, int(config["input_char_limit"]))
            input_dir = self.experiment_root / "runs" / study_id / "input"
            protocol_path = input_dir / "protocol_input.txt"
            crf_path = input_dir / "crf_not_provided.txt"
            _write_text(protocol_path, visible)
            _write_text(
                crf_path,
                "No study-specific CRF was supplied. This is a protocol-only benchmark input.",
            )
            manifest = {
                "study_id": study_id,
                "track": "protocol_only",
                "original_documents": [
                    {
                        "document_id": document_id,
                        "path": str(self._source_path(documents[document_id])),
                        "sha256": documents[document_id]["sha256"],
                    }
                    for document_id in question["input_document_ids"]
                ],
                "model_visible_inputs": [
                    {"path": str(protocol_path), "sha256": sha256(protocol_path)},
                    {"path": str(crf_path), "sha256": sha256(crf_path)},
                ],
                "protocol_chars_available": len(plain),
                "protocol_chars_visible": len(visible),
                "truncated": len(plain) > len(visible),
                "selection_strategy": "domain_balanced_whole_document_v1",
                "selection": selection,
            }
            write_json(input_dir / "manifest.json", manifest)
            prepared.append(manifest)
        result = {"prepared": len(prepared), "studies": prepared}
        write_json(self.experiment_root / "input-report.json", result)
        return result

    def _api_key(self) -> str:
        config = self._config()
        key = os.getenv("QNY_API_KEY") or _env_value(Path(config["legacy_env_file"]), "QNY_API_KEY")
        if not key:
            raise RuntimeError("QNY_API_KEY is not configured")
        return key

    def _client(self, *, judge: bool = False) -> OpenAIChatClient:
        config = self._config()
        return OpenAIChatClient(
            api_key=self._api_key(),
            model=config["judge_model"] if judge else config["model"],
            base_url=config["api_base_url"],
            max_tokens=int(config["max_output_tokens"]),
            max_attempts=5 if judge else 3,
        )

    def _adapter(self, method: str):
        config = self._config()
        if method == "direct_llm_native":
            return DirectLLMNativeAdapter(self._client())
        if method == "sap_ver1":
            adapter = LegacyHTTPAdapter(config["legacy_base_url"])
            adapter.healthcheck()
            return adapter
        if method == "dsh_sap":
            return DSHSAPAdapter(
                experiment_root=self.experiment_root,
                api_key=self._api_key(),
                base_url=config["api_base_url"],
                model=config["model"],
                max_tokens=int(config["max_output_tokens"]),
                node_executable=Path(config["dsh_node"]) if config.get("dsh_node") else None,
                dsh_js=Path(config["dsh_js"]) if config.get("dsh_js") else None,
            )
        raise ValueError(f"Unknown method: {method}")

    def run_generation(
        self,
        *,
        methods: Iterable[str] = METHODS,
        study_ids: set[str] | None = None,
        force: bool = False,
    ) -> dict[str, Any]:
        config = self._config()
        requested = tuple(methods)
        unknown = set(requested) - set(METHODS)
        if unknown:
            raise ValueError(f"Unknown methods: {sorted(unknown)}")
        rows = []
        for method in requested:
            adapter = self._adapter(method)
            try:
                for question in self._sample()["questions"]:
                    study_id = question["study_id"]
                    if study_ids and study_id not in study_ids:
                        continue
                    run_dir = self.experiment_root / "runs" / study_id
                    output_path = run_dir / method / "candidate.md"
                    metadata_path = run_dir / method / "run.json"
                    if output_path.exists() and metadata_path.exists() and not force:
                        rows.append(load_json(metadata_path))
                        continue
                    protocol_path = run_dir / "input" / "protocol_input.txt"
                    crf_path = run_dir / "input" / "crf_not_provided.txt"
                    protocol_text = protocol_path.read_text(encoding="utf-8")
                    started_at = time.time()
                    try:
                        outcome: GenerationOutcome = adapter.generate(
                            protocol_text, protocol_path, crf_path
                        )
                        _write_text(output_path, outcome.text)
                        metadata = {
                            "experiment_id": config["experiment_id"],
                            "study_id": study_id,
                            "method": method,
                            "status": "complete",
                            "model": config["model"],
                            "max_output_tokens": config["max_output_tokens"],
                            "temperature_policy": config["temperature_policy"],
                            "input_manifest": str(run_dir / "input" / "manifest.json"),
                            "output_path": str(output_path),
                            "output_sha256": sha256(output_path),
                            "elapsed_ms": outcome.elapsed_ms,
                            "calls": outcome.calls,
                            "usage": outcome.usage,
                            "metadata": outcome.metadata,
                            "started_at_epoch": started_at,
                        }
                    except Exception as exc:  # noqa: BLE001 - persist per-run failure and continue
                        metadata = {
                            "experiment_id": config["experiment_id"],
                            "study_id": study_id,
                            "method": method,
                            "status": "failed",
                            "model": config["model"],
                            "max_output_tokens": config["max_output_tokens"],
                            "temperature_policy": config["temperature_policy"],
                            "error": f"{type(exc).__name__}: {exc}",
                            "started_at_epoch": started_at,
                        }
                    write_json(metadata_path, metadata)
                    rows.append(metadata)
            finally:
                close = getattr(adapter, "close", None)
                if close is not None:
                    close()
        report = {
            "complete": sum(row["status"] == "complete" for row in rows),
            "failed": sum(row["status"] == "failed" for row in rows),
            "runs": rows,
        }
        write_json(self.experiment_root / "generation-report.json", report)
        return report

    def run_judging(
        self,
        *,
        methods: Iterable[str] = METHODS,
        study_ids: set[str] | None = None,
        force: bool = False,
    ) -> dict[str, Any]:
        judge = SemanticJudge(benchmark_root=self.benchmark_root, client=self._client(judge=True))
        rows = []
        for question in self._sample()["questions"]:
            study_id = question["study_id"]
            if study_ids and study_id not in study_ids:
                continue
            run_dir = self.experiment_root / "runs" / study_id
            protocol_text = (run_dir / "input" / "protocol_input.txt").read_text(encoding="utf-8")
            for method in methods:
                candidate_path = run_dir / method / "candidate.md"
                output_path = run_dir / method / "evaluation.json"
                if output_path.exists() and not force:
                    rows.append(load_json(output_path))
                    continue
                if not candidate_path.exists():
                    rows.append(
                        {"study_id": study_id, "method": method, "status": "missing_candidate"}
                    )
                    continue
                try:
                    result = judge.evaluate(
                        question=question,
                        protocol_text=protocol_text,
                        candidate_text=candidate_path.read_text(encoding="utf-8"),
                    )
                    result["method"] = method
                    result["status"] = "complete"
                except Exception as exc:  # noqa: BLE001 - persist per-judge failure and continue
                    result = {
                        "study_id": study_id,
                        "method": method,
                        "status": "failed",
                        "error": f"{type(exc).__name__}: {exc}",
                    }
                write_json(output_path, result)
                rows.append(result)
        report = {
            "complete": sum(row.get("status") == "complete" for row in rows),
            "failed": sum(row.get("status") == "failed" for row in rows),
            "missing_candidate": sum(row.get("status") == "missing_candidate" for row in rows),
            "evaluations": rows,
        }
        write_json(self.experiment_root / "evaluation-report.json", report)
        return report

    def summarize(self) -> dict[str, Any]:
        detail_rows = []
        for question in self._sample()["questions"]:
            study_id = question["study_id"]
            for method in METHODS:
                path = self.experiment_root / "runs" / study_id / method / "evaluation.json"
                if not path.exists():
                    continue
                value = load_json(path)
                if value.get("status") != "complete":
                    continue
                summary = value["summary"]
                row = {
                    "study_id": study_id,
                    "method": method,
                    "weighted_score": summary["weighted_score"],
                    "critical_pass": summary["critical_pass"],
                    **{
                        f"sap7_{key}": score
                        for key, score in summary["sap7_category_scores"].items()
                    },
                }
                detail_rows.append(row)
        method_summaries = []
        for method in METHODS:
            rows = [row for row in detail_rows if row["method"] == method]
            scores = [
                float(row["weighted_score"]) for row in rows if row["weighted_score"] is not None
            ]
            method_summaries.append(
                {
                    "method": method,
                    "completed_studies": len(rows),
                    "mean_weighted_score": round(sum(scores) / len(scores), 2) if scores else None,
                    "critical_pass_rate": round(
                        sum(bool(row["critical_pass"]) for row in rows) / len(rows), 4
                    )
                    if rows
                    else None,
                }
            )
        payload = {"methods": method_summaries, "study_method_scores": detail_rows}
        write_json(self.experiment_root / "summary.json", payload)
        csv_path = self.experiment_root / "scores.csv"
        fieldnames = sorted({key for row in detail_rows for key in row})
        with csv_path.open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(detail_rows)
        return payload

from __future__ import annotations

from typing import Any, Literal

from pydantic import Field

from sapgen.domain.models import SAPIR, StrictModel, ValidationReport
from sapgen.harness.base import HarnessAdapter


class RepairOperation(StrictModel):
    op: Literal["add", "replace", "remove"]
    path: str
    value: Any | None = None


class RepairPlan(StrictModel):
    operations: list[RepairOperation] = Field(default_factory=list)
    unresolved: list[str] = Field(default_factory=list)


class ValidationRepairer:
    """Apply small, reviewable JSON-pointer patches instead of regenerating the whole IR."""

    def __init__(self, harness: HarnessAdapter) -> None:
        self.harness = harness

    def repair(
        self,
        ir: SAPIR,
        report: ValidationReport,
        *,
        source_context: str,
        session_id: str,
    ) -> SAPIR:
        errors = [item for item in report.issues if item.severity.value == "error"]
        if not errors:
            return ir
        payload = self.harness.complete_json(
            system_prompt=(
                "You repair a clinical-trial SAP intermediate representation. Return the smallest "
                "RFC-6901-style JSON-pointer patch that resolves structural validation errors. "
                "Use only source-supported facts. If a decision is unsupported, remove the invalid "
                "record and add or preserve a precise clarification; never invent a replacement."
            ),
            user_prompt=(
                "VALIDATION ERRORS\n"
                f"{ValidationReport(issues=errors).model_dump_json(indent=2)}\n\n"
                "CURRENT SAP-IR\n"
                f"{ir.model_dump_json(indent=2, exclude={'generated_sections'})}\n\n"
                f"SOURCE MATERIALS\n{source_context}"
            ),
            schema=RepairPlan.model_json_schema(),
            session_id=session_id,
        )
        plan = RepairPlan.model_validate(payload)
        document = ir.model_dump(mode="json")
        for operation in plan.operations:
            self._apply(document, operation)
        return SAPIR.model_validate(document)

    @staticmethod
    def _apply(document: dict[str, Any], operation: RepairOperation) -> None:
        if not operation.path.startswith("/"):
            raise ValueError(f"Repair path must be an absolute JSON pointer: {operation.path}")
        parts = [
            part.replace("~1", "/").replace("~0", "~") for part in operation.path[1:].split("/")
        ]
        if not parts or parts[0] in {"schema_version", "created_at"}:
            raise ValueError(f"Repair path is not allowed: {operation.path}")
        parent: Any = document
        for part in parts[:-1]:
            parent = parent[int(part)] if isinstance(parent, list) else parent[part]
        key = parts[-1]
        if operation.op == "remove":
            if isinstance(parent, list):
                parent.pop(int(key))
            else:
                parent.pop(key, None)
            return
        value = operation.value
        if isinstance(parent, list):
            if key == "-":
                parent.append(value)
            elif operation.op == "add":
                parent.insert(int(key), value)
            else:
                parent[int(key)] = value
        else:
            parent[key] = value

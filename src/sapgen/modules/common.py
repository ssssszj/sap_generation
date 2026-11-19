from __future__ import annotations

from sapgen.domain.models import SAPIR, ClarificationItem


def add_clarification(
    ir: SAPIR,
    *,
    item_id: str,
    module: str,
    question: str,
    paths: list[str],
    blocking: bool = True,
) -> None:
    if any(item.id == item_id for item in ir.clarifications):
        return
    ir.clarifications.append(
        ClarificationItem(
            id=item_id,
            module=module,
            question=question,
            related_paths=paths,
            blocking=blocking,
        )
    )

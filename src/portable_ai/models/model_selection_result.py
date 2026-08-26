from dataclasses import dataclass

from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)


@dataclass(frozen=True)
class ModelSelectionResult:
    """
    Represents a selected model/runtime pair.
    """

    model: ModelDescriptor

    runtime: str

    capability: str

    reason: str

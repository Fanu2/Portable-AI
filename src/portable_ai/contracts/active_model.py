from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class ActiveModel:
    """
    Represents the currently selected model.
    """

    model_name: str

    runtime_name: str

    capability: Optional[str] = None

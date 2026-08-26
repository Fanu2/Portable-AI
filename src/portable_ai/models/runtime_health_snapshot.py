from dataclasses import dataclass
from datetime import datetime

from portable_ai.models.runtime_health import (
    RuntimeHealth,
)


@dataclass(frozen=True)
class RuntimeHealthSnapshot:
    """
    Runtime health observation.
    """

    runtime_name: str

    health: RuntimeHealth

    checked_at: datetime

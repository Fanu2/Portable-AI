from dataclasses import dataclass

from portable_ai.models.runtime_health import (
    RuntimeHealth,
)


@dataclass(frozen=True)
class RuntimeReadiness:
    """
    Runtime execution readiness state.
    """

    runtime_name: str

    health: RuntimeHealth

    ready: bool

    reason: str

from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionResult:
    """
    Represents runtime execution output.
    """

    runtime: str

    model: str

    response: str

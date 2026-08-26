from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionError:
    """
    Represents execution failure.
    """

    runtime: str
    model: str
    message: str

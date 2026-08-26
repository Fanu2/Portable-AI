from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionRequest:
    """
    Describes an AI execution request.
    """

    runtime: str

    model: str

    prompt: str

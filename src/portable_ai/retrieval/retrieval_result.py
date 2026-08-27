from dataclasses import dataclass


@dataclass(frozen=True)
class RetrievalResult:
    """
    Immutable retrieval result.

    Represents retrieved assistant context.

    Does not:
        - store documents
        - perform retrieval
    """

    content: str

    metadata: dict | None = None

from portable_ai.retrieval.retrieval_contract import (
    RetrievalProvider,
)

from portable_ai.retrieval.retrieval_result import (
    RetrievalResult,
)


class MemoryRetrievalProvider(
    RetrievalProvider
):
    """
    In-memory retrieval provider.

    Used for:
        - testing
        - development
        - provider validation

    Does not:
        - load documents
        - index data
        - persist storage
    """

    def __init__(
        self,
        results: list[RetrievalResult] | None = None,
    ) -> None:

        self._results = (
            results
            or []
        )

    def retrieve(
        self,
        query: str,
    ) -> list[RetrievalResult]:
        """
        Return stored retrieval results.
        """

        return self._results

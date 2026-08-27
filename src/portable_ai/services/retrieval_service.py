from portable_ai.retrieval.retrieval_contract import (
    RetrievalProvider,
)

from portable_ai.retrieval.retrieval_result import (
    RetrievalResult,
)


class RetrievalService:
    """
    Coordinates retrieval requests.

    Responsibilities:
        - accept retrieval queries
        - delegate to retrieval provider
        - expose retrieval results

    Does not:
        - index documents
        - manage storage
        - create embeddings
        - execute search logic
    """

    def __init__(
        self,
        provider: RetrievalProvider | None = None,
    ) -> None:

        self._provider = provider

    def retrieve(
        self,
        query: str,
    ) -> list[RetrievalResult]:
        """
        Retrieve matching context.

        Returns empty results when
        no provider is configured.
        """

        if self._provider is None:

            return []

        return (
            self._provider
            .retrieve(
                query
            )
        )

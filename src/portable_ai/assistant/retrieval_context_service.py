from portable_ai.services.retrieval_service import (
    RetrievalService,
)

from portable_ai.assistant.prompt_context_service import (
    PromptContextService,
)


class RetrievalContextService:
    """
    Bridges retrieval results into assistant prompt context.

    Does not:
        - perform retrieval
        - manage documents
        - create indexes
    """

    def __init__(
        self,
        retrieval_service: RetrievalService,
        prompt_context_service: PromptContextService,
    ) -> None:

        self._retrieval = retrieval_service

        self._prompt_context = (
            prompt_context_service
        )

    def update(
        self,
        query: str,
    ) -> None:
        """
        Retrieve context and expose it
        through prompt context boundary.
        """

        results = (
            self._retrieval
            .retrieve(query)
        )

        self._prompt_context.set_retrieval_context(
            results
        )

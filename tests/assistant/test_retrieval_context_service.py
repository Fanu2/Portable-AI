from portable_ai.assistant.retrieval_context_service import (
    RetrievalContextService,
)

from portable_ai.assistant.prompt_context_service import (
    PromptContextService,
)

from portable_ai.services.retrieval_service import (
    RetrievalService,
)

from portable_ai.retrieval.retrieval_contract import (
    RetrievalProvider,
)

from portable_ai.retrieval.retrieval_result import (
    RetrievalResult,
)


class FakeRetrievalProvider(
    RetrievalProvider
):

    def retrieve(
        self,
        query: str,
    ):

        return [
            RetrievalResult(
                content="context"
            )
        ]


def test_retrieval_context_service_updates_prompt_context():

    prompt_context = PromptContextService()

    retrieval = RetrievalService(
        FakeRetrievalProvider()
    )

    service = RetrievalContextService(
        retrieval,
        prompt_context,
    )

    service.update(
        "hello"
    )

    context = (
        prompt_context
        .get_context()
    )

    assert (
        context.retrieval_context
        is not None
    )

    assert (
        context.retrieval_context[0]
        .content
        == "context"
    )

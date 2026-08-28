from portable_ai.assistant.assistant_service import (
    AssistantService,
)

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
                content="retrieved context"
            )
        ]


def test_assistant_service_automatically_updates_retrieval_context():

    prompt_context = PromptContextService()

    retrieval_context = (
        RetrievalContextService(
            RetrievalService(
                FakeRetrievalProvider()
            ),
            prompt_context,
        )
    )

    assistant = AssistantService(
        prompt_context_service=prompt_context,
        retrieval_context_service=retrieval_context,
    )

    assistant.send_message(
        "hello"
    )

    context = (
        assistant.prompt_context()
    )

    assert (
        context.retrieval_context[0].content
        == "retrieved context"
    )

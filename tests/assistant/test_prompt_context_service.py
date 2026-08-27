from portable_ai.assistant.prompt_context_service import (
    PromptContextService,
)


def test_prompt_context_defaults():

    service = PromptContextService()

    context = (
        service.get_context()
    )

    assert (
        context.conversation
        is None
    )


def test_prompt_context_stores_conversation():

    service = PromptContextService()

    service.set_conversation(
        ["hello"]
    )

    context = (
        service.get_context()
    )

    assert (
        context.conversation
        == ["hello"]
    )


def test_prompt_context_stores_retrieval_placeholder():

    service = PromptContextService()

    service.set_retrieval_context(
        ["document"]
    )

    context = (
        service.get_context()
    )

    assert (
        context.retrieval_context
        == ["document"]
    )

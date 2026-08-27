from portable_ai.assistant.prompt_context_service import (
    PromptContextService,
)

from portable_ai.workspace.workspace_context import (
    WorkspaceContext,
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


def test_prompt_context_stores_workspace_context():

    service = PromptContextService()

    workspace = WorkspaceContext(
        workspace_id="test-workspace",
        active_sources=[
            "document1"
        ],
    )

    service.set_workspace_context(
        workspace
    )

    context = (
        service.get_context()
    )

    assert (
        context.workspace_context
        == workspace
    )

from dataclasses import dataclass
from typing import Optional

from portable_ai.workspace.workspace_context import (
    WorkspaceContext,
)


@dataclass(frozen=True)
class PromptContext:
    """
    Immutable prompt preparation context.

    Contains:
        - conversation context
        - user context
        - retrieval context
        - workspace context

    Does not:
        - execute models
        - retrieve documents
        - make decisions
    """

    conversation: Optional[list] = None

    user_context: Optional[dict] = None

    retrieval_context: Optional[list] = None

    workspace_context: Optional[WorkspaceContext] = None


class PromptContextService:
    """
    Manages assistant prompt context.

    Responsibilities:
        - create prompt context
        - update context sections
        - expose current context

    Does not:
        - call models
        - execute requests
        - retrieve documents
    """

    def __init__(
        self,
    ) -> None:

        self._context = PromptContext()

    def get_context(
        self,
    ) -> PromptContext:

        return self._context

    def set_conversation(
        self,
        conversation: list,
    ) -> None:

        self._context = PromptContext(
            conversation=conversation,
            user_context=self._context.user_context,
            retrieval_context=self._context.retrieval_context,
            workspace_context=self._context.workspace_context,
        )

    def set_user_context(
        self,
        user_context: dict,
    ) -> None:

        self._context = PromptContext(
            conversation=self._context.conversation,
            user_context=user_context,
            retrieval_context=self._context.retrieval_context,
            workspace_context=self._context.workspace_context,
        )

    def set_retrieval_context(
        self,
        retrieval_context: list,
    ) -> None:

        self._context = PromptContext(
            conversation=self._context.conversation,
            user_context=self._context.user_context,
            retrieval_context=retrieval_context,
            workspace_context=self._context.workspace_context,
        )

    def set_workspace_context(
        self,
        workspace_context: WorkspaceContext,
    ) -> None:

        self._context = PromptContext(
            conversation=self._context.conversation,
            user_context=self._context.user_context,
            retrieval_context=self._context.retrieval_context,
            workspace_context=workspace_context,
        )

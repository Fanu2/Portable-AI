from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.contracts.ui_context import (
    UIContext,
)

from portable_ai.services.execution_ui_service import (
    ExecutionUIService,
)

from portable_ai.services.assistant_ui_service import (
    AssistantUIService,
)


class UIFactory:
    """
    Creates GUI service context.

    Responsibilities:
        - assemble UI-facing services
        - keep GUI dependencies isolated

    Architecture:

        ApplicationContext
              |
              X

        UIContext
              |
              ├── ExecutionUIService
              |
              └── AssistantUIService
                        |
                        ▼
                AssistantService
                        |
              ┌─────────┴─────────┐
              ▼                   ▼
    ConversationService   AssistantContextService

    Core application services remain untouched.
    """

    def create(
        self,
        active_execution,
    ) -> UIContext:

        #
        # Execution UI boundary.
        #
        # Provides controlled access
        # to existing execution flow.
        #
        execution = (
            ExecutionUIService(
                active_execution
            )
        )

        #
        # Assistant composition boundary.
        #
        # AssistantService owns:
        #   - conversation state
        #   - assistant context
        #
        # It does not execute models.
        #
        assistant_service = (
            AssistantService()
        )

        #
        # GUI-facing assistant boundary.
        #
        # Conversation widgets consume
        # this service only.
        #
        assistant = (
            AssistantUIService(
                assistant_service
            )
        )

        return UIContext(
            execution=execution,
            assistant=assistant,
        )

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

    Does not:
        - create runtimes
        - create providers
        - manage execution
        - own assistant lifecycle

    Supports:
        - default assistant creation
        - injected assistant services

    This preserves existing GUI bootstrap
    while allowing future application-level
    dependency injection.
    """

    def create(
        self,
        active_execution,
        assistant_service=None,
    ) -> UIContext:

        #
        # Execution UI boundary.
        #
        execution = (
            ExecutionUIService(
                active_execution
            )
        )

        #
        # Assistant service boundary.
        #
        # Backward compatible:
        # create default assistant when
        # no service is injected.
        #
        if assistant_service is None:

            assistant_service = (
                AssistantService()
            )

        #
        # GUI-facing assistant boundary.
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

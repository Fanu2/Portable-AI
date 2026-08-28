from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.assistant.response_generation_service import (
    ResponseGenerationService,
)

from portable_ai.assistant.providers.execution_assistant_provider import (
    ExecutionAssistantProvider,
)


class AssistantFactory:
    """
    Creates configured assistant services.

    Responsibilities:
        - assemble assistant dependencies
        - connect assistant to execution layer

    Does not:
        - manage UI
        - manage runtimes
        - manage models
        - execute directly
    """

    def create(
        self,
        active_execution_service=None,
    ) -> AssistantService:
        """
        Create assistant service.

        Active execution service is optional.

        When absent:
            assistant remains available
            without generation backend.
        """

        provider = None

        if active_execution_service is not None:

            provider = (
                ExecutionAssistantProvider(
                    active_execution_service
                )
            )

        response_generation = (
            ResponseGenerationService(
                provider
            )
        )

        return AssistantService(
            response_generation_service=(
                response_generation
            )
        )

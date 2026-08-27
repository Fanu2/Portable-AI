from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.assistant.response_generation_service import (
    ResponseGenerationService,
)

from portable_ai.assistant.providers.runtime_assistant_provider import (
    RuntimeAssistantProvider,
)


class AssistantFactory:
    """
    Creates configured assistant services.

    Responsibilities:
        - assemble assistant dependencies
        - connect assistant to runtime provider

    Does not:
        - manage UI
        - manage runtimes
        - manage models
        - execute directly
    """

    def create(
        self,
        runtime_provider=None,
    ) -> AssistantService:
        """
        Create assistant service.

        Runtime provider is optional.

        When absent:
            assistant remains available
            without generation backend.
        """

        provider = None

        if runtime_provider is not None:

            provider = (
                RuntimeAssistantProvider(
                    runtime_provider
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

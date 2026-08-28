from portable_ai.assistant.assistant_factory import (
    AssistantFactory,
)

from portable_ai.assistant.assistant_service import (
    AssistantService,
)

from portable_ai.contracts.execution_result import (
    ExecutionResult,
)


class FakeActiveExecutionService:
    """
    Fake active execution service.
    """

    def execute(
        self,
        prompt,
    ):

        return ExecutionResult(
            runtime="ollama",
            model="qwen3:4b",
            response="response",
        )


def test_assistant_factory_creates_default_assistant():

    factory = AssistantFactory()

    assistant = factory.create()

    assert isinstance(
        assistant,
        AssistantService,
    )


def test_assistant_factory_creates_execution_backed_assistant():

    factory = AssistantFactory()

    execution = FakeActiveExecutionService()

    assistant = factory.create(
        execution
    )

    assert isinstance(
        assistant,
        AssistantService,
    )

    response = (
        assistant.generate_response()
    )

    # No prompt context yet.
    # Generation boundary exists,
    # but no conversation has been added.
    assert response is None or isinstance(
        response,
        str,
    )

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
            response=(
                "Hello! "
                "How can I assist you today?"
            ),
        )


def test_ollama_runtime_generates_assistant_response():

    execution = (
        FakeActiveExecutionService()
    )

    assistant = (
        AssistantFactory()
        .create(
            execution
        )
    )

    assistant.send_message(
        "Say hello in one sentence"
    )

    response = (
        assistant.generate_response()
    )

    assert response is not None

    assert isinstance(
        response,
        str,
    )

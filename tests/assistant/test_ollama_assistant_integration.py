from portable_ai.assistant.assistant_factory import (
    AssistantFactory,
)

from portable_ai.contracts.runtime_descriptor import (
    RuntimeDescriptor,
)

from portable_ai.runtimes.provider_factory import (
    ProviderFactory,
)


def test_ollama_runtime_generates_assistant_response():

    descriptor = RuntimeDescriptor(
        name="Ollama",
        version=None,
        available=True,
        capabilities=frozenset(
            {
                "text_generation",
            }
        ),
        endpoint=(
            "http://127.0.0.1:11434"
        ),
    )

    runtime = (
        ProviderFactory()
        .create(descriptor)
    )

    assistant = (
        AssistantFactory()
        .create(runtime)
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

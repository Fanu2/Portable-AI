from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.models.runtime_registry import (
    RuntimeRegistry,
)

from portable_ai.services.runtime_model_compatibility_service import (
    RuntimeModelCompatibilityService,
)


class FakeRuntime:

    name = "ollama"

    def capabilities(self):
        return {
            "text_generation",
            "embeddings",
        }


def test_runtime_can_execute_model():

    models = ModelRegistry()

    models.register(
        ModelDescriptor(
            name="Qwen3.5-4B",
            version="1.0",
            format="GGUF",
            quantization="Q4_K_M",
            size_gb=2.7,
            license="Apache-2.0",
            capabilities=frozenset(
                {"text_generation"}
            ),
        )
    )

    runtimes = RuntimeRegistry()

    runtimes.register(
        FakeRuntime()
    )

    service = RuntimeModelCompatibilityService(
        models,
        runtimes,
    )

    assert service.can_execute(
        "Qwen3.5-4B",
        "ollama",
    )

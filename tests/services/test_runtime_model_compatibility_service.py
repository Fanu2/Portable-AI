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

def test_runtime_rejects_model_from_different_runtime():

    models = ModelRegistry()

    models.register(
        ModelDescriptor(
            name="tiny-gpt2",
            version="runtime",
            format="unknown",
            quantization=None,
            size_gb=0.0,
            license="unknown",
            capabilities=frozenset(
                {"text_generation"}
            ),
            source_runtime="huggingface",
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

    assert not service.can_execute(
        "tiny-gpt2",
        "ollama",
    )
	


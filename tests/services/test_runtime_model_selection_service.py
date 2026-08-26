from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.models.runtime_registry import (
    RuntimeRegistry,
)

from portable_ai.services.runtime_model_selection_service import (
    RuntimeModelSelectionService,
)


class FakeRuntime:

    name = "ollama"

    def capabilities(self):
        return {
            "text_generation",
        }


def test_runtime_aware_model_selection():

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
                {
                    "text_generation",
                }
            ),
        )
    )

    runtimes = RuntimeRegistry()

    runtimes.register(
        FakeRuntime()
    )

    service = RuntimeModelSelectionService(
        models,
        runtimes,
    )

    result = service.select(
        "text_generation",
        "ollama",
    )

    assert result is not None

    assert (
        result.model.name
        == "Qwen3.5-4B"
    )

    assert (
        result.runtime
        == "ollama"
    )

    assert (
        result.capability
        == "text_generation"
    )

    assert (
        result.reason
        == "matched capability and runtime"
    )

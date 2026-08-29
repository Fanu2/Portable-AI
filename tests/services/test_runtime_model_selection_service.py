from portable_ai.contracts.hardware_info import (
    HardwareInfo,
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

from portable_ai.services.runtime_model_selection_service import (
    RuntimeModelSelectionService,
)


class FakeRuntime:

    name = "ollama"

    def capabilities(self):
        return {
            "text_generation",
        }


class FakeHuggingFaceRuntime:

    name = "huggingface"

    def capabilities(self):
        return {
            "text_generation",
        }


def create_service():

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
            minimum_ram_gb=8.0,
        )
    )

    models.register(
        ModelDescriptor(
            name="tiny-gpt2",
            version="runtime",
            format="unknown",
            quantization=None,
            size_gb=0.0,
            license="unknown",
            capabilities=frozenset(
                {
                    "text_generation",
                }
            ),
            source_runtime="huggingface",
        )
    )

    runtimes = RuntimeRegistry()

    runtimes.register(
        FakeRuntime()
    )

    runtimes.register(
        FakeHuggingFaceRuntime()
    )

    return RuntimeModelSelectionService(
        models,
        runtimes,
    )


def test_runtime_aware_model_selection():

    service = create_service()

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


def test_runtime_model_selection_with_hardware():

    service = create_service()

    hardware = HardwareInfo(
        cpu_cores=8,
        ram_gb=16.0,
    )

    result = service.select_with_hardware(
        "text_generation",
        "ollama",
        hardware,
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
        == "matched capability, runtime, and hardware"
    )


def test_huggingface_model_selected_for_huggingface():

    service = create_service()

    result = service.select(
        "text_generation",
        "huggingface",
    )

    assert result is not None

    assert (
        result.model.name
        == "tiny-gpt2"
    )

    assert (
        result.runtime
        == "huggingface"
    )


def test_huggingface_model_not_selected_for_ollama():

    service = create_service()

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


def test_huggingface_model_selection_with_hardware():

    service = create_service()

    hardware = HardwareInfo(
        cpu_cores=8,
        ram_gb=16.0,
    )

    result = service.select_with_hardware(
        "text_generation",
        "huggingface",
        hardware,
    )

    assert result is not None

    assert (
        result.model.name
        == "tiny-gpt2"
    )

    assert (
        result.runtime
        == "huggingface"
    )

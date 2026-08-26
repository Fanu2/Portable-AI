from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.services.hardware_model_compatibility_service import (
    HardwareModelCompatibilityService,
)


def create_model(
    minimum_ram_gb: float,
) -> ModelDescriptor:

    return ModelDescriptor(
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
        minimum_ram_gb=minimum_ram_gb,
    )


def test_model_runs_with_sufficient_memory():

    service = HardwareModelCompatibilityService()

    model = create_model(
        8.0,
    )

    hardware = HardwareInfo(
        cpu_cores=8,
        ram_gb=16.0,
    )

    assert service.can_run(
        model,
        hardware,
    )


def test_model_rejected_with_insufficient_memory():

    service = HardwareModelCompatibilityService()

    model = create_model(
        32.0,
    )

    hardware = HardwareInfo(
        cpu_cores=4,
        ram_gb=8.0,
    )

    assert not service.can_run(
        model,
        hardware,
    )

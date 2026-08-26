from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)

from portable_ai.contracts.model_resource import (
    ModelResource,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.services.model_compatibility_service import (
    ModelCompatibilityService,
)


def test_model_capability_matching():

    registry = ModelRegistry()

    registry.register(
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

    service = ModelCompatibilityService(
        registry
    )

    assert service.supports(
        "Qwen3.5-4B",
        "text_generation",
    )

    assert not service.supports(
        "Qwen3.5-4B",
        "vision",
    )


class FakeHardwareCompatibilityService:
    """
    Fake hardware compatibility checker.
    """

    def can_run(
        self,
        model,
        hardware,
    ) -> bool:

        return (
            hardware.ram_gb
            >= 4.0
        )


def test_model_hardware_compatibility():

    service = ModelCompatibilityService(
        registry=None,
        hardware_service=(
            FakeHardwareCompatibilityService()
        ),
    )

    model = ModelResource(
        model_name="Qwen3.5-4B",
        path=None,
        size_gb=2.7,
        format="GGUF",
    )

    hardware = HardwareInfo(
        cpu_cores=8,
        ram_gb=8.0,
        storage_gb=100.0,
    )

    assert service.can_run(
        model,
        hardware,
    )


def test_model_hardware_rejection():

    service = ModelCompatibilityService(
        registry=None,
        hardware_service=(
            FakeHardwareCompatibilityService()
        ),
    )

    model = ModelResource(
        model_name="LargeModel",
        path=None,
        size_gb=20.0,
        format="GGUF",
    )

    hardware = HardwareInfo(
        cpu_cores=4,
        ram_gb=2.0,
        storage_gb=50.0,
    )

    assert not service.can_run(
        model,
        hardware,
    )

from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)

from portable_ai.contracts.model_descriptor import (
    ModelDescriptor,
)


class HardwareModelCompatibilityService:
    """
    Checks whether hardware can support a model.
    """

    def can_run(
        self,
        model: ModelDescriptor,
        hardware: HardwareInfo,
    ) -> bool:

        if (
            model.minimum_ram_gb is not None
            and hardware.ram_gb < model.minimum_ram_gb
        ):
            return False

        return True

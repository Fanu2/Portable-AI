from dataclasses import dataclass

from portable_ai.services.configuration_service import ConfigurationService
from portable_ai.services.storage_service import StorageService
from portable_ai.services.hardware_service import HardwareService


@dataclass(frozen=True)
class ApplicationContext:
    """
    Provides access to core Portable-AI services.
    """

    configuration: ConfigurationService
    storage: StorageService
    hardware: HardwareService

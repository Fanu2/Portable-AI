from dataclasses import dataclass
from typing import Optional

from portable_ai.services.configuration_service import (
    ConfigurationService,
)

from portable_ai.services.storage_service import (
    StorageService,
)

from portable_ai.services.hardware_service import (
    HardwareService,
)

from portable_ai.services.runtime_service import (
    RuntimeService,
)

from portable_ai.services.dashboard_service import (
    DashboardService,
)

from portable_ai.services.runtime_monitor_service import (
    RuntimeMonitorService,
)


@dataclass(frozen=True)
class ApplicationContext:
    """
    Provides access to core Portable-AI services.
    """

    configuration: ConfigurationService
    storage: StorageService
    hardware: HardwareService

    # Runtime and GUI preparation services
    runtime: Optional[RuntimeService] = None
    dashboard: Optional[DashboardService] = None
    monitor: Optional[RuntimeMonitorService] = None

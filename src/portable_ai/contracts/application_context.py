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

from portable_ai.services.capability_service import (
    CapabilityService,
)

from portable_ai.services.runtime_model_selection_service import (
    RuntimeModelSelectionService,
)

from portable_ai.services.model_catalog_service import (
    ModelCatalogService,
)

from portable_ai.services.execution_service import (
    ExecutionService,
)


@dataclass(frozen=True)
class ApplicationContext:
    """
    Provides access to core Portable-AI services.
    """

    configuration: ConfigurationService
    storage: StorageService
    hardware: HardwareService

    # Runtime, GUI, capability, model, and execution services
    runtime: Optional[RuntimeService] = None
    dashboard: Optional[DashboardService] = None
    monitor: Optional[RuntimeMonitorService] = None
    capabilities: Optional[CapabilityService] = None
    model_selection: Optional[RuntimeModelSelectionService] = None
    model_catalog: Optional[ModelCatalogService] = None
    execution: Optional[ExecutionService] = None

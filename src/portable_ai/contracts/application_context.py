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

from portable_ai.services.hardware_detection_service import (
    HardwareDetectionService,
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

from portable_ai.services.model_catalog_service import (
    ModelCatalogService,
)

from portable_ai.services.model_inventory_service import (
    ModelInventoryService,
)

from portable_ai.services.model_compatibility_service import (
    ModelCompatibilityService,
)

from portable_ai.services.runtime_model_selection_service import (
    RuntimeModelSelectionService,
)

from portable_ai.services.active_model_service import (
    ActiveModelService,
)

from portable_ai.services.execution_service import (
    ExecutionService,
)

from portable_ai.services.execution_request_service import (
    ExecutionRequestService,
)

from portable_ai.services.execution_adapter_service import (
    ExecutionAdapterService,
)

from portable_ai.services.active_execution_service import (
    ActiveExecutionService,
)

from portable_ai.assistant.assistant_service import (
    AssistantService,
)

@dataclass(frozen=True)
class ApplicationContext:
    """
    Provides access to core Portable-AI services.
    """

    configuration: ConfigurationService

    storage: StorageService

    hardware: HardwareService

    # Runtime services
    runtime: Optional[RuntimeService] = None
    dashboard: Optional[DashboardService] = None
    monitor: Optional[RuntimeMonitorService] = None

    # Capability services
    capabilities: Optional[CapabilityService] = None

    # Model services
    model_catalog: Optional[ModelCatalogService] = None
    model_inventory: Optional[ModelInventoryService] = None
    model_compatibility: Optional[ModelCompatibilityService] = None
    model_selection: Optional[RuntimeModelSelectionService] = None
    active_model: Optional[ActiveModelService] = None

    # Execution services
    execution: Optional[ExecutionService] = None

    execution_request: Optional[ExecutionRequestService] = None

    execution_adapter: Optional[ExecutionAdapterService] = None

    active_execution: Optional[ActiveExecutionService] = None

    # Hardware services
    hardware_detection: Optional[
        HardwareDetectionService
    ] = None

    # Assistant services
    assistant_service: Optional[
        AssistantService
    ] = None

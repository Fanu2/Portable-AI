from pathlib import Path

from portable_ai.contracts.application_context import (
    ApplicationContext,
)

from portable_ai.contracts.model_resource import (
    ModelResource,
)

from portable_ai.config.local_config_manager import (
    LocalConfigManager,
)

from portable_ai.config.config_layer import (
    ConfigLayer,
)

from portable_ai.services.configuration_service import (
    ConfigurationService,
)

from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)

from portable_ai.runtimes.http_transport import (
    HttpTransport,
)

from portable_ai.runtimes.ollama_client import (
    OllamaClient,
)

from portable_ai.runtimes.ollama_provider import (
    OllamaRuntimeProvider,
)

from portable_ai.runtimes.ollama_executor import (
    OllamaExecutor,
)

from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)

from portable_ai.models.model_registry import (
    ModelRegistry,
)

from portable_ai.models.runtime_registry import (
    RuntimeRegistry,
)

from portable_ai.models.executor_registry import (
    ExecutorRegistry,
)

from portable_ai.models.catalog.runtime_catalog import (
    RUNTIME_DEFINITIONS,
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

from portable_ai.services.runtime_service import (
    RuntimeService,
)

from portable_ai.services.runtime_status_service import (
    RuntimeStatusService,
)

from portable_ai.services.runtime_health_service import (
    RuntimeHealthService,
)

from portable_ai.services.runtime_monitor_service import (
    RuntimeMonitorService,
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

from portable_ai.services.execution_result_validator import (
    ExecutionResultValidator,
)

from portable_ai.services.hardware_detection_service import (
    HardwareDetectionService,
)

from portable_ai.services.hardware_model_compatibility_service import (
    HardwareModelCompatibilityService,
)

from portable_ai.services.dashboard_service import (
    DashboardService,
)


class ApplicationFactory:
    """
    Creates the Portable-AI application context.

    Responsible for assembling application services.
    Keeps service construction in one place.
    """

    def __init__(
        self,
        root: Path,
    ) -> None:

        self._root = root

    def create(
        self,
    ) -> ApplicationContext:

        # -------------------------------------------------
        # Configuration layer
        # -------------------------------------------------

        config_manager = LocalConfigManager(
            self._root
            / "config"
            / "portable-ai.json"
        )

        configuration = ConfigurationService(
            config_manager,
            ConfigLayer(),
        )

        # -------------------------------------------------
        # Runtime provider layer
        # -------------------------------------------------

        runtime_registry = RuntimeProviderRegistry()

        ollama_client = OllamaClient(
            HttpTransport()
        )

        ollama_provider = OllamaRuntimeProvider(
            ollama_client
        )

        runtime_registry.register(
            "ollama",
            ollama_provider,
        )

        runtime = RuntimeService(
            runtime_registry,
        )

        runtime_status = RuntimeStatusService(
            runtime_registry,
        )

        runtime_health = RuntimeHealthService(
            runtime_registry,
        )

        runtime_monitor = RuntimeMonitorService(
            runtime_health,
        )

        # -------------------------------------------------
        # Capability layer
        # -------------------------------------------------

        capability_registry = CapabilityRegistry()

        capability_service = CapabilityService(
            capability_registry,
        )

        capability_service.register_runtime_capabilities(
            "ollama",
            ollama_provider.capabilities(),
        )

        # -------------------------------------------------
        # Runtime catalog layer
        # -------------------------------------------------

        runtime_catalog_registry = RuntimeRegistry()

        for definition in RUNTIME_DEFINITIONS:

            runtime_catalog_registry.register(
                definition
            )

        # -------------------------------------------------
        # Model intelligence layer
        # -------------------------------------------------

        model_registry = ModelRegistry()

        model_catalog = ModelCatalogService(
            model_registry,
        )

        model_catalog.load_catalog()

        model_inventory = ModelInventoryService()

        # Scan local model storage
        model_inventory.scan(
            [
                self._root / "models",
            ]
        )

        # Provide fallback catalog models
        # when no local models exist
        if not model_inventory.all():

            model_inventory.register(
                ModelResource(
                    model_name="Qwen3.5-4B",
                    path="catalog://Qwen3.5-4B",
                    size_gb=2.7,
                    format="GGUF",
                    available=True,
                    installed=False,
                    minimum_ram_gb=4.0,
                )
            )

            model_inventory.register(
                ModelResource(
                    model_name="nomic-embed-text",
                    path="catalog://nomic-embed-text",
                    size_gb=0.0,
                    format="GGUF",
                    available=True,
                    installed=False,
                    minimum_ram_gb=1.0,
                )
            )

        # Selects compatible runtime/model combinations
        model_selection = RuntimeModelSelectionService(
            model_registry,
            runtime_catalog_registry,
        )

        # Checks whether models can run locally
        hardware_compatibility = (
            HardwareModelCompatibilityService()
        )

        model_compatibility = ModelCompatibilityService(
            model_registry,
            hardware_compatibility,
        )

        # -------------------------------------------------
        # Active model state layer
        #
        # Maintains the user's selected model.
        #
        # Responsibilities:
        #   - Store active model selection
        #   - Restore previous selection
        #   - Provide state boundary for execution
        #
        # Persistence:
        #
        # ActiveModelService
        #        |
        #        ▼
        # ConfigurationService
        #        |
        #        ▼
        # portable-ai.json
        #
        # No execution logic exists here.
        # -------------------------------------------------

        active_model = ActiveModelService(
            configuration
        )

        active_model.restore()

        # -------------------------------------------------
        # Execution layer
        #
        # Responsible for:
        #   - Runtime executor registration
        #   - Model execution requests
        #   - Result validation
        #
        # Active model selection will connect
        # to this layer in P4.5.
        # -------------------------------------------------

        executor_registry = ExecutorRegistry()

        executor_registry.register(
            "ollama",
            OllamaExecutor(
                ollama_provider,
            ),
        )

        execution = ExecutionService(
            executor_registry,
            ExecutionResultValidator(),
        )

        # -------------------------------------------------
        # Hardware and dashboard layer
        #
        # Hardware:
        #   Provides local machine information.
        #
        # Dashboard:
        #   Aggregates runtime visibility.
        # -------------------------------------------------

        hardware_detection = (
            HardwareDetectionService()
        )

        dashboard = DashboardService(
            runtime,
            runtime_status,
            runtime_health,
        )

        # -------------------------------------------------
        # Final application context
        #
        # Central dependency container.
        #
        # All future features should consume
        # services through this boundary.
        # -------------------------------------------------

        return ApplicationContext(
            configuration=configuration,

            storage=None,

            hardware=None,

            # Runtime services
            runtime=runtime,
            dashboard=dashboard,
            monitor=runtime_monitor,

            # Capability services
            capabilities=capability_service,

            # Model services
            model_catalog=model_catalog,
            model_inventory=model_inventory,
            model_compatibility=model_compatibility,
            model_selection=model_selection,
            active_model=active_model,

            # Execution services
            execution=execution,

            # Hardware services
            hardware_detection=hardware_detection,
        )

from pathlib import Path

from portable_ai.contracts.application_context import (
    ApplicationContext,
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

from portable_ai.models.capability_registry import (
    CapabilityRegistry,
)

from portable_ai.services.capability_service import (
    CapabilityService,
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

from portable_ai.services.dashboard_service import (
    DashboardService,
)


class ApplicationFactory:
    """
    Creates Portable-AI application context.
    """

    def __init__(
        self,
        root: Path,
    ) -> None:
        self._root = root

    def create(self) -> ApplicationContext:

        config_manager = LocalConfigManager(
            self._root / "config" / "portable-ai.json"
        )

        configuration = ConfigurationService(
            config_manager,
            ConfigLayer(),
        )

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

        capability_registry = CapabilityRegistry()

        capability_service = CapabilityService(
            capability_registry,
        )

        capability_service.register_runtime_capabilities(
            "ollama",
            ollama_provider.capabilities(),
        )

        dashboard = DashboardService(
            runtime,
            runtime_status,
            runtime_health,
        )

        return ApplicationContext(
            configuration=configuration,
            storage=None,
            hardware=None,
            runtime=runtime,
            dashboard=dashboard,
            monitor=runtime_monitor,
            capabilities=capability_service,
        )

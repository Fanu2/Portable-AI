from pathlib import Path

from portable_ai.contracts.application_context import (
    ApplicationContext,
)
from portable_ai.config.local_config_manager import (
    LocalConfigManager,
)
from portable_ai.config.config_layer import ConfigLayer
from portable_ai.services.configuration_service import (
    ConfigurationService,
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

        return ApplicationContext(
            configuration=configuration,
            storage=None,
            hardware=None,
        )

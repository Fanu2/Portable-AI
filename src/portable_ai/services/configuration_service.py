from portable_ai.contracts.config_manager import ConfigManager
from portable_ai.config.config_layer import ConfigLayer


class ConfigurationService:
    """
    Application service for configuration handling.
    """

    def __init__(
        self,
        manager: ConfigManager,
        layer: ConfigLayer,
    ) -> None:
        self._manager = manager
        self._layer = layer

    def load(self) -> dict:
        return self._manager.load()

    def save(self, config: dict) -> None:
        self._manager.save(config)

    def merge(
        self,
        *configs: dict,
    ) -> dict:
        return self._layer.merge(*configs)

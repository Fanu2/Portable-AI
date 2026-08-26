from portable_ai.contracts.config_manager import (
    ConfigManager,
)

from portable_ai.config.config_layer import (
    ConfigLayer,
)


class ConfigurationService:
    """
    Application service for configuration handling.

    Provides:
        - loading configuration
        - saving configuration
        - merging configuration layers
        - accessing individual settings

    Keeps configuration storage details hidden
    from application services.
    """

    def __init__(
        self,
        manager: ConfigManager,
        layer: ConfigLayer,
    ) -> None:

        self._manager = manager

        self._layer = layer

    def load(
        self,
    ) -> dict:

        return self._manager.load()

    def save(
        self,
        config: dict,
    ) -> None:

        self._manager.save(
            config
        )

    def merge(
        self,
        *configs: dict,
    ) -> dict:

        return self._layer.merge(
            *configs
        )

    def get(
        self,
        key: str,
        default=None,
    ):
        """
        Read a single configuration value.
        """

        config = self.load()

        return config.get(
            key,
            default,
        )

    def set(
        self,
        key: str,
        value,
    ) -> None:
        """
        Update a single configuration value.
        """

        config = self.load()

        config[key] = value

        self.save(
            config
        )

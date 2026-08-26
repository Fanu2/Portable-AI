import json
from pathlib import Path

from portable_ai.contracts.config_manager import ConfigManager


class LocalConfigManager(ConfigManager):
    """
    JSON-based local configuration manager.
    """

    def __init__(self, path: Path) -> None:
        self._path = path

    def config_path(self) -> Path:
        return self._path

    def load(self) -> dict:
        if not self._path.exists():
            return {}

        return json.loads(
            self._path.read_text()
        )

    def save(self, config: dict) -> None:
        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        self._path.write_text(
            json.dumps(
                config,
                indent=2,
            )
        )

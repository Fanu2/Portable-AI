from pathlib import Path


class StorageManifest:
    """
    Describes the expected Portable-AI storage layout.
    """

    REQUIRED_DIRECTORIES = (
        "models",
        "data",
        "config",
        "cache",
        "logs",
    )

    def __init__(self, root: Path) -> None:
        self._root = root

    def missing_directories(self) -> list[str]:
        return [
            directory
            for directory in self.REQUIRED_DIRECTORIES
            if not (self._root / directory).exists()
        ]

    def is_valid(self) -> bool:
        return len(self.missing_directories()) == 0

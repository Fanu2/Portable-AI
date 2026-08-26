from pathlib import Path

from portable_ai.contracts.model_resource import (
    ModelResource,
)


class ModelScannerService:
    """
    Scans local storage for model files.
    """

    SUPPORTED_FORMATS = {
        ".gguf": "GGUF",
        ".bin": "BIN",
        ".safetensors": "SAFETENSORS",
    }

    def scan(
        self,
        folders: list[Path],
    ) -> list[ModelResource]:

        models: list[ModelResource] = []

        for folder in folders:

            if not folder.exists():

                continue

            for path in folder.rglob("*"):

                if not path.is_file():

                    continue

                model_format = (
                    self.SUPPORTED_FORMATS.get(
                        path.suffix.lower()
                    )
                )

                if model_format is None:

                    continue

                size_gb = round(
                    path.stat().st_size
                    / (1024 ** 3),
                    2,
                )

                models.append(
                    ModelResource(
                        model_name=path.stem,
                        path=str(path),
                        size_gb=size_gb,
                        format=model_format,
                        available=True,
                        installed=True,
                    )
                )

        return models

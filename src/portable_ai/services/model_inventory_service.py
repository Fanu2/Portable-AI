from pathlib import Path

from portable_ai.contracts.model_resource import (
    ModelResource,
)

from portable_ai.services.model_scanner_service import (
    ModelScannerService,
)


class ModelInventoryService:
    """
    Tracks available local model resources.
    """

    def __init__(
        self,
        scanner: ModelScannerService | None = None,
    ) -> None:

        self._models: dict[
            str,
            ModelResource,
        ] = {}

        self._scanner = (
            scanner
            or ModelScannerService()
        )

    def register(
        self,
        resource: ModelResource,
    ) -> None:

        self._models[
            resource.model_name
        ] = resource

    def scan(
        self,
        folders: list[Path],
    ) -> None:

        scanned = self._scanner.scan(
            folders
        )

        for model in scanned:

            self.register(
                model
            )

    def get(
        self,
        model_name: str,
    ) -> ModelResource | None:

        return self._models.get(
            model_name
        )

    def all(
        self,
    ) -> list[ModelResource]:

        return list(
            self._models.values()
        )

    def available(
        self,
    ) -> list[ModelResource]:

        return [
            model
            for model in self._models.values()
            if model.available
        ]

    def installed(
        self,
    ) -> list[ModelResource]:

        return [
            model
            for model in self._models.values()
            if model.installed
        ]

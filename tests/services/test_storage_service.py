from pathlib import Path

from portable_ai.services.storage_service import StorageService


class FakeStorage:
    def root(self):
        return Path("/portable-ai")

    def models_path(self):
        return Path("/portable-ai/models")

    def data_path(self):
        return Path("/portable-ai/data")

    def config_path(self):
        return Path("/portable-ai/config")


def test_storage_service_exposes_paths():
    service = StorageService(
        FakeStorage()
    )

    assert service.root() == Path("/portable-ai")
    assert service.models() == Path("/portable-ai/models")
    assert service.data() == Path("/portable-ai/data")
    assert service.config() == Path("/portable-ai/config")

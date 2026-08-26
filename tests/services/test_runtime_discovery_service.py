from portable_ai.models.runtime_registry import RuntimeRegistry
from portable_ai.services.runtime_discovery_service import RuntimeDiscoveryService


class FakeExecutableFinder:
    def find(self, executable: str) -> str | None:
        if executable == "ollama":
            return "/usr/local/bin/ollama"

        return None


def test_runtime_discovery_detects_defined_runtime():
    registry = RuntimeRegistry()
    finder = FakeExecutableFinder()

    service = RuntimeDiscoveryService(
        finder,
        registry,
    )

    runtimes = service.discover()

    assert len(runtimes) == 4

    ollama = registry.get("Ollama")

    assert ollama is not None
    assert ollama.available
    assert ollama.executable == "/usr/local/bin/ollama"

from portable_ai.config.config_layer import ConfigLayer
from portable_ai.services.configuration_service import (
    ConfigurationService,
)


class FakeConfigManager:
    def load(self):
        return {
            "runtime": "Ollama",
        }

    def save(self, config):
        self.saved = config


def test_configuration_service_loads_configuration():
    service = ConfigurationService(
        FakeConfigManager(),
        ConfigLayer(),
    )

    config = service.load()

    assert config["runtime"] == "Ollama"


def test_configuration_service_merges_configuration():
    service = ConfigurationService(
        FakeConfigManager(),
        ConfigLayer(),
    )

    result = service.merge(
        {"offline": True},
        {"runtime": "Jan"},
    )

    assert result["offline"] is True
    assert result["runtime"] == "Jan"

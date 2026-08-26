import pytest

from portable_ai.contracts.config_manager import ConfigManager


def test_config_manager_is_abstract():
    with pytest.raises(TypeError):
        ConfigManager()

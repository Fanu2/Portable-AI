import pytest

from portable_ai.contracts.runtime_discovery import RuntimeDiscovery


def test_runtime_discovery_is_abstract():
    with pytest.raises(TypeError):
        RuntimeDiscovery()

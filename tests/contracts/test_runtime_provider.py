import pytest

from portable_ai.contracts.runtime_provider import RuntimeProvider


def test_runtime_provider_is_abstract():
    with pytest.raises(TypeError):
        RuntimeProvider()

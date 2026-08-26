import pytest

from portable_ai.contracts.storage_manager import StorageManager


def test_storage_manager_is_abstract():
    with pytest.raises(TypeError):
        StorageManager()

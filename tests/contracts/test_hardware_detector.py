import pytest

from portable_ai.contracts.hardware_detector import HardwareDetector


def test_hardware_detector_is_abstract():
    with pytest.raises(TypeError):
        HardwareDetector()

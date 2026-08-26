from portable_ai.hardware.system_hardware_detector import (
    SystemHardwareDetector,
)


def test_system_hardware_detector_returns_profile():
    detector = SystemHardwareDetector()

    profile = detector.detect()

    assert profile.operating_system
    assert profile.architecture
    assert profile.ram_gb > 0
    assert profile.storage_free_gb is not None

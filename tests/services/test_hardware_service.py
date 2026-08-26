from portable_ai.contracts.hardware_profile import HardwareProfile
from portable_ai.services.hardware_service import HardwareService


class FakeHardwareDetector:
    def detect(self) -> HardwareProfile:
        return HardwareProfile(
            operating_system="Linux",
            architecture="x86_64",
            cpu="Test CPU",
            ram_gb=16.0,
        )


def test_hardware_service_returns_profile():
    service = HardwareService(
        FakeHardwareDetector()
    )

    profile = service.profile()

    assert profile.operating_system == "Linux"
    assert profile.ram_gb == 16.0


def test_hardware_service_preserves_detector_result():
    expected = HardwareProfile(
        operating_system="TestOS",
        architecture="test",
        cpu="TestCPU",
        ram_gb=8.0,
    )

    class CustomDetector:
        def detect(self) -> HardwareProfile:
            return expected

    service = HardwareService(CustomDetector())

    assert service.profile() == expected

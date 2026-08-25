from portable_ai.contracts.hardware_profile import HardwareProfile


def test_hardware_profile_creation():
    profile = HardwareProfile(
        operating_system="Linux",
        architecture="x86_64",
        cpu="Generic CPU",
        ram_gb=16.0,
        gpu="Integrated GPU",
        vram_gb=2.0,
        storage_free_gb=100.0,
    )

    assert profile.operating_system == "Linux"
    assert profile.architecture == "x86_64"
    assert profile.ram_gb == 16.0
    assert profile.gpu == "Integrated GPU"

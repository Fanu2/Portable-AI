from portable_ai.contracts.hardware_info import (
    HardwareInfo,
)


def test_hardware_info_contract():

    info = HardwareInfo(
        cpu_cores=8,
        ram_gb=16.0,
        gpu_name="RTX",
        gpu_memory_gb=8.0,
    )

    assert info.cpu_cores == 8
    assert info.ram_gb == 16.0
    assert info.gpu_name == "RTX"

def test_runtime_monitor_is_service_boundary():

    from portable_ai.services.runtime_monitor_service import (
        RuntimeMonitorService,
    )

    assert (
        RuntimeMonitorService.__module__
        .startswith(
            "portable_ai.services"
        )
    )

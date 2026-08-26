from portable_ai.services.dashboard_service import (
    DashboardService,
)


class FakeRuntimeService:

    def available_runtimes(self):
        return [
            "ollama",
        ]


class FakeRuntimeStatusService:

    def status(self):
        return {
            "ollama": False,
        }


class FakeRuntimeHealthService:

    def snapshot(
        self,
        runtime_name,
    ):
        return None


def test_dashboard_service_summary():

    service = DashboardService(
        FakeRuntimeService(),
        FakeRuntimeStatusService(),
        FakeRuntimeHealthService(),
    )

    result = service.summary()

    assert result == {
        "runtimes": {
            "ollama": False,
        },
        "available_runtime_count": 1,
    }

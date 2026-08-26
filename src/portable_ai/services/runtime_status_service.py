from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)


class RuntimeStatusService:
    """
    Provides runtime health information.
    """

    def __init__(
        self,
        registry: RuntimeProviderRegistry,
    ) -> None:
        self._registry = registry

    def status(self) -> dict[str, bool]:
        result = {}

        for name, provider in self._registry._providers.items():
            result[name] = provider.health()

        return result

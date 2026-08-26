from portable_ai.contracts.runtime_provider import RuntimeProvider


class RuntimeProviderRegistry:
    """
    Registry for runtime provider adapters.
    """

    def __init__(self) -> None:
        self._providers: dict[str, RuntimeProvider] = {}

    def register(
        self,
        name: str,
        provider: RuntimeProvider,
    ) -> None:
        self._providers[name] = provider

    def get(
        self,
        name: str,
    ) -> RuntimeProvider | None:
        return self._providers.get(name)

    def all(self) -> list[RuntimeProvider]:
        return list(self._providers.values())

    def all_named(self) -> dict[str, RuntimeProvider]:
        """
        Return registered providers by name.
        """
        return self._providers.copy()

    def available(self) -> list[RuntimeProvider]:
        return [
            provider
            for provider in self._providers.values()
            if provider.health()
        ]

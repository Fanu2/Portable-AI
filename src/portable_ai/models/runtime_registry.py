from portable_ai.contracts.runtime_descriptor import RuntimeDescriptor


class RuntimeRegistry:
    """
    Registry of AI runtimes discovered on the host.
    """

    def __init__(self) -> None:
        self._runtimes: dict[str, RuntimeDescriptor] = {}

    def register(self, runtime: RuntimeDescriptor) -> None:
        self._runtimes[runtime.name] = runtime

    def get(self, name: str) -> RuntimeDescriptor | None:
        return self._runtimes.get(name)

    def all(self) -> list[RuntimeDescriptor]:
        return list(self._runtimes.values())

    def available(self) -> list[RuntimeDescriptor]:
        return [
            runtime
            for runtime in self._runtimes.values()
            if runtime.available
        ]
        

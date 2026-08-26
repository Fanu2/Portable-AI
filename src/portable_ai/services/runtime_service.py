from portable_ai.runtimes.runtime_provider_registry import (
    RuntimeProviderRegistry,
)


class RuntimeService:
    """
    Application service for AI runtime access.
    """

    def __init__(
        self,
        registry: RuntimeProviderRegistry,
    ) -> None:
        self._registry = registry

    def available_runtimes(self):
        return self._registry.available()

    def get_runtime(
        self,
        name: str,
    ):
        return self._registry.get(name)

    def generate(
        self,
        runtime_name: str,
        prompt: str,
        **kwargs,
    ) -> str:
        runtime = self.get_runtime(
            runtime_name
        )

        if runtime is None:
            raise ValueError(
                f"Runtime not found: {runtime_name}"
            )

        return runtime.generate(
            prompt,
            **kwargs,
        )

    def embed(
        self,
        runtime_name: str,
        text: str,
    ) -> list[float]:
        runtime = self.get_runtime(
            runtime_name
        )

        if runtime is None:
            raise ValueError(
                f"Runtime not found: {runtime_name}"
            )

        return runtime.embed(
            text
        )

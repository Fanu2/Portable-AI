from portable_ai.contracts.runtime_descriptor import RuntimeDescriptor
from portable_ai.hardware.executable_finder import ExecutableFinder
from portable_ai.models.runtime_registry import RuntimeRegistry
from portable_ai.models.catalog.runtime_catalog import RUNTIME_DEFINITIONS


class RuntimeDiscoveryService:
    """
    Discovers AI runtimes using the runtime catalog.
    """

    def __init__(
        self,
        finder: ExecutableFinder,
        registry: RuntimeRegistry,
    ) -> None:
        self._finder = finder
        self._registry = registry

    def discover(self) -> list[RuntimeDescriptor]:
        runtimes: list[RuntimeDescriptor] = []

        for definition in RUNTIME_DEFINITIONS:
            runtime = self._discover_runtime(definition)
            self._registry.register(runtime)
            runtimes.append(runtime)

        return runtimes

    def _discover_runtime(self, definition) -> RuntimeDescriptor:
        executable = None

        for executable_name in definition.executable_names:
            executable = self._finder.find(executable_name)

            if executable is not None:
                break

        return RuntimeDescriptor(
            name=definition.name,
            version=None,
            available=executable is not None,
            capabilities=definition.capabilities,
            executable=executable,
        )

from portable_ai.contracts.runtime_definition import RuntimeDefinition


RUNTIME_DEFINITIONS = (
    RuntimeDefinition(
        name="Ollama",
        executable_names=("ollama",),
        capabilities=frozenset(
            {
                "text_generation",
                "embeddings",
            }
        ),
    ),
    RuntimeDefinition(
        name="llama.cpp",
        executable_names=("llama-cli", "main"),
        capabilities=frozenset(
            {
                "text_generation",
            }
        ),
    ),
    RuntimeDefinition(
        name="LM Studio",
        executable_names=("lms",),
        capabilities=frozenset(
            {
                "text_generation",
                "embeddings",
            }
        ),
    ),
    RuntimeDefinition(
        name="Jan",
        executable_names=("jan",),
        capabilities=frozenset(
            {
                "text_generation",
            }
        ),
    ),
)

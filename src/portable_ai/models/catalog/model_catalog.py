from portable_ai.contracts.model_definition import ModelDefinition


MODEL_DEFINITIONS = (
    ModelDefinition(
        name="Qwen3.5-4B",
        format="GGUF",
        capabilities=frozenset(
            {
                "text_generation",
            }
        ),
        default_quantization="Q4_K_M",
        license="Apache-2.0",
    ),
    ModelDefinition(
        name="nomic-embed-text",
        format="GGUF",
        capabilities=frozenset(
            {
                "embeddings",
            }
        ),
        license="Apache-2.0",
    ),
)

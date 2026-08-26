from portable_ai.config.config_layer import ConfigLayer


def test_config_layers_merge_by_priority():
    layer = ConfigLayer()

    result = layer.merge(
        {
            "offline": True,
            "runtime": "Ollama",
        },
        {
            "runtime": "Jan",
        },
    )

    assert result["offline"] is True
    assert result["runtime"] == "Jan"

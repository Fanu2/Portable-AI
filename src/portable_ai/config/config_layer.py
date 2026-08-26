class ConfigLayer:
    """
    Merges configuration layers in priority order.
    """

    def merge(
        self,
        *layers: dict,
    ) -> dict:
        result = {}

        for layer in layers:
            result.update(layer)

        return result

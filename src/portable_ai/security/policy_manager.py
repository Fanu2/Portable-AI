from portable_ai.contracts.security_policy import SecurityPolicy


class PolicyManager:
    """
    Manages Portable-AI security policy.
    """

    def __init__(
        self,
        policy: SecurityPolicy,
    ) -> None:
        self._policy = policy

    def policy(self) -> SecurityPolicy:
        return self._policy

    def network_allowed(self) -> bool:
        return self._policy.allow_network

    def offline(self) -> bool:
        return self._policy.offline_mode

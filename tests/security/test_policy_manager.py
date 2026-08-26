from portable_ai.contracts.security_policy import SecurityPolicy
from portable_ai.security.policy_manager import PolicyManager


def test_policy_manager_exposes_policy():
    manager = PolicyManager(
        SecurityPolicy()
    )

    assert manager.offline()
    assert not manager.network_allowed()

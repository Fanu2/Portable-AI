from portable_ai.contracts.security_policy import SecurityPolicy


def test_security_policy_defaults_to_safe_mode():
    policy = SecurityPolicy()

    assert policy.offline_mode
    assert not policy.allow_network
    assert not policy.allow_external_tools

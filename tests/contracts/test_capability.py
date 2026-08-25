from portable_ai.contracts.capability import CapabilityDescriptor


def test_capability_support():
    capability = CapabilityDescriptor(
        frozenset({"text_generation", "vision"})
    )

    assert capability.supports("text_generation")
    assert capability.supports("vision")
    assert not capability.supports("audio")

from dataclasses import dataclass


@dataclass(frozen=True)
class SecurityPolicy:
    """
    Defines Portable-AI security settings.
    """

    offline_mode: bool = True
    allow_network: bool = False
    allow_external_tools: bool = False

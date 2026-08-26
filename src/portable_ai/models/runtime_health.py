from enum import Enum


class RuntimeHealth(str, Enum):
    """
    Runtime health states.
    """

    ONLINE = "online"

    DEGRADED = "degraded"

    OFFLINE = "offline"

    UNKNOWN = "unknown"

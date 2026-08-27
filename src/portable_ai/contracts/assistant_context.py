from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class AssistantContext:
    """
    Assistant service boundary.

    Contains assistant-specific state only.

    Keeps assistant features isolated from:
        - ApplicationContext
        - UIContext
        - Execution services

    Future additions:
        - conversation memory
        - prompt context
        - retrieval context
    """

    conversation_id: Optional[str] = None

    user_context: Optional[dict] = None

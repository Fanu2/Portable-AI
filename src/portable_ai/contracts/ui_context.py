from dataclasses import dataclass
from typing import Optional

from portable_ai.services.execution_ui_service import (
    ExecutionUIService,
)

from portable_ai.services.assistant_ui_service import (
    AssistantUIService,
)


@dataclass(frozen=True)
class UIContext:
    """
    GUI service boundary.

    Contains presentation-facing services only.

    Core application services remain in
    ApplicationContext.
    """

    # Controlled execution UI
    execution: Optional[
        ExecutionUIService
    ] = None

    # Controlled assistant UI
    #
    # Provides conversation interface.
    # Does not provide autonomous behavior.
    assistant: Optional[
        AssistantUIService
    ] = None

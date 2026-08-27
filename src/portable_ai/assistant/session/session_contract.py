from dataclasses import (
    dataclass,
    field,
)

from portable_ai.workspace.workspace_context import (
    WorkspaceContext,
)


@dataclass
class AssistantSession:
    """
    Assistant session state contract.

    Represents current assistant state.

    Responsibilities:
        - describe session state
        - hold conversation state
        - hold assistant context
        - expose workspace context boundary
        - provide future persistence boundary

    Does not:
        - store data permanently
        - manage files
        - load documents
        - execute assistant logic
        - perform retrieval

    Session state remains in-memory.
    """

    #
    # Conversation messages.
    #
    # Managed by AssistantService.
    #
    conversation: list = field(
        default_factory=list
    )

    #
    # Assistant-specific context.
    #
    # Examples:
    #   - preferences
    #   - temporary state
    #
    context: dict = field(
        default_factory=dict
    )

    #
    # Session metadata.
    #
    # Future use:
    #   - timestamps
    #   - identifiers
    #
    metadata: dict = field(
        default_factory=dict
    )

    #
    # Workspace integration boundary.
    #
    # Does not own workspace logic.
    #
    # Future use:
    #   - documents
    #   - retrieval context
    #   - workspace intelligence
    #
    workspace: WorkspaceContext = field(
        default_factory=WorkspaceContext
    )

    #
    # Session lifecycle state.
    #
    active: bool = True

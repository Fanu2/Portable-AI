from dataclasses import dataclass, field


@dataclass
class WorkspaceContext:
    """
    Workspace context contract.

    Represents assistant-visible
    workspace information.

    Responsibilities:
        - describe workspace state
        - provide future integration boundary

    Does not:
        - load documents
        - perform retrieval
        - manage storage
        - execute tools
    """

    workspace_id: str | None = None

    active_sources: list = field(
        default_factory=list
    )

    metadata: dict = field(
        default_factory=dict
    )

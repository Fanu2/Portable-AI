from PySide6.QtWidgets import (
    QVBoxLayout,
    QWidget,
)

from portable_ai.gui.widgets.assistant.conversation_widget import (
    ConversationWidget,
)


class AssistantPanelWidget(QWidget):
    """
    Assistant UI container.

    Responsibilities:
        - compose assistant widgets
        - provide assistant UI boundary
        - expose conversation area

    Does not:
        - manage assistant logic
        - execute models
        - access providers
        - manage workspace state
    """

    def __init__(
        self,
        assistant_ui_service,
    ) -> None:

        super().__init__()

        #
        # GUI-facing assistant boundary.
        #
        self._assistant_ui = (
            assistant_ui_service
        )

        #
        # Conversation interface.
        #
        self._conversation = (
            ConversationWidget(
                assistant_ui_service
            )
        )

        layout = QVBoxLayout()

        layout.addWidget(
            self._conversation
        )

        self.setLayout(
            layout
        )

        #
        # Ensure panel remains visible
        # when composed with dashboard.
        #
        self.setMinimumHeight(
            180
        )

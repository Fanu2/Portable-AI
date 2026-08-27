from dataclasses import dataclass


@dataclass(frozen=True)
class ConversationMessage:
    """
    Immutable conversation message.

    Represents one entry in assistant history.

    Fields:
        sender:
            Origin of message.
            Examples:
                - user
                - assistant

        content:
            Message text.
    """

    sender: str

    content: str


class ConversationService:
    """
    Manages assistant conversation state.

    Responsibilities:
        - store conversation messages
        - retrieve message history
        - clear conversation state

    Boundary rules:
        - no model execution
        - no runtime selection
        - no tool access
        - no autonomous behavior

    This service only manages conversation data.
    """

    def __init__(
        self,
    ) -> None:

        # Internal conversation storage.
        #
        # Kept private so future changes
        # (database, persistence, memory)
        # do not affect callers.
        self._messages: list[
            ConversationMessage
        ] = []

    def add_message(
        self,
        sender: str,
        content: str,
    ) -> None:
        """
        Add a message to conversation history.

        Example:

            add_message(
                "user",
                "Hello",
            )
        """

        self._messages.append(
            ConversationMessage(
                sender=sender,
                content=content,
            )
        )

    def history(
        self,
    ) -> list[ConversationMessage]:
        """
        Return conversation history.

        Returns a copy to prevent external
        modification of internal state.
        """

        return list(
            self._messages
        )

    def clear(
        self,
    ) -> None:
        """
        Remove all conversation messages.

        Does not affect:
            - execution state
            - model state
            - application state
        """

        self._messages.clear()

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, init=False)
class ExecutionRequest:
    """
    Describes a model execution request.

    Supports both:
        runtime / model

    and future-friendly:
        runtime_name / model_name

    This preserves the existing execution
    boundary while allowing P4.5 model
    activation integration.
    """

    runtime: str

    model: str

    prompt: str

    capability: Optional[str]

    def __init__(
        self,
        runtime: Optional[str] = None,
        model: Optional[str] = None,
        prompt: str = "",
        capability: Optional[str] = None,
        runtime_name: Optional[str] = None,
        model_name: Optional[str] = None,
    ) -> None:

        object.__setattr__(
            self,
            "runtime",
            runtime
            or runtime_name
            or "",
        )

        object.__setattr__(
            self,
            "model",
            model
            or model_name
            or "",
        )

        object.__setattr__(
            self,
            "prompt",
            prompt,
        )

        object.__setattr__(
            self,
            "capability",
            capability,
        )

    @property
    def runtime_name(
        self,
    ) -> str:
        """
        Compatibility alias.
        """

        return self.runtime

    @property
    def model_name(
        self,
    ) -> str:
        """
        Compatibility alias.
        """

        return self.model

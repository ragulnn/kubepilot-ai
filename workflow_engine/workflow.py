from dataclasses import dataclass, field


@dataclass
class Workflow:

    # Workflow identity
    name: str

    # Resource
    type: str = ""

    target: str = ""

    namespace: str = "default"

    # Investigation
    intent: str = ""

    severity: str = "medium"

    investigation: list[str] = field(default_factory=list)

    capabilities: list[str] = field(default_factory=list)

    # Confidence
    confidence: float = 0.0

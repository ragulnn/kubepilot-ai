from dataclasses import dataclass, field


@dataclass
class AIResponse:

    success: bool

    raw: str = ""

    parsed: object = None

    verified: bool = False

    provider: str = ""

    model: str = ""

    metadata: dict = field(default_factory=dict)

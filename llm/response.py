from dataclasses import dataclass, field


@dataclass
class LLMResponse:

    success: bool

    content: str

    provider: str = ""

    model: str = ""

    tokens: int = 0

    metadata: dict = field(default_factory=dict)

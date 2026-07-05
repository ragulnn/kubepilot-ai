from dataclasses import dataclass, field


@dataclass
class PlannerRequest:

    question: str

    current_confidence: float = 0.0

    collected: list = field(default_factory=list)

    memory: list = field(default_factory=list)

    knowledge: dict = field(default_factory=dict)

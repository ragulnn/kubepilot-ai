from dataclasses import dataclass


@dataclass
class RiskResult:

    level: str

    score: float

    requires_approval: bool

from dataclasses import dataclass, field


@dataclass
class ObservationResult:

    success: bool

    health_score: float

    observations: list = field(default_factory=list)

    recommendation: str = ""

from dataclasses import dataclass, field


@dataclass
class FleetInvestigationResult:

    cluster: str

    root_cause: str

    confidence: float

    findings: list = field(default_factory=list)

    recommendations: list = field(default_factory=list)

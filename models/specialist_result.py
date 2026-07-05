from dataclasses import dataclass, field


@dataclass
class SpecialistResult:

    source: str

    summary: str

    root_cause: str

    confidence: float

    findings: list = field(default_factory=list)

    recommendations: list = field(default_factory=list)

    metadata: dict = field(default_factory=dict)

from dataclasses import dataclass, field


@dataclass
class InvestigationReport:

    root_cause: str

    confidence: float

    evidence: list[str] = field(

        default_factory=list

    )

    recommended_fix: list[str] = field(

        default_factory=list

    )

    sources: list[str] = field(

        default_factory=list

    )

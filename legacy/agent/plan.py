from dataclasses import dataclass


@dataclass
class InvestigationPlan:

    target_type: str

    target_name: str

    namespace: str = "default"

    confidence: float = 1.0

from dataclasses import dataclass


@dataclass
class PlannerResponse:

    next_step: str

    reason: str

    confidence: float

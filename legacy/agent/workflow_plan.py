from dataclasses import dataclass


@dataclass
class WorkflowPlan:

    workflow: str

    target: str

    namespace: str = "default"

    confidence: float = 1.0

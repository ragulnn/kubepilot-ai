from dataclasses import dataclass, field


@dataclass
class RemediationAction:

    action: str

    resource_type: str

    resource_name: str

    namespace: str

    parameters: dict = field(default_factory=dict)

    reason: str = ""

    confidence: float = 0.0

from dataclasses import dataclass, field

from remediation_engine.action import RemediationAction


@dataclass
class RemediationResponse:

    actions: list[RemediationAction] = field(default_factory=list)

    reasoning: str = ""

    risk: str = "LOW"

    requires_approval: bool = True

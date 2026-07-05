import uuid
from dataclasses import dataclass, field


@dataclass
class Incident:

    id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    question: str = ""

    resource_name: str = ""

    namespace: str = "default"

    root_cause: str = ""

    confidence: float = 0.0

    findings: list = field(default_factory=list)

    recommendations: list = field(default_factory=list)

    timestamp: str = ""

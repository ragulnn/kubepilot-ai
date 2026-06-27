from dataclasses import dataclass, field


@dataclass
class AgentRequest:

    cluster: str

    request_id: str

    user: str

    evidence_type: str

    namespace: str | None = None

    resource: str | None = None

    keyword: str | None = None

    labels: dict = field(default_factory=dict)

    filters: dict = field(default_factory=dict)

    options: dict = field(default_factory=dict)

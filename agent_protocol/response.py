from dataclasses import dataclass, field


@dataclass
class AgentResponse:

    request_id: str

    cluster: str

    success: bool

    connector: str

    evidence: list = field(default_factory=list)

    message: str = ""

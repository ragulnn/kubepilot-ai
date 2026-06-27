from dataclasses import dataclass, field


@dataclass
class AgentCapabilities:

    cluster: str

    kubernetes: bool = True

    prometheus: bool = False

    opentelemetry: bool = False

    elasticsearch: bool = False

    jaeger: bool = False

    supported: list = field(default_factory=list)

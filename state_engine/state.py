from dataclasses import dataclass, field


@dataclass
class ClusterState:

    pods: dict = field(default_factory=dict)

    deployments: dict = field(default_factory=dict)

    services: dict = field(default_factory=dict)

    nodes: dict = field(default_factory=dict)

    events: list = field(default_factory=list)

    timestamp: str = ""

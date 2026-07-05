from dataclasses import dataclass, field


@dataclass
class ClusterInventory:

    pods: int = 0

    deployments: int = 0

    services: int = 0

    nodes: int = 0

    namespaces: set = field(default_factory=set)

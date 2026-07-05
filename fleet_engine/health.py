from dataclasses import dataclass, field


@dataclass
class FleetHealth:

    score: float

    healthy_clusters: int

    unhealthy_clusters: int

    total_clusters: int

    critical_clusters: list = field(default_factory=list)

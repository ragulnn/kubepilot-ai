from dataclasses import dataclass


@dataclass
class AgentHeartbeat:

    cluster: str

    version: str

    healthy: bool

    cpu_usage: float

    memory_usage: float

    active_requests: int

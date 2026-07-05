from dataclasses import dataclass


@dataclass
class ClusterEvent:

    type: str

    resource: str

    namespace: str

    reason: str

    message: str

    timestamp: str

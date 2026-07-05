from dataclasses import dataclass


@dataclass
class Cluster:

    name: str

    provider: str

    context: str

    environment: str

    active: bool = False

from dataclasses import dataclass


@dataclass
class Cluster:

    name: str

    provider: str

    environment: str

    kubeconfig_context: str

    enabled: bool = True

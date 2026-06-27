from connectors.registry import ConnectorRegistry

from connectors.kubernetes.connector import (
    KubernetesConnector,
)

registry = ConnectorRegistry()

registry.register(
    KubernetesConnector()
)

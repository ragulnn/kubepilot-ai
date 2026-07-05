from connectors.registry import ConnectorRegistry

from connectors.kubernetes.connector import KubernetesConnector
from connectors.prometheus.connector import PrometheusConnector
from connectors.loki.connector import LokiConnector
from connectors.tempo.connector import TempoConnector

registry = ConnectorRegistry()

# Kubernetes
registry.register(
    KubernetesConnector()
)

# Prometheus
registry.register(
    PrometheusConnector()
)

# Loki
registry.register(
    LokiConnector()
)

# Tempo
registry.register(
    TempoConnector()
)

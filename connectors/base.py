from abc import ABC, abstractmethod

from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse


class Connector(ABC):
    """
    Base class for every external data source.

    Examples:
        Kubernetes
        Prometheus
        Elasticsearch
        Jaeger
    """

    name = ""

    capabilities = []

    @abstractmethod
    def connect(self) -> bool:
        """
        Initialize connection to backend.
        """
        pass

    @abstractmethod
    def healthy(self) -> bool:
        """
        Returns True if backend is healthy.
        """
        pass

    @abstractmethod
    def collect(
        self,
        request: EvidenceRequest,
    ) -> EvidenceResponse:
        """
        Collect evidence.
        """
        pass

from connectors.default_registry import registry
from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse


class EvidenceCollector:

    def collect(
        self,
        request: EvidenceRequest,
    ) -> EvidenceResponse:

        return registry.collect(request)

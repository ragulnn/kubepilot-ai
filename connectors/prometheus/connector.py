from connectors.base import Connector
from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse

from providers.registry import TOOLS
from connectors.prometheus.health import prometheus_healthy

class PrometheusConnector(Connector):

    name = "prometheus"

    capabilities = [
        "metrics",
        "cpu",
        "memory",
        "network",
        "filesystem",
        "restarts",
    ]

    def connect(self):
        return True
    
    def healthy(self):

       return prometheus_healthy()
    
    def collect(
        self,
        request: EvidenceRequest,
    ) -> EvidenceResponse:

        tool = TOOLS["metrics"]

        metric = request.metric or "cpu"

        evidence = tool.run(

            name=request.name,

            metric=metric,

        )

        return EvidenceResponse(

            source=self.name,

            success=True,

            evidence=[evidence],

            message=f"{metric} collected successfully",

        )

from connectors.base import Connector
from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse

from providers.registry import TOOLS

from connectors.loki.health import loki_healthy


class LokiConnector(Connector):

    name = "loki"

    capabilities = [

        "logs",

        "errors",

        "warnings",

        "exceptions",

    ]

    def connect(self):

        return True

    def healthy(self):

        return loki_healthy()

    def collect(

        self,

        request: EvidenceRequest,

    ) -> EvidenceResponse:

        tool = TOOLS["loki"]

        logs = tool.run(

            resource=request.kind,

            name=request.name,

            namespace=request.namespace,

        )

        return EvidenceResponse(

            request=request,

            source=self.name,

            success=True,

            evidence=logs,

            message="Logs collected successfully.",

        )

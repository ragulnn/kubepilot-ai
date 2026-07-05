from connectors.base import Connector
from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse

from providers.registry import TOOLS
from connectors.tempo.health import tempo_healthy


class TempoConnector(Connector):

    name = "tempo"

    capabilities = [
        "traces",
        "trace",
        "spans",
    ]

    def connect(self):
        return True

    def healthy(self):
        return tempo_healthy()

    def collect(
        self,
        request: EvidenceRequest,
    ) -> EvidenceResponse:

        tool = TOOLS["tempo"]

        if request.trace_id:

            traces = tool.run(
                trace_id=request.trace_id,
            )

        else:

            traces = tool.run()

        return EvidenceResponse(
            request=request,
            source=self.name,
            success=True,
            evidence=traces,
            message="traces collected successfully",
        )

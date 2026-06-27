from connectors.base import Connector
from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse


class ConnectorRegistry:

    def __init__(self):

        self.connectors = []

    def register(
        self,
        connector: Connector,
    ):

        self.connectors.append(connector)

    def connector_for(
        self,
        evidence_type: str,
    ):

        for connector in self.connectors:

            if evidence_type in connector.capabilities:

                return connector

        return None

    def collect(
        self,
        request: EvidenceRequest,
    ) -> EvidenceResponse:

        connector = self.connector_for(
            request.type
        )

        if connector is None:

            return EvidenceResponse(

                source="registry",

                success=False,

                message=f"No connector supports '{request.type}'",

            )

        return connector.collect(request)

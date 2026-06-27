from connectors.base import Connector
from connectors.request import EvidenceRequest
from connectors.response import EvidenceResponse

from providers.registry import TOOLS
from connectors.kubernetes.health import cluster_healthy

class KubernetesConnector(Connector):

    name = "kubernetes"

    capabilities = [

        "pods",
        "deployments",
        "services",
        "events",
        "logs",
        "describe",
        "nodes",
        "namespaces",
        "configmap",
        "secret",
        "pv",
        "pvc",
        "ingress",

    ]

    def connect(self):

        return True

    def healthy(self):

        return cluster_healthy()
    def collect(
        self,
        request: EvidenceRequest,
    ) -> EvidenceResponse:

        tool_name = request.type

        if tool_name not in TOOLS:

            return EvidenceResponse(

                source=self.name,

                success=False,

                message=f"Unknown tool: {tool_name}",

            )

        tool = TOOLS[tool_name]

        output = tool.run(

            namespace=request.namespace,

            resource=request.resource,

        )

        return EvidenceResponse(

            source=self.name,

            success=True,

            evidence=[output],

        )

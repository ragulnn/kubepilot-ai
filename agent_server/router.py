from connectors.request import EvidenceRequest


class RequestRouter:

    def __init__(self, registry):

        self.registry = registry

    def handle(self, request):

        evidence = EvidenceRequest(

            cluster=request.cluster,

            type=request.evidence_type,

            namespace=request.namespace,

            resource=request.resource,

            keyword=request.keyword,

            labels=request.labels,

            filters=request.filters,

        )

        return self.registry.collect(
            evidence
        )

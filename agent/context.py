from connectors.default_registry import registry
from connectors.request import EvidenceRequest


class ClusterContext:

    def load(self):

        namespaces = registry.collect(
            EvidenceRequest(type="namespaces")
        )

        pods = registry.collect(
            EvidenceRequest(type="pods")
        )

        services = registry.collect(
            EvidenceRequest(type="services")
        )

        return {

            "namespaces": namespaces.evidence[0]
            if namespaces.success and namespaces.evidence
            else "",

            "pods": pods.evidence[0]
            if pods.success and pods.evidence
            else "",

            "services": services.evidence[0]
            if services.success and services.evidence
            else "",

        }

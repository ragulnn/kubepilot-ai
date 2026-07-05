from agent.context_cache import cache

from connectors.default_registry import registry
from connectors.request import EvidenceRequest


class ClusterContext:

    def load(self):

        if cache.valid():

            print("Using cached cluster context")

            return cache.get()

        print("Refreshing cluster context")

        namespaces = registry.collect(
            EvidenceRequest(type="namespaces")
        )

        pods = registry.collect(
            EvidenceRequest(type="pods")
        )

        services = registry.collect(
            EvidenceRequest(type="services")
        )

        data = {

            "namespaces": (
                namespaces.evidence[0]
                if namespaces.success and namespaces.evidence
                else ""
            ),

            "pods": (
                pods.evidence[0]
                if pods.success and pods.evidence
                else ""
            ),

            "services": (
                services.evidence[0]
                if services.success and services.evidence
                else ""
            ),

        }

        cache.set(data)

        return data

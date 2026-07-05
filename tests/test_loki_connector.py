from connectors.default_registry import registry

from connectors.request import EvidenceRequest

response = registry.collect(

    EvidenceRequest(

        type="errors",

        namespace="monitoring",

    )

)

print()

print(response.source)

print(response.success)

print(response.message)

print(len(response.evidence))

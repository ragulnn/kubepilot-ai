from connectors.request import EvidenceRequest

from connectors.default_registry import registry

request = EvidenceRequest(
    type="pods",
)

response = registry.collect(
    request
)

print()

print("Source")

print(response.source)

print()

print("Success")

print(response.success)

print()

print("Evidence")

print(response.evidence)

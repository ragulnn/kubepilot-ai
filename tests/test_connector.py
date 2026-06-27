from connectors.kubernetes.connector import KubernetesConnector
from connectors.request import EvidenceRequest


connector = KubernetesConnector()

request = EvidenceRequest(

    type="pods",

)

response = connector.collect(request)

print()

print("Source")

print(response.source)

print()

print("Success")

print(response.success)

print()

print("Evidence")

print(response.evidence)

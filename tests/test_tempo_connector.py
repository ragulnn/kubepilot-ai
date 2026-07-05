import providers

from connectors.tempo.connector import TempoConnector
from connectors.request import EvidenceRequest

print("=" * 60)
print("Tempo Connector")
print("=" * 60)

connector = TempoConnector()

trace_id = input(
    "Trace ID (leave empty to search): "
).strip()

if trace_id:

    request = EvidenceRequest(

        type="traces",

        trace_id=trace_id,

    )

else:

    request = EvidenceRequest(

        type="traces",

    )

response = connector.collect(

    request

)

print()

print("Success :", response.success)

print("Source  :", response.source)

print("Message :", response.message)

print()

print("Evidence")

print("-" * 40)

for item in response.evidence:

    print(item)

from connectors.prometheus.connector import PrometheusConnector
from connectors.request import EvidenceRequest

connector = PrometheusConnector()

response = connector.collect(

    EvidenceRequest(

        type="metrics",

        name="nginx-7f8fbb96d-pt7cq",

        metric="cpu",

    )

)

print(response.source)
print(response.success)
print(response.message)
print(response.evidence)

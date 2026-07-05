from prometheus.client import PrometheusClient


client = PrometheusClient()

result = client.query("up")

print(result)

from loki.client import LokiClient
from loki import queries

client = LokiClient()

logs = client.query(

    queries.NAMESPACE_LOGS % "monitoring"

)

print()

print("Logs Found:", len(logs))

for log in logs[:5]:

    print(log)						

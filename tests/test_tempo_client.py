from tempo.client import TempoClient

print("=" * 60)
print("Tempo Client")
print("=" * 60)

client = TempoClient()

trace_id = input("Trace ID: ").strip()

result = client.trace(trace_id)

print(result)

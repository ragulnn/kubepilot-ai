from tempo.client import TempoClient

print("=" * 60)
print("Tempo Search Parser")
print("=" * 60)

client = TempoClient()

results = client.search()

print(f"Found {len(results)} traces\n")

for trace in results:

    print(trace)

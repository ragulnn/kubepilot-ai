from tempo.client import TempoClient

print("=" * 60)
print("Tempo Search")
print("=" * 60)

client = TempoClient()

result = client.search()

print(result)

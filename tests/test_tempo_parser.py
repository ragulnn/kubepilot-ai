from tempo.parser import TempoParser

parser = TempoParser()

print("=" * 60)
print("Tempo Parser")
print("=" * 60)

result = parser.parse({})

print(result)

assert result == []

print("\n✅ Parser test passed.")

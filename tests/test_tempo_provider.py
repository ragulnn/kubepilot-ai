from providers.registry import TOOLS

print("=" * 60)
print("Tempo Provider")
print("=" * 60)

tool = TOOLS["tempo"]

trace_id = input("Trace ID: ").strip()

result = tool.run(trace_id=trace_id)

print(result)

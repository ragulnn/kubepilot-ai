from tempo.models import Trace

trace = Trace(
    trace_id="123",
    span_id="456",
    parent_span_id=None,
    name="homepage",
    kind="SPAN_KIND_INTERNAL",
    start_time="100",
    end_time="200",
    status={},
    service="kubepilot-demo",
)

print("=" * 60)
print("Tempo Model")
print("=" * 60)

print(trace)

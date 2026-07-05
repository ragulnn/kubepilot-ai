from analysis_engine.correlation import CorrelationEngine
from analysis_engine.evidence import Evidence

engine = CorrelationEngine()

evidence = [

    Evidence(
        source="prometheus",
        category="metrics",
        name="memory",
        value=0.98,
    ),

    Evidence(
        source="prometheus",
        category="metrics",
        name="restarts",
        value=8,
    ),

    Evidence(
        source="loki",
        category="logs",
        name="logs",
        value="OOMKilled",
    ),

    Evidence(
        source="tempo",
        category="trace",
        name="traces",
        value="Exception",
    ),

]

result = engine.correlate(evidence)

print("=" * 60)
print("Correlation Engine")
print("=" * 60)

for item in result:

    print(item)

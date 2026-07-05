from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.schemas.analyzer import ANALYZER_SCHEMA

print("=" * 60)
print("AI Engine")
print("=" * 60)

engine = AIEngine()

request = AIRequest(

    prompt="""
Analyze the Kubernetes evidence and identify the most likely root cause.
""",

    schema=ANALYZER_SCHEMA,

    evidence="""
Memory Usage: 98%
Restart Count: 8
Logs: OOMKilled
Trace: PaymentService Exception
""",
)

response = engine.analyze(request)

print()

print("Raw Response")
print("-" * 40)
print(response.raw)

print()

print("Parsed Response")
print("-" * 40)
print(response.parsed)

print()

print("Verified :", response.verified)

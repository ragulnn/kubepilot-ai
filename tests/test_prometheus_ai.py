from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import PROMETHEUS_PROMPT
from llm.schemas.prometheus import PROMETHEUS_SCHEMA

print("=" * 60)
print("Prometheus AI")
print("=" * 60)

engine = AIEngine()

request = AIRequest(

    prompt=PROMETHEUS_PROMPT,

    schema=PROMETHEUS_SCHEMA,

    evidence="""
CPU : 18%
Memory : 98%
Restart Count : 8
""",

)

response = engine.analyze(request)

print()
print(response.parsed)

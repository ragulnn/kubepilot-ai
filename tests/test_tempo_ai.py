from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import TEMPO_PROMPT
from llm.schemas.tempo import TEMPO_SCHEMA

print("=" * 60)
print("Tempo AI")
print("=" * 60)

engine = AIEngine()

response = engine.analyze(

    AIRequest(

        prompt=TEMPO_PROMPT,

        schema=TEMPO_SCHEMA,

        evidence="""
Service : payment-service
Span : ProcessPayment
Latency : 2450ms
Exception : java.lang.OutOfMemoryError
""",

    )

)

print()
print(response.parsed)

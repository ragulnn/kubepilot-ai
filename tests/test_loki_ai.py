from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import LOKI_PROMPT
from llm.schemas.loki import LOKI_SCHEMA

print("=" * 60)
print("Loki AI")
print("=" * 60)

engine = AIEngine()

response = engine.analyze(

    AIRequest(

        prompt=LOKI_PROMPT,

        schema=LOKI_SCHEMA,

        evidence="""
OOMKilled
CrashLoopBackOff
java.lang.OutOfMemoryError
""",

    )

)

print()

print(response.parsed)


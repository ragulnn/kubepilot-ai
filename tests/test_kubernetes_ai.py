from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import KUBERNETES_PROMPT
from llm.schemas.kubernetes import KUBERNETES_SCHEMA

print("=" * 60)
print("Kubernetes AI")
print("=" * 60)

engine = AIEngine()

response = engine.analyze(

    AIRequest(

        prompt=KUBERNETES_PROMPT,

        schema=KUBERNETES_SCHEMA,

        evidence="""
Pod Status : CrashLoopBackOff
Event : OOMKilled
Ready : False
Restarts : 8
""",

    )

)

print(response.parsed)

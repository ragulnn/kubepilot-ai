from analysis_engine.evidence import Evidence
from llm.verifier import DiagnosisVerifier

evidence = [

    Evidence(

        source="kubernetes",

        category="logs",

        name="logs",

        value="OOMKilled",

    ),

    Evidence(

        source="prometheus",

        category="metric",

        name="memory",

        value=0.98,

    ),

    Evidence(

        source="prometheus",

        category="metric",

        name="restarts",

        value=12,

    ),

]

response = DiagnosisVerifier().verify(

    question="Why is nginx restarting?",

    evidence=evidence,

    diagnosis="Memory Exhaustion",

    confidence=0.90,

)

print(response)

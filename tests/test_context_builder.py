from analysis_engine.evidence import Evidence

from context_engine.builder import InvestigationContextBuilder

builder = InvestigationContextBuilder()

context = builder.build(

    question="Why is nginx restarting?",

    evidence=[

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

    ],

    diagnosis={

        "root_cause":"Memory Exhaustion",

        "confidence":0.90,

    }

)

print(context)

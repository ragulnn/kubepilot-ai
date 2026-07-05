from evidence_engine.dispatcher import EvidenceDispatcher
from evidence_engine.response_builder import (
    EvidenceResponseBuilder,
)

dispatcher = EvidenceDispatcher()

responses = dispatcher.collect(

    requests=[

        {
            "type": "pods",
            "namespace": "default",
        }

    ],

)
builder = EvidenceResponseBuilder()

report = builder.build(

    "Show nginx pods",

    responses,

)

print(report)

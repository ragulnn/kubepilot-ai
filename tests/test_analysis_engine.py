from connectors.response import EvidenceResponse

from analysis_engine.normalizer import EvidenceNormalizer
from analysis_engine.analyzer import Analyzer


responses = [

    EvidenceResponse(

        source="kubernetes",

        success=True,

        message="logs",

        evidence=[

            "OOMKilled"

        ],

    ),

    EvidenceResponse(

        source="prometheus",

        success=True,

        message="memory",

        evidence=[

            0.98

        ],

    ),

    EvidenceResponse(

        source="prometheus",

        success=True,

        message="restarts",

        evidence=[

            12

        ],

    ),

]
normalizer = EvidenceNormalizer()

evidence = normalizer.normalize(responses)

result = Analyzer().analyze(evidence)

print()

print("Evidence")

for item in evidence:

    print(item)

print()

print("Analysis")

print(result)

from aggregation_engine.aggregator import SpecialistAggregator
from models.specialist_result import SpecialistResult

results = [

    SpecialistResult(

        source="prometheus",

        summary="Memory pressure",

        root_cause="Memory Exhaustion",

        confidence=0.95,

        findings=["Memory 98%"],

        recommendations=["Increase memory"],

    ),

    SpecialistResult(

        source="loki",

        summary="OOMKilled",

        root_cause="Memory Exhaustion",

        confidence=0.92,

        findings=["OOMKilled"],

        recommendations=["Investigate memory leak"],

    ),

]

aggregator = SpecialistAggregator()

print(

    aggregator.aggregate(results)

)

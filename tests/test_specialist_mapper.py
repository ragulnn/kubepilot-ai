from models.mapper import SpecialistMapper

mapper = SpecialistMapper()

prometheus = {

    "critical_metrics": [

        "Memory 98%",

        "Restart Count 8",

    ],

    "summary": "Memory pressure",

    "root_cause": "Memory Exhaustion",

    "confidence": 0.95,

    "recommendations": [

        "Increase memory",

    ],

}

result = mapper.from_prometheus(

    prometheus

)

print(result)

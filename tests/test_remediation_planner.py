from remediation_engine.planner import RemediationPlanner
from remediation_engine.request import RemediationRequest

planner = RemediationPlanner()

request = RemediationRequest(

    analysis={

        "root_cause":"Memory Exhaustion",

        "confidence":0.96,

        "critical_evidence":[

            "Memory 98%",

            "OOMKilled",

            "Restart Count 8",

        ],

    },

    verification={

        "verified":True,

    },

    memory=[

        {

            "root_cause":"Memory Exhaustion",

            "recommended_fix":"Increase memory",

        }

    ],

    knowledge={

        "Memory Exhaustion":42,

    },

)

response = planner.plan(

    request

)

print(response)

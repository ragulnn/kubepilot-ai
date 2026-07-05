from planner_ai.planner import AIInvestigationPlanner
from planner_ai.request import PlannerRequest

planner = AIInvestigationPlanner()

request = PlannerRequest(

    question="Why is nginx restarting?",

    current_confidence=0.42,

    collected=[

        "kubernetes",

    ],

    memory=[

        {

            "root_cause":"Memory Exhaustion"

        }

    ],

    knowledge={

        "Memory Exhaustion":12

    },

)

result = planner.plan(

    request

)

print(result)

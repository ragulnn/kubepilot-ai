from agent.planner import Planner

planner = Planner()

result = planner.next_action(
    question="Show all pods",
    observations=[],
    history="",
    resources={
        "pods": [],
        "deployments": [],
        "nodes": [],
        "services": [],
    },
    context={},
    investigation=None,
)

print(result)

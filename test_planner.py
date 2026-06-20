from agent.planner import Planner

planner = Planner()

plan = planner.create_plan(
    "Show me all pods and services"
)

print(plan)

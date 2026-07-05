from agent.resource_planner import ResourcePlanner

planner = ResourcePlanner()

plan = planner.plan(

    "Why is nginx failing?"

)

print(plan)

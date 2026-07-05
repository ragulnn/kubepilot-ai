from agent.resource_planner import ResourcePlanner
from expansion_engine.automatic_expander import AutomaticExpander

planner = ResourcePlanner()

plan = planner.plan(

    "Why is nginx failing?"

)

requests = AutomaticExpander().expand(plan)

for r in requests:

    print(r)

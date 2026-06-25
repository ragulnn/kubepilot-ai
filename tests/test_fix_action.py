from agent.planner import Planner

planner = Planner()

action = {
    "tool": "logs"
}

fixed = planner.fix_action(
    action,
    "Missing fields: namespace, pod"
)

print(fixed)

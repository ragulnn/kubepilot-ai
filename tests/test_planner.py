from agent.planner import Planner

planner = Planner()

question = "Show all pods"

observations = []

result = planner.next_action(
    question,
    observations
)

print("=" * 50)
print("Planner Output")
print("=" * 50)
print(result)

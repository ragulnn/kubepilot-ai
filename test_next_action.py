from agent.planner import Planner

planner = Planner()

question = "Why is my nginx pod restarting?"

observations = []

result = planner.next_action(
    question,
    observations
)

print("=" * 50)
print("Planner Output")
print("=" * 50)
print(result)

from agent.planner import Planner

planner = Planner()

question = input("Question: ")

plan = planner.plan(question)

print("\nReturned object:\n")
print(plan)

print("\nType:")
print(type(plan))

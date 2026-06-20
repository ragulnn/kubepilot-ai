import tools.pods
import tools.services
import tools.namespaces

from agent.executor import Executor
from agent.planner import Planner

planner = Planner()
executor = Executor()

question = input("Question: ")

plan = planner.create_plan(question)

print("\nExecution Plan")

print(plan)

for tool in plan:

    print("=" * 60)
    print(tool)
    print("=" * 60)

    try:
        print(executor.execute(tool))
    except Exception as e:
        print(e)

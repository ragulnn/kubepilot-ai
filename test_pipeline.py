import tools.pods
import tools.services

from agent.planner import Planner
from agent.executor import Executor

planner = Planner()
executor = Executor()

question = "Show me pods and services"

plan = planner.create_plan(question)

print("Plan")

print(plan)

for tool in plan:

    print("=" * 50)

    print(tool)

    print("=" * 50)

    print(executor.execute(tool))

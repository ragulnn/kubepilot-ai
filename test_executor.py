import tools.pods

from agent.executor import Executor

executor = Executor()

action = {
    "tool":"pods"
}

result = executor.execute(action)

print(result)

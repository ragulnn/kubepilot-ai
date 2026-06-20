from agent.planner import Planner
from agent.executor import Executor
from agent.analyzer import Analyzer
from agent.memory import Memory


class KubernetesAgent:

    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.analyzer = Analyzer()
        self.memory = Memory()

    def investigate(self, question):

        plan = self.planner.plan(question)

        print("\nExecution Plan\n")
        print(plan)

        for action in plan["actions"]:

            print(f"\nExecuting: {action}")

            try:
                result = self.executor.execute(action)
                self.memory.add(action, result)

            except Exception as e:
                self.memory.add(action, str(e))

        return self.analyzer.analyze(
            question,
            self.memory.all()
        )

import time

from agent.context import ClusterContext
from agent.planner import Planner
from agent.executor import Executor
from agent.analyzer import Analyzer
from utils.logger import Timer

planner = Planner()
executor = Executor()
analyzer = Analyzer()


def planner_node(state):

    with Timer("Planner Node"):

        print(f"Question : {state['question']}")

        print("\nLoading cluster context...")

        context = ClusterContext().load()

        print("✅ Context Loaded")

        action = planner.next_action(
            state["question"],
            state["observations"],
            context
        )

        print("\nPlanner Decision")

        print(action)

        return {
            "current_action": action
        }


def executor_node(state):

    with Timer("Executor Node"):

        action = state["current_action"]

        print(f"Executing : {action}")

        result = executor.execute(action)

        observation = {
            "step": len(state["observations"]) + 1,
            "tool": action["tool"],
            "result": result
        }

        observations = state["observations"] + [observation]

        print("✅ Tool Executed")

        return {
            "observations": observations
        }


def analyzer_node(state):

    with Timer("Analyzer Node"):

        print("Analyzing observations...")

        answer = analyzer.analyze(
            state["question"],
            state["observations"]
        )

        print("✅ Investigation Completed")

        return {
            "answer": answer
        }

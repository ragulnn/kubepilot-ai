from agent.planner import Planner
from agent.executor import Executor
from agent.analyzer import Analyzer

planner = Planner()
executor = Executor()
analyzer = Analyzer()


def planner_node(state):
    print("\n📋 Planner Node")

    action = planner.next_action(
        state["question"],
        state["observations"]
    )

    print(action)

    return {
        "current_action": action
    }


def executor_node(state):
    print("\n⚙️ Executor Node")

    action = state["current_action"]

    print(f"Running: {action}")

    result = executor.execute(action)

    observations = state["observations"] + [
        {
            "tool": action["tool"],
            "result": result
        }
    ]

    return {
        "observations": observations
    }


def analyzer_node(state):
    print("\n🧠 Analyzer Node")

    answer = analyzer.analyze(
        state["question"],
        state["observations"]
    )

    return {
        "answer": answer
    }

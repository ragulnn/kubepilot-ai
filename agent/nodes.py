from agent.planner import Planner
from agent.executor import Executor
from agent.analyzer import Analyzer

planner = Planner()
executor = Executor()
analyzer = Analyzer()


def planner_node(state):
    print("\n📋 Planner Node")

    plan = planner.plan(state["question"])

    print(plan)

    return {
        "actions": plan["actions"]
    }

def executor_node(state):
    print("\n⚙️ Executor Node")

    observations = []

    for action in state["actions"]:
        print(f"Running: {action}")

        result = executor.execute(action)

        observations.append({
            "action": action,
            "result": result
        })

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

import tools.pods
import tools.services
import tools.events
import tools.nodes
import tools.namespaces

from agent.graph import graph

result = graph.invoke(
    {
        "question": "Show all pods",
        "actions": [],
        "observations": [],
        "current_action": None,
        "answer": "",
        "finished": False,
    }
)

print("\n========================")
print("FINAL ANSWER")
print("========================\n")

print(result["answer"])

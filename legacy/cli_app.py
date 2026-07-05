from agent.router import Router
from agent.graph import graph
from agent.executor import Executor
from tools.pods import get_pods
from tools.logs import get_logs
from tools.describe import describe_pod
from tools.events import get_events
from tools.nodes import get_nodes
from tools.services import get_services
from tools.troubleshoot import troubleshoot_pod

from tools.deployments import get_deployments
from tools.ingress import get_ingress
from tools.configmap import get_configmaps
from tools.secrets import get_secrets
from tools.namespaces import get_namespaces
from tools.pvc import get_pvc
from tools.pv import get_pv

from agent.ai import analyze_cluster

    router = Router() 
    executor = Executor()

def print_menu():
    print("\n" + "=" * 60)
    print("🤖 KubePilot AI")
    print("=" * 60)
    print("1.  List Pods")
    print("2.  View Pod Logs")
    print("3.  Describe Pod")
    print("4.  View Events")
    print("5.  List Nodes")
    print("6.  List Services")
    print("7.  List Deployments")
    print("8.  List Ingress")
    print("9.  List ConfigMaps")
    print("10. List Secrets")
    print("11. List Persistent Volume Claims")
    print("12. List Persistent Volumes")
    print("13. List Namespaces")
    print("14. AI Troubleshoot Pod")
    print("15. Exit")
    print("=" * 60)


def main():

      while True:

    print("\n==============================")
    print("🤖 KubePilot AI")
    print("==============================")

    question = input("\nAsk a Kubernetes question: ")

    if question.lower() == "exit":
        break

    intent = router.route(question)

    print(f"\nDetected Intent: {intent}")

    if intent == "information":

        tool = question.split()[-1]

        print("\nRunning Tool...\n")

        try:
            print(executor.execute({"tool": tool}))
        except Exception:
            print("Unknown tool.")

    elif intent == "investigation":

        result = graph.invoke(
            {
                "question": question,
                "actions": [],
                "observations": [],
                "current_action": None,
                "answer": "",
                "finished": False,
            }
        )

        print("\nAI Diagnosis\n")
        print(result["answer"])

    elif intent == "action":

        print("\n⚠️ Destructive operations are not enabled yet.")
        print("Approval workflow will be added in Phase 8.")

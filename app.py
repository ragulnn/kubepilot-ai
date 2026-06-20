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

        print_menu()

        choice = input("\nChoose an option: ")

        if choice == "1":
            print(get_pods())

        elif choice == "2":
            namespace = input("Namespace: ")
            pod = input("Pod Name: ")
            print(get_logs(pod, namespace))

        elif choice == "3":
            namespace = input("Namespace: ")
            pod = input("Pod Name: ")
            print(describe_pod(pod, namespace))

        elif choice == "4":
            print(get_events())

        elif choice == "5":
            print(get_nodes())

        elif choice == "6":
            print(get_services())

        elif choice == "7":
            print(get_deployments())

        elif choice == "8":
            print(get_ingress())

        elif choice == "9":
            print(get_configmaps())

        elif choice == "10":
            print(get_secrets())

        elif choice == "11":
            print(get_pvc())

        elif choice == "12":
            print(get_pv())

        elif choice == "13":
            print(get_namespaces())

        elif choice == "14":

            namespace = input("Namespace: ")
            pod = input("Pod Name: ")

            print("\nCollecting Kubernetes information...\n")

            report = troubleshoot_pod(pod, namespace)

            print("Analyzing with AI...\n")

            result = analyze_cluster(report)

            print(result)

        elif choice == "15":

            print("\nGoodbye 👋")

            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()

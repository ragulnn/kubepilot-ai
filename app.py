from tools.pods import get_pods
from tools.logs import get_logs
from tools.describe import describe_pod
from tools.events import get_events
from tools.nodes import get_nodes
from tools.services import get_services


def menu():
    while True:
        print("\n" + "=" * 50)
        print("🤖 KubePilot AI")
        print("=" * 50)
        print("1. List Pods")
        print("2. View Pod Logs")
        print("3. Describe Pod")
        print("4. View Events")
        print("5. List Nodes")
        print("6. List Services")
        print("7. Exit")

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
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    menu()

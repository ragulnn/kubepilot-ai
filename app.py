from kubernetes import config

from state_engine.manager import StateManager
from inventory_engine.manager import InventoryManager
from inventory_engine.summary import InventorySummary
from cli.controller import CLIController


def initialize():

    print("=" * 60)
    print("Kubepilot AI")
    print("=" * 60)

    config.load_kube_config()

    state_manager = StateManager()

    state = state_manager.refresh()

    inventory = InventoryManager().build(state)

    summary = InventorySummary().summarize(inventory)

    print()
    print("Cluster Connected")
    print("--------------------")
    print(summary)

    return state_manager


def main():

    initialize()

    CLIController().run()


if __name__ == "__main__":

    main()

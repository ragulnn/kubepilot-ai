from inventory_engine.inventory import ClusterInventory


class InventoryManager:

    def build(self, state):

        inventory = ClusterInventory()

        inventory.pods = len(state.pods)

        inventory.deployments = len(state.deployments)

        inventory.services = len(state.services)

        inventory.nodes = len(state.nodes)

        for pod in state.pods.values():

            inventory.namespaces.add(

                pod["namespace"]

            )

        return inventory

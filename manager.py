from collections import Counter

from inventory_engine.inventory import ClusterInventory


class InventoryManager:

    def build(self, state):

        inventory = ClusterInventory()

        inventory.pods = len(state.pods)

        inventory.deployments = len(state.deployments)

        inventory.services = len(state.services)

        inventory.nodes = len(state.nodes)

        phases = Counter()

        for pod in state.pods.values():

            inventory.namespaces.add(

                pod["namespace"]

            )

            phases[pod["phase"]] += 1

        inventory.pod_status = dict(phases)

        return inventory

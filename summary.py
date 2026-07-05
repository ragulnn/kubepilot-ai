class InventorySummary:

    def summarize(self, inventory):

        return {

            "pods": inventory.pods,

            "deployments": inventory.deployments,

            "services": inventory.services,

            "nodes": inventory.nodes,

            "namespaces": sorted(

                list(inventory.namespaces)

            ),

            "pod_status": inventory.pod_status,

        }

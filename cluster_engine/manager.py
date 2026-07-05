from cluster_engine.cluster import Cluster
from cluster_engine.registry import ClusterRegistry


class ClusterManager:

    def __init__(self):

        self.registry = ClusterRegistry()

    def load_default_clusters(self):

        self.registry.register(

            Cluster(

                name="kind",

                provider="Kind",

                environment="development",

                kubeconfig_context="kind",

            )

        )

        self.registry.register(

            Cluster(

                name="aks",

                provider="Azure",

                environment="staging",

                kubeconfig_context="aks",

            )

        )

        self.registry.register(

            Cluster(

                name="eks",

                provider="AWS",

                environment="production",

                kubeconfig_context="eks",

            )

        )

    def list_clusters(self):

        return self.registry.all()

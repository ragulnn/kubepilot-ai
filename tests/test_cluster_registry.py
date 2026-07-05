from fleet.cluster import Cluster
from fleet.manager import FleetManager

manager = FleetManager()

manager.register(

    Cluster(

        name="kind",

        provider="Kind",

        context="kind-kubernetes-demo-cluster",

        environment="development",

    )

)

manager.register(

    Cluster(

        name="aks",

        provider="Azure",

        context="aks-context",

        environment="staging",

    )

)

cluster = manager.activate(

    "kind"

)

print(cluster)

print()

print(manager.active_cluster())

print()

print(manager.clusters())

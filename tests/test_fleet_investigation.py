from fleet.cluster import Cluster

from state_engine.state import ClusterState

from fleet_engine.manager import FleetManagerEngine

engine = FleetManagerEngine()

clusters = [

    Cluster(

        name="kind",

        provider="Kind",

        context="kind",

        environment="development",

    ),

    Cluster(

        name="aks",

        provider="Azure",

        context="aks",

        environment="staging",

    ),

]

kind = ClusterState()

kind.pods = {

    "nginx": {}

}

kind.events = [

    {

        "reason": "Started"

    }

]

aks = ClusterState()

aks.pods = {}

aks.events = []

states = {

    "kind": kind,

    "aks": aks,

}

result = engine.investigate(

    clusters,

    states,

)

print(result)

from fleet.cluster import Cluster

from fleet.registry import ClusterRegistry

from fleet.context import ClusterContext


class FleetManager:

    def __init__(self):

        self.registry = ClusterRegistry()

        self.context = ClusterContext()

    def register(

        self,

        cluster,

    ):

        self.registry.register(

            cluster

        )

    def activate(

        self,

        name,

    ):

        cluster = self.registry.get(

            name

        )

        if cluster is None:

            raise ValueError(

                "Cluster not found."

            )

        for c in self.registry.all():

            c.active = False

        cluster.active = True

        self.context.switch(

            cluster

        )

        return cluster

    def active_cluster(self):

        return self.registry.active()

    def clusters(self):

        return self.registry.all()

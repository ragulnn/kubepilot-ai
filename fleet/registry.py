class ClusterRegistry:

    def __init__(self):

        self.clusters = {}

    def register(self, cluster):

        self.clusters[cluster.name] = cluster

    def get(self, name):

        return self.clusters.get(name)

    def all(self):

        return list(

            self.clusters.values()

        )

    def active(self):

        for cluster in self.clusters.values():

            if cluster.active:

                return cluster

        return None

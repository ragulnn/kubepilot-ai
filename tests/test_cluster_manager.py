from cluster_engine.manager import ClusterManager

manager = ClusterManager()

manager.load_default_clusters()

for cluster in manager.list_clusters():

    print(cluster)

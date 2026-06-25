from agent.context import ClusterContext

context = ClusterContext()

cluster = context.load()

print(cluster)

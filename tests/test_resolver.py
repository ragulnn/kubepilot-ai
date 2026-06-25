from agent.context import ClusterContext
from agent.resolver import ResourceResolver

print("=" * 60)
print("🧪 Testing Resource Resolver")
print("=" * 60)

context = ClusterContext().load()

resolver = ResourceResolver()

pod = resolver.resolve_pod(context, "nginx")

print(f"Resolved Pod: {pod}")

if pod:
    namespace = resolver.resolve_namespace(context, pod)
    print(f"Namespace: {namespace}")
else:
    print("Pod not found")

print("=" * 60)

from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class NamespacesTool(KubernetesTool):

    name = "namespaces"

    description = "List Kubernetes namespaces"

    def run(
        self,
        resource="",
        name="",
        namespace="default",
        **kwargs,
    ):

        return run_kubectl(
            "get namespaces"
        )

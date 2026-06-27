from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class NodesTool(KubernetesTool):

    name = "nodes"

    description = "List Kubernetes nodes"

    def run(self, **kwargs):

        return run_kubectl(
            "get nodes"
        )

from tools.base import KubernetesTool
from tools.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class IngressTool(KubernetesTool):

    name = "ingress"

    description = "List Kubernetes ingress"

    def run(self, **kwargs):

        namespace = kwargs.get("namespace")

        if namespace:

            return run_kubectl(
                f"get ingress -n {namespace}"
            )

        return run_kubectl(
            "get ingress -A"
        )

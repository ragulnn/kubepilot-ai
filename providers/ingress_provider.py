from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class IngressTool(KubernetesTool):

    name = "ingress"

    description = "List Kubernetes ingress"

    def run(
        self,
        resource="",
        name="",
        namespace="default",
        **kwargs,
    ):

        if namespace:

            return run_kubectl(
                f"get ingress -n {namespace}"
            )

        return run_kubectl(
            "get ingress -A"
        )

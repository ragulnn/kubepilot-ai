from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class EventsTool(KubernetesTool):

    name = "events"

    description = "List Kubernetes events"

    def run(self, **kwargs):

        namespace = kwargs.get("namespace")

        if namespace:

            return run_kubectl(
                f"get events -n {namespace}"
            )

        return run_kubectl(
            "get events -A"
        )

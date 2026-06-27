from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class PVCTool(KubernetesTool):

    name = "pvc"

    description = "List Persistent Volume Claims"

    def run(self, **kwargs):

        namespace = kwargs.get("namespace")

        if namespace:

            return run_kubectl(
                f"get pvc -n {namespace}"
            )

        return run_kubectl(
            "get pvc -A"
        )

from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class ConfigMapTool(KubernetesTool):

    name = "configmap"

    description = "List ConfigMaps"

    def run(self, **kwargs):

        namespace = kwargs.get("namespace")

        if namespace:

            return run_kubectl(
                f"get configmaps -n {namespace}"
            )

        return run_kubectl(
            "get configmaps -A"
        )

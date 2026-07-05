from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class SecretsTool(KubernetesTool):

    name = "secrets"

    description = "List Kubernetes secrets"

    def run(
        self,
        resource="",
        name="",
        namespace="default",
        **kwargs,
    ):

        if namespace:

            return run_kubectl(
                f"get secrets -n {namespace}"
            )

        return run_kubectl(
            "get secrets -A"
        )

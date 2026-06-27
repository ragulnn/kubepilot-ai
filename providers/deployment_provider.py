from tools.base import KubernetesTool
from tools.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class DeploymentsTool(KubernetesTool):

    name = "deployments"

    description = "List Kubernetes deployments"

    def run(self, **kwargs):

        namespace = kwargs.get("namespace")

        if namespace:

            return run_kubectl(
                f"get deployments -n {namespace}"
            )

        return run_kubectl(
            "get deployments -A"
        )

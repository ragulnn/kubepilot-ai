from tools.base import KubernetesTool
from tools.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class LogsTool(KubernetesTool):

    name = "logs"

    description = "Get pod logs"

    def run(self, **kwargs):

        pod = kwargs["pod"]

        namespace = kwargs.get(
            "namespace",
            "default"
        )

        return run_kubectl(
            f"logs {pod} -n {namespace}"
        )

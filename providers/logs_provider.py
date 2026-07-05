from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class LogsTool(KubernetesTool):

    name = "logs"

    description = "Get pod logs"

    def run(
        self,
        resource="",
        name="",
        namespace="default",
        **kwargs,
    ):

        if not name:
            raise Exception(
                "LogsTool requires a resource name."
            )

        return run_kubectl(
            f"logs {name} -n {namespace}"
        )

from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class ReadOnlyKubectlTool(KubernetesTool):

    name = "kubectl"

    description = "Execute safe read-only kubectl commands."

    ALLOWED_COMMANDS = {
        "get",
        "describe",
        "logs",
        "top",
        "api-resources",
        "version",
    }

    def run(
        self,
        command="",
        resource="",
        name="",
        namespace="default",
        **kwargs,
    ):

        if command not in self.ALLOWED_COMMANDS:
            raise Exception(
                f"Blocked kubectl command: {command}"
            )

        cmd = command

        if resource:
            cmd += f" {resource}"

        if name:
            cmd += f" {name}"

        if namespace:
            cmd += f" -n {namespace}"

        return run_kubectl(cmd)

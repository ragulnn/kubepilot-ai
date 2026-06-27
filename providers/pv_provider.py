from tools.base import KubernetesTool
from tools.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class PVTool(KubernetesTool):

    name = "pv"

    description = "List Persistent Volumes"

    def run(self, **kwargs):

        return run_kubectl(
            "get pv"
        )

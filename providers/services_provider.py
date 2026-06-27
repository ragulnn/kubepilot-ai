from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class ServicesTool(KubernetesTool):

    name = "services"

    description = "List Kubernetes Services"

    def run(self, **kwargs):
        return run_kubectl("get svc -A")

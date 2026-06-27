from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class PodsTool(KubernetesTool):

    name = "pods"
    description = "List Kubernetes Pods"

    def run(self, **kwargs):
        return run_kubectl("get pods -A")

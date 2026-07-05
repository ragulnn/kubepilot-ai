from providers.base import KubernetesTool
from providers.registry import register_tool

from utils.kubectl import run_kubectl
from parsers.kubernetes.pods import PodsParser


@register_tool
class PodsTool(KubernetesTool):

    name = "pods"

    description = "List Kubernetes Pods"

    def run(self, **kwargs):

        output = run_kubectl("get pods -A")

        return PodsParser().parse(output)

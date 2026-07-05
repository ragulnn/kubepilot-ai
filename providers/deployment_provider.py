from providers.base import KubernetesTool
from providers.registry import register_tool

from utils.kubectl import run_kubectl
from parsers.kubernetes.deployments import DeploymentsParser


@register_tool
class DeploymentTool(KubernetesTool):

    name = "deployments"

    description = "List Kubernetes Deployments"

    def run(
        self,
        resource="",
        name="",
        namespace="default",
        **kwargs,
    ):

        output = run_kubectl(
            "get deployments -A"
        )

        return DeploymentsParser().parse(output)

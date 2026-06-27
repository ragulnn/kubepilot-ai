from providers.base import KubernetesTool
from providers.registry import register_tool
from utils.kubectl import run_kubectl


@register_tool
class DescribeTool(KubernetesTool):

    name = "describe"

    description = "Describe Kubernetes resources"

    def run(self, **kwargs):

        resource = kwargs.get(
            "resource",
            "pod"
        )

        name = kwargs.get("name")

        namespace = kwargs.get(
            "namespace",
            "default"
        )

        if not name:
            raise Exception(
                "DescribeTool requires a resource name."
            )

        return run_kubectl(
            f"describe {resource} {name} -n {namespace}"
        )

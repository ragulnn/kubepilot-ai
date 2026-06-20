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

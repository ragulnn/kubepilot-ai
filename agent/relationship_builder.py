class RelationshipBuilder:

    def build(self, graph):

        node_names = list(graph.nodes.keys())

        # -------------------------
        # Deployment -> Pod
        # -------------------------

        deployments = [
            n for n in node_names
            if n.startswith("deployment:")
        ]

        pods = [
            n for n in node_names
            if n.startswith("pod:")
        ]

        for deployment in deployments:

            deployment_name = deployment.split(":")[1]

            for pod in pods:

                pod_name = pod.split(":")[1]

                if deployment_name in pod_name:

                    graph.add_edge(
                        deployment,
                        "manages",
                        pod,
                    )

        # -------------------------
        # Service -> Pod
        # -------------------------

        services = [
            n for n in node_names
            if n.startswith("service:")
        ]

        for service in services:

            service_name = service.split(":")[1]

            for pod in pods:

                pod_name = pod.split(":")[1]

                if service_name in pod_name:

                    graph.add_edge(
                        service,
                        "routes_to",
                        pod,
                    )

        return graph

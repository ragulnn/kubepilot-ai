import re


class ResourceExtractor:
    """
    Extract Kubernetes resources from raw kubectl output.

    This component DOES NOT make decisions.
    It simply converts raw text into structured objects.
    """

    def extract(self, tool: str, raw_output: str):

        if tool == "pods":
            return self._extract_pods(raw_output)

        elif tool == "deployments":
            return self._extract_deployments(raw_output)

        elif tool == "nodes":
            return self._extract_nodes(raw_output)

        elif tool == "services":
            return self._extract_services(raw_output)

        return {}

    # ---------------------------------------------------------
    # Pods
    # ---------------------------------------------------------

    def _extract_pods(self, raw_output):

        pods = []

        lines = raw_output.splitlines()

        if len(lines) <= 1:
            return {"pods": []}

        for line in lines[1:]:

            parts = re.split(r"\s+", line.strip())

            # kubectl get pods -A
            #
            # NAMESPACE NAME READY STATUS RESTARTS AGE

            if len(parts) < 6:
                continue

            namespace = parts[0]
            name = parts[1]
            ready = parts[2]
            status = parts[3]

            try:
                restarts = int(parts[4])
            except Exception:
                restarts = 0

            age = parts[5]

            pods.append(
                {
                    "kind": "Pod",
                    "namespace": namespace,
                    "name": name,
                    "ready": ready,
                    "status": status,
                    "restarts": restarts,
                    "age": age,
                }
            )

        return {
            "pods": pods
        }

    # ---------------------------------------------------------
    # Deployments
    # ---------------------------------------------------------

    def _extract_deployments(self, raw_output):

        deployments = []

        lines = raw_output.splitlines()

        if len(lines) <= 1:
            return {"deployments": []}

        for line in lines[1:]:

            parts = re.split(r"\s+", line.strip())

            if len(parts) < 2:
                continue

            deployments.append(
                {
                    "kind": "Deployment",
                    "namespace": parts[0],
                    "name": parts[1],
                }
            )

        return {
            "deployments": deployments
        }

    # ---------------------------------------------------------
    # Nodes
    # ---------------------------------------------------------

    def _extract_nodes(self, raw_output):

        nodes = []

        lines = raw_output.splitlines()

        if len(lines) <= 1:
            return {"nodes": []}

        for line in lines[1:]:

            parts = re.split(r"\s+", line.strip())

            if len(parts) < 2:
                continue

            nodes.append(
                {
                    "kind": "Node",
                    "name": parts[0],
                    "status": parts[1],
                }
            )

        return {
            "nodes": nodes
        }

    # ---------------------------------------------------------
    # Services
    # ---------------------------------------------------------

    def _extract_services(self, raw_output):

        services = []

        lines = raw_output.splitlines()

        if len(lines) <= 1:
            return {"services": []}

        for line in lines[1:]:

            parts = re.split(r"\s+", line.strip())

            if len(parts) < 2:
                continue

            services.append(
                {
                    "kind": "Service",
                    "namespace": parts[0],
                    "name": parts[1],
                }
            )

        return {
            "services": services
        }

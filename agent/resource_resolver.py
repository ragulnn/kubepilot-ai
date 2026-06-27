class ResourceResolver:

    def resolve(self, action, resources):

        tool = action.get("tool")

        if tool == "describe":
            return self._resolve_describe(action, resources)

        if tool == "logs":
            return self._resolve_logs(action, resources)

        return action

    def _resolve_describe(self, action, resources):

        if action.get("name"):
            return action

        pods = resources.get("pods", [])

        if not pods:
            return action

        # Prefer unhealthy pods
        for pod in pods:

            if pod["status"] != "Running":

                action["resource"] = "pod"
                action["name"] = pod["name"]
                action["namespace"] = pod["namespace"]

                return action

        # Otherwise use first pod
        pod = pods[0]

        action["resource"] = "pod"
        action["name"] = pod["name"]
        action["namespace"] = pod["namespace"]

        return action

    def _resolve_logs(self, action, resources):

        if action.get("pod"):
            return action

        pods = resources.get("pods", [])

        if not pods:
            return action

        for pod in pods:

            if pod["status"] != "Running":

                action["pod"] = pod["name"]
                action["namespace"] = pod["namespace"]

                return action

        pod = pods[0]

        action["pod"] = pod["name"]
        action["namespace"] = pod["namespace"]

        return action

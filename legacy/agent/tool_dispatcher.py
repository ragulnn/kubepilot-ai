class ToolDispatcher:

    RESOURCE_TOOL_MAP = {

        "pods": "pods",

        "pod": "describe",

        "services": "services",

        "service": "services",

        "nodes": "nodes",

        "deployments": "deployments",

        "events": "events",

        "namespaces": "namespaces",

        "pv": "pv",

        "pvc": "pvc",

        "configmaps": "configmap",

        "configmap": "configmap",

        "secrets": "secrets",

        "ingress": "ingress",
    }

    def dispatch(self, action):

        tool = action.get("tool")

        if tool != "kubectl":
            return action

        resource = action.get(
            "resource",
            ""
        ).lower()

        command = action.get(
            "command",
            ""
        ).lower()

        if (
            command == "get"
            and resource in self.RESOURCE_TOOL_MAP
        ):

            mapped = self.RESOURCE_TOOL_MAP[resource]

            action["tool"] = mapped

            action.pop("command", None)

        return action

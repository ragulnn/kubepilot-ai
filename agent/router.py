class Router:

    INFORMATION_KEYWORDS = [
        "show",
        "list",
        "get",
        "display",
        "describe",
        "namespaces",
        "pods",
        "services",
        "nodes",
        "events",
        "deployments",
        "ingress"
    ]

    INVESTIGATION_KEYWORDS = [
        "why",
        "diagnose",
        "investigate",
        "analyze",
        "root cause",
        "issue",
        "problem",
        "crash",
        "crashing",
        "restart",
        "restarting",
        "failed",
        "failing",
        "down",
        "503",
        "500"
    ]

    ACTION_KEYWORDS = [
        "delete",
        "scale",
        "restart",
        "rollout",
        "apply",
        "create",
        "patch",
        "edit"
    ]

    def route(self, question):

        q = question.lower()

        for word in self.ACTION_KEYWORDS:
            if word in q:
                return "action"

        for word in self.INVESTIGATION_KEYWORDS:
            if word in q:
                return "investigation"

        return "information"

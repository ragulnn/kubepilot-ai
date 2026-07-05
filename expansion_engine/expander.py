from expansion_engine.rules import (
    POD_EXPANSION,
    DEPLOYMENT_EXPANSION,
    SERVICE_EXPANSION,
)


class ExpansionEngine:

    def expand(self, resource):

        kind = resource.get(
            "kind",
            "",
        ).lower()

        if kind == "pod":
            return POD_EXPANSION

        if kind == "deployment":
            return DEPLOYMENT_EXPANSION

        if kind == "service":
            return SERVICE_EXPANSION

        return []

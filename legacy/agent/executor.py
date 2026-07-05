from connectors.request import EvidenceRequest
from connectors.default_registry import registry


class Executor:

    def execute(self, action: dict):

        if not isinstance(action, dict):
            raise Exception("Action must be a dictionary.")

        tool = action.get("tool")

        if tool == "finish":
            return "Investigation completed."

        if tool is None:
            raise Exception("Planner did not return a tool.")

        print(f"Running Tool : {tool}")

        request = EvidenceRequest(

            type=tool,

            namespace=action.get(
                "namespace"
            ),

            resource=action.get(
                "resource"
            ),

            keyword=action.get(
                "keyword"
            ),

            labels=action.get(
                "labels",
                {},
            ),

            filters=action.get(
                "filters",
                {},
            ),

        )

        response = registry.collect(
            request
        )

        if not response.success:

            raise Exception(
                response.message
            )

        if response.evidence:

            return response.evidence[0]

        return ""

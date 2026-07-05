class ToolSelector:

    MAP = {

        "pod": "pods",

        "log": "logs",

        "event": "events",

        "service": "services",

        "deployment": "deployments",

        "node": "nodes",

    }

    def next_tool(self, missing):

        if not missing:

            return {

                "tool": "finish"

            }

        return {

            "tool": self.MAP[

                missing[0]

            ]

        }


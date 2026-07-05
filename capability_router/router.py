class CapabilityRouter:

    def route(self, workflow):

        capabilities = []

        capabilities.append("planning")

        capabilities.append("resource_discovery")

        if workflow:

            for capability in workflow.capabilities:

                if capability not in capabilities:

                    capabilities.append(capability)

        for capability in [

            "aggregation",

            "analysis",
           
            "verification",

            "memory",

            "knowledge",

            "learning",

            "report",

            "remediation",

        ]:

            if capability not in capabilities:

                capabilities.append(capability)

        return capabilities

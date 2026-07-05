from workflow_engine.workflow import Workflow
from workflow_engine.types import WorkflowType


class WorkflowSelector:

    def select(self, question):

        q = question.lower()

        # --------------------------------------------------
        # Pod Investigation
        # --------------------------------------------------

        if any(x in q for x in [
            "pod",
            "container",
            "crash",
            "crashloop",
            "restart",
            "nginx",
        ]):

            return Workflow(

                name=WorkflowType.POD,

                type="Pod",

                intent="Crash Investigation",

                severity="high",

                investigation=[
                    "describe",
                    "logs",
                    "events",
                    "metrics",
                ],

                capabilities=[
                    "logs",
                    "describe",
                    "events",
                    "metrics",    
                    "errors",
                ],

                confidence=0.95,
            )

        # --------------------------------------------------
        # Deployment Investigation
        # --------------------------------------------------

        if "deployment" in q:

            return Workflow(

                name=WorkflowType.DEPLOYMENT,

                type="Deployment",

                intent="Deployment Investigation",

                severity="medium",

                investigation=[
                    "describe",
                    "events",
                    "metrics",
                ],

                capabilities=[
                    "describe",
                    "events",
                    "metrics",
                    "errors",
                ],

                confidence=0.95,
            )

        # --------------------------------------------------
        # Service Investigation
        # --------------------------------------------------

        if "service" in q:

            return Workflow(

                name=WorkflowType.SERVICE,

                type="Service",

                intent="Service Investigation",

                severity="medium",

                investigation=[
                    "describe",
                    "events",
                ],

                capabilities=[
                    "describe",
                    "events",
                ],

                confidence=0.95,
            )

        # --------------------------------------------------
        # Network Investigation
        # --------------------------------------------------

        if any(x in q for x in [

            "ingress",
            "network",
            "dns",

        ]):

            return Workflow(

                name=WorkflowType.NETWORK,

                type="Network",

                intent="Network Investigation",

                severity="high",

                investigation=[
                    "describe",
                    "events",
                ],

                capabilities=[
                    "network",
                ],

                confidence=0.95,
            )

        # --------------------------------------------------
        # Storage Investigation
        # --------------------------------------------------

        if any(x in q for x in [

            "pv",
            "pvc",
            "storage",
            "volume",

        ]):

            return Workflow(

                name=WorkflowType.STORAGE,

                type="Storage",

                intent="Storage Investigation",

                severity="medium",

                investigation=[
                    "describe",
                    "events",
                ],

                capabilities=[
                    "storage",
                ],

                confidence=0.95,
            )

        # --------------------------------------------------
        # Node Investigation
        # --------------------------------------------------

        if "node" in q:

            return Workflow(

                name=WorkflowType.NODE,

                type="Node",

                intent="Node Investigation",

                severity="high",

                investigation=[
                    "describe",
                    "events",
                    "metrics",
                ],

                capabilities=[
                    "describe",
                    "events",
                    "metrics",
                ],

                confidence=0.95,
            )

        # --------------------------------------------------
        # Generic Investigation
        # --------------------------------------------------

        return Workflow(

            name=WorkflowType.GENERIC,

            type="Generic",

            intent="General Investigation",

            severity="low",

            investigation=[
                "describe",
            ],

            capabilities=[
                "describe",
            ],

            confidence=0.20,
        )

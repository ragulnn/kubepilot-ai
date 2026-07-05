from agent.workflow_plan import WorkflowPlan
from agent.workflow_types import WorkflowType


class WorkflowSelector:

    def select(self, question: str):

        q = question.lower()

        if "pod" in q or "nginx" in q:

            return WorkflowPlan(

                workflow=WorkflowType.POD,

                target="",

                confidence=0.95,

            )

        if "deployment" in q:

            return WorkflowPlan(

                workflow=WorkflowType.DEPLOYMENT,

                target="",

                confidence=0.95,

            )

        if "service" in q:

            return WorkflowPlan(

                workflow=WorkflowType.SERVICE,

                target="",

                confidence=0.95,

            )

        if "ingress" in q:

            return WorkflowPlan(

                workflow=WorkflowType.NETWORK,

                target="",

                confidence=0.90,

            )

        return WorkflowPlan(

            workflow=WorkflowType.GENERIC,

            target="",

            confidence=0.40,

        )

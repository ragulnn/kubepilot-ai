from agents.base import Agent

from workflow_engine.executor import WorkflowExecutor


class EvidenceAgent(Agent):

    name = "evidence"
    capabilities = [
        "evidence",
    ]
    def __init__(self):

        super().__init__()

        self.executor = WorkflowExecutor()

    def run(self, state):

        # Prefer the Agent Bus
        workflow = None

        if self.bus:
            workflow = self.bus.get("workflow")

        # Fallback
        if workflow is None:
            workflow = state.get("workflow")

        if workflow is None:
            return state

        responses = self.executor.execute(

            workflow,

            state["question"]

        )

        # Backward compatibility
        state["responses"] = responses

        # Publish to Agent Bus
        if self.bus:
            self.bus.publish(
                "responses",
                responses,
            )

        return state

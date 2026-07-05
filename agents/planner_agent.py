from agents.base import Agent

from workflow_engine.router import WorkflowRouter


class PlannerAgent(Agent):

    name = "planner"
    capabilities = [
        "planning",
    ]
    def __init__(self):

        super().__init__()

        self.router = WorkflowRouter()

    def run(self, state):

        workflow = self.router.route(
            state["question"]
        )

        # Old architecture (keep)
        state["workflow"] = workflow

        # New Agent Bus
        if self.bus:

            self.bus.publish(
                "workflow",
                workflow,
            )

        return state

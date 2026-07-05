from workflow_engine.selector import WorkflowSelector


class WorkflowRouter:

    def __init__(self):

        self.selector = WorkflowSelector()

    def route(self, question):

        workflow = self.selector.select(question)

        if workflow is None:

            return None

        if getattr(workflow.name, "value", workflow.name) == "generic":

            return None

        return workflow

from expansion_engine.automatic_expander import AutomaticExpander


class WorkflowRegistry:

    def __init__(self):

        self.expander = AutomaticExpander()

    def execute(self, plan):

        return self.expander.expand(plan)

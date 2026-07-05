from planning_engine.planner import InvestigationPlanner


class InvestigationExecutor:

    def __init__(self):

        self.planner = InvestigationPlanner()

    def execute(

        self,

        question,

        confidence,

        collected,

    ):

        return self.planner.plan(

            question,

            confidence,

            collected,

        )

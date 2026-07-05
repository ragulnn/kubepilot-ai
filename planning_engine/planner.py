from planning_engine.confidence import InvestigationConfidence
from planning_engine.decision import InvestigationDecision
from planning_engine.selector import StrategySelector


class InvestigationPlanner:

    def __init__(self):

        self.confidence = InvestigationConfidence()

        self.decision = InvestigationDecision()

        self.selector = StrategySelector()

    def plan(

        self,

        question,

        confidence,

        collected,

    ):

        strategy = self.selector.select(

            question

        )

        if self.confidence.enough(

            confidence

        ):

            return {

                "completed": True,

                "strategy": strategy,

                "next": None,

            }

        return {

            "completed": False,

            "strategy": strategy,

            "next": self.decision.next_step(

                strategy,

                collected,

            ),

        }

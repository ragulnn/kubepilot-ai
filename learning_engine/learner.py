from learning_engine.statistics import InvestigationStatistics
from learning_engine.optimizer import StrategyOptimizer


class InvestigationLearner:

    def __init__(self):

        self.statistics = InvestigationStatistics()

        self.optimizer = StrategyOptimizer()

    def learn(self, incidents):

        if incidents is None:
            incidents = []

        # ----------------------------------
        # Generate Statistics
        # ----------------------------------

        stats = self.statistics.summarize(
            incidents
        )

        # ----------------------------------
        # Optimize Investigation Strategy
        # ----------------------------------

        strategy = self.optimizer.optimize(
            stats
        )

        # ----------------------------------
        # Learning Result
        # ----------------------------------

        learned = {

            "statistics": stats,

            "recommended_strategy": strategy,

            "incident_count": len(incidents),

            "success": len(incidents) > 0,

        }

        return learned

from agents.base import Agent

from aggregation_engine.aggregator import SpecialistAggregator


class AggregatorAgent(Agent):

    name = "aggregator"

    capabilities = [
        "aggregation",
    ]

    def __init__(self):

        super().__init__()

        self.aggregator = SpecialistAggregator()

    def run(self, state):

        specialist_results = []

        if self.bus:

            for key in [

                "prometheus_result",

                "loki_result",

                "tempo_result",

                "kubernetes_result",

            ]:

                result = self.bus.get(key)

                if result:

                    specialist_results.append(result)

        aggregated = self.aggregator.aggregate(
            specialist_results
        )

        # Keep both representations
        state["specialist_results"] = specialist_results
        state["aggregated"] = aggregated

        if self.bus:

            self.bus.publish(
                "specialist_results",
                specialist_results,
            )

            self.bus.publish(
                "aggregated",
                aggregated,
            )

        print()
        print("=" * 60)
        print("AI Aggregator")
        print("=" * 60)
        print()
        print(aggregated)

        return state

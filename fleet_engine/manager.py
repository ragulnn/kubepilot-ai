from fleet_engine.investigator import FleetInvestigator

from fleet_engine.aggregator import FleetAggregator


class FleetManagerEngine:

    def __init__(self):

        self.investigator = FleetInvestigator()

        self.aggregator = FleetAggregator()

    def investigate(

        self,

        clusters,

        states,

    ):

        reports = []

        for cluster in clusters:

            state = states.get(cluster.name)

            if state is None:

                continue

            reports.append(

                self.investigator.investigate(

                    cluster,

                    state,

                )

            )

        return self.aggregator.aggregate(

            reports

        )

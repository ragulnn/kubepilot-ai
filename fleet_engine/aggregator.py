class FleetAggregator:

    def aggregate(

        self,

        reports,

    ):

        return {

            "clusters": len(reports),

            "healthy": sum(

                1

                for report in reports

                if report.root_cause == "Cluster healthy"

            ),

            "issues": sum(

                1

                for report in reports

                if report.root_cause != "Cluster healthy"

            ),

            "reports": reports,

        }

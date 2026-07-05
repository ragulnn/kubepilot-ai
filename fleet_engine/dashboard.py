from fleet_engine.health import FleetHealth


class FleetDashboard:

    def build(self, fleet_result):

        total = fleet_result["clusters"]

        healthy = fleet_result["healthy"]

        unhealthy = fleet_result["issues"]

        score = 0.0

        if total > 0:

            score = round(

                healthy / total,

                2,

            )

        critical = []

        for report in fleet_result["reports"]:

            if report.root_cause != "Cluster healthy":

                critical.append(

                    report.cluster

                )

        return FleetHealth(

            score=score,

            healthy_clusters=healthy,

            unhealthy_clusters=unhealthy,

            total_clusters=total,

            critical_clusters=critical,

        )

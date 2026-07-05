from fleet_engine.result import FleetInvestigationResult


class FleetInvestigator:

    def investigate(

        self,

        cluster,

        state,

    ):

        findings = []

        recommendations = []

        if len(state.events) > 0:

            findings.append(

                f"{len(state.events)} recent Kubernetes events"

            )

        if len(state.pods) == 0:

            findings.append(

                "No running Pods"

            )

            root = "Cluster unavailable"

            confidence = 0.95

        else:

            root = "Cluster healthy"

            confidence = 0.90

        recommendations.append(

            "Continue monitoring"

        )

        return FleetInvestigationResult(

            cluster=cluster.name,

            root_cause=root,

            confidence=confidence,

            findings=findings,

            recommendations=recommendations,

        )

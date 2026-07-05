from remediation_engine.health import ClusterHealth
from remediation_engine.observation import ObservationResult


class ObservationEngine:

    def __init__(self):

        self.health = ClusterHealth()

    def observe(self, metrics):

        score, observations = self.health.evaluate(

            metrics

        )

        return ObservationResult(

            success=score >= 0.80,

            health_score=score,

            observations=observations,

            recommendation=(
                "Rollback recommended"
                if score < 0.80
                else "System healthy"
            ),

        )

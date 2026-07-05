class ClusterHealth:

    def evaluate(self, metrics):

        score = 1.0

        observations = []

        if metrics.get("restarts", 0) > 0:

            score -= 0.20

            observations.append(

                "Pods restarted."

            )

        if metrics.get("oomkilled", False):

            score -= 0.40

            observations.append(

                "OOMKilled detected."

            )

        if metrics.get("ready", True) is False:

            score -= 0.30

            observations.append(

                "Pods not Ready."

            )

        return score, observations

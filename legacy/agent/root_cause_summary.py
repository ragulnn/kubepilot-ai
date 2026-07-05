class RootCauseSummary:

    def summarize(self, ranked):

        if not ranked:

            return {

                "root_cause": "Unknown",

                "confidence": 0.0,
            }

        best = ranked[0]

        return {

            "root_cause": best["root_cause"],

            "confidence": best["confidence"],

            "resource": best["resource"],

            "status": best["status"],
        }

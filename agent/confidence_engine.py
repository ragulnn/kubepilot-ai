class ConfidenceEngine:

    def calculate(self, evidence_store):

        score = 0.0

        evidence = evidence_store.all()

        if not evidence:
            return 0.0

        for item in evidence:

            if item.type == "pod":
                score += 0.15

            elif item.type == "event":
                score += 0.20

            elif item.type == "log":
                score += 0.25

            elif item.type == "deployment":
                score += 0.10

            elif item.type == "service":
                score += 0.10

            elif item.type == "node":
                score += 0.20

        return min(score, 1.0)

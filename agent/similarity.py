class SimilarityEngine:

    def compare(
        self,
        current,
        previous
    ):

        score = 0

        if (
            current.get("root_cause")
            ==
            previous.get("root_cause")
        ):
            score += 40

        if (
            current.get("symptom")
            ==
            previous.get("symptom")
        ):
            score += 30

        if (
            current.get("namespace")
            ==
            previous.get("namespace")
        ):
            score += 10

        if (
            current.get("resource_name")
            ==
            previous.get("resource_name")
        ):
            score += 10

        if (
            current.get("severity")
            ==
            previous.get("severity")
        ):
            score += 10

        return score

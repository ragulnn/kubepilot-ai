class SimilarityEngine:

    def score(

        self,

        current,

        previous,

    ):

        score = 0

        if current["root_cause"] == previous["root_cause"]:

            score += 40

        if current["resource_name"] == previous["resource_name"]:

            score += 30

        if current["namespace"] == previous["namespace"]:

            score += 20

        if current["question"] == previous["question"]:

            score += 10

        return score

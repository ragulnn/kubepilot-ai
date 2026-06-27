class RootCauseRanker:

    def rank(self, causes):

        return sorted(

            causes,

            key=lambda x: x["confidence"],

            reverse=True,

        )


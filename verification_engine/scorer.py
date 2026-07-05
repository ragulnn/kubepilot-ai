class VerificationScorer:

    def score(

        self,

        matched,

        total,

    ):

        if total == 0:

            return 0.0

        return round(

            matched / total,

            2,

        )

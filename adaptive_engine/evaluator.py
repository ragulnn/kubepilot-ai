class ConfidenceEvaluator:

    def update(

        self,

        analysis,

    ):

        return analysis.get(

            "confidence",

            0.0,

        )

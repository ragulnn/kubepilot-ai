class InvestigationDecision:

    def next_step(

        self,

        strategy,

        collected,

    ):

        for step in strategy:

            if step not in collected:

                return step

        return None

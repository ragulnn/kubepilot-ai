from agent.investigation_mode import InvestigationMode


class InvestigationGuard:

    def __init__(self):

        self.mode = InvestigationMode()

        self.max_steps = 8

    def should_finish(
        self,
        question,
        report,
        observations,
    ):

        mode = self.mode.detect(question)

        # -------------------------
        # Information request
        # -------------------------

        if mode == InvestigationMode.INFO:

            if len(observations) >= 1:

                return (
                    True,
                    "Information request completed."
                )

        # -------------------------
        # Safety stop
        # -------------------------

        if len(observations) >= self.max_steps:

            return (
                True,
                "Maximum investigation steps reached."
            )

        # -------------------------
        # Analyzer confidence
        # -------------------------

        confidence = report.get(
            "confidence",
            0.0,
        )

        if confidence >= 0.95:

            return (
                True,
                f"High confidence ({confidence:.2f})."
            )

        # -------------------------
        # Manual review
        # -------------------------

        if report.get(
            "requires_manual_review",
            False,
        ):

            return (
                True,
                "Manual review required."
            )

        return (
            False,
            "Continue investigation."
        )


from agents.base import Agent

from verification_engine.verifier import AIVerifier


class VerificationAgent(Agent):

    name = "verification"

    capabilities = [
        "verification",
    ]

    def __init__(self):

        super().__init__()

        self.verifier = AIVerifier()

    def run(self, state):

        print()
        print("=" * 60)
        print("Verification Agent")
        print("=" * 60)
        print()

        analysis = {}

        if self.bus:

            analysis = self.bus.get("analysis")

        if not analysis:

            analysis = state.get(
                "analysis",
                {},
            )

        if not analysis:

            print("No analysis available.")

            return state

        verification = self.verifier.verify(
            analysis
        )

        state["verification"] = verification

        if self.bus:

            self.bus.publish(
                "verification",
                verification,
            )

        print()

        print("Verification")

        print("------------------------------")

        print(verification)

        return state

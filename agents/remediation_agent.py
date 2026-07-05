from agents.base import Agent

from remediation_engine.planner import RemediationPlanner
from remediation_engine.request import RemediationRequest


class RemediationAgent(Agent):

    name = "remediation"

    capabilities = [
        "remediation",
    ]

    def __init__(self):

        super().__init__()

        self.planner = RemediationPlanner()

    def run(self, state):

        print()
        print("=" * 60)
        print("Remediation Agent")
        print("=" * 60)
        print()

        # -----------------------------
        # Analysis
        # -----------------------------

        analysis = None

        verification = {}

        memory = []

        knowledge = {}

        if self.bus:

            analysis = self.bus.get(
                "analysis"
            )

            verification = self.bus.get(
                "verification"
            ) or {}

            memory = self.bus.get(
                "memory"
            ) or []

            knowledge = self.bus.get(
                "knowledge"
            ) or {}

        if analysis is None:

            analysis = state.get(
                "analysis"
            )

        if not verification:

            verification = state.get(
                "verification",
                {},
            )

        if not memory:

            memory = state.get(
                "memory",
                [],
            )

        if not knowledge:

            knowledge = state.get(
                "knowledge",
                {},
            )

        if analysis is None:

            print("No analysis available.")

            return state

        # -----------------------------
        # AI Planning
        # -----------------------------

        request = RemediationRequest(

            analysis=analysis,

            verification=verification,

            memory=memory,

            knowledge=knowledge,

        )

        remediation = self.planner.plan(
            request
        )

        # -----------------------------
        # Store
        # -----------------------------

        state["remediation"] = remediation

        if self.bus:

            self.bus.publish(

                "remediation",

                remediation,

            )

        # -----------------------------
        # Display
        # -----------------------------

        print()

        print("Risk")

        print("------------------------------")

        print(remediation.risk)

        print()

        print("Requires Approval")

        print("------------------------------")

        print(remediation.requires_approval)

        print()

        print("Actions")

        print("------------------------------")

        for action in remediation.actions:

            print(action)

        return state

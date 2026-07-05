from agents.base import Agent

from connectors.default_registry import registry
from connectors.request import EvidenceRequest

from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import KUBERNETES_PROMPT
from llm.schemas.kubernetes import KUBERNETES_SCHEMA

from models.mapper import SpecialistMapper


class KubernetesAgent(Agent):

    name = "kubernetes"

    capabilities = [
        "kubernetes",
        "describe",
        "events",
    ]

    def __init__(self):

        super().__init__()

        self.ai = AIEngine()

        self.mapper = SpecialistMapper()

    def run(self, state):

        print()
        print("=" * 60)
        print("Kubernetes Agent")
        print("=" * 60)
        print()

        # ----------------------------------
        # Get Resources
        # ----------------------------------

        resources = state.get("resources", [])

        if self.bus:

            bus_resources = self.bus.get("resources")

            if bus_resources:

                resources = bus_resources

        if not resources:

            print("No resources found.")

            return state

        resource = resources[0]

        evidence = []

        # ----------------------------------
        # Collect Describe
        # ----------------------------------

        describe = registry.collect(

            EvidenceRequest(

                type="describe",

                kind=resource["kind"],

                name=resource["name"],

                namespace=resource["namespace"],

            )

        )

        if describe.success:

            evidence.extend(

                describe.evidence

            )

        # ----------------------------------
        # Collect Events
        # ----------------------------------

        events = registry.collect(

            EvidenceRequest(

                type="events",

                kind=resource["kind"],

                name=resource["name"],

                namespace=resource["namespace"],

            )

        )

        if events.success:

            evidence.extend(

                events.evidence

            )

        # ----------------------------------
        # Prepare Evidence
        # ----------------------------------

        evidence_text = "\n".join(

            str(item)

            for item in evidence

        )

        # ----------------------------------
        # AI Analysis
        # ----------------------------------

        ai_response = self.ai.analyze(

            AIRequest(

                prompt=KUBERNETES_PROMPT,

                schema=KUBERNETES_SCHEMA,

                evidence=evidence_text,

            )

        )

        # ----------------------------------
        # Normalize Result
        # ----------------------------------

        result = self.mapper.from_kubernetes(

            ai_response.parsed

        )

        # ----------------------------------
        # Store
        # ----------------------------------

        state["kubernetes"] = evidence

        state["kubernetes_ai"] = result

        # ----------------------------------
        # Publish
        # ----------------------------------

        if self.bus:

            self.bus.publish(

                "kubernetes",

                evidence,

            )

            self.bus.publish(

                "kubernetes_result",

                result,

            )

        # ----------------------------------
        # Display
        # ----------------------------------

        print()

        print("Collected Kubernetes Evidence")

        print("------------------------------")

        print(len(evidence))

        print()

        print("Kubernetes Specialist Result")

        print("------------------------------")

        print(result)

        return state

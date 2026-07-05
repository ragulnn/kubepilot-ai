from agents.base import Agent

from connectors.default_registry import registry
from connectors.request import EvidenceRequest

from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import PROMETHEUS_PROMPT
from llm.schemas.prometheus import PROMETHEUS_SCHEMA

from models.mapper import SpecialistMapper


class PrometheusAgent(Agent):

    name = "prometheus"

    capabilities = [
        "metrics",
        "performance",
        "capacity",
    ]

    def __init__(self):

        super().__init__()

        self.ai = AIEngine()

        self.mapper = SpecialistMapper()

    def run(self, state):

        print()
        print("=" * 60)
        print("Prometheus Agent")
        print("=" * 60)
        print()

        # ----------------------------------
        # Get discovered resources
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

        # ----------------------------------
        # Collect Metrics
        # ----------------------------------

        response = registry.collect(

            EvidenceRequest(

                type="metrics",

                kind=resource.get("kind"),

                name=resource.get("name"),

                namespace=resource.get("namespace"),

            )

        )

        if not response.success:

            print("Failed to collect metrics.")

            return state

        # ----------------------------------
        # Convert metrics to text
        # ----------------------------------

        evidence = "\n".join(

            str(item)

            for item in response.evidence

        )

        # ----------------------------------
        # AI Analysis
        # ----------------------------------

        ai_response = self.ai.analyze(

            AIRequest(

                prompt=PROMETHEUS_PROMPT,

                schema=PROMETHEUS_SCHEMA,

                evidence=evidence,

            )

        )

        # ----------------------------------
        # Normalize AI Output
        # ----------------------------------

        result = self.mapper.from_prometheus(

            ai_response.parsed

        )

        # ----------------------------------
        # Store
        # ----------------------------------

        state["prometheus"] = response.evidence

        state["prometheus_ai"] = result

        # ----------------------------------
        # Publish
        # ----------------------------------

        if self.bus:

            self.bus.publish(

                "prometheus",

                response.evidence,

            )

            self.bus.publish(

                "prometheus_result",

                result,

            )

        # ----------------------------------
        # Display
        # ----------------------------------

        print()

        print("Collected Metrics")

        print("------------------------------")

        print(len(response.evidence))

        print()

        print("Prometheus Specialist Result")

        print("------------------------------")

        print(result)

        return state

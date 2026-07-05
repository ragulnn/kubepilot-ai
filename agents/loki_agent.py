from agents.base import Agent

from connectors.default_registry import registry
from connectors.request import EvidenceRequest

from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import LOKI_PROMPT
from llm.schemas.loki import LOKI_SCHEMA

from models.mapper import SpecialistMapper


class LokiAgent(Agent):

    name = "loki"

    capabilities = [

        "logs",

        "errors",

        "warnings",

        "exceptions",

    ]

    def __init__(self):

        super().__init__()

        self.ai = AIEngine()

        self.mapper = SpecialistMapper()

    def run(self, state):

        print()
        print("=" * 60)
        print("Loki Agent")
        print("=" * 60)
        print()

        namespace = "default"
        pod_name = None

        resources = state.get(
            "resources",
            [],
        )

        if self.bus:

            bus_resources = self.bus.get(
                "resources"
            )

            if bus_resources:

                resources = bus_resources

        if resources:

            resource = resources[0]

            namespace = resource.get(
                "namespace",
                "default",
            )

            pod_name = resource.get(
                "name"
            )

        # ----------------------------------
        # Collect Logs
        # ----------------------------------

        response = registry.collect(

            EvidenceRequest(

                type="errors",

                kind="pod",

                name=pod_name,

                namespace=namespace,

            )

        )

        if not response.success:

            print("Failed to collect logs.")

            return state

        evidence = "\n".join(

            str(item)

            for item in response.evidence

        )

        ai_response = self.ai.analyze(

            AIRequest(

                prompt=LOKI_PROMPT,

                schema=LOKI_SCHEMA,

                evidence=evidence,

            )

        )

        result = self.mapper.from_loki(

            ai_response.parsed

        )

        state["loki"] = response.evidence
        state["loki_ai"] = result

        if self.bus:

            self.bus.publish(

                "loki",

                response.evidence,

            )

            self.bus.publish(

                "loki_result",

                result,

            )

        print()
        print("Collected Log Entries")
        print("------------------------------")
        print(len(response.evidence))

        print()
        print("Loki Specialist Result")
        print("------------------------------")
        print(result)

        return state

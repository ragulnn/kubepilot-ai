from agents.base import Agent

from connectors.default_registry import registry
from connectors.request import EvidenceRequest

from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import TEMPO_PROMPT
from llm.schemas.tempo import TEMPO_SCHEMA

from models.mapper import SpecialistMapper


class TempoAgent(Agent):

    name = "tempo"

    capabilities = [
        "traces",
        "trace",
        "spans",
    ]

    def __init__(self):

        super().__init__()

        self.ai = AIEngine()

        self.mapper = SpecialistMapper()

    def run(self, state):

        print()
        print("=" * 60)
        print("Tempo Agent")
        print("=" * 60)
        print()

        # ----------------------------------
        # Get Trace ID
        # ----------------------------------

        trace_id = state.get("trace_id")

        if self.bus:

            bus_trace = self.bus.get("trace_id")

            if bus_trace:

                trace_id = bus_trace

        if not trace_id:

            print("No trace id available.")

            return state

        # ----------------------------------
        # Collect Trace
        # ----------------------------------

        response = registry.collect(

            EvidenceRequest(

                type="traces",

                trace_id=trace_id,

            )

        )

        if not response.success:

            print("Failed to collect traces.")

            return state

        # ----------------------------------
        # Prepare Evidence
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

                prompt=TEMPO_PROMPT,

                schema=TEMPO_SCHEMA,

                evidence=evidence,

            )

        )

        # ----------------------------------
        # Normalize AI Output
        # ----------------------------------

        result = self.mapper.from_tempo(

            ai_response.parsed

        )

        # ----------------------------------
        # Store
        # ----------------------------------

        state["traces"] = response.evidence

        state["tempo_ai"] = result

        # ----------------------------------
        # Publish
        # ----------------------------------

        if self.bus:

            self.bus.publish(

                "traces",

                response.evidence,

            )

            self.bus.publish(

                "tempo_result",

                result,

            )

        # ----------------------------------
        # Display
        # ----------------------------------

        print()

        print("Collected Trace Entries")

        print("------------------------------")

        print(len(response.evidence))

        print()

        print("Tempo Specialist Result")

        print("------------------------------")

        print(result)

        return state

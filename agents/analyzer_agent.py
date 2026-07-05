from agents.base import Agent

from analysis_engine.incremental_analyzer import IncrementalAnalyzer
from analysis_engine.ai_analyzer import AIAnalyzer


class AnalyzerAgent(Agent):

    name = "analyzer"

    capabilities = [
        "analysis",
    ]

    def __init__(self):

        super().__init__()

        self.incremental = IncrementalAnalyzer()

        self.ai = AIAnalyzer()

    def run(self, state):

        print()
        print("=" * 60)
        print("Analyzer Agent")
        print("=" * 60)
        print()

        specialist_results = []

        if self.bus:

            for key in [

                "kubernetes_result",

                "loki_result",

                "prometheus_result",

                "tempo_result",

            ]:

                result = self.bus.get(key)

                if result:

                    specialist_results.append(result)

        if not specialist_results:

            print("No specialist results.")

            return state

        # ----------------------------------
        # Incremental Analysis
        # ----------------------------------

        incremental = self.incremental.analyze(

            specialist_results

        )

        state["incremental"] = incremental

        if self.bus:

            self.bus.publish(

                "incremental",

                incremental,

            )

        # ----------------------------------
        # AI Analysis
        # ----------------------------------

        aggregated = state.get(

            "aggregated",

            {},

        )

        analysis = self.ai.analyze(

            aggregated

        )

        analysis["incremental"] = incremental

        state["analysis"] = analysis

        if self.bus:

            self.bus.publish(

                "analysis",

                analysis,

            )

        print()

        print("Final AI Analysis")

        print("------------------------------")

        print(analysis)

        return state

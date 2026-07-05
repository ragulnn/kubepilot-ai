from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from llm.prompts import ANALYZER_PROMPT
from llm.schemas.analyzer import ANALYZER_SCHEMA


class AIAnalyzer:

    def __init__(self):

        self.ai = AIEngine()

    def analyze(self, aggregated):

        evidence = []

        for source, summary in zip(

            aggregated["sources"],

            aggregated["summaries"],

        ):

            evidence.append(

                f"{source}: {summary}"

            )

        for finding in aggregated["findings"]:

            evidence.append(

                f"Finding: {finding}"

            )

        evidence = "\n".join(evidence)

        response = self.ai.analyze(

            AIRequest(

                prompt=ANALYZER_PROMPT,

                schema=ANALYZER_SCHEMA,

                evidence=evidence,

            )

        )

        return response.parsed

from llm.client import LLMClient
from llm.prompts import VERIFY_PROMPT

from context_engine.builder import InvestigationContextBuilder


class DiagnosisVerifier:

    def __init__(self):

        self.llm = LLMClient()

        self.builder = InvestigationContextBuilder()

    def verify(

        self,

        question,

        evidence,

        diagnosis,

        confidence,

    ):

        investigation = self.builder.build(

            question=question,

            evidence=evidence,

            diagnosis={

                "diagnosis": diagnosis,

                "confidence": confidence,

            },

        )

        prompt = VERIFY_PROMPT.format(

            investigation=investigation,

        )

        return self.llm.generate(prompt)

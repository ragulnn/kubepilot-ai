from llm.client import LLMClient

from ai_engine.request import AIRequest
from ai_engine.response import AIResponse
from ai_engine.schema import JSONSchemaParser


class AIEngine:

    def __init__(self):

        self.client = LLMClient()

        self.parser = JSONSchemaParser()

    def analyze(
        self,
        request: AIRequest,
    ) -> AIResponse:

        prompt = request.prompt.strip()

        if request.schema:

            prompt += "\n\n"

            prompt += request.schema.strip()

        if request.evidence:

            prompt += "\n\nEvidence:\n"

            prompt += request.evidence.strip()

        llm = self.client.generate(prompt)

        parsed = self.parser.parse(
            llm.content
        )

        return AIResponse(

            success=llm.success,

            raw=llm.content,

            parsed=parsed,

            verified=parsed is not None,

            provider=llm.provider,

            model=llm.model,

            metadata=llm.metadata,

        )

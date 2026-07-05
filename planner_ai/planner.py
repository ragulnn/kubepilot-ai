from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from planner_ai.response import PlannerResponse


class AIInvestigationPlanner:

    def __init__(self):

        self.ai = AIEngine()

    def plan(self, request):

        prompt = f"""
Question:
{request.question}

Confidence:
{request.current_confidence}

Collected:
{request.collected}

Memory:
{request.memory}

Knowledge:
{request.knowledge}

Return the next investigation step.
"""

        response = self.ai.analyze(

            AIRequest(

                prompt=prompt,

                schema="""
{
    "next_step":"",
    "reason":"",
    "confidence":0.0
}
""",

                evidence="",

            )

        )

        return PlannerResponse(

            next_step=response.parsed["next_step"],

            reason=response.parsed["reason"],

            confidence=response.parsed["confidence"],

        )

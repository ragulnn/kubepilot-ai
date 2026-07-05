from ai_engine.engine import AIEngine
from ai_engine.request import AIRequest

from remediation_engine.action import RemediationAction
from remediation_engine.response import RemediationResponse

from llm.prompts import REMEDIATION_PROMPT
from llm.schemas.remediation import REMEDIATION_SCHEMA


class RemediationPlanner:

    def __init__(self):

        self.ai = AIEngine()

    def plan(self, request):

        evidence = f"""
Analysis:
{request.analysis}

Verification:
{request.verification}

Memory:
{request.memory}

Knowledge:
{request.knowledge}
"""

        response = self.ai.analyze(

            AIRequest(

                prompt=REMEDIATION_PROMPT,

                schema=REMEDIATION_SCHEMA,

                evidence=evidence,

            )

        )

        parsed = response.parsed or {}

        action_items = parsed.get("actions", [])

        actions = []

        for item in action_items:

            if not isinstance(item, dict):
                continue

            actions.append(

                RemediationAction(

                    action=item.get(
                        "action",
                        "",
                    ),

                    resource_type=item.get(
                        "resource_type",
                        "",
                    ),

                    resource_name=item.get(
                        "resource_name",
                        item.get("resource", ""),
                    ),

                    namespace=item.get(
                        "namespace",
                        "default",
                    ),

                    parameters=item.get(
                        "parameters",
                        {},
                    ),

                    reason=item.get(
                        "reason",
                        "",
                    ),

                    confidence=float(

                        item.get(
                            "confidence",
                            0.0,
                        )

                    ),

                )

            )

        return RemediationResponse(

            actions=actions,

            reasoning=parsed.get(
                "reasoning",
                "",
            ),

            risk=parsed.get(
                "risk",
                "LOW",
            ),

            requires_approval=parsed.get(
                "requires_approval",
                True,
            ),

        )

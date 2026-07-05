from remediation_engine.risk_registry import ACTION_RISK
from remediation_engine.risk_result import RiskResult


class RiskEngine:

    def evaluate(self, action):

        level = ACTION_RISK.get(

            action.action,

            "HIGH",

        )

        scores = {

            "LOW": 0.20,

            "MEDIUM": 0.60,

            "HIGH": 0.90,

        }

        score = scores[level]

        return RiskResult(

            level=level,

            score=score,

            requires_approval=level != "LOW",

        )

from verification_engine.rules import RULES
from verification_engine.scorer import VerificationScorer


class AIVerifier:

    def __init__(self):

        self.scorer = VerificationScorer()

    def verify(

        self,

        analysis,

    ):

        root = analysis.get(

            "root_cause",

            "",

        ).lower()

        evidence = analysis.get(

            "critical_evidence",

            [],

        )

        matched = 0

        total = 0

        expected = []

        if "memory" in root:

            expected = RULES["memory"]

        elif "cpu" in root:

            expected = RULES["cpu"]

        elif "network" in root:

            expected = RULES["network"]

        total = len(expected)

        for keyword in expected:

            for item in evidence:

                if keyword.lower() in item.lower():

                    matched += 1

                    break

        score = self.scorer.score(

            matched,

            total,

        )

        verified = score >= 0.75

        return {

            "verified": verified,

            "verification_score": score,

            "matched_rules": matched,

            "expected_rules": total,

        }

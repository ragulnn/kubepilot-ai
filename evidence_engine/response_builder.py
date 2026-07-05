class EvidenceResponseBuilder:

    def build(self, question, responses):

        evidence = []

        for response in responses:

            if not response.success:
                continue

            evidence.extend(response.evidence)

        return {

            "question": question,

            "evidence": evidence,

            "count": len(evidence),

        }

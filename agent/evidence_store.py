from agent.evidence import Evidence


class EvidenceStore:

    def __init__(self):

        self.evidence = []

    def add(self, evidence: Evidence):

        self.evidence.append(evidence)

    def all(self):

        return self.evidence

    def by_type(self, evidence_type):

        return [

            e

            for e in self.evidence

            if e.type == evidence_type

        ]

    def clear(self):

        self.evidence.clear()
    def count(self):

         return len(self.evidence)
    
    def summary(self):

      return {

        "total": len(self.evidence),

        "types": list({

            e.type

            for e in self.evidence

        })
    }

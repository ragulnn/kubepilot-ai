class InvestigationState:

    def __init__(self):

        self.collected = []

        self.confidence = 0.0

        self.completed = False

    def add(self, evidence):

        if evidence not in self.collected:

            self.collected.append(evidence)

from analysis_engine.rules import RuleEngine
from analysis_engine.correlation import CorrelationEngine


class Analyzer:

    def __init__(self):

        self.rules = RuleEngine()

        self.correlation = CorrelationEngine()

    def analyze(self, evidence):

        evidence = self.correlation.correlate(

            evidence

        )

        return self.rules.evaluate(

            evidence

        )

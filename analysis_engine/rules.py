from analysis_engine.confidence import ConfidenceCalculator
from analysis_engine.rule_loader import RuleLoader


class RuleEngine:

    def __init__(self):

        self.rules = RuleLoader().load()
        self.confidence = ConfidenceCalculator()

    def evaluate(self, evidence):

        matches = 0

        memory = None
        restart = None
        logs = ""
        trace_errors = ""

        for item in evidence:

            if item.name == "logs":

                logs += str(item.value)

            elif item.name == "traces":

                trace_errors += str(item.value)

            elif item.name == "memory":

                memory = item.value

            elif item.name == "restarts":

                restart = item.value
            elif item.name == "memory_restart":

               matches += 1

               evidence_used.append(

                 "Memory spike with frequent restarts"

               )
            elif item.name == "logs_traces":

               matches += 1

               evidence_used.append(

                  "Logs correlate with trace failures"

               )
        evidence_used = []
        fixes = []

        # ---------------------------------
        # Rule 1 - OOMKilled
        # ---------------------------------

        if "OOMKilled" in logs:

            matches += 1

            evidence_used.append(

                "Logs contain OOMKilled"

            )

        # ---------------------------------
        # Rule 2 - Memory Usage
        # ---------------------------------

        if memory is not None and memory >= 0.95:

            matches += 1

            evidence_used.append(

                f"Memory usage {memory:.2f}"

            )

        # ---------------------------------
        # Rule 3 - Restart Count
        # ---------------------------------

        if restart is not None and restart > 5:

            matches += 1

            evidence_used.append(

                f"Restart count {restart}"

            )

        # ---------------------------------
        # Rule 4 - Tempo Exception
        # ---------------------------------

        if "Exception" in trace_errors:

            matches += 1

            evidence_used.append(

                "Tempo trace contains exception"

            )

        # ---------------------------------
        # Memory Exhaustion Diagnosis
        # ---------------------------------

        if matches >= 2:

            fixes.extend([

                "Increase memory limit",

                "Check for memory leak",

                "Review container memory requests",

            ])

            return {

                "root_cause": "Memory Exhaustion",

                "confidence": self.confidence.score(matches),

                "evidence": evidence_used,

                "recommended_fix": fixes,

            }

        # ---------------------------------
        # Default
        # ---------------------------------

        return {

            "root_cause": "Unknown",

            "confidence": 0.0,

            "evidence": [],

            "recommended_fix": [],

        }

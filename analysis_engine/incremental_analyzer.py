from analysis_engine.confidence import ConfidenceTracker

from models.specialist_result import SpecialistResult


class IncrementalAnalyzer:

    def __init__(self):

        self.tracker = ConfidenceTracker()

    def analyze(self, specialist_results):

        confidence = 0.0

        summaries = []

        root_causes = []

        sources = []

        recommendations = []

        findings = []

        for result in specialist_results:

            if not isinstance(result, SpecialistResult):
                continue

            confidence = self.tracker.update(result)

            summaries.append(result.summary)

            root_causes.append(result.root_cause)

            sources.append(result.source)

            findings.extend(result.findings)

            recommendations.extend(result.recommendations)

        return {

            "confidence": confidence,

            "summaries": summaries,

            "root_causes": root_causes,

            "sources": sources,

            "findings": list(dict.fromkeys(findings)),

            "recommendations": list(dict.fromkeys(recommendations)),

        }

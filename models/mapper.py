from models.specialist_result import SpecialistResult


class SpecialistMapper:

    def from_prometheus(self, data):

        return SpecialistResult(

            source="prometheus",

            summary=data.get(

                "summary",

                "",

            ),

            root_cause=data.get(

                "root_cause",

                "",

            ),

            confidence=data.get(

                "confidence",

                0.0,

            ),

            findings=data.get(

                "critical_metrics",

                [],

            ),

            recommendations=data.get(

                "recommendations",

                [],

            ),

        )

    def from_loki(self, data):

        return SpecialistResult(

            source="loki",

            summary=data.get(

                "root_cause",

                "",

            ),

            root_cause=data.get(

                "root_cause",

                "",

            ),

            confidence=data.get(

                "confidence",

                0.0,

            ),

            findings=data.get(

                "critical_errors",

                [],

            ),

            recommendations=data.get(

                "recommendations",

                [],

            ),

        )

    def from_tempo(self, data):

        return SpecialistResult(

            source="tempo",

            summary=data.get(

                "root_cause",

                "",

            ),

            root_cause=data.get(

                "root_cause",

                "",

            ),

            confidence=data.get(

                "confidence",

                0.0,

            ),

            findings=data.get(

                "failed_spans",

                [],

            ),

            recommendations=data.get(

                "recommendations",

                [],

            ),

        )

    def from_kubernetes(self, data):

        return SpecialistResult(

            source="kubernetes",

            summary=data.get(

                "root_cause",

                "",

            ),

            root_cause=data.get(

                "root_cause",

                "",

            ),

            confidence=data.get(

                "confidence",

                0.0,

            ),

            findings=data.get(

                "issues",

                [],

            ),

            recommendations=data.get(

                "recommendations",

                [],

            ),

        )

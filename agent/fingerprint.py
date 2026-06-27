from datetime import datetime


class FingerprintGenerator:

    def generate(
        self,
        report,
        observations,
        cluster="default"
    ):

        tools = []

        for obs in observations:

            tools.append(
                obs["tool"]
            )

        fingerprint = {

            "cluster": cluster,

            "resource_type": report.get(
                "resource_type",
                ""
            ),

            "resource_name": report.get(
                "affected_resource",
                ""
            ),

            "namespace": report.get(
                "namespace",
                ""
            ),

            "symptom": report.get(
                "symptom",
                ""
            ),

            "root_cause": report.get(
                "root_cause",
                ""
            ),

            "confidence": report.get(
                "confidence",
                0
            ),

            "severity": report.get(
                "severity",
                ""
            ),

            "tool_history": tools,

            "evidence": report.get(
                "evidence",
                []
            ),

            "timestamp": datetime.utcnow().isoformat()

        }

        return fingerprint

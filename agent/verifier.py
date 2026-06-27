class MemoryVerifier:

    def verify(
        self,
        current,
        previous,
    ):

        checks = [

            "root_cause",
            "symptom",
            "resource_name",
            "namespace",
        ]

        matched = 0

        for field in checks:

            if (
                current.get(field)
                ==
                previous.get(field)
            ):

                matched += 1

        confidence = matched / len(checks)

        return {

            "verified": confidence >= 0.75,

            "confidence": confidence,

        }

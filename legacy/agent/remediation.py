class Remediation:

    def __init__(self):

        self.fixes = {

            "CrashLoopBackOff": [
                "Inspect pod logs.",
                "Verify environment variables.",
                "Check mounted secrets."
            ],

            "OOMKilled": [
                "Increase memory limits.",
                "Reduce application memory usage."
            ],

            "ImagePullBackOff": [
                "Verify image name.",
                "Check imagePullSecrets.",
                "Verify registry access."
            ],

            "Pending": [
                "Check node resources.",
                "Inspect scheduler events."
            ]
        }

    def recommend(self, issue):

        return self.fixes.get(
            issue,
            ["No recommendation available."]
        )


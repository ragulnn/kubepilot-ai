class EvidenceQualityEngine:

    WEIGHTS = {

        # Healthy

        "Running": 0.05,

        "Completed": 0.05,

        # Warning

        "Pending": 0.20,

        "ContainerCreating": 0.25,

        "Terminating": 0.25,

        # Errors

        "CrashLoopBackOff": 0.60,

        "ImagePullBackOff": 0.80,

        "ErrImagePull": 0.80,

        "OOMKilled": 0.75,

        "Error": 0.60,

        "Failed": 0.70,

        "Unknown": 0.40,
    }

    def score(self, evidence):

        return self.WEIGHTS.get(

            evidence.value,

            0.10,

        )

class RootCauseEngine:

    RULES = {

        "CrashLoopBackOff":
            "Application Crash",

        "ImagePullBackOff":
            "Container Image Missing",

        "ErrImagePull":
            "Container Image Missing",

        "OOMKilled":
            "Out Of Memory",

        "Pending":
            "Scheduling Problem",

        "ContainerCreating":
            "Container Startup",

        "NodeNotReady":
            "Node Failure",

        "Failed":
            "Workload Failure",
    }

    def detect(self, evidence_store):

        findings = []

        for evidence in evidence_store.all():

            cause = self.RULES.get(
                evidence.value
            )

            if cause:

                findings.append({

                    "resource": evidence.resource,

                    "namespace": evidence.namespace,

                    "status": evidence.value,

                    "root_cause": cause,

                    "confidence": evidence.confidence,
                })

        return findings

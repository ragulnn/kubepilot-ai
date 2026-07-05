class CapabilityRouter:

    def route(self, question: str):

        question = question.lower()

        # -----------------------------
        # Discovery
        # -----------------------------

        if "pod" in question:

            return [
                {
                    "type": "pods",
                    "namespace": "default",
                }
            ]

        if "deployment" in question:

            return [
                {
                    "type": "deployments",
                    "namespace": "default",
                }
            ]

        if "service" in question:

            return [
                {
                    "type": "services",
                    "namespace": "default",
                }
            ]

        if "node" in question:

            return [
                {
                    "type": "nodes",
                }
            ]

        if "namespace" in question:

            return [
                {
                    "type": "namespaces",
                }
            ]

        if "ingress" in question:

            return [
                {
                    "type": "ingress",
                    "namespace": "default",
                }
            ]

        if "configmap" in question:

            return [
                {
                    "type": "configmap",
                    "namespace": "default",
                }
            ]

        if "secret" in question:

            return [
                {
                    "type": "secrets",
                    "namespace": "default",
                }
            ]

        if "persistentvolume" in question or "pv" in question:

            return [
                {
                    "type": "pv",
                }
            ]

        if "persistentvolumeclaim" in question or "pvc" in question:

            return [
                {
                    "type": "pvc",
                    "namespace": "default",
                }
            ]

        # -----------------------------
        # Troubleshooting
        # -----------------------------
        #
        # DO NOT request logs or describe yet.
        # They require a specific pod name.
        #
        # Phase 24 will introduce a Resource
        # Discovery Engine that finds the pod
        # first, then expands into:
        #
        # pods -> describe -> logs -> events
        #
        # -----------------------------

        if any(
            word in question
            for word in [
                "crash",
                "crashloop",
                "restart",
                "error",
                "failed",
                "pending",
                "backoff",
                "imagepull",
                "investigate",
                "debug",
                "diagnose",
                "not working",
                "why",
                "issue",
                "problem",
            ]
        ):

            return [

                {
                    "type": "pods",
                    "namespace": "default",
                },

                {
                    "type": "events",
                    "namespace": "default",
                },

            ]

        # -----------------------------
        # Default
        # -----------------------------

        return [
            {
                "type": "pods",
                "namespace": "default",
            }
        ]

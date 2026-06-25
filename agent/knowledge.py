class KnowledgeEngine:

    def __init__(self):

        self.rules = {

            "CrashLoopBackOff": {
                "next_tool": "logs",
                "reason": "Container is repeatedly crashing."
            },

            "ImagePullBackOff": {
                "next_tool": "describe",
                "reason": "Image cannot be pulled."
            },

            "ErrImagePull": {
                "next_tool": "describe",
                "reason": "Image pull failed."
            },

            "Pending": {
                "next_tool": "events",
                "reason": "Pod scheduling problem."
            },

            "OOMKilled": {
                "next_tool": "describe",
                "reason": "Container exceeded memory."
            },

            "Error": {
                "next_tool": "logs",
                "reason": "Application error."
            }
        }

    def next_step(self, pod_status):

        return self.rules.get(pod_status)

import re


class EntityMatcher:

    # Kubernetes words that are NOT resource names
    KEYWORDS = {

        "pod",
        "pods",
        "deployment",
        "deployments",
        "service",
        "services",
        "logs",
        "log",
        "events",
        "event",
        "namespace",
        "namespaces",
        "describe",
        "investigate",
        "kubernetes",
        "cluster",
        "node",
        "nodes",
        "container",
        "containers",
        "ingress",
        "configmap",
        "secret",
        "pvc",
        "pv",

    }

    # Common English words
    STOP_WORDS = {

        "a",
        "an",
        "the",
        "is",
        "are",
        "was",
        "were",
        "be",
        "been",
        "being",
        "why",
        "what",
        "when",
        "where",
        "who",
        "how",
        "show",
        "list",
        "find",
        "display",
        "all",
        "my",
        "of",
        "to",
        "for",
        "in",
        "on",
        "at",
        "from",
        "with",
        "by",
        "and",
        "or",
        "please",

    }

    # Investigation verbs
    ACTION_WORDS = {

        "crash",
        "crashing",
        "crashed",
        "restart",
        "restarting",
        "restarted",
        "running",
        "pending",
        "failed",
        "failure",
        "broken",
        "slow",
        "healthy",
        "unhealthy",
        "error",
        "errors",
        "debug",
        "investigate",
        "check",
        "inspect",

    }

    def extract(self, question: str):

        words = re.findall(
            r"[a-zA-Z0-9-]+",
            question.lower(),
        )

        entities = []

        for word in words:

            if word in self.KEYWORDS:
                continue

            if word in self.STOP_WORDS:
                continue

            if word in self.ACTION_WORDS:
                continue

            if len(word) < 2:
                continue

            entities.append(word)

        # Remove duplicates while preserving order
        return list(dict.fromkeys(entities))

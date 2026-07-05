from connectors.default_registry import registry
from connectors.request import EvidenceRequest

from resource_engine.entity_matcher import EntityMatcher
from resource_engine.scorer import ResourceScorer


class ResourceDiscovery:

    def __init__(self):

        self.matcher = EntityMatcher()
        self.scorer = ResourceScorer()

    def discover(self, question):

        # -------------------------
        # Extract entities
        # -------------------------

        entities = self.matcher.extract(question)

        print("Entities:", entities)

        if not entities:
            return []

        # -------------------------
        # Collect Pods
        # -------------------------

        response = registry.collect(

            EvidenceRequest(
                type="pods",
                namespace="default",
            )

        )

        if not response.success:
            return []

        pods = response.evidence[0]

        if not isinstance(pods, list):
            return []

        print("Number of pods:", len(pods))

        # -------------------------
        # Score Matches
        # -------------------------

        matches = []

        for pod in pods:

            if not isinstance(pod, dict):
                continue

            name = pod.get("name", "")

            best_score = 0

            for entity in entities:

                score = self.scorer.score(
                    entity,
                    name,
                )

                best_score = max(
                    best_score,
                    score,
                )

            if best_score >= 60:

                resource = pod.copy()

                resource["match_score"] = best_score

                matches.append(resource)

        # -------------------------
        # Highest score first
        # -------------------------

        matches.sort(

            key=lambda x: x["match_score"],

            reverse=True,

        )

        return matches

from agent.plan import InvestigationPlan

from resource_engine.discovery import ResourceDiscovery


class ResourcePlanner:

    def __init__(self):

        self.discovery = ResourceDiscovery()

    def plan(self, question):

        resources = self.discovery.discover(question)

        if not resources:

            return None

        best = resources[0]

        return InvestigationPlan(

            target_type=best["kind"],

            target_name=best["name"],

            namespace=best["namespace"],

            confidence=best["match_score"] / 100,
        )

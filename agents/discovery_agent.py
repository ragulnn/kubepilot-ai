from agents.base import Agent

from resource_engine.discovery import ResourceDiscovery


class DiscoveryAgent(Agent):

    name = "discovery"

    capabilities = [
        "resource_discovery",
    ]

    def __init__(self):

        super().__init__()

        self.discovery = ResourceDiscovery()

    def run(self, state):

        print()
        print("=" * 60)
        print("Discovery Agent")
        print("=" * 60)

        # ----------------------------------
        # Get Investigation Question
        # ----------------------------------

        question = state.get("question")

        if self.bus:

            bus_question = self.bus.get("question")

            if bus_question:

                question = bus_question

        if not question:

            print("No investigation question found.")

            return state

        # ----------------------------------
        # Resource Discovery
        # ----------------------------------

        resources = self.discovery.discover(question)

        state["resources"] = resources

        # ----------------------------------
        # Publish
        # ----------------------------------

        if self.bus:

            self.bus.publish(
                "resources",
                resources,
            )

        # ----------------------------------
        # Display
        # ----------------------------------

        print()
        print("Discovered Resources")
        print("------------------------------")

        if resources:

            for resource in resources:

                print(resource)

        else:

            print("No matching Kubernetes resources found.")

        return state

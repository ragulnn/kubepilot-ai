from datetime import datetime

from agents.base import Agent

from memory.incident import Incident
from memory.repository import IncidentRepository
from memory.search import IncidentSearch


class MemoryAgent(Agent):

    name = "memory"

    capabilities = [
        "memory",
    ]

    def __init__(self):

        super().__init__()

        self.repo = IncidentRepository()

        self.search = IncidentSearch()

    def run(self, state):

        print()
        print("=" * 60)
        print("Memory Agent")
        print("=" * 60)

        analysis = state.get("analysis")

        if not analysis:

            print("No analysis available.")

            return state

        resources = state.get("resources", [])

        resource = {}

        if resources:

            resource = resources[0]

        incident = Incident(

            question=state.get("question", ""),

            resource_name=resource.get("name", ""),

            namespace=resource.get("namespace", "default"),

            root_cause=analysis.get("root_cause", ""),

            confidence=analysis.get("confidence", 0.0),

            findings=analysis.get(

                "critical_evidence",

                [],

            ),

            recommendations=analysis.get(

                "recommended_fix",

                [],

            ),

            timestamp=str(

                datetime.now()

            ),

        )

        self.repo.save(

            incident

        )

        matches = self.search.find(

            incident.__dict__

        )

        state["memory"] = matches

        if self.bus:

            self.bus.publish(

                "memory",

                matches,

            )

        print()

        print("Similar Incidents")

        print("--------------------")

        for match in matches:

            print(

                f"Score: {match['score']}"

            )

        return state

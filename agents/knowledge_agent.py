from agents.base import Agent

from knowledge_base.engine import KnowledgeEngine


class KnowledgeAgent(Agent):

    name = "knowledge"

    capabilities = [
        "knowledge",
    ]

    def __init__(self):

        super().__init__()

        self.engine = KnowledgeEngine()

    def run(self, state):

        print()
        print("=" * 60)
        print("Knowledge Agent")
        print("=" * 60)

        memory = state.get(

            "memory",

            []

        )

        knowledge = self.engine.build(

            memory

        )

        state["knowledge"] = knowledge

        if self.bus:

            self.bus.publish(

                "knowledge",

                knowledge,

            )

        print()

        print(knowledge)

        return state

from agents.base import Agent

from learning_engine.engine import LearningEngine


class LearningAgent(Agent):

    name = "learning"

    capabilities = [
        "learning",
    ]

    def __init__(self):

        super().__init__()

        self.engine = LearningEngine()

    def run(self, state):

        print()
        print("=" * 60)
        print("Learning Agent")
        print("=" * 60)
        print()

        # ----------------------------------
        # Learn From Historical Incidents
        # ----------------------------------

        learning = self.engine.update()

        # ----------------------------------
        # Store
        # ----------------------------------

        state["learning"] = learning

        # ----------------------------------
        # Publish
        # ----------------------------------

        if self.bus:

            self.bus.publish(
                "learning",
                learning,
            )

        # ----------------------------------
        # Display
        # ----------------------------------

        print("Learning Result")
        print("------------------------------")
        print(learning)

        return state

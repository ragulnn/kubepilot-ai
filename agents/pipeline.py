from capability_router.router import CapabilityRouter

from agents.default_registry import registry

from agent_bus.bus import AgentBus


class AgentPipeline:

    def __init__(self):

        self.bus = AgentBus()

        self.router = CapabilityRouter()

        for name in registry.list():

            registry.get(name).bus = self.bus

    def run(self, state):

        self.bus.publish(
            "question",
            state["question"],
        )

        workflow = state.get("workflow")

        capabilities = self.router.route(workflow)

        executed = set()

        for capability in capabilities:

            for agent in registry.by_capability(capability):

                if agent.name in executed:
                    continue

                print()
                print("=" * 60)
                print(f"Running {agent.name}")
                print("=" * 60)

                state = agent.run(state)

                executed.add(agent.name)

        return state

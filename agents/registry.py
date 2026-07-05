class AgentRegistry:

    def __init__(self):

        self._agents = {}

    def register(self, agent):

        self._agents[agent.name] = agent

    def get(self, name):

        return self._agents.get(name)

    def list(self):

        return list(self._agents.keys())

    def unregister(self, name):

        self._agents.pop(name, None)

    def by_capability(self, capability):

        agents = []

        for agent in self._agents.values():

            if capability in agent.capabilities:

                agents.append(agent)

        return agents

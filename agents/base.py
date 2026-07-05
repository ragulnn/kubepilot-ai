from abc import ABC, abstractmethod


class Agent(ABC):

    name = "agent"

    capabilities = []

    priority = 100

    def __init__(self):

        self.bus = None

    @abstractmethod
    def run(self, state):

        pass

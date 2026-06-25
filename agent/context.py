from tools.pods import PodsTool
from tools.namespaces import NamespacesTool
from tools.services import ServicesTool


class ClusterContext:

    def __init__(self):

        self.pods = []
        self.namespaces = []
        self.services = []

    def load(self):

        self.namespaces = NamespacesTool().run()

        self.pods = PodsTool().run()

        self.services = ServicesTool().run()

        return {
            "namespaces": self.namespaces,
            "pods": self.pods,
            "services": self.services,
        }
